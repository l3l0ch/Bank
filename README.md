import time

class ContaBancaria:

    def __init__(self, nome: str, numero: str, saldo: float):
        self.__titular = nome
        self.numero_conta = numero
        self._saldo = saldo

    def depo(self, depo):
        assert depo > 0
        if type(depo) == int or type(depo) == float:
            self._saldo += depo

    def saq(self, saq):
        self._saldo -= saq

    def verificando_possibilidade_saque_corrente(self,saque):
        total = ContaCorrente._CHEQUE_ESPECIAL + self._saldo
        if saque > total:
            raise SaldoInsuficiente(f'Não há saldo para R$ {saque} em conta corrente.')

    def verificando_possibilidade_saque_poupanca(self, saque):
        if saque > self._saldo:
            raise SaldoInsuficiente(f'Não há saldo para R$ {saque} em conta poupança.')

    def __str__(self) -> str:
        return f'''
        Titular: {self.__titular}
        Saldo: {self._saldo:.2f}
        Número da Conta: {self.__numero_conta}
        '''

    @property
    def nome(self):
        return self.__titular

    @nome.setter
    def nome(self, newnome):
        self.__titular = newnome

    @property
    def numero_conta(self):
        return self.__numero_conta

    @numero_conta.setter
    def numero_conta(self, number):
        assert len(number) == 7 and number[5] == '-' and number[0:5].isdigit() and number[6] in '1234567890xX', "Número da Conta Inválido. Formato: 12345-X ou 12345-0"
        self.__numero_conta = number

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, newsaldo):
        assert newsaldo >= 0, print('Saldo não pode ser negativo, precisa ser maior ou igual que 0 !')
        assert type(newsaldo) == float or type(newsaldo) == int, print('Saldo Precisa Sser Int ou Float')
        self._saldo = newsaldo

class LimiteChequeEspecialExcedente(Exception):
    pass

class ContaPoupanca(ContaBancaria):

    def __init__(self, nome: str, numero: str, saldo: float, taxa_juros: float = 0.010):
        super().__init__(nome, numero, saldo)
        # taxa juros entre 0 a 1, Ex: 0.20, 0.15
        self._taxa_juros = taxa_juros

    def ganhoanual(self):
        self.ganho_anual = (super().saldo * self._taxa_juros)
        # self.ganho_anual = (super().saldo * ((1 + self._taxa_juros) ** 12))
        return f'{self.ganho_anual:.2f}'

    def __str__(self) -> str:
        return f'''
        {super().__str__()}Taxa de Juros: {self._taxa_juros}
        '''

    @property
    def taxa(self):
        return self._taxa_juros

    @taxa.setter
    def taxa(self,ntaxa):
        # self.__taxa_juros = taxa_juros if taxa_juros >= 0 and taxa_juros <= 1 else print('Informe uma taxa valida !')
        assert 0 <= ntaxa <= 1, print('Taxa Fora do Padrão de 0 à 1 !')
        self._taxa_juros = ntaxa

class SaldoInsuficiente(Exception):
    pass

class ContaCorrente(ContaBancaria):

    _CHEQUE_ESPECIAL = 1000.00

    def __init__(self, nome: str, numero: str, saldo: float):
        super().__init__(nome, numero, saldo)

    def saq_cheque_especial(self, saque):
        if self._saldo <= 0:
            assert saque <= ContaCorrente._CHEQUE_ESPECIAL, print(f'Saldo insuficiênte Para Saque de R$ {saque:.2f} do Cheque Especial')
            print('Operação Realizada Com Sucesso.')
            ContaCorrente._CHEQUE_ESPECIAL -= saque
            self._saldo = ContaCorrente._CHEQUE_ESPECIAL - (ContaCorrente._CHEQUE_ESPECIAL + saque)

    def __str__(self) -> str:
        return f"""
        {super().__str__()}
        Cheque Especial: {ContaCorrente._CHEQUE_ESPECIAL:.2f}
"""

    @property
    def cheque_especial(self):
        return ContaCorrente._CHEQUE_ESPECIAL

    @cheque_especial.setter
    def cheque_especial(self,valor):
        assert ContaCorrente._CHEQUE_ESPECIAL >= 0, print('Limite do Cheque Especial precisa ser maior que 0 !')
        assert type(ContaCorrente._CHEQUE_ESPECIAL) == float or type(ContaCorrente._CHEQUE_ESPECIAL) == int, print('Cheque especial precisa ser um int ou float')
        ContaCorrente._CHEQUE_ESPECIAL = valor
        if valor > 2000:
            raise LimiteChequeEspecialExcedente(' Valor atribuido ao cheque especial é superior ao limite')

