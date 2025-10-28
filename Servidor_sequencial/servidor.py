import json
import socket
from urllib.parse import unquote

#constante
ID = "c8345b76db27676e16c2fe213aec1079"

arquivo = "filmes.json"

lista_filmes = []

class Filme:
    def __init__(self, nome, ano, duracao, sinopse):
        self.nome = nome
        self.ano = int(ano) 
        self.duracao = duracao
        self.sinopse = sinopse


def filmes_json(arquivo):
    lista = []
    with open(arquivo, 'r', encoding='utf-8') as f:
        dados_json = json.load(f)
        for nome_filme, informacao in dados_json.items():
            novo_filme = Filme(nome=nome_filme, ano=informacao['ano'], duracao=informacao['duracao'], sinopse=informacao['sinopse'])
            lista.append(novo_filme)
    return lista

lista_filmes = filmes_json(arquivo)

HOST = '79.21.0.2'
PORT = 80


def extrair_valores_split(request_string):
    try:
        primeira_linha = request_string.split('\r\n')[0]
        partes = primeira_linha.split(' ')
        metodo = partes[0]
        path = partes[1] 
        partes_path = path.split('/') 
        id_valor = partes_path[1]
        filme_codificado = partes_path[2]
        filme_valor = unquote(filme_codificado)
        return metodo, id_valor, filme_valor
    except (IndexError, AttributeError):
        return None, None, None


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor escutando em http://{HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Conexão recebida de {addr}")
            while True:
                try: 
                    data = conn.recv(1024)
                    if not data:
                        break

                    metodo, id, filme = extrair_valores_split(data.decode('utf-8'))
                    http_resposta = "" 
                    if id != ID:
                        print(f"ID Incorreto: {id}")
                        http_resposta = "HTTP/1.1 403 Forbidden\n\nID Invalido."
                    else:
                        filme_encontrado = None
                        for i in lista_filmes:
                            if i.nome == filme:
                                filme_encontrado = i
                                break 
                        if filme_encontrado:
                            print(f"Filme encontrado: {filme_encontrado.nome}")
                            http_resposta = (f"HTTP/1.1 200 OK\nContent-Type: text/plain; charset=utf-8\n\nAno:{filme_encontrado.ano}\nDuração:{filme_encontrado.duracao}\nSinopse:{filme_encontrado.sinopse}! A resposta veio do servidor.")
                        else:
                            print(f"Filme nao encontrado: {filme}")
                            http_resposta = "HTTP/1.1 404 Not Found\n\nFilme nao encontrado."
                    conn.sendall(http_resposta.encode('utf-8'))
                except socket.error as e:
                    print(f"Erro na conexão com {addr}: {e}")
                    break 