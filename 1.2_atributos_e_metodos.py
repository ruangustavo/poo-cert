class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Salve, meu nome é {self.nome}!")


ruan = Pessoa("Ruan")
ruan.apresentar()
