class Carro:
    def __init__(self, v_max=200, velocidade=0):
        self.v_max = v_max
        self.velocidade = velocidade

    def acelerar(self, delta=5):
        maxima = self.v_max
        nova = self.velocidade + delta
        self.velocidade = nova if nova < maxima else maxima
        return self.velocidade

    def frear(self, delta=5):
        nova = self.velocidade - delta
        self.velocidade = nova if nova > 0 else 0
        return self.velocidade


if __name__ == "__main__":
    c1 = Carro(180)

    for _ in range(25):
            print(c1.acelerar(8))

    for _ in range(10):
            print(c1.frear(delta=20))
