import pickle
import os

def verificar_Existencia(nome, pasta=False):
    #Verifica arquivo existe
    diretorio = os.getcwd()
    if not pasta == False:
        diretorio = os.path.join(diretorio, pasta)
    diretorio = os.path.join(diretorio, nome)
    julgamento = os.path.exists(diretorio)
    return julgamento

def verificar_se_pastar_existe(Nome):
    #Verifica se pasta existe se nao existir ele cria a mesma
    diretorio = os.getcwd()
    diretorio = diretorio + f'\\{Nome}\\'
    while not os.path.exists(diretorio):
        os.makedirs(diretorio)
        if os.path.exists(diretorio):
            break

def Salvar(memoria,pasta,nome,extensao):
    diretorio = os.getcwd()
    filename = f'{diretorio}\\{pasta}\\{nome}.{extensao}'
    with open(filename, 'wb') as file:
        pickle.dump(memoria, file)

def Carregar(Pasta, nome):
    diretorio = os.getcwd()
    filename = f'{diretorio}\\{Pasta}\\{nome}'
    with open(filename, 'rb') as file:
        modelo_carregado = pickle.load(file)
    return modelo_carregado

def Lista_de_Arquivos(pasta):
    diretorio = os.getcwd()
    filename = f'{diretorio}\\{pasta}'
    verificar_se_pastar_existe(pasta)
    preLista=os.listdir(filename)
    return preLista

