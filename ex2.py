import time
n = int (input('Digite um número para fazer sua contagem: '))
while n > 0 :
    n -= 1 
    print (f'{n}...')
    time.sleep(1)
print ('Acabou a contagem')