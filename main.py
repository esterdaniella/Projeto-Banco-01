from conta import Conta

# Criando a conta inicial
conta_dani = Conta(numero="123-4", titular="Dani", senha="123", saldo_inicial=500)

print("=-" * 25)
print(f"Bem-Vindo {conta_dani.titular}! Esse é o terminal do Banco Carvalho")
print("=-" * 25)

while True: 
    print("\n[1] Sacar")
    print("[2] Depositar")
    print("[3] Sair")
    print("[4] Extrato")

    opcao = input('Escolha uma opção: ')

    if opcao == "1": 
        try: 
            valor = float(input(f'Seu saldo é R$ {conta_dani.saldo:.2f}. Quanto deseja sacar? R$ '))
            conta_dani.sacar(valor)
        except ValueError: 
            print('Erro: Por favor digite apenas números.')

    elif opcao == "2": 
        try: 
            valor = float(input('Digite o valor que deseja depositar: R$ '))
            conta_dani.depositar(valor)
        except ValueError: 
            print('Erro: Por favor digite apenas números.')

    elif opcao == "3":
        print(f'Obrigada por usar nosso banco, {conta_dani.titular}!')
        break

    elif opcao == "4":
        conta_dani.exibir_saldo()

    else: 
        print('Opção inválida. Escolha entre 1 e 4.')