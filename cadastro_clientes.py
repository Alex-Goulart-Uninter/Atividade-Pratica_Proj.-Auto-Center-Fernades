#Criação da Classe Cliente que irá representar os clientes a serem cadastrados
class Cliente:
    def __init__(self, nome_cliente, cpf, email, telefone, endereco):
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    #Função que exibirá os clientes cadastrados
    def __repr__(self):
        return (f"""
                Cliente  Nome: '{self.nome_cliente}',
                          CPF: '{self.cpf}',
                        Email: '{self.email}',
                     Telefone: '{self.telefone}',
                     Endereço: '{self.endereco}',
                """)

#Essa Classe irá gerenciar a lista de clientes cadastrados
class GerenciamentoDeClientes:
    def __init__(self):
        self.clientes = [] #Irá inicializar a lista que servirá de banco de dados temporário

    #Função que irá adicionar um novo cliente na lista de clientes
    def cadastro_cliente(self,cliente):
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso!!!")
    
    #Função que irá verificar se há clientes cadastrados e os imprime
    def lista_clientes(self):
        if not self.clientes:
            print('Ops!!! Não há clientes cadastrados!!')

        else:
            print('\nLista de Clientes Cadstrados')
            for cliente in self.clientes:
                print(cliente)

#Programa Principal
def main():

    #Instancia de gerenciamento dos clientes
    gerenciamento_cliente = GerenciamentoDeClientes()

    print("----------------------------------------------------------------------------------")
    
    #Menu principal do programa
    while True:
        print("""\nMenu para cadastro de clientes
              1. Cadastrar Cliente
              2. Listar Clientes
              3. Sair """)
        
        #Solicita ao usuário que escolha uma opção do menu
        escolha = input('Escolha uma das opções do menu: ')
        print("----------------------------------------------------------------------------------")

        #Esta opção irá solicitar ao usuário as informações do cliente a serem cadastradas
        if escolha =="1":
            nome_cliente = input('Digite o Nome do cliente: ')
            cpf = input('Digite o CPF do cliente: ')
            email = input('Digite o E-mail do cliente: ')
            telefone = input('Digite o Telefone do cliente: ')
            endereco = input('Digite o Endereço do cliente: ')

            #Variável que irá receber as informações do cliente
            cliente = Cliente(nome_cliente, cpf, email, telefone, endereco)

            #Cria o cadastro do cliente no gerenciamento_cleinte
            gerenciamento_cliente.cadastro_cliente(cliente)
            print("----------------------------------------------------------------------------------")
            
        #Essa opção irá imprimir os clientes cadastrados
        elif escolha == '2':
            gerenciamento_cliente.lista_clientes()
            print("----------------------------------------------------------------------------------")

        #Opção que encerra o programa
        elif escolha == '3':
            print('O programa esta sendo encerrado !!')
            break

        #Em caso de algum problema durante a escolha das opções do menu, será exibida uma mensagem de erro
        else:
            print("Ops!!! Opção inválida, tente novamente.")

#Excecuta o programa pincipal
if __name__ == "__main__":
    main()