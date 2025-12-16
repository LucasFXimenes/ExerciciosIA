import random
import time
print('-'*18)
print ('Bem-vindo ao menu!')
print('-'*18)
opcao = 0
n = 0 
while opcao != 3:
    print(' 1 - Mensagem',end="|")
    print(' 2 - Número aleatório',end="|")
    print(' 3 - Sair')
    opcao = int (input('Digite uma opção do menu: '))
    if opcao == 1:
        print ('Olá toma aqui sua mensagem!')
    if opcao == 2:
        n = random.randint(1,100)
        print(f'O número aleatório foi o {n}')
    if opcao ==3:
        print('Você saiu!')
        break
    if opcao >3 or opcao <0:
        print('Digite uma opção valida! ')