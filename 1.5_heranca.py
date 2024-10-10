class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf


class PessoaJuridica(Pessoa):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj
