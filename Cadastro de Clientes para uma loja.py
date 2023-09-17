import json
# Função para cadastrar um cliente
def cadastrar_cliente():
    print('\n')
    print('\t --- Cadastrando cliente --- ')
    print('\n') 
    dic_cliente = {}
    dic_documentos = {}
    dic_cliente["nome"] = input('NOME: ')
    dic_cliente["endereco"] = input('ENDEREÇO: ')
    dic_cliente["renda"] = input('RENDA: ')
    dic_documentos["cpf"] = input('CPF: ')
    dic_documentos["rg"] = input('RG: ')
    dic_cliente["documentos"]= dic_documentos
    print('\n')
    print('\t --- Cadastrando compra --- ')
    print('\n')
    compras = []
    while True:
        dic_compras = {}
        dic_compras["data"] = input('DATA DA COMPRA: ')
        dic_compras["quant_produtos"] = input('QUANTIDADE DE PRODUTOS: ')
        dic_compras["valor"] = input('VALOR TOTAL: ')
        compras.append(dic_compras)
        print('\n')
        resp = input('1 - Cadastrar mais compras \n0 - Voltar ao menu - > ')
        if resp not in ('1', '0'):
            print('Resposta incorreta')
        else:
            if resp == '1':
                continue
            elif resp == '0':
                break
    dic_cliente["compras"] = compras
    cadastro.append(dic_cliente)

# Função para salvar os dados em um arquivo JSON
def salvar():
    with open('cadastro.json', 'w') as arquivo:
        json.dump(cadastro, arquivo)

# Função para visualizar o cadastro em formato JSON
def visualizar_cadastro():
    print(json.dumps(cadastro, sort_keys=False, indent=4))

# Função para ler dados de um arquivo JSON
def ler_arquivo():
    try:
        with open('cadastro.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Função para remover um objeto (cliente) pelo CPF
def remover_objeto(cpf):
    for p in cadastro:
        if p["documentos"]["cpf"] == cpf:
            cadastro.remove(p)
            return True
    return False

# Inicializa a lista cadastro no início do programa lendo dados do arquivo ou criando uma lista vazia
cadastro = ler_arquivo()

# Função principal do menu
def menu():
    while True:
        print("---"*30)
        print('1 - Cadastrar cliente \n2 - Remover \n3 - Visualizar cadastro \n0 - Finalizar Programa')
        menu_opcao = input('Digite o número da sua opção: ')
        if menu_opcao not in ('0', '1', '2', '3'):
            print('Opção incorreta, digite novamente')
        else:
            if menu_opcao == '0':
                salvar()
                break
            elif menu_opcao == '1':
                cadastrar_cliente()
            elif menu_opcao == '2':
                print("\t --- Removendo cpf ---")
                cpf = input('Informe o CPF que deseja remover: ')
                if remover_objeto(cpf):
                    print("--- CPF foi removido ---")
                else:
                    print("--- Objeto não encontrado ---")
            elif menu_opcao == '3':
                visualizar_cadastro()

# Chama a função menu para iniciar o programa
menu()
