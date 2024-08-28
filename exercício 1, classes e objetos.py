class Carro:
    portas = 4

    def __init__(self, cor, marca, modelo, ano):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def info(self):
        print (f"Carro: {self.cor} {self.marca} {self.modelo} ({self.ano}).")

    
    
meu_carro = Carro (input("Qual a cor do carro?"),"Toyota", "Corolla", 2024)
meu_carro.info()


meu_carro = Carro(input ("Qual a cor do carro? (É permitido que haja alterações): "), "Toyota", "Corolla", 2024)
meu_carro.info()
print(f"O carro tem {meu_carro.portas} portas. ") # Imprime: 4

print("aaaaaaaaaaaaa")


