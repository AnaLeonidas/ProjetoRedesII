import hashlib
import random
import socket
import statistics
import time
from urllib.parse import quote

# constantes 
MATRICULA = "20239037921"
NOME = "Ana"

lista_tempos = []
lista_original = ["Scooby Doo na ilha dos zumbis", "Noivas em guerra", "Vestida para casar", "La la land", "Crepúsculo", "Batman", "Aves de Rapina", "Os suspeitos", "Scooby Doo e a bruxa fantasma", "A viagem de chihiro", "Ponyo", "Scooby Doo e o rei dos duendes", "Barbie fairytopia", "Barbie mermaidia", "Barbie a magia do arco iris", "A bussola de ouro", "Coração de tinta", "O labirinto do fauno", "Alice no pais das maravilhas", "Mulherzinhas", "Tinker Bell uma aventura no mundo das fadas"]

random.seed(42)
lista_aleatoria = random.choices(lista_original, k=5)
lista_filmes = lista_aleatoria * 2

SERVER_HOST = '79.21.0.2'
SERVER_PORT = 80

time.sleep(5)


def gerar_ID(matricula, nome):
    texto = f"{matricula} {nome}"
    hash_md5 = hashlib.md5(texto.encode('utf-8')).hexdigest()
    return hash_md5


def gerar_http_requisicao(id, filme):
    filme_codificado = quote(filme)
    http_requisicao = f"GET /{id}/{filme_codificado} HTTP/1.1\r\nHost: {SERVER_HOST}\r\n\r\n"
    return http_requisicao

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        print(f"Conectando ao servidor em {SERVER_HOST}:{SERVER_PORT}...")
        # Conecta ao servidor
        s.connect((SERVER_HOST, SERVER_PORT))
        print("Conectado! Enviando requisição HTTP...")
        for i in range(10):
            tempo_inicial = time.perf_counter()
            for filme in lista_filmes:
                    X_Custom_ID = gerar_ID(MATRICULA, NOME)
                    http_requisicao = gerar_http_requisicao(X_Custom_ID, filme)
                    s.sendall(http_requisicao.encode('utf-8'))

                    resposta = s.recv(1024)        
                    print("\n--- Resposta do Servidor ---")
                    print(resposta.decode('utf-8'))
                    print("----------------------------")
            tempo_final = time.perf_counter()
            tempo_rodada = tempo_final - tempo_inicial
            lista_tempos.append(tempo_rodada)

    except ConnectionRefusedError:
        print("Erro: A conexão foi recusada. O servidor está rodando?")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

media = statistics.mean(lista_tempos)
desvio_padrao = statistics.stdev(lista_tempos)
tempo_total = sum(lista_tempos)

print("\n--- Resultados Finais ---")
print("\nTempos de cada rodada (em segundos):")
for k, tempo in enumerate(lista_tempos):
    print(f"  Rodada {k+1}: {tempo:.4f} s")
print("\nEstatísticas:")
print(f"  Tempo Total: {tempo_total:.4f} s")
print(f"  Média: {media:.4f} s")
print(f"  Desvio Padrão: {desvio_padrao:.4f} s")