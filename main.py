menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        
        valor = input("Forneça o valor do depósito:")

        valor = float(valor)

        if valor > 0:

            saldo += valor
            extrato = extrato + f'depósito: R$ {valor:.2f}\n'
        else:
            print('Não é possivel depósitar valores negativos, faça o depósito novamente')
    
    elif opcao == "s":

        if numero_saques < LIMITE_SAQUES:
            valor = input('Valor do saque:')
            valor = float(valor)

            if valor <= 500:

                if valor <= saldo:
                    saldo -= valor
                    extrato = extrato + f'saque: R$ {valor:.2f}\n'
                    numero_saques +=1
                
                else:
                    print(f'Valor para saque indisponível, superior ao saldo de {saldo:.2f}')

            else:
                print('Não é possível realizar o saque porque o limite é R$ 500 por saque')

            

        else:
            print('Não é possível realizar o saque porque você atingiu o limite diário de saque')
        
    elif opcao == "e":

         print(extrato)
         print(f'saldo: R$ {saldo:.2f}')
       

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")