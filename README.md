# AppBancaPython
Um App Python para simular um sistema de banco, para efeito de estudo

App conta com 5 arquivos .py  e 2 pasta para simular banco de dados sao criadas automaticamente.
---Main.py              Iniciar a aplicacao
---auxiliares.py        Interacoa interna do menu
---InteracaoUser.py     Interacoes com o usuario
---TituloArquivo.py     so mudo o nome do Titulo no MSDOS
---salvar_importar.py   salvar e importa, e verifica se existe os arquivos


Menu Inicial 

---Novo Cliente
-----Adicionar novo cliente
-------Deposito Inicial Minimo 50$

---Ja Sou Cliente
-----Verificacoes na conta
--------Ver Saldo
--------Deposito
--------Retirada
--------Extrato
--------Sair


A Aplicacao conta:
Verificacao de senha: senha de 6 digitos, nao aceita 2 numeros iguais em sequencia, 3 ou mais numeros em sequencia crescente ou descrente.
Verificador de resposta: ele valida resposta do usuario, ve se resposta e a esperada. se nao fica no loop.

Banco de Dados 
2 Pasta
---BancoContas:
-----Salva dados da conta data criacao da conta , nome cliente , saldos , extratos, tarifas , rendimento
---BancoSenhas:
-----Arquivo que nome do arquivo é nome do cliente e nele so contem a senha

Não sei como funciona esse sistema em bancos reais, mais acredito que conforme eu implementei 
seja opcao viavel de so carregar dados de um cliente e nao e vasta lista com dados de varias cliente 
onde pode ser manipulado de forma erradas, e com isso pode em casa real vai gerar muitas arquivos, 
porem isso deve ser facilmente organizado pelo numero das agencias e acredito que seja perto de como 
é na realidade. 



