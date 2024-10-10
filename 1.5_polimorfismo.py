class Animal:
    def fazer_barulho(self):
        pass


class Gato(Animal):
    def fazer_barulho(self):
        print("Miau")


class Cachorro(Animal):
    def fazer_barulho(self):
        print("Au au")


def fazer_barulho(animal):
    animal.fazer_barulho()


gato = Gato()
cachorro = Cachorro()

# Perceba-se que aceita os dois objetos, isso é polimorfismo
# Pq ambos herdam `fazer_barulho` de Animal
fazer_barulho(gato)
fazer_barulho(cachorro)
