import sys

opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Depositar \n"))
saldo = 500.0

if opcao == 1:
    valor = float(input("Digite o valor que deseja sacar: "))
    if valor > saldo:
        print("Saldo insuficiente. Por favor, faça um depósito.")
    else:
        saldo -= valor
        print("Seu saldo atual é: R$ ", saldo)
elif opcao == 2:
    valor = float(input("Digite o valor que deseja depositar: "))
    saldo += valor
    print("Seu saldo atualizado é: R$ ", saldo)
else:
    sys.exit("Opção inválida")
      
                 