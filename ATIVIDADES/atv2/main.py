from modelos.carro import Carro
from modelos.moto import Moto

def main():
    carro1 = Carro('Fiat', 'Uno', 4)
    carro2 = Carro('Chevrolet', 'Celta', 2)
    carro3 = Carro('Ford', 'Ka', 3)
    print(carro1)
    print(carro2)
    print(carro3)
    moto1 = Moto('Honda', 'Biz', 'Esportiva')
    moto2 = Moto('Yamaha', 'Factor', 'Casual')
    moto3 = Moto('Suzuki', 'Boulevard', 'Casual')
    print(moto1)
    print(moto2)
    print(moto3)
    
if __name__ == "__main__":
    main()