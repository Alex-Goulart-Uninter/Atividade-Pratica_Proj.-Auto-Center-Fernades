# Classe Funcionário que irá representar os funcionários que serão cadastrados e seus atributos
class Funcionario:
    def __init__(self, nome_funcionario, cpf, email, telefone, endereco, matricula_funcionario, cargo, salario, tipo_login, permissoes):
        self.nome_funcionario = nome_funcionario
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.matricula_funcionario = matricula_funcionario
        self.cargo = cargo
        self.salario = salario
        self.tipo_login = tipo_login  # Define o tipo de login do funcionário, como "admin" ou "usuario"
        self.permissoes = permissoes  # Lista de permissões associadas ao funcionário

    # Função que irá exibir os funcionários cadastrados
    def __repr__(self):
        return (f"""
        Funcionário: 
          Matrícula: '{self.matricula_funcionario}'
            Nome: '{self.nome_funcionario}'
             CPF: '{self.cpf}'
          E-Mail: '{self.email}'
        Telefone: '{self.telefone}'
        Endereço: '{self.endereco}'
           Cargo: '{self.cargo}'
        Salário R$: '{self.salario}'
     Tipo de Login: '{self.tipo_login}'
        Permissões: '{self.permissoes}'
        """)

# Classe que irá gerenciar a lista de funcionários cadastrados
class GerenciamentoDeFuncionarios:
    def __init__(self):
        self.funcionarios = []  # Inicializa a lista que servirá como banco de dados temporário

    # Função que irá adicionar um novo ou atualizar um funcionário na lista de funcionários e verifica se o mesmo tem as devidas permissões de acesso.
    def cadastro_funcionario(self, funcionario, usuario_logado):
        if 'cadastrar' in usuario_logado.permissoes:
            funcionario_existente = self.buscar_funcionario_por_matricula(funcionario.matricula_funcionario)
            if funcionario_existente:
                self.atualizar_funcionario(funcionario_existente, funcionario.email, funcionario.telefone, funcionario.endereco,
                                            funcionario.cargo, funcionario.salario)
            else:
                self.funcionarios.append(funcionario)
                print("Funcionário cadastrado com sucesso!")
                
                # Solicita o login do novo funcionário cadastrado
                print("Por favor, realize o login do novo funcionário cadastrado.")
                novo_usuario_logado = login(self.funcionarios)
                
                if novo_usuario_logado and novo_usuario_logado.matricula_funcionario == funcionario.matricula_funcionario:
                    print(f"Login do novo funcionário {novo_usuario_logado.nome_funcionario} realizado com sucesso!")
                else:
                    print("Falha no login do novo funcionário.")
        else:
            print("Permissão Negada: Usuário não tem permissão para cadastrar funcionários!")

    # Função que verifica se há funcionários cadastrados e imprime, verificando se o mesmo tem as devidas permissões de acesso.
    def lista_funcionarios(self, usuario_logado):
        if 'listar' in usuario_logado.permissoes:
            if not self.funcionarios:
                print("Não há funcionários cadastrados!")
            else:
                print("Lista de Funcionários Cadastrados:")
                for funcionario in self.funcionarios:
                    print(funcionario)
        else:
            print("Permissão Negada: Usuário não tem permissão para listar funcionários!")

    # Função que irá buscar o funcionário pela matrícula
    def buscar_funcionario_por_matricula(self, matricula_funcionario):
        for funcionario in self.funcionarios:
            if funcionario.matricula_funcionario == matricula_funcionario:
                return funcionario
        return None

    # Função que irá atualizar os dados do funcionário já cadastrado
    def atualizar_funcionario(self, funcionario_existente, email=None, telefone=None, 
                             endereco=None, cargo=None, salario=None):
        if email:
            funcionario_existente.email = email
        if telefone:
            funcionario_existente.telefone = telefone
        if endereco:
            funcionario_existente.endereco = endereco
        if cargo:
            funcionario_existente.cargo = cargo
        if salario:
            funcionario_existente.salario = salario
        print("Dados do funcionário atualizados com sucesso!")

    # Função que irá atualizar as permissões do funcionário/usuário
    def atualizar_permissoes(self, funcionario_existente, novas_permissoes):
        funcionario_existente.permissoes = novas_permissoes
        print("Permissões do funcionário/usuário atualizadas com sucesso!")

# Função que realizará o login do funcionário com base na matrícula
def login(funcionarios):
    matricula_funcionario = input("Digite sua Matrícula: ")
    funcionario = next((f for f in funcionarios if f.matricula_funcionario == matricula_funcionario), None)
    if funcionario:
        print(f"Bem-Vindo, {funcionario.nome_funcionario}!")
        return funcionario
    else:
        print("Matrícula não encontrada, Acesso negado!")
        return None

# Programa Principal
def main():

    # Instância de gerenciamento dos funcionários
    gerenciamento_funcionarios = GerenciamentoDeFuncionarios()

    # Cria um funcionário administrador com permissões completas
    funcionario_admin = Funcionario("Alex Marcos", "00000000000", "admin@example.com", "999999999", "Admin Street", "849112", "Gerente", "5000", "admin", ["cadastrar", "listar", "atualizar"])
    gerenciamento_funcionarios.cadastro_funcionario(funcionario_admin, funcionario_admin)

    # Irá realizar o login do usuário
    usuario_logado = login(gerenciamento_funcionarios.funcionarios)
    if not usuario_logado:
        return  # Irá encerrar o programa caso o login falhe

    print("---------------------------------------------------------------------------------------")

    # Menu principal do programa
    while True:
        print("""Menu para Cadastro de Funcionários
              1. Cadastrar Funcionários
              2. Listar Funcionários
              3. Atualizar Dados do Funcionário
              4. Sair
              """)

        # Solicita ao usuário que escolha uma opção do menu
        escolha = input("Escolha uma das opções do menu: ")
        print("---------------------------------------------------------------------------------------")

        # Opção de entrada de dados do funcionário a ser cadastrado
        if escolha == '1':
            matricula_funcionario = input("Digite a Matrícula do Funcionário: ")
            nome_funcionario = input("Digite o nome do Funcionário: ")
            cpf = input("Digite o CPF do Funcionário: ")
            email = input("Digite o E-Mail do Funcionário: ")
            telefone = input("Digite o Telefone do Funcionário: ")
            endereco = input("Digite o Endereço do Funcionário: ")
            cargo = input("Digite o Cargo do Funcionário: ")
            salario = input("Digite o Salário do Funcionário R$: ")
            tipo_login = input("Digite o Tipo de Login do admin/usuário: ")
            permissoes = input("Digite as Permissões (Separadas por vírgula): ").split(',')

            # Variável que irá receber as informações do funcionário
            funcionario = Funcionario(nome_funcionario, cpf, email, telefone, endereco, matricula_funcionario, cargo, salario, tipo_login, permissoes)
            gerenciamento_funcionarios.cadastro_funcionario(funcionario, usuario_logado)

            print("---------------------------------------------------------------------------------------")

        # Opção de impressão dos funcionários cadastrados
        elif escolha == '2':
            gerenciamento_funcionarios.lista_funcionarios(usuario_logado)
            print("---------------------------------------------------------------------------------------")

        # Opção de atualização dos dados cadastrais do funcionário
        elif escolha == '3':
            matricula_funcionario = input("Digite a matrícula do funcionário que deseja atualizar os dados: ")
            funcionario_existente = gerenciamento_funcionarios.buscar_funcionario_por_matricula(matricula_funcionario)

            if funcionario_existente:
                while True:
                    print(f"{funcionario_existente}")
                    print("""Qual dos dados será atualizado?
                             1. Atualizar o E-mail
                             2. Atualizar o Telefone
                             3. Atualizar o Endereço
                             4. Atualizar o Cargo
                             5. Atualizar o Salário
                             6. Atualizar Permissões de Acesso
                             7. Voltar ao Menu Principal """)

                    escolha_atualizacao = input("Escolha a opção que deseja atualizar: ")

                    if escolha_atualizacao == '1':
                        novo_email = input("Digite o novo E-mail do Funcionário: ")
                        gerenciamento_funcionarios.atualizar_funcionario(funcionario_existente, email=novo_email)
                    elif escolha_atualizacao == '2':
                        novo_telefone = input("Digite o novo Telefone do Funcionário: ")
                        gerenciamento_funcionarios.atualizar_funcionario(funcionario_existente, telefone=novo_telefone)
                    elif escolha_atualizacao == '3':
                        novo_endereco = input("Digite o novo Endereço do Funcionário: ")
                        gerenciamento_funcionarios.atualizar_funcionario(funcionario_existente, endereco=novo_endereco)
                    elif escolha_atualizacao == '4':
                        novo_cargo = input("Digite o novo Cargo do Funcionário: ")
                        gerenciamento_funcionarios.atualizar_funcionario(funcionario_existente, cargo=novo_cargo)
                    elif escolha_atualizacao == '5':
                        novo_salario = input("Digite o novo Salário do Funcionário: ")
                        gerenciamento_funcionarios.atualizar_funcionario(funcionario_existente, salario=novo_salario)
                    elif escolha_atualizacao == '6':
                        novas_permissoes = input("Digite as novas Permissões (separadas por vírgula): ").split(',')
                        gerenciamento_funcionarios.atualizar_permissoes(funcionario_existente, novas_permissoes)
                    elif escolha_atualizacao == '7':
                        break
                    else:
                        print("Opção inválida, tente novamente!")
            else:
                print("Funcionário não encontrado, verifique se a matrícula foi digitada corretamente!")
                print("---------------------------------------------------------------------------------------")

        # Opção que irá encerrar o programa
        elif escolha == '4':
            print("Programa está sendo encerrado!")
            break

        # Mensagem de erro caso entre com alguma opção que não existe
        else:
            print("Opção inválida, escolha uma opção válida!")

# Executará o programa principal
if __name__ == "__main__":
    main()
    print("---------------------------------------------------------------------------------------")
