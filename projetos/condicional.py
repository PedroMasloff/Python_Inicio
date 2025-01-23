idade = int(input("Informe a sua idade: "))

if idade < 18:
    print("Menor de idade")
elif 18 <= idade < 65:
    print("Adulto")
else:
    print("Idoso")