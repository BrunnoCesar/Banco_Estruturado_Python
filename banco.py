saldo,LIMITE_DIARIO, LIMITE_SAQUE,opt= 0,3,500," "
def Depositar(valor):   
    global saldo  ; saldo += valor  ; return f"deposito de R${valor:.2f} efetuado seu saldo é R${saldo:.2f}"

def Sacar():
    global saldo, LIMITE_DIARIO , LIMITE_SAQUE
    if LIMITE_DIARIO == 0 : print('Você atingiu seu limite diário de saques ')
    sacar = float(input(f"Você ainda pode fazer : {LIMITE_DIARIO} saque[s]\nQUANTO Você GOSTARIA DE SACAR ? : "))
    if sacar > saldo : print('Você não pode sacar mais do que tem')
    elif saldo == 0 : print('Você não tem nada para sacar')
    elif sacar > 500 : print('Você não pode sacar mais que R$ 500,00')
    else : saldo -= sacar ; LIMITE_DIARIO -= 1 ; print('saque efetuado')

def Mostrar_Saldo() : print(f"R$:{saldo:.2f}")

while True:
    print('''
    1- depositar
    2- sacar
    3- mostrar saldo
    4- sair         
          ''')
    opt = input("digite a opção: ")
    if opt == "1" : print(Depositar(float(input("informe quanto vc gostaria de depositar: "))))
    elif opt == "2" : Sacar()
    elif opt == "3" : Mostrar_Saldo()
    elif opt == "4" : break
    else : print("opção inválida")