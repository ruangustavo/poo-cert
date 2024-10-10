# Nota: ctz que cai
# Atributo público -> acessível por qualquer parte do código
# Atributo protegido -> acessível por a classe e suas subclasses
# Atributo privado -> acessível apenas dentro da própria classe


class Pessoa:
    def __init__(self, nome, idade, salario):
        self.nome = nome  # Atributo público
        self._idade = idade  # Atributo protegido (representado com um underscore)
        self.__salario = salario  # Atributo privado (representado com dois underscores)

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self._idade}")
        print(f"Salário: {self.__salario}")

    def _mostrar_idade(self):
        print(f"Idade (protegido): {self._idade}")

    def __mostrar_salario(self):
        print(f"Salário (privado): {self.__salario}")


pessoa = Pessoa("Ruan", 14, 100)
print(pessoa.nome)
pessoa.mostrar_dados()
