import json

def salvar_dados(lista):
    with open('manutencoes.json', 'w') as f:
        json.dump(lista, f, indent=4)

def carregar_dados():
    try:
        with open('manutencoes.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def adicionar_servico(lista):
    item = input("Aparelho (ex: PS5, iPhone 13): ")
    defeito = input("Descrição do defeito: ")
    valor = float(input("Valor orçado: R$ "))
    lista.append({"aparelho": item, "defeito": defeito, "valor": valor, "status": "Pendente"})
    salvar_dados(lista)
    print("Serviço registrado com sucesso!")

# Estrutura do Menu Principal
servicos = carregar_dados()
while True:
    print("\n1. Novo Serviço | 2. Listar Todos | 3. Sair")
    opcao = input("Escolha: ")
    if opcao == '1':
        adicionar_servico(servicos)
    elif opcao == '2':
        for i, s in enumerate(servicos):
            print(f"{i} - {s['aparelho']} [{s['status']}] - R$ {s['valor']}")
    elif opcao == '3':
        break