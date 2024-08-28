class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    class Carro:
        portas = 4

        def __init__(self, marca, modelo, ano):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano

        def info(self):
            print (f"Carro: {self.marca} {self.modelo} ({self.ano}).")
    


    class Moto:
        guidão = input("Qual o tipo de guidão da moto?(normal ou esportivo?): ")

        def __init__(self, marca, modelo, ano):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano
    
        def infoM(self):
            print(f"Moto: {self.marca} {self.modelo} {self.ano}")



    meu_carro = Carro ("Toyota", "Corolla", 2024)
    meu_carro.info()
    print (f"O carro tem {meu_carro.portas} portas.")

    print ("\n")

    minha_moto = Moto ("Yamaha", "scooter", 2024)
    minha_moto.infoM()
    print (f"O guidão da moto é {minha_moto.guidão}.")






