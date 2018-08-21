import cadastro
import exibir
import atualiza
import remove

def menu():
    nomes = []
    escolha = ""
    while escolha != "0":
        escolha = input("1 - Cadastro | 2 - Mostrar | 3 - Atualizar | 4 - Deletar| 0 - Terminar \n")
        if(escolha == "1"):
            cadastro.cadastrar(nomes)
        elif(escolha == "2"):
            exibir.mostrar(nomes)
        elif(escolha == "3"):
            atualiza.atualizar(nomes)
        elif(escolha == "4"):
            remove.remove(nomes)

menu()
