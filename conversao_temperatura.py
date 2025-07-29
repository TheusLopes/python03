def converter_temperatura(valor, origem, destino):
        if origem == "C":
                celsius = valor
        elif origem == "F":
                celsius = (valor - 32) * 5/9
        elif origem == "K":
                celsius = valor - 273.15
        else:
                return "Unidade invalida"

        if destino == "C":
                return celsius
        elif destino == "F":
                return (celsius * 9/5) + 32
        elif destino == "K":
                return celsius + 273.15
        else:
                return "Unidade de destino inválida"
        
valor = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F, K): ").upper()
destino = input("Digite a unidade de destino (C, F, K): ").upper()

resultado = converter_temperatura(valor, origem, destino)
print(f"A temperatura convertida é: {resultado:.2f} {destino}")