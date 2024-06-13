conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2600
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Sque realizado com o uso do cheque especial!")
elif conta_universitaria:   
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")