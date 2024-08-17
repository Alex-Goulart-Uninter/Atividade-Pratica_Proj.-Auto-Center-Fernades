#Classe produtos representa os produtos a serem caastados
class Produto:
    def __init__(self, nome_produto, codigo_produto, marca, quantidade_estoque, valor_unitario):
        self.nome_produto = nome_produto
        self.codigo_produto = codigo_produto
        self.marca = marca
        self.quantidade_estoque = quantidade_estoque
        self.valor_unitario = valor_unitario

# Essa função irá exibir os produtos cadastrados
    def __repr__(self):
        return (f""" 
                Produto  Nome: '{self.nome_produto}', 
                         Código: '{self.codigo_produto}', 
                         Marca: '{self.marca}',
                         Quantidade em estoque: '{self.quantidade_estoque}',
                         Valor unitario: R$'{self.valor_unitario:.2f}',
                """)

#Classe que gerencia a lista de produtos cadastrados
# Lista criada somente para demonstração do exercicio em um caso real seria utilizado um banco de dados.
class GerenciamentoDeProdutos:
    def __init__(self):
        self.produtos = [] # inicializado a lista que servirá de banco de dados temporário

#Função que irá adicionar um novo produto na lista de produtos
    def cadastro_produto(self, produto):
        self.produtos.append(produto)
        print(f"""Produto: {produto.nome_produto} - Codigo: {produto.codigo_produto} - Marca: {produto.marca} - Valor Unitário: R${produto.valor_unitario}
              cadastrado com sucesso!!""")

#Função verifica se há produtos cadastrados e os imprime
    def lista_produtos(self):
        if not self.produtos:
            print('Não há produtos cadastrados!')

        else:
            print("\nLista de Produtos Cadastrados: ")
            for produto in self.produtos:
                print(produto)

            #Irá exibir o valor total em estoque
            total = self.valor_total_estoque() 
            print(f"Valor total em estoque: R${total:.2f}")

#Função que irá efetuar o calculo do valor total em estoque
    def valor_total_estoque(self):
        return sum(produto.quantidade_estoque * produto.valor_unitario for produto in self.produtos)

#Programa principal
#Função para executar o programa principal
def main():
    
    #Instancia de gerenciamento dos produtos
    gerenciamento_produto = GerenciamentoDeProdutos()

    #Menu principal do programa
    while True:
        print(""" \nOpções
              1. Cadastrar Produtos
              2. Listar Produtos
              3. Sair """)
        
    # Solicitação para que o usuário esolha um opção do menu
        escolha = input('Entre com algumas das opções do menu: ')

        #Essa opçõa irá solicita ao usuário as informações do produto a ser cadastrado
        if escolha == '1':
            nome_produto = input("Digite o nome do produto: ")
            codigo_produto = input("Digite o código do produto: ")
            marca = input("Digite a marca do produto: ")
            quantidade_estoque = int(input("Digite a quandtidade do produto no estoque: "))
            valor_unitario = float(input("Digite o valor unitario do produto:"))
        
            #Variável que ira receber as informações do produto
            produto = Produto(nome_produto, codigo_produto, marca, quantidade_estoque, valor_unitario)

            #Gera o cadastro do produto no gerenciamento_produto
            gerenciamento_produto.cadastro_produto(produto)
        
        #Essa opção irá imprimir todos os produtos que estão cadastrados
        elif escolha == "2":
            gerenciamento_produto.lista_produtos()

        #Essa opção irá encerrar o programa
        elif escolha =='3':
            print("O programa esta sendo encerrado!!!")
            break

        #Em caso de erro durante a escolha das opções no menu será exibido uma mensagem de erro.
        else:
            print("Cuidado opção escolhida é inválida!!! Tente novamente.")

#Execução do script
if __name__ == "__main__":
    main()