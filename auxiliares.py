from salvar_importar import *
from InteracaoUser import *
FinalOperacao=False

def SalvarNovaSenhaCliente(Cliente,Senha):
    verificar_se_pastar_existe('BancoSenhas')
    Salvar(Senha,'BancoSenhas',Cliente,'key')

def SalvarConta(conta):
    verificar_se_pastar_existe('BancoContas')
    Salvar(conta,'BancoContas',conta['Nome'],'acc')

def TaxacaoConta(conta):
    """
    1 - PP = Poupanca - Tarifa = 0
    2 - CD = ContaDigital Tarifa = $20 / mes
    3 - PI = ContaInvestimento
    Tarifa = % 2 / rendimentoMes
    """
    taxa=0
    if not conta['Digital']:
        taxa+=20
    if not conta['Investimento']:
        taxa+=conta['Rendimento']*0.02
    return taxa

def NovoCliente():
    limpar_terminal()
    tipo_cliente =TipoCliente()
    NomeCliente=DigiteNome(tipo_cliente,Logar=False)
    SenhaCliente=Senha(Nova=True)
    conta =DigiteModalidadeDaConta()
    data_abertura = datetime.now().strftime('%d/%m/%y %H:%M')
    #{"data":None,"Nome":None,"Poupanca":False,"Digital":False,"Investimento":False,'Taxa':None,"Rendimento":0}
    conta["data"]=data_abertura
    conta["Nome"]=NomeCliente
    conta["Taxa"]=TaxacaoConta(conta)
    conta['TipoConta']=tipo_cliente
    print('Faça Primeiro Deposito')
    conta=FazerDeposito(conta,True)
    SalvarNovaSenhaCliente(NomeCliente, SenhaCliente)
    SalvarConta(conta)
    sleep(3)
    print('Seu Deposito foi concluido com Sucesso')
    sleep(5)

def Cliente(conta=None):
    if not conta is None:
        contaAtual=conta
    else:
        contaAtual=Logar()
    while True:
        resp=OpcoesConta()
        if resp==1:
            VerSaldo(contaAtual)
        elif resp==2:
            contaAtual=FazerDeposito(contaAtual, Nova=False)
            Salvar(contaAtual,'BancoContas',f'{contaAtual["Nome"]}','acc')
        elif resp==3:
            saldos=VerSaldo(contaAtual,mostrar=False)
            FazerRetirada(contaAtual,saldos)
        elif resp==4:
            MostrarExtrato(contaAtual)
        elif resp==5:
            break


def VerSaldo(conta,mostrar=True):
    saldo=0
    lista={}
    for i in range(len(tiposConta)):
        if conta[tiposConta[i]]:
            parcial=Saldo(conta,tiposConta[i])
            lista[tiposConta[i]]=parcial
            saldo+=parcial
            if mostrar:
                print(f'Seu saldo na {tiposConta[i]} é de {parcial}')
    if mostrar:
        print(f'Seu saldo Total atual é de {saldo}')
    return lista

def Logar():
    TpConta=TipoCliente('Qual modalidade de conta:')
    Nome=DigiteNome(TpConta,Logar=True)
    Verificar_senha(Nome)
    return Carregar('BancoContas',f'{Nome}.acc')

def Saldo(Account,TipoConta):
    saldo=0
    if Account[TipoConta]:
        saldo=Account[TipoConta]
    return saldo


if __name__ == '__main__':
    pass
    conta=Carregar('BancoContas',f'ContaTeste.acc')
    print(conta)
    #print(conta)
    #VerSaldo(conta)
    #Cliente(conta)
    #FazerDeposito(conta, Nova=False)
    #print(conta)
    saldos = VerSaldo(conta, mostrar=False)
    #MostrarExtrato(conta)
    FazerRetirada(conta,saldos)


