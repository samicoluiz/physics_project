class Particula():
    def __init__(self, q, unidade='C', pos=0):
        self.q = q*10**-9 if unidade == 'nC' else q*10**-3 if unidade == 'mC' else q
        self.pos = pos
        self.posCampo = [] # Apagar caso não seja utilizado
        pass

    def __str__(self):
        return f'A carga elétrica desta particula é {self.q} e\
 a sua posição é {"na origem" if self.pos==0 else self.pos}.'

    def campoEletrico(self, r):
        print(self.q)
        return ((9*10**9)*self.q)/((r)**2)

    # Esta equação está correta desde que a partícula esteja na origem.
    # verificar a fórmula para a possibilidade de calcular a distancia como abs(self.pos - r),
    # sendo r Ex, Ey e Ez. Assim, a função será mais generalista.
    def vCampoEletrico(self, Ex, Ey, Ez):
        return self.campoEletrico(Ex) + self.campoEletrico(Ey) + self.campoEletrico(Ez)

def fEntreCargas(Q, q, r, cosAlpha=None):
    return ((9*10**9)*Q*q)/r**2

# Módulo do campo elétrico resultante
def cER(vCampo1, vCampo2, angulo):
    # Resultante de campos elétricos paralelos
    if angulo == 0:
        return vCampo1 + vCampo2
    elif angulo == 180:
        return vCampo1 - vCampo2
    elif angulo == 90:
        # Na hora de anotar lembrar de colocar a raiz
        return (vCampo1**2) + (vCampo2**2)
    else:
        return (vCampo1**2) + (vCampo2**2) + 2*vCampo1*vCampo2*cosAlpha
    pass


h20 = Particula(10, 'mC')
coords = [-0.2, -0.2, -0.2]
print(h20)