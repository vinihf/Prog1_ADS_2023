import random

jogada1 = int(input("Informe sua jogada: (1) Pedra (2)Papel (3)Tesoura"))
jogada2 = random.randint(1,3)

j1 = 0
j2 = 0

if jogada1 == jogada2:
    j1 = j1 + 1
    j2 = j2 + 1
elif jogada1 == 1:
    if jogada2 == 2:
        j2 = j2 + 1
    elif jogada2 == 3:
        j1 = j1 + 1
elif jogada1 == 2:
    if jogada2 == 1:
        j1 = j1 + 1
    elif jogada2 == 3:
        j2 = j2 + 1
elif jogada1 == 3:
    if jogada2 == 1:
        j2 = j2 + 1
    elif jogada2 == 2:
        j1 = j1 + 1

jogada1 = int(input("Informe sua jogada: (1) Pedra (2)Papel (3)Tesoura"))
jogada2 = random.randint(1,3)

if jogada1 == jogada2:
    j1 = j1 + 1
    j2 = j2 + 1
elif jogada1 == 1:
    if jogada2 == 2:
        j2 = j2 + 1
    elif jogada2 == 3:
        j1 = j1 + 1
elif jogada1 == 2:
    if jogada2 == 1:
        j1 = j1 + 1
    elif jogada2 == 3:
        j2 = j2 + 1
elif jogada1 == 3:
    if jogada2 == 1:
        j2 = j2 + 1
    elif jogada2 == 2:
        j1 = j1 + 1

jogada1 = int(input("Informe sua jogada: (1) Pedra (2)Papel (3)Tesoura"))
jogada2 = random.randint(1,3)

if jogada1 == jogada2:
    j1 = j1 + 1
    j2 = j2 + 1
elif jogada1 == 1:
    if jogada2 == 2:
        j2 = j2 + 1
    elif jogada2 == 3:
        j1 = j1 + 1
elif jogada1 == 2:
    if jogada2 == 1:
        j1 = j1 + 1
    elif jogada2 == 3:
        j2 = j2 + 1
elif jogada1 == 3:
    if jogada2 == 1:
        j2 = j2 + 1
    elif jogada2 == 2:
        j1 = j1 + 1

if j1>j2:
    print(f"\033[34m Jogador 1 venceu.\033[m")
elif j2>j1:
    print(f"\033[35m Jogador 2 venceu.\033[m")
else:
    print("Empatou!")