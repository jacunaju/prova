# Ana Julia Cruz Simplicio, Jaqueline Alves Benevides

# 1. o que é pipeline? pipeline é um termo usado em diversos contextos,porem conhecemos como um processo ou fluxo de trabalho composto por etapas sequenciais que transformam uma entrada inicial em um resultado final
# 2. o que são requisitos funcionais e nao funcionais? funcionais são os recursos utilizaveis e que aparecem no codigo, site e etc. ja o nao funiconal nao aparece. ex: funcional: pesquisas num site, categorias. nao funcionass: senha, email

class Pou:
    def __init__(self, tipo, cor):
        self.__tipo= tipo
        self.__cor= cor

    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, novo_tipo):
        self.__tipo = novo_tipo

    def get_cor(self):
        return self.__cor
    
    def set_cor(self, nova_cor):
        self.__cor = nova_cor

class Estoque:
    def __init__(self):
        self.__pous = []

    def add_pou(self, pou):
        self.__pous.append(pou)
        print(f"Tipo do pou: {pou.get_tipo()}, Cor: {pou.get_cor()} adicionado ao estoque.")

    def listar_pous(self):
        if not self.__pous:
            print("Nenhum Pou disponível no estoque.")
        else:
            for i, pou in enumerate(self.__pous, start=1):
                print(f"{i}. Tipo: {pou.get_tipo()}, Cor: {pou.get_cor()}")

pou = Pou("pontudo", "preto")

def menu(self, estoque):
    self.__estoque = Estoque(pou)
    print(f"{pou}")
    print(pou.get_tipo())  # Saída: pontudo
    print(pou.get_cor())   # Saída: preto

# Alterando os valores com os setters
    pou.set_tipo("gorducho")
    pou.set_cor("bege")
while True:
        print("1. Adicionar Pou")
        print("2. Listar Pous")
        print("3. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == "1":
            tipo = input("Digite o tipo do Pou: ")
            cor = input("Digite a cor do Pou: ")
            novo_pou = Pou(tipo, cor)
            estoque.add_pou(novo_pou)
        elif opcao == "2":
            estoque.listar_pous({pou})
        elif opcao == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

