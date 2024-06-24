# Gerador de requirements.txt

Este projeto é um script Python que automatiza a geração de um arquivo requirements.txt para projetos Python. O script utiliza a ferramenta pipreqs para analisar o código fonte e gerar um arquivo `requirements.txt` com base nas importações detectadas.

## Descrição

O objetivo deste script é simplificar a criação do arquivo requirements.txt, necessário para listar as dependências de um projeto Python.

## Requisitos

- Python 3.x

## Instalação

1. Clone o repositório para sua máquina local:
```
git clone https://github.com/luizelias8/cli-gerador-requirements.git
```

2. Navegue até o diretório do projeto:
```
cd cli-gerador-requirements
```
Nota: Se o pipreqs não estiver instalado, o script irá automaticamente instalá-lo.

## Uso

Para gerar o arquivo `requirements.txt`, simplesmente execute o script:
```
python cli_gerador_requirements.py
```
Isso irá analisar o diretório atual e gerar um arquivo requirements.txt com todas as dependências encontradas.

## Argumentos Opcionais
- `-v`, `--version`: Exibe a versão do script.

## Contribuição

Contribuições são bem-vindas!

## Autor

- [Luiz Elias](https://github.com/luizelias8)