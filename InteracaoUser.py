import os
import sys
from salvar_importar import *
from time import sleep
from datetime import datetime
"""
/*Versao Final*/
geralConta={"data":None,"Nome":None,'TipoConta':None,
            "Poupanca":False,"Digital":False,"Investimento":False,
            "ExtratoPoupanca": False, "ExtratoDigital": False, "ExtratoInvestimento": False,
            'Taxa':None,'Rendimento':0}
"""
geralConta={"data":None,"Nome":None,'TipoConta':None,
            "Poupanca":False,"Digital":False,"Investimento":False,
            'Taxa':None,'Rendimento':0}
tiposConta=['Poupanca','Digital','Investimento']

def Start():
    fala='Escolha a Opcao' \
         '\n1 - Novo Cliente' \
         '\n2 - Ja sou Cliente '
    lista=[1,2]
    while True:
        try:
            resp=int(input(fala))
            if resp in lista :
                break
            else:
                print('resposta Invalida')
        except:
            print('Erro Inesperado')
    return resp

def DigiteNome(tipoConta=1,Logar=True):
    if tipoConta=='1':
        fala='razao social da empresa:'
    else:
        fala='seu nome: '
    while True :
        try:
            res=input(f'Digite {fala} ')
            if not res.isdigit():
                if Logar:
                    if verificar_Existencia(f'{res}.key','BancoSenhas'):
                        return res.capitalize()
                    else:
                        print('Desculpa nao foi possivel encontrar sua conta')
                else:
                    if not verificar_Existencia(f'{res}.key','BancoSenhas'):
                        return res.capitalize()
                    else:
                        print('Desculpa mais ja consta em nosso sistema um cliente com este exato nome '
                              '\ntente nome diferente')
            else:
                print('Nome Invalido')
        except:
            print('Erro Inexperado')

def DigiteModalidadeDaConta():
    fala=FalaAddTpConta('Qual modalidade de Conta deseja:')
    conta=geralConta
    y=0
    while True :
        try:
            res=input(f'{fala}')
            if res.isdigit():
                conta[tiposConta[int(res)-1]]=None
                y+=1
                if y < len(tiposConta):
                    prx=FalaGeralSN('Deseja adicionar outra modalidade')
                    if not prx:
                        break
                    else:
                        fala=FalaAddTpConta(fala='Qual modalidade de Conta deseja:',contaAtual=conta)
                        if fala==None:
                            break
                else:
                    break

            else:
                print('Nome Invalido')
        except:
            print('Erro Inexperado')
    return conta

def FalaGeralSN(Fala=''):
    while True:
        resp=input(f'{Fala} (S) (N): ')
        if resp.upper()=='S' or resp.upper()=='SIM':
            return True
        elif resp.upper()=='N' or resp.upper()=='NAO':
            return False
        else:
            limpar_terminal()
            print('Resposta Invalida')

def TipoCliente(fala='Qual tipo de conta deseja:'):
    while True:
        try:
            res = input(f'{fala}'
                        '\n(1) PJ'
                        '\n(2) PF\n')
            if res.isdigit():
                return res
            else:
                print('Nome Invalido')
        except:
            print('Erro Inexperado')

def FazerRetirada(ContaCliente,Saldos):
    if len(Saldos)==0:
        print('Voce esta com saldo zerado, faca deposito para evitar fechamento automatica da sua conta')
        sleep(5)
    else:
        fala, listaMod = FalaContaParaDeposito("Escolha tipo da Conta", ContaCliente,True)
        modalidade=EscolherTpConta(fala,listaMod)
        fala='Digite valor da Retirada '
        saldoAtual=Saldos[modalidade]
        saldoTotal=0
        sair=False
        for i in list(listaMod.keys()):
            saldoTotal+=Saldos[listaMod[i]]
        while True:
            try:
                resp=float(input(f'{fala}'))
                if resp > 0:
                    if saldoAtual > resp:
                        ContaCliente[modalidade]=round(ContaCliente[modalidade] - resp,2)
                        agora = datetime.now().strftime('%d/%m/%y %H:%M')
                        ContaCliente[f'Extrato{modalidade}'].append([agora,-resp])
                        print('Processando sua solicitacao')
                        Salvar(ContaCliente, 'BancoContas', ContaCliente["Nome"], "acc")
                        sleep(2)
                        sair=True
                        break
                    elif saldoTotal > resp:
                        Parcial = 0
                        falta = abs(resp - saldoAtual)
                        if len(list(listaMod.keys()))>2:
                            modusadas=[modalidade]
                            falaParcial=''
                            while True:
                                inicio=True
                                for i in list(listaMod.keys()):
                                    if not listaMod[i] in modusadas:
                                        outroMod = listaMod[i]
                                        modusadas.append(listaMod[i])
                                        if inicio:
                                            falaParcial+=outroMod
                                            inicio=False
                                        else:
                                            falaParcial+=f':\n{outroMod}'
                                Parcial+=Saldos[outroMod]
                                if (Parcial+saldoTotal)>=0:
                                    print(f'Não tem saldo suficiente na {modalidade}')
                                    if inicio:
                                        aceit = FalaGeralSN(f'Aceitar retirar {falta}:\n{outroMod}:\n')
                                    else:
                                        aceit = FalaGeralSN(f'Aceitar retirar {falta}:\n{falaParcial}:\n')
                                    if aceit:
                                        sair = True
                                        agora = datetime.now().strftime('%d/%m/%y %H:%M')
                                        totalretirada=resp
                                        for i in  modusadas:
                                            if ContaCliente[i] <= totalretirada:
                                                totalretirada = abs(round(ContaCliente[i]-totalretirada,2))
                                                ContaCliente[f'Extrato{i}'].append([agora, -ContaCliente[i]])
                                                ContaCliente[i] = 0.0
                                            else:
                                                totalretirada = -abs(round(totalretirada,2))
                                                ContaCliente[f'Extrato{i}'].append([agora, totalretirada])
                                                ContaCliente[i] = abs(round(ContaCliente[i]-abs(totalretirada),2))
                                        print('Processando sua solicitacao')
                                        Salvar(ContaCliente, 'BancoContas', ContaCliente["Nome"], "acc")
                                        sleep(2)
                                        break
                                    else:
                                        sair=True
                                        break
                        else:
                            outroMod = ''
                            for i in list(listaMod.keys()):
                                if not listaMod[i]==modalidade:
                                    outroMod = listaMod[i]
                            falta = abs(resp - saldoAtual)
                            print(f'Não tem saldo suficiente na {modalidade}')
                            aceit = FalaGeralSN(f'Aceitar remover retirar {falta} da {outroMod}:\n')
                            if not aceit:
                                sair=True
                                break
                            else:
                                sair=True
                                ContaCliente[outroMod]=round(ContaCliente[outroMod]-falta,2)
                                agora = datetime.now().strftime('%d/%m/%y %H:%M')
                                ContaCliente[f'Extrato{modalidade}'].append([agora,-ContaCliente[modalidade]])
                                ContaCliente[f'Extrato{outroMod}'].append([agora, -falta])
                                ContaCliente[modalidade] = 0.0
                                Salvar(ContaCliente, 'BancoContas', ContaCliente["Nome"], "acc")
                                print('Processando solicitando')
                                sleep(2)
                                break
                    else:
                        print('Saldo insulficiente')
                else:
                    if sair:
                        break
                    else:
                        print('Erro de Digitacao')
                if sair:
                    break
            except:
                print('Erro de Digitacao')
    return ContaCliente

def FazerDeposito(ContaCliente,Nova=False):
    fala, listaMod = FalaContaParaDeposito("Escolha tipo da Conta", ContaCliente)
    modalidade=EscolherTpConta(fala,listaMod)
    if Nova:
        fala='Digite valor do deposito. Valor Abertura Minimo de 50$ '
    else:
        fala='Digite valor do deposito '
    while True:
        try:
            resp=float(input(f'{fala}'))
            if resp > 0:
                if Nova:
                    if resp < 50:
                        limpar_terminal()
                        print('Valor abaixo do Minimo')
                    else:
                        break
                else:
                    break
            else:
                print('Erro de Digitacao')
        except:
            print('Erro de Digitacao')
    agora=datetime.now().strftime('%d/%m/%y %H:%M')
    if ContaCliente[modalidade] is None:
        ContaCliente[f'Extrato{modalidade}']=[[agora, resp]]
        ContaCliente[modalidade]=resp
    else:
        ContaCliente[f'Extrato{modalidade}'].append([agora,resp])
        ContaCliente[modalidade]+=resp
    return ContaCliente

