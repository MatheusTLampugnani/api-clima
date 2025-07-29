# API de Consulta de Clima

Este projeto consiste em uma API e uma interface web para consultar o clima de uma cidade. O usuário pode inserir um CEP ou o nome de uma cidade para obter informações meteorológicas.

## Funcionalidades

* **Consulta por CEP ou Cidade**: Permite ao usuário buscar o clima informando um CEP (Código de Endereçamento Postal) ou o nome de uma cidade.
* **Informações Detalhadas**: Exibe a temperatura, condição climática (como "céu limpo" ou "nublado"), umidade e velocidade do vento.
* **Interface Simples**: Uma página web intuitiva para realizar as consultas.
* **Validação de Entrada**: Informa ao usuário se a localização não foi encontrada ou se ocorreu um erro na consulta.

## Como Funciona

A aplicação é composta por um backend em Python com FastAPI e um frontend em HTML, CSS e JavaScript.

1.  O usuário insere um CEP ou nome de cidade na página web e clica em "Consultar".
2.  A interface envia uma requisição para o backend.
3.  O backend, por sua vez, utiliza as seguintes APIs externas:
    * **ViaCEP**: Para obter a cidade e o estado a partir de um CEP.
    * **OpenWeatherMap**: Para obter as coordenadas geográficas (latitude e longitude) e, em seguida, os dados meteorológicos da localidade.
4.  As informações do clima são retornadas para a interface e exibidas ao usuário.

## Tecnologias Utilizadas

* **Backend**: Python, FastAPI
* **Frontend**: HTML, CSS, JavaScript
* **APIs Externas**: ViaCEP, OpenWeatherMap

## Como Executar

1.  **Backend**:
    * Certifique-se de ter Python e o `pip` instalados.
    * Instale as dependências: `fastapi`, `uvicorn`, `httpx`.
    * Execute o servidor a partir do diretório do projeto com o comando: `uvicorn main:app --reload`
2.  **Frontend**:
    * Abra o arquivo `index.html` em um navegador web.
    * Certifique-se de que o backend esteja em execução para que as consultas funcionem.
