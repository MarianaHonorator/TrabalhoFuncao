def calculo(B,b,h):
    area = (B+b)*h/2
    return area


B = float(input("Digit o valor da base maior do trapézio: "))
b = float(input("Digit o valor da base menor do trapézio: "))
h = float(input("Digit o valor da altura do trapézio: "))

print(f"Área: {calculo(B,b,h)} m²")


