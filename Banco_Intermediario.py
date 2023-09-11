opt = ""
Clientes_Dict,Conta_Dict= {} ,{}
saldo,LIMITE_DIARIO, LIMITE_SAQUE,opt= 0,3,500," "

def Add_Saldo(saldo,valor):
    saldo += valor 
    return saldo

def Is_CPF(cpf) : 
    if cpf in Clientes_Dict : return True

def GerarConta() :
    num_conta = 1000 * len(Clientes_Dict)
    return str(num_conta)[::-1]

def Get_Cpf(Clientes_Dict):
    cpf = input("digite seu cpf:  ")
    if Is_CPF(cpf) : print("o cpf já está cadastrado tente novamente" ) ; return Get_Cpf(Clientes_Dict)
    return cpf

def Add_Cliente():
    cpf = Get_Cpf(Clientes_Dict)
    Clientes_Dict[cpf] = [input("digite seu nome: "),input("digite sua idade: ")]
    Conta_Dict[cpf] = [input("digite uma senha : "),GerarConta(),0] #o último valor representa o saldo
    return cpf

def Depositar(valor,cpf):   
    Conta_Dict.get(cpf)[2]  ; Conta_Dict.get(cpf)[2] += valor  ; return f"deposito de R${Conta_Dict.get(cpf)[2]:.2f} efetuado seu saldo é R${Conta_Dict.get(cpf)[2]:.2f}"

def Sacar(cpf):
    global LIMITE_DIARIO , LIMITE_SAQUE
    if LIMITE_DIARIO == 0 : print('Você atingiu seu limite diário de saques ')
    sacar = float(input(f"Você ainda pode fazer : {LIMITE_DIARIO} saque[s]\nQUANTO Você GOSTARIA DE SACAR ? : "))
    if sacar > Conta_Dict.get(cpf)[2] : print('Você não pode sacar mais do que tem')
    elif Conta_Dict.get(cpf)[2] == 0 : print('Você não tem nada para sacar')
    elif Conta_Dict.get(cpf)[2] > 500 : print('Você não pode sacar mais que R$ 500,00')
    else : Conta_Dict.get(cpf)[2] -= sacar ; LIMITE_DIARIO -= 1 ; print('saque efetuado')

def Mostrar_Saldo(cpf) : print(f"R$:{Conta_Dict.get(cpf)[2]:.2f}")

while True :
    print(""" 1-Cadastrar Cliente e Conta
              2 -Caixa eletronico 
              3 - Sair
          """)
    opt = input("digite a opcão desejada : ")

    if opt == "1" : Add_Cliente()
    elif opt == "2" :
        cpf = input("Digite o seu cpf : ")
        if Is_CPF(cpf) :
            senha = input("Digite sua senha ")
            if Conta_Dict.get(cpf)[0] == senha :
                #opt = ""                
                while True:
                     print(f"Seja bem-vindo {Clientes_Dict.get(cpf)[0]} Conta: {Conta_Dict.get(cpf)[1]}4")
                     print('''
                           1- depositar
                           2- sacar
                           3- mostrar saldo
                           4- sair         
                           ''')
                     opt = input("digite a opção: ")
                     if opt == "1" : print(Depositar(float(input("informe quanto vc gostaria de depositar: ")),cpf))
                     elif opt == "2" : Sacar(cpf)
                     elif opt == "3" : Mostrar_Saldo(cpf)
                     elif opt == "4" : break
                     else : print("opção inválida")

            else :
                print("a senha não confere voltando ao menu principal")
                
        else :
            print("esse cpf não pertence a um de nossos correntistas voltando ao menu principal")
    elif opt == "3" : break
    else : print("Opção inválida")

        

        
    


