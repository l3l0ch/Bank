# class SaqueNaoPermitido( Exception ):
#     pass
class Caixa:

    def __init__(self, nota: int, valor_em_caixa: int):
        self.__nota = nota
        self.valorEmCaixa = valor_em_caixa
    def sacar(self, saque):
        # assert saque <= self.__valorEmCaixa, f"Valor em caixa insuficiente para saque R$ {saque}."
        # if saque > 0 or saque >= self.__valorEmCaixa:
        #     raise SaqueNaoPermitido("Saque Inválido !")
        assert type(saque) == int, "Saque deve ser um valor int"
        possiveis_saques = []
        for i in range ( 1, self.__valorEmCaixa + 1 ):
            a = i * self.nota
            possiveis_saques.append(a)
            if a == self.__valorEmCaixa:
                break
        assert saque in possiveis_saques, "Saque invalido, só é possível sacar notas de R$ 50,00"
        self.__valorEmCaixa -= saque
        return print(possiveis_saques)

    @property
    def nota(self):
        return self.__nota

    @property
    def valorEmCaixa(self):
        return self.__valorEmCaixa

    @valorEmCaixa.setter
    def valorEmCaixa(self, valor):
        assert valor > 0, "Atribuição do valor em caixa não pode ser negativo !"
        self.__valorEmCaixa = valor

    def __str__(self):
        return f"Nesse caixa só é possível sacar notas de R$ {self.__nota}\nValor em caixa: R${self.__valorEmCaixa}"

if __name__ == '__main__':

    try:
        caixa = Caixa(50,50)
        while True:
            try:
                print ( caixa )
                valor = int( input ( 'Saque: ' ) )
                caixa.sacar ( valor )
                print ( caixa.valorEmCaixa )
            except AssertionError as msg:
                print ( msg )
            except ValueError as msg:
                continue

    except AssertionError as msg:
        print ( msg )






# sacar
        # assert saque > 0, "Saque deve ser maior que 0 !"
        # # assert self.saldo % saque == 0, "Nota invalida !"
        # if self.valorEmCaixa <= 0 or saque > self.valorEmCaixa:
        #     raise SaldoInsuficiente(f"Não há saldo suficiente para R$ {saque}!")
