# Criar o projeto no firebaseio
# Criar o Database (Atenção às regras de segurança)
# Estrutura de Árvore
# Interação com o Database (REST API)
import requests
import json
import pprint

link = 'https://crud-project-c1dc7-default-rtdb.firebaseio.com/'

# # # Criar uma venda (POST)    #Link padrão mais o caminho a ser editado, finalizando com o .json
dados = {'cliente': 'Ronaldo', 'preco': 150, 'produto': 'teclado PC'}
requisicao = requests.post(f'{link}/Vendas.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

# # Criar um novo produto (POST)
dados = {'nome': 'Mussarella', 'preco': 5.5, 'quantidade': 200}
requisicao = requests.post(f'{link}/Produtos.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

# # Editar a venda (PATCH)
dados ={'cliente': 'Thiago de Loreto'}
requisicao = requests.patch(f'{link}/Vendas/-NY5EYsX_KZYPooiwY1C/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

# Pegar uma venda específica ou todas as vendas (GET)
requisicao = requests.get(f'{link}/Vendas.json')
print(requisicao)
dic_requisicao = requisicao.json()

id_thiago = None
for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['cliente']
    if cliente == 'Thiago de Loreto':
        print(f'O ID da venda é {id_venda}')
        id_thiago = id_venda

# Deletar uma venda (DELETE)
requisicao = requests.delete(f'{link}/Vendas/{id_thiago}/.json')
print(requisicao)
print(requisicao.text)

# O que é legal de fazer?
# Autenticação 
# Criar outras estruturas de dados (Vendedor, Lojas, Clientes, Estoque, etc.)
