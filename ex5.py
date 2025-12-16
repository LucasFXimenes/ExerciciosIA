total = 0 
contador = 0 
while total < 100:
    n = int(input('Digite um número: '))
    if n < 0:
        print('Números negativos não são permitidos. Tente novamente.')
        continue
    total += n
    contador +=1
    print(f'Você contou {contador} número(s)')
    print(f'Total acumulado:{total}')
print ('Você ultrapassou de 100!')
print('Finalizando o programa')