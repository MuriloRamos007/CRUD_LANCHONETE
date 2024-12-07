class Cliente:

    def __init__(self, parCod, parNome, parCpf, parendereco, parTelefone):
        self.cod=parCod
        self.Nome=parNome
        self.Cpf=parCpf
        self.endereco=parendereco
        self.Telefone=parTelefone

    def Listar(self):
        print(f"Cod.: {self.cod}"
              f"| Nome: {self.Nome}"
              f"| Cpf: {self.Cpf}"
              f"| Endereço: {self.endereco}"
              f"| Telefone: {self.Telefone}")