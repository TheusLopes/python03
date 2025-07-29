idade = int(input("Digite a idade do usuário: "))

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade < 59:
    print("Adulto")
else:
    print("Idoso")