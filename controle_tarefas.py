
# PROJETO INTEGRADOR - UNISA
# Sistema Simples de Controle de Tarefas
# Linguagem: Python

# Lista para armazenar as tarefas
tarefas = []

# Lista para armazenar os status
status = []

# Repetir o menu ate o usuario escolher sair
while True:

    print("\n================================")
    print("     CONTROLE DE TAREFAS")
    print("================================")

    print("1 - Cadastrar tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Sair")

    opcao = input("\nEscolha uma opcao: ")

    # OPCAO 1 - CADASTRAR TAREFA
    if opcao == "1":

        tarefa = input("Digite o nome da tarefa: ").strip()

        if tarefa == "":
            print("O nome da tarefa nao pode ficar vazio.")

        else:
            tarefas.append(tarefa)
            status.append("Pendente")

            print("Tarefa cadastrada com sucesso!")

    # OPCAO 2 - VISUALIZAR TAREFAS
    elif opcao == "2":

        print("\nTAREFAS CADASTRADAS:")

        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")

        else:
            for i in range(len(tarefas)):
                print(
                    i + 1, "-",
                    tarefas[i],
                    "|", status[i]
                )

    # OPCAO 3 - CONCLUIR TAREFA
    elif opcao == "3":

        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")

        else:
            print("\nESCOLHA A TAREFA:")

            for i in range(len(tarefas)):
                print(
                    i + 1, "-",
                    tarefas[i],
                    "|", status[i]
                )

            numero = input(
                "\nDigite o numero da tarefa: "
            )

            if numero.isdigit():

                indice = int(numero) - 1

                if 0 <= indice < len(tarefas):

                    if status[indice] == "Concluida":
                        print("Esta tarefa ja foi concluida.")

                    else:
                        status[indice] = "Concluida"
                        print("Tarefa concluida com sucesso!")

                else:
                    print("Numero de tarefa invalido.")

            else:
                print("Digite apenas numeros.")

    # OPCAO 4 - SAIR
    elif opcao == "4":

        print("\nEncerrando o programa.")
        print("Obrigado por utilizar o sistema!")

        break

    # OPCAO INVALIDA
    else:
        print("Opcao invalida. Tente novamente.")