if __name__ == '__main__':

    def menu_operacoes():
        print('''
        +-----------------------------------+
                    OPERAÇÕES
        +-----------------------------------+
        [1] - Extrato
        [2] - Deposito Na Poupança
        [3] - Deposito Na Conta Corrente   
        [4] - Saque Conta Poupança    
        [5] - Saque Conta Corrente
        [6] - Saque Cheque Especial
        [7] - Saldo Conta Corrente
        [8] - Saldo Conta Poupança
        [9] - Rendimento Anual Poupança
        +-----------------------------------+
        [0] - Sair da Conta 
        +-----------------------------------+
        ''')

    def informacoes_conta_corrente():
        print('+------------------Conta Corrente-------------------+')
        print(conta_corrente)
        print('+---------------------------------------------------+')

    def informacoes_conta_poupanca():
        print('+------------------Conta Poupança-------------------+')
        print(conta_poupanca)
        print('+---------------------------------------------------+')

    def rendimentos_anuais_poupanca():
        print(f'Rendimentos Anuais R$ {conta_poupanca.ganhoanual()}')

    while True:
        try:
            name = input('Titular: ')
            numero = str(input('Número da Conta: '))
            conta_poupanca = ContaPoupanca(name, numero, 1000.00)
            conta_corrente = ContaCorrente(name, numero, 0.00)
            break
        except AssertionError as msg:
            print(msg)
            continue

    while True:
        menu_operacoes()
        try:
            operacao = int(input('Selecione Uma Operação: '))
            assert 0 <= operacao <= 9, "Operacação Inválida. Tente Novamente!"
        except AssertionError as msg:
            print(msg)
            continue
        except ValueError as msg:
            print(msg)
            continue

        if operacao == 0:
            print('Encerrando Operações...')
            time.sleep(2)
            break

        elif operacao == 1:
            informacoes_conta_corrente()
            informacoes_conta_poupanca()
            rendimentos_anuais_poupanca()
            continue
        elif operacao == 2:
            deposito = float(input('Valor: '))
            conta_poupanca.depo(deposito)
            print(conta_poupanca)
            continue
        elif operacao == 3:
            deposito = float(input('Valor: '))
            conta_corrente.depo(deposito)
            print(conta_corrente)
            continue
        elif operacao == 4:
            try:
                saque = float(input('Saque: '))
                conta_poupanca.verificando_possibilidade_saque_poupanca(saque)
                conta_poupanca.saq(saque)
                print(conta_poupanca)
            except SaldoInsuficiente as msg:
                print(msg)
                pass
            continue
        elif operacao == 5:
            try:
                saque = float(input('Saque: '))
                conta_corrente.verificando_possibilidade_saque_corrente(saque)
                conta_corrente.saq(saque)
                print(conta_corrente)
            except SaldoInsuficiente as msg:
                print(msg)
                pass
            continue
        elif operacao == 6:
            try:
                saque = float(input('Saque: '))
                conta_corrente.saq_cheque_especial(saque)
            except AssertionError as msg:
                print(msg)
                pass
            print(conta_corrente)
            continue
        elif operacao == 7:
            informacoes_conta_corrente()
            continue
        elif operacao == 8:
            informacoes_conta_poupanca()
            continue
        elif operacao == 9:
            rendimentos_anuais_poupanca()
            continue
