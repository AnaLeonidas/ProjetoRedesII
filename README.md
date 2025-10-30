# Comparação de Desempenho: Servidor TCP Sequencial vs. Concorrente

Este projeto realiza uma análise comparativa de desempenho entre duas arquiteturas de servidor TCP implementadas em Python: um servidor **Sequencial** (que processa uma requisição por vez) e um servidor **Concorrente** (que utiliza *multithreading* para processar múltiplas requisições simultaneamente).
O objetivo é medir, sob diferentes quantidades de requisições, como cada arquitetura responde em termos de **tempo de resposta** e **estabilidade**.
Os servidores simulam uma API de consulta de filmes, lendo um arquivo `filmes.json`, enquanto os clientes realizam requisições HTTP `GET` para obter dados.

## 🚀 Tecnologias Utilizadas

* **Python 3:** Linguagem de programação principal para os servidores e clientes.
* **Docker:** Para criar ambientes isolados (contêineres) para cada servidor e cliente.
* **Docker Compose:** Para orquestrar e facilitar a execução dos diferentes cenários de teste.

## ⚙️ Como Executar

O projeto é totalmente conteinerizado, facilitando a reprodução dos testes.

### 1. Testando o Servidor Sequencial

Este comando irá construir e iniciar os contêineres do **servidor sequencial** e **um cliente** (`cliente_01`), que executará um lote de testes contra ele.

docker-compose up --build servidor_sequencial cliente_01

### 2. Testando o Servidor Concorrente

Este comando irá construir e iniciar os contêineres do **servidor concorrente** e **dois clientes** (`cliente_02` e `cliente_03`), que executará um lote de testes contra eles.

docker-compose up --build servidor_concorrente cliente_02 cliente_03

### 3. Links
Vídeo: https://youtu.be/loR5VfVbOPI
Github: https://github.com/AnaLeonidas/ProjetoRedesII
>>>>>>> ebd0295c7420ac212c4c4e645239d417fe8a9437
