class Carro:
    def __init__(self, v_max=200, velocidade=0):
        self.v_max = v_max
        self.velocidade = velocidade

    def acelerar(self, delta=5):
        if self.velocidade + delta > self.v_max:
            self.velocidade = self.v_max
        else:
            self.velocidade = self.velocidade + delta
        return self.velocidade

    def frear(self, delta=5):
        if self.velocidade - delta < 0:
            self.velocidade = 0
        else:
            self.velocidade = self.velocidade - delta
        return self.velocidade


if __name__ == "__main__":
    c1 = Carro(180)

    for _ in range(25):
            print(c1.acelerar(8))

    for _ in range(10):
            print(c1.frear(delta=20))
