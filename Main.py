from datetime import datetime
from auxiliares import *
from InteracaoUser import *
from time import sleep
"""
Tipo Cliente = 
1 - PJ - Pessoa Juridica
2 - PF - Pessoa Fisica
Tipo Conta 
1 - PP = Poupanca    -       Tarifa = 0 
2 - CD = ContaDigital        Tarifa = $20/mes
3 - PI = ContaInvestimento   Tarifa = %2/rendimentoMes
pode ter ter mais de uma modalidade exemplo 1,2,3 ou 2,3 ou 1,3
"""




def Main():
    while True:
        limpar_terminal()
        resp=int(Start())
        if resp==1:
            NovoCliente()
        else:
            Cliente()


if __name__=='__main__':
    Main()




