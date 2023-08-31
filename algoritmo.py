from Classes import *
import os

def main():
    indice = 00
    sair = False
    while sair == False:
        try:

            print("--- MENU ---")
            print("01 - ADICIONAR TAREFA")
            print("02 - EXCLUIR TAREFA")
            print("03 - LISTAR TAREFA")
            print("00 - SAIR")
            print("------------")
            print("  ")

            print("Qual opção deseja:")
            menu = int(input("->"))
            os.system("pause")

            match menu:
                case 1:
                    id = indice +1
                    os.system("cls")
                    print("--- ADICIONAR TAREFAS ---")
                    descricao = input("Tarefa - ")

                    ToDoList.adicionar_tarefas(id,descricao)
                    print("TAREFA REGISTRADA")
                    print("----------==-----")
                    os.system("pause")

                case 2:
                    os.system("cls")
                    print("--- EXCLUIR TAREFA ---")

                    ToDoList.excluir_tarefa.tarefas(id,descricao)
                    print("TAREFA EXCLUIDA")
                    print("---------------")
                    os.system("pause")

                case 3:
                    os.system("cls")
                    print("--- LISTAR TAREFAS ---")
                    ToDoList.listar_tarefa()
                    os.system("pause")

                case 0: 
                    os.system("cls")
                    print(" SAINDO ...")
                    print(" ")
                    sair = True
                
                case _:
                    print("Valor Inválido")

        except Exception as erro:
            print("Valor invalido")
            print("Erro: ", erro.__class__.__name__)
            print("")