def Senha(fala='Crie sua Senha ',Nova=False):
    if Nova:
        print('Sua senha numerica de conter 6 numeros')
    while True:
        try:
            resp=input(f'{fala}')
            if resp.isdigit():
                if len(resp)==6:
                    if Nova:
                        if Valide(resp):
                            return resp
                    else:
                        break
                else:
                    if Nova:
                        print('Senha deve Conter 6 Digitos')
                    else:
                        print('Senha de 6 digitos')
            else:
                if Nova:
                    print('Senha Invalida')
        except:
            print('Erro de Digitacao da Senha')
    return resp

def FalaAddTpConta(fala,contaAtual=None):
    if contaAtual is None:
        contaAtual = geralConta
    j=0
    for i in range(len(tiposConta)):
        if not contaAtual[tiposConta[i]]:
            if not contaAtual[tiposConta[i]] is None:
                fala += f'\n{ i + 1 } - {tiposConta[i]} '
            else:
                j+=1
        else:
            j+=1
    if j==len(tiposConta):
        fala=None
    return fala

def FalaContaParaDeposito(fala,contaAtual=None,Retirada=False,Extrato=False):
    listaModalidades={}
    for i in range(len(tiposConta)):
        if contaAtual[tiposConta[i]]:
            fala += f'\n{ i + 1 } - {tiposConta[i]} '
            listaModalidades[i+1]=tiposConta[i]
        elif Extrato==True:
            if not contaAtual[tiposConta[i]]==False:
                fala += f'\n{i + 1} - {tiposConta[i]} '
                listaModalidades[i + 1] = tiposConta[i]
        if not Retirada:
            if contaAtual[tiposConta[i]] is None:
                fala += f'\n{ i + 1 } - {tiposConta[i]} '
                listaModalidades[i+1]=tiposConta[i]
    return fala,listaModalidades

def limpar_terminal():
    os.system('cls')

def EscolherTpConta(fala,Modalidade):
    listaPossivel=list(Modalidade.keys())
    while True:
        try:
            resp=input(fala)
            if resp.isdigit() and int(resp) in listaPossivel:
                break
            else:
                print('Escolha Invalida')
        except:
            print('Erro desconhecido')
    return Modalidade[int(resp)]

def OpcoesConta():
    fala='Escolha Opcao:' \
         '\n1 - Ver Saldo' \
         '\n2 - Depositar' \
         '\n3 - Retirada' \
         '\n4 - Extrato ' \
         '\n5 - Sair '

    listaOp=[1,2,3,4,5]
    while True:
        try:
            resp=int(input(fala))
            if resp in listaOp:
                break
            else:
                print('Opcao Invalida')
        except:
            print('Erro inesperado')
    return int(resp)

def Verificar_senha(Nome):
    vlr=Carregar('BancoSenhas',f'{Nome}.key')
    contErros=0
    fala='Digite sua Senha: '
    while True:
        try:
            resp=int(input(fala))
            if resp==int(vlr):
                print('Carregando dados da Conta')
                sleep(4)
                break
            else:
                print('Senha incorreta')
                contErros+=1
            if contErros==3:
                print('Exedida quandidade de Erros tento mais tarde')
                sys.exit()
        except:
            print('Erro Inesperado')
            contErros+=1

def Valide(senha):
    for i in range(len(senha) - 2):
        if (int(senha[i])==int(senha[i + 1]) - 1==int(senha[i + 2]) - 2) or (
                int(senha[i])==int(senha[i + 1]) + 1==int(senha[i + 2]) + 2):
            print('Senha não pode conter:'
                  '\n3 digitos em seguencia'
                  '\nCrescente ou Decresente')
            return False
    for i in range(len(senha)):
        if i==0:
            carac=senha[0]
        else:
            if carac==senha[i]:
                print('Senha não pode conter:'
                      '\n2 valores iguais em sequencia')
                return False
    return True

def MostrarExtrato(ContaCliente):
    fala, listaMod = FalaContaParaDeposito("Qual Conta deseja ver o Extrato:",ContaCliente,Extrato=True)
    modalidade=EscolherTpConta(fala,listaMod)
    while True:
        try:
            Extrato=list(ContaCliente[f'Extrato{modalidade}'])
            print(f'Extrato da sua conta {(modalidade).capitalize()}')
            for i in range(len(Extrato)):
                print(f'Data: {Extrato[i][0]} Valor {Extrato[i][1]}')
        except:
            print('Erro de Digitacao')
    return ContaCliente




