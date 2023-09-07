class coche:

    ruedas = 4 # atributo de clase

    def __init__(self, color, aceleracion):
        
        # atributos de instancia
        self.color = color
        self.aceleracion = aceleracion
        self.velociodad = 0

    # metodo de instancia
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    # metodo de instacia
    def frena(self):
        v = self.velocidad -self.aceleracion
        if v < 0:
            v = 0
        self.velocidad = v

# atributo de instancia
c1 = coche('rojo', 20)
c2 = coche('azul', 25)

print(c1.color)
print(c2.color)

# atributo de clase
coche.ruedas = 6 # modificara todas las instancias de la clase, ya que se modifica la clase directamente

print(c1.ruedas, ' ', c1.color)
print(c2.ruedas, ' ', c2.color)
