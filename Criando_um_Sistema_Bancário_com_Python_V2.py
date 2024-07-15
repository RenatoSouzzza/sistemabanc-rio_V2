from time import sleep
from pprint import pprint

users = {}
gera_conta = 1

def menu():
    while True:
        try:
            opção = int(input(
""" *** OPERAÇÕES BANCÁRIAS ***
[1] Criar Usuário
[2] Criar/Atribuir Conta
[3] Depósito
[4] Saque
[5] Extrato
[0] Sair
=> Informe a opção Desejada: """))
            if 0 <= opção <= 5:
                break
            else:
                print('Verifique as opções de menu e selecione o serviço desejado')
        except ValueError:
            print('Verifique as opções de menu e selecione o serviço desejado')
    
    if opção == 0:
        print('Encerrando...')
        sleep(1)
    elif opção == 1:
        create_user()
    elif opção == 2:
        create_account(users)
    elif opção == 3:
        deposito(users)
    elif opção == 4:
        saque(users)
    elif opção == 5:
        extrato(users)
    '''elif opção == 6:
        print('Acessando menu Listar Contas...')# pendente
        sleep(2)'''
        

def create_user():
    print('Acessando menu Criar Usuário...')
    sleep(1)
    while True:
        print('Informe os dados a seguir: ')
        sleep(1)
        cpf = input('CPF: ')  
        nome = input('Nome: ')
        nasc = input('Nascimento: ')
        endereço = input('Endereço: ')
        user = {cpf: {'nome': nome, 'nasc': nasc, 'endereço': endereço}}
        users.update(user)
        cont = input('Deseja Continuar? (S/N): ').upper().strip()
        if cont == 'S':
            continue
        elif cont == 'N':
            break  
    menu()
        


def create_account(users):
    print('Acessando o menu Criar/Atribuir Conta...')
    sleep(1)
    global gera_conta
    cpf_found = False
    valida_cpf = input('Informe o CPF: ')  
    if valida_cpf in users:
        print(f'CPF {valida_cpf} já cadastrado para o cliente {users[valida_cpf]["nome"]}')
        sleep(1)
        print('Criando nova conta...')
        sleep(1)
        conta_num = gera_conta
        users[valida_cpf]['contas'] = users[valida_cpf].get('contas', {})
        users[valida_cpf]['contas'][conta_num] = {'agencia': '0001', 'saldo': 0, 'extrato': ''}
        gera_conta += 1
        cpf_found = True
        print('Retornando ao menu...')
        sleep(1)
        menu()
    if not cpf_found:
        print(f'CPF {valida_cpf} não cadastrado.')
        return_menu = int(input(""" 
[1] Consultar CPF
[2] Criar novo cadastro
[3] Voltar ao menu inicial """))
        if return_menu == 1:
            create_account(users)
        elif return_menu == 2:
            create_user()
        elif return_menu == 3:
            menu()


def deposito(users): # ajustar métodos
    print('Acessando menu Depósito...')
    sleep(1)
    print('Agência 0001')
    cpf = input('Informe o CPF: ')
    if cpf in users:
        print(f'Olá {users[cpf]["nome"]}! ')
        num_conta = int(input('Informe o número da conta: '))
        if num_conta in users[cpf].get('contas', {}):
            while True:
                valor = float(input('Valor do Depósito: R$: '))
                if valor > 0:
                    users[cpf]['contas'][num_conta]['saldo'] += valor
                    users[cpf]['contas'][num_conta]['extrato']+= f'Depósito no valor de R${valor:.2f}\n'
                    print(f"Depósito realizado com sucesso! Novo saldo: R${users[cpf]['contas'][num_conta]['saldo']:.2f}")
                    continuar = str(input('Continuar Depositando? (S/N): ')).upper().strip()
                    if continuar != 'S':
                        break
                else:
                    print('Valor deve ser maior que 0!')
        else:
            print('Número da conta não encontrado.')
    else:
        print('CPF não localizado! ')
    print('Retornando ao menu inicial...')
    sleep(1)
    menu()
    

def saque(users): # ajustar métodos
    print('Acessando menu Saque...')
    sleep(1)
    print('Agência 0001')
    cpf = input('Informe o CPF: ')
    if cpf in users:
        print(f'Olá {users[cpf]["nome"]}! ')
        num_conta = int(input('Informe o número da conta: '))
        if num_conta in users[cpf].get('contas', {}):
            while True:
                saque = float(input('Valor do Saque: R$: '))
                saldo = users[cpf]['contas'][num_conta]['saldo']
                if saque <= saldo:
                        users[cpf]['contas'][num_conta]['saldo'] -= saque
                        users[cpf]['contas'][num_conta]['extrato'] += f'Saque no valor de R${saque:.2f}\n'
                        print(f"Saque realizado com sucesso! Novo Saldo: R${users[cpf]['contas'][num_conta]['saldo']:.2f}")
                        break
                else:
                    print('Saldo insuficiente! ')
        else:
            print('Conta inexistente para o cliente! ')
    else:
        print('CPF não localizado! ')
    print('Retornando ao menu inicial...')
    sleep(1)
    menu()
    
    
def extrato(users): # ajustar métodos
    print('Acessando menu Extrato...')
    sleep(1)
    cpf = input('Informe o CPF: ')
    if cpf in users:
        print(f'Olá {users[cpf]["nome"]}! ')
        print('Agência: 0001')
        num_conta = int(input('Informe o número da conta: '))
        if num_conta in users[cpf].get('contas', {}):
            print('Gerando extrato...')
            sleep(1)
            extrato = users[cpf]['contas'][num_conta]['extrato']
            print('=' * 6, 'EXTRATO', '=' * 6 )
            print()
            print('Agência 0001')
            print(f'Conta: {num_conta}')
            print()
            print('Não houveram movimentações.' if extrato == '' else extrato)
            print()
            print('=' * 6, 'FIM DO HISTÓRICO', '=' * 6 )
        else:
            print('Conta inexistente para o cliente! ')
    else:
        print('CPF não localizado! ')
    print('Retornando ao menu inicial...')
    sleep(1)
    menu()

menu()