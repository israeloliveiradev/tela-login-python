import customtkinter as ctk








print("=========================================================================")
print("                            SISTEMA DE GESTÃO                            ")
print("=========================================================================")

acesso = input("DIGITE SEU LOGIN DE ACESSO: ").upper()
senha = input("DIGITE SUA SENHA DE ACESSO: ")
if acesso != "ISRAEL":
    print("ACESSO NEGADO")
elif senha != "1234":
    print("ACESSO NEGADO")
else:
    nome = []
    preco = []
    categ = []
    quantidade = []

    while True:
        print(">>>>> MENU <<<<<")
        print("OLÁ ", acesso, " ACESSO LIBERADO")
        print("DIGITE [1] para ADD NOVOS PRODUTOS: ")
        print("DIGITE [2] para EXCLUIR PRODUTOS: ")
        print ("DIGITE [3] para VISUALIZAR O ESTOQUE: ")
        print("DIGITE [4] para SAIR: ")
        resposta = int(input("DIGITE AQUI: "))

        if resposta == 1:
            adicionar = "ADD"
            while adicionar == "ADD":
                nome.append(input("NOME DO PRODUTO: "))
                preco.append(float(input("PREÇO DO PRODUTO: ")))
                categ.append(input("CATEGORIA: "))
                quantidade.append(int(input("QUANTIDADE: ")))
                adicionar = (input("DIGITE \"ADD\" PARA ADICIONAR NOVOS PRODUTOS OU \"SAIR\" PARA VOLTAR AO MENU : ")).upper()

                #FIM ADD PRODUTOS

        elif resposta == 2:
                #EXCLUIR PRODUTOS
            print (">>> ESTOQUE DISPONÍVEL <<<<")
            for estoque in range(len(nome)):
                print("SKU: ", estoque+1, "-", nome[estoque], "| PREÇO: ", preco[estoque], "| CATEGORIA: ", categ[estoque], "| QUANTIDADE: ", quantidade[estoque])
            if len(nome) > 0:
                excluir_prod = int(input("DIGITE O SKU DO PRODUTO QUE DESEJA EXCLUIR: "))
                quant_ex = int(input("DIGITE A QUANTIDADE: "))
                del quantidade[estoque-1]
            else:
                print("O ESTOQUE ESTÁ VAZIO.")


        if resposta == 3:
            for estoque in range(len(nome)):
                print("SKU: ", estoque + 1, "-", nome[estoque], "| PREÇO: ", preco[estoque], "| CATEGORIA: ", categ[estoque], "| QUANTIDADE: ", quantidade[estoque])
            #SAIR
        elif resposta == 4:
            print("SAINDO...")
            break

        else:
            print("OPÇÃO INVALIDA. POR FAVOR, ESCOLHA UMA DAS OPÇÕES LISTADAS. ")


















