#Classe Funcionários que irá representar os funcinários que seram cadastrados
class Funcionario:
    def __init__(self, nome_funcionario, cpf, email, telefone, endereco, matricula_funcionario, cargo, salario):
        self.nome_funcionario = nome_funcionario
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.matricula_funcionario = matricula_funcionario
        self.cargo = cargo
        self.salario = salario

    #Função que irá exibir os funcionários cadastrados
    def __repr__(self):
        return (f"""
            Funcionário:  Matrícula: '{self.matricula_funcionario}'
                               Nome: '{self.nome_funcionario}',
                                CPF: '{self.cpf}',
                             E-Mail: '{self.email}',
                           Telefone: '{self.telefone}',
                           Endereço: '{self.endereco}',
                              Cargo: '{self.cargo}',
                            Salário: '{self.salario}'
                """)
    
#Classe que irá gerenciar a lista de funcionário cadastrados
class GerenciamentoDeFuncionarios:
    def __init__(self):
        self.funcionarios = [] #Irá inicializar a lista que servirá como banco de dados temporário

    #Função que irá adicionar um novo ou atulizar um funcionários na lista de funcionários
    def cadastro_funcionario(self, funcionario):
        funcionario_existente = self.buscar_funcionarioPorMatricula(funcionario.matricula_funcionario)
        if funcionario_existente:
            self.atualizar_funcionario(funcionario_existente, funcionario.email, funcionario.telefone, 
                                      funcionario.endereco, funcionario.cargo, funcionario.salario, funcionario.matricula_funcionario)
        
        else:
            self.funcionarios.append(funcionario)
            print("Funcionário cadastrado com sucesso!!!")

    #Função que verifica se há funcionários cadastrados e imprime
    def lista_funcionarios(self):
        if not self.funcionarios:
            print("Ops..Funcionário não cadastrado!!!")

        else:
            print("Lista de Funcionarios Cadastrados")
            for funcionario in self.funcionarios:
                print(funcionario)

    #Função que irá buscar o funcionario pela matrícula
    def buscar_funcionarioPorMatricula(self, matricula_funcionario):
        for funcionario in self.funcionarios:
            if funcionario.matricula_funcionario == matricula_funcionario:
                return funcionario
            return None
    
    #Função que irá atualizar os dados do funcionário já cadastrado
    def atualizar_funcionario(self, funcionario_existente, matricula_funcionario=None, email=None, telefone=None, 
                             endereco=None, cargo=None, salario=None):
        if matricula_funcionario:
            funcionario_existente.matricula = matricula_funcionario
        if email:
            funcionario_existente.emai = email
        if telefone:
            funcionario_existente.telefone = telefone
        if endereco:
            funcionario_existente.endereco = endereco
        if cargo:
            funcionario_existente.cargo = cargo
        if salario:
            funcionario_existente.salario = salario
        print("Dados do funcionário atualizado com sucesso!!")
    
#Programa Principal
def main():

    #Instância de gerenciamento dos funcionários
    Gerenciamento_Funcionarios = GerenciamentoDeFuncionarios()
    print("---------------------------------------------------------------------------------------")

    #Menu principal do programa
    while True:
        print(""" Menu para Cadastro de Funcionários
              1. Cadastrar Funionários
              2. Lsitar Funcionários
              3. Atualizar Dados do Funcionário
              4. Sair
              """)
        
        #Solicita ao uruário que esolha uma opção do menu
        escolha = input("Escolha um das opções do menu: ")
        print("---------------------------------------------------------------------------------------")

        #Opção de entrada de dados do funcionário a ser cadastrado
        if escolha == '1':
            matricula_funcionario = input("Digite o Matrícula do Funcionário: ")
            nome_funcionario = input("Digite o nome do Funcionário: ")
            cpf = input("Digite o CPF do Funcionário: ")
            email = input("Digite o E-Mail do Funcionário: ")
            telefone = input("Digite o Telefone do Funcionário: ")
            endereco = input("Digite o Endereço do Funcionário: ")
            cargo = input("Digite o Cargo do Funcionário: ")
            salario = input("Digite o Salario do Funcionário: ")

            #Variável que irá recer as informações do funcionário
            funcionario = Funcionario(nome_funcionario, cpf, email, telefone, endereco, matricula_funcionario, cargo, salario)

            #Criando o cadastro do funcionário no gerenciamento de funcionário
            Gerenciamento_Funcionarios.cadastro_funcionario(funcionario)
            print("---------------------------------------------------------------------------------------")
        #Opção de impressão dos funcionários cadastrados
        elif escolha =='2':
            Gerenciamento_Funcionarios.lista_funcionarios()
            print("---------------------------------------------------------------------------------------")
        
        #Opção de atualização dos dados cadastrais do funcinário
        elif escolha =='3':
            matricula_funcionario = input("Digite a matrícula do funcionário que deseja atualizar os dados: ")
            funcionario_existente = Gerenciamento_Funcionarios.buscar_funcionarioPorMatricula(matricula_funcionario)

            if funcionario_existente:
                while True:
                    print(f"{funcionario_existente}")
                    print("""Qual dos dados será atualizado?
                             1. Atualizar a Matricula
                             2. Atualizar o E-mail
                             3. Atulizar o Telefone
                             4. Atualizar o Endereço
                             5. Atualizar o Cargo
                             6. Atualizar o Salario
                             7. Voltar ao Menu Principal """)
                    
                    escolha_atualização = input("Escolha a opção que deseja atualziar: ")
                    
                    if escolha_atualização == '1':
                        nova_matricula = input("Digite o nova Matrícula do Funcionário: ")
                        Gerenciamento_Funcionarios.atualizar_funcionario(funcionario_existente, matricula_funcionario=nova_matricula)
                    elif escolha_atualização == '2':
                        novo_email = input("Digite o novo E-mail do Funcionário: ")
                        Gerenciamento_Funcionarios.atualizar_funcionario(funcionario_existente, email=novo_email)
                    elif escolha_atualização == '3':
                        novo_telefone = input("Digite o novo Telefone do Funcionário: ")
                        Gerenciamento_Funcionarios.atualizar_funcionario(funcionario_existente, telefone=novo_telefone)
                    elif escolha_atualização == '4':
                        novo_endereco = input("Digite o novo Endereço do Funcionário: ")
                        Gerenciamento_Funcionarios.atualizar_funcionario(funcionario_existente, endereco=novo_endereco)
                    elif escolha_atualização == '5':
                        novo_cargo = input("Digite o novo cargo do Funcionário: ")
                        Gerenciamento_Funcionarios.atualizar_funcionario(funcionario_existente, cargo=novo_cargo)
                    elif escolha_atualização == '6':
                        novo_salario = input("Digite o novo Salário do Funcionário: ")
                        Gerenciamento_Funcionarios.atualizar_funcionario(funcionario_existente, salario=novo_salario)
                    elif escolha =='7':
                        break
                    else:
                        print('Ops..!! Algo deu errado, tente novamente!!')
            else:
                print("Cliente não encontrado, verifique se a maticula foi digitada corretamente!!!")
                print("---------------------------------------------------------------------------------------")
        
        #Opção que irá encerrar o programa
        elif escolha == '4':
            print("Programa esta sendo encerrado!!")
            break

        #Mensagem de erro caso entre com alguma opção que não existe
        else:
            print("Opção inválida, escolha uma opção válida!!!")

#Executará o programa principal
if __name__ == "__main__":
    main()
    print("---------------------------------------------------------------------------------------")