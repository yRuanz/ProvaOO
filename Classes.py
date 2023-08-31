class ToDoList:
    def __init__(self, data):
        self.data = data
        self.tarefa = {}


    def adicionar_tarefas(self, descricao: str): # Recebe a descrição de uma tarefa como parâmetro e a adiciona à lista de tarefas.
        self.id = id
        self.descricao = descricao
        self.tarefa[self.id] = [self.descricao]
        for chave, valor in self.tarefa.items():
            print(f"{chave}. {descricao}")

    def excluir_tarefa(self, indice: int): # Recebe o índice de uma tarefa na lista e a remove.
        self.indice = id
        self.descricao = descricao
        self.tarefa[self.id] = [self.descricao]
        for chave, valor in self.tarefa.items():
            print(f"{chave}. {descricao}")


    def listar_tarefa(self): # Exibe na tela todas as tarefas presentes na lista, numeradas sequencialmente.
        for chave, valor in self.tarefa.items():
            print(f"{chave}. {descricao}")