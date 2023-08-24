'''

En programación orientada a objetos, la abstracción es el proceso de 
ocultar los detalles de implementación de un objeto de su interfaz. 
Esto permite que los usuarios de un objeto solo interactúen con él de 
la manera prevista, lo que puede ayudar a proteger los datos del objeto 
y a garantizar que el objeto funcione de manera consistente.

En Python, la abstracción se puede lograr utilizando clases, métodos y 
herencia.

En Python, un método abstracto es un método que no tiene implementación. 
Los métodos abstractos se utilizan para especificar el comportamiento que 
debe tener una clase, pero dejan la implementación específica a las clases 
hijas.


''' 

# Ejemplo 1

class Animal:
    def eat(self):
        # El método eat() está definido como abstracto
        raise NotImplementedError


class Dog(Animal):
    def eat(self):
        # La clase Dog implementa el método eat()
        print("El perro está comiendo.")


class Cat(Animal):
    def eat(self):
        # La clase Cat implementa el método eat()
        print("El gato está comiendo.")


dog = Dog()
dog.eat()

cat = Cat()
cat.eat()

#------------------------------------

# Ejemplo 2

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        # El método draw() está definido como abstracto
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def draw(self):
        print("Dibujando un rectángulo de color {} de ancho {} y alto {}.".format(
            self.color, self.width, self.height
        ))


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        print("Dibujando un círculo de color {} de radio {}.".format(
            self.color, self.radius
        ))


rectangle = Rectangle("rojo", 100, 50)
rectangle.draw()

circle = Circle("azul", 20)
circle.draw()