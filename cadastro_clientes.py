#Criação da Classe Cliente que irá representar os clientes a serem cadastrados
class Cliente:
    def __init__(self, nome_cliente, cpf, email, telefone, endereco):
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.compras = [] #Lista para armazenar as compras realizadas pelos clientes

    #Função que exibirá os clientes cadastrados
    def __repr__(self):
        return (f"""
                Cliente  Nome: '{self.nome_cliente}',
                          CPF: '{self.cpf}',
                        Email: '{self.email}',
                     Telefone: '{self.telefone}',
                     Endereço: '{self.endereco}',
                      Compras: '{self.compras}'
                """)
    
    #Método que irá adicionar as compras dos cliente
    def add_compra(self,descricao, quantidade, valor_unitario):
        valor_total = quantidade * valor_unitario
        compra = {
            "Descricao":descricao,
            "Quantidade":quantidade,
            "Valor Unitário": valor_unitario,
            "Valor Total": valor_total
        }
        self.compras.append(compra)
        print(f"Compra feita com sucesso!!!")

    #Método que irá remover a compra do cliente
    def remover_compra(self, descricao):
        for compra in self.compras:
            if compra['Descricao'] == descricao:
                self.compras.remove(compra)
            print("Compra removida com sucesso!!!")
            return    
        print("Compra não encontrada!!!")

#Essa Classe irá gerenciar a lista de clientes cadastrados
class GerenciamentoDeClientes:
    def __init__(self):
        self.clientes = [] #Irá inicializar a lista que servirá de banco de dados temporário

    #Função que irá adicionar um novo cliente na lista de clientes
    def cadastro_cliente(self,cliente):
        cliente_existente = self.buscar_clientePorCpf(cliente.cpf)
        if cliente_existente: #Atualiza o cliente existente
            self.atualizar_cliente(cliente_existente, cliente.email, cliente.telefone, cliente.endereco)
        
        else:
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
    
    #Função que irá buscar cliente pelo CPF
    def buscar_clientePorCpf(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None
    
    #Função que irá atualizar os dados do cliente já cadastrado
    def atualizar_cliente(self, cliente_existente, email=None, telefone=None, endereco=None):
        if email:
            cliente_existente.email = email
        if telefone:
            cliente_existente.telefone = telefone
        if endereco:
            cliente_existente.endereco = endereco
        print('Dados do cliente atualizados com sucesso!!!')
        
    #Função que irá adicionar a compra ao cliente
    def add_compra(self, cpf, descricao, quantidade, valor_unitario):
        cliente = self.buscar_clientePorCpf(cpf)
        if cliente:
            cliente.add_compra(descricao, quantidade, valor_unitario)
        else:
            print("Cliente não encontrado, verifique o CPF novamente!!!")

    #Função que irá remover a compra do cliente
    def remover_compra(self, cpf, descricao):
        cliente = self.buscar_clientePorCpf(cpf)
        if cliente:
            cliente.remover_compra(descricao)
        else:
            print("Cliente não encontrado, verifique o CPF novamente!!!")

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
              3. Atualizar Cliente
              4. Adicionar Compra
              5. Remover Compra
              6. Sair """)
        
        #Solicita ao usuário que escolha uma opção do menu
        escolha = input('Escolha uma das opções do menu: ')
        print("----------------------------------------------------------------------------------")

        #Opção de entrada dos dados do cliente a ser cadastrado
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
            
        #Opção de impressão dos clientes cadastrados
        elif escolha == '2':
            gerenciamento_cliente.lista_clientes()
            print("----------------------------------------------------------------------------------")

        #Opção de Atualização de dados cadastrais do cliente
        elif escolha == '3':
            cpf = input('Digite o CPF do cliente que deseja atualizar os dados existentes: ')
            cliente_existente = gerenciamento_cliente.buscar_clientePorCpf(cpf)

            if cliente_existente:
                while True:
                    print(f"{cliente_existente}")
                    print("""Qual opção a ser atualizada!
                            1. Atualizar o E-mail
                            2. Atualizar o Telefone
                            3. Atualizar o Endereço
                            4. Voltar ao Menu Principal """)
                    
                    escolha_atualizacao = input('Escolha o dado que deseja atualizar: ')

                    if escolha_atualizacao =="1":
                        novo_email = input("Digite o novo E-mail do cliente: ")
                        gerenciamento_cliente.atualizar_cliente(cliente_existente, email=novo_email)
                    elif escolha_atualizacao =="2":
                        novo_telefone = input("Digite o novo Telefone do cliente: ")
                        gerenciamento_cliente.atualizar_cliente(cliente_existente, telefone=novo_telefone)
                    elif escolha_atualizacao == "3":
                        novo_endereco = input("Digite o novo Endereço do cliente: ")
                        gerenciamento_cliente.atualizar_cliente(cliente_existente, endereco=novo_endereco)
                    elif escolha_atualizacao == "4":
                        break
                    else:
                        print("Ops...!! Algo Deu Errado, Tente novamente!!!!")
            else:
                print("Cliente não encontrado! Verifique novamente o CPF digitado!!")
            print("----------------------------------------------------------------------------------")

        #Opção que irá adicionar um compra ao cliente
        elif escolha == "4":
            cpf = input("Digite o CPF do cliente que deseja efetuar uma compra: ")
            descricao = input("Digite a descrição o item a ser comprado: ")
            quantidade = int(input("Digite a quantidade o item a ser comprado: "))
            valor_unitario = float(input("Digite a valor do item a ser comprado: "))
            gerenciamento_cliente.add_compra(cpf, descricao, quantidade, valor_unitario)
            print("----------------------------------------------------------------------------------")

        #Opção que irá remover a compra do cliente
        elif escolha == "5":
           cpf = input("Digite o CPF do cliente que deseja remover uma compra: ")
           descricao = input("Digite a descrição o item a ser removido: ")
           gerenciamento_cliente.remover_compra(cpf, descricao)
        
        #opção que irá encerrar o programa
        elif escolha =="6":
            print('O programa está sendo encerrado!!')
            break

        #Em caso de algum problema durante a escolha das opções do menu, será exibida uma mensagem de erro
        else:
            print("Ops!!! Opção inválida, tente novamente.")

#Excecuta o programa pincipal
if __name__ == "__main__":
    main()
    print("----------------------------------------------------------------------------------")