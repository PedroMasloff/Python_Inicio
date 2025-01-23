import random

numero_secreto = random.randint(1, 10)
tentativas = 0
acertou = False

while not acertou:
    chute = int(input("Adivinhe o número (entre 1 e 10): "))
    tentativas += 1

    if chute == numero_secreto:
        print("Parabéns! Você acertou em", tentativas, "tentativas!")
        acertou = True
    elif chute < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
