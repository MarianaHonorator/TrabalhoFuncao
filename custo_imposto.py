def soma_imposto(taxa_imposto,custo):
    return taxa_imposto * custo




custo = float(input("Digite o valor do custo: "))
print("Exemplo: 50% = 1.5")
print("Exemplo: 2% = 1.02")
taxa_imposto = float(input(f"Digite o valor do imposto(%):"))

print(f"O preço do produto com imposto é R$ {soma_imposto(taxa_imposto,custo)} ")
