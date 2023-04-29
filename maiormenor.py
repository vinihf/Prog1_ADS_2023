contador = 1
soma = 0
media = 0
maior = -9999
menor = 9000
while contador <=7:
    temp = float(input(f'Dia {contador}:'))
    soma+=temp
    if temp > maior:
        maior = temp
    if temp < menor:
        menor = temp
    contador+=1
print(f'A média das temperaturas foi de {soma/(contador-1)}')
print(f'A maior das temperaturas foi {maior}')
print(f'A menor das temperaturas foi {menor}')