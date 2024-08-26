#Classe Funcionários que irá representar os funcinários que seram cadastrados
class funcionario:
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
            self.atulizar_funcionario(funcionario_existente, funcionario.email, funcionario.telefone, 
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
    def atulizar_funcionario(self, funcionario_existente, matricula=None, email=None, telefone=None, 
                             endereco=None, cargo=None, salario=None):
        if matricula:
            funcionario_existente.matricula = matricula
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