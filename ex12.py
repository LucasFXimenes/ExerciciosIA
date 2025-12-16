import random
import time
print('-'*16)
print ('Acerte o número!')
print('-'*16)
n = 0 
pc = random.randint (1,10)
while True:
    n = int (input('Digite um número: '))
    print('Vamos verificar hmmm...')
    time.sleep(1)
    if n != pc:
        print('Número errado tente de novo!')
    else:
        break
print('Parabéns você acertou!')