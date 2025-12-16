print('-'*20)
print('Soma')
print('-'*20)
n1 = 1
n2 = 1
while True:
    n1 = int(input('Digite um número :'))
    if n1 == 0:
        print ('Você digitou 0 programa parando...')
        break
    n2 = int(input('Digite um número :'))
    if n2 == 0:
        print ('Você digitou 0 programa parando...')
        break
    soma = n1 + n2
    print(f'A soma {n1} + {n2} = {soma}')
   
    