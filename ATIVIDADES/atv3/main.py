from modelos.carro import Carro

def main():
    carro1 = Carro("Toyota", "Corolla", "Prata")
    carro2 = Carro("Honda", "Civic", "Preto")
    carro3 = Carro("Ford", "Focus", "Azul")
    
    print(carro1)
    print(carro2)
    print(carro3)

if __name__ == "__main__":
    main()