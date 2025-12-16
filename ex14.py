n = 0 
while n != -1:
    n = int(input('Digite um número (-1 para sair): '))
    if n > 1:
        # Verificação de número primo
        eh_primo = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                eh_primo = False
                break
        if eh_primo:
            print(f'{n} é um número primo!')
        else:
            print(f'{n} não é primo.')
    elif n != -1:
        print('Digite um número maior que 1 para verificar se é primo.')
