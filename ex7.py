while True: 
    idade = int(input('Digite sua idade: '))
    print(f'Sua idade é: {idade}')
    if idade < 0 or idade > 100:
        print('Idade inválida')
        break
print('Finalizando...')
    