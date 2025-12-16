inicio = int(input('Digite o número que deseja iniciar: '))
fim = int(input('Digite o número final: '))
passo = int(input('Deseja fazer a contagem pulando de quanto em quanto? '))

for i in range(inicio, fim+1, passo):
    print(i)