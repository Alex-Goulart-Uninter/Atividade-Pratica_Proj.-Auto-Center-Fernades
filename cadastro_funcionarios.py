from enum import Enum
import uuid

# Enum para os tipos de login
class TipoLogin(Enum):
    ADMIN = "Admin"
    USER = "User"
    GUEST = "Guest"

# Classe para representar um funcionário
class Funcionario:
    def __init__(self, nome, cpf, cargo, salario, tipo_login):
        self.matricula = str(uuid.uuid4())[:8]  # Gera um identificador único curto como matrícula
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario
        self.tipo_login = tipo_login

    def atualizar_dados(self, cargo=None, salario=None, tipo_login=None):
        if cargo:
            self.cargo = cargo
        if salario:
            self.salario = salario
        if tipo_login:
            self.tipo_login = tipo_login

    def verificar_permissao(self):
        if self.tipo_login == TipoLogin.ADMIN:
            return "Acesso total ao sistema."
        elif self.tipo_login == TipoLogin.USER:
            return "Acesso limitado a funcionalidades de usuário."
        elif self.tipo_login == TipoLogin.GUEST:
            return "Acesso restrito a visualização."
        else:
            return "Tipo de login desconhecido."

    def __str__(self):
        return (f"Matrícula: {self.matricula}\nNome: {self.nome}\nCPF: {self.cpf}\n"
                f"Cargo: {self.cargo}\nSalário: {self.salario}\nTipo de Login: {self.tipo_login.value}\n"
                f"Permissão: {self.verificar_permissao()}")

# Classe para gerenciar o sistema de funcionários
class SistemaCadastro:
    def __init__(self):
        self.funcionarios = []

    def cadastrar_funcionario(self):
        nome = input("Digite o nome do funcionário: ")
        cpf = input("Digite o CPF do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))
        
        # Seleção do tipo de login
        print("Selecione o tipo de login:")
        for tipo in TipoLogin:
            print(f"{tipo.name}: {tipo.value}")
        tipo_login_str = input("Digite o tipo de login (Admin, User, Guest): ").upper()
        
        tipo_login = TipoLogin[tipo_login_str] if tipo_login_str in TipoLogin.__members__ else None
        if not tipo_login:
            print("Tipo de login inválido. Cadastro não realizado.")
            return
        
        funcionario = Funcionario(nome, cpf, cargo, salario, tipo_login)
        self.funcionarios.append(funcionario)
        print(f"Funcionário {nome} cadastrado com sucesso!\n")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
            return
        for funcionario in self.funcionarios:
            print(funcionario)
            print("-" * 40)

    def atualizar_funcionario(self, matricula):
        for funcionario in self.funcionarios:
            if funcionario.matricula == matricula:
                print("Deixe em branco se não deseja alterar um campo.")
                novo_cargo = input(f"Novo cargo (atual: {funcionario.cargo}): ") or funcionario.cargo
                novo_salario_str = input(f"Novo salário (atual: {funcionario.salario}): ") or funcionario.salario
                novo_salario = float(novo_salario_str) if novo_salario_str != funcionario.salario else funcionario.salario
                
                # Atualizar tipo de login
                print("Selecione o novo tipo de login (ou deixe em branco para manter o atual):")
                for tipo in TipoLogin:
                    print(f"{tipo.name}: {tipo.value}")
                novo_tipo_login_str = input(f"Novo tipo de login (atual: {funcionario.tipo_login.value}): ").upper() or funcionario.tipo_login.name
                novo_tipo_login = TipoLogin[novo_tipo_login_str] if novo_tipo_login_str in TipoLogin.__members__ else funcionario.tipo_login

                # Atualizando os dados do funcionário
                funcionario.atualizar_dados(cargo=novo_cargo, salario=novo_salario, tipo_login=novo_tipo_login)
                print(f"Funcionário {funcionario.nome} atualizado com sucesso!")
                return
        
        print("Funcionário não encontrado.")

# Exemplo de uso
sistema = SistemaCadastro()

# Loop principal para interação com o usuário
while True:
    print("\n1. Cadastrar funcionário")
    print("2. Listar funcionários")
    print("3. Atualizar funcionário")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        sistema.cadastrar_funcionario()
    elif opcao == "2":
        sistema.listar_funcionarios()
    elif opcao == "3":
        matricula = input("Digite a matrícula do funcionário que deseja atualizar: ")
        sistema.atualizar_funcionario(matricula)
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
