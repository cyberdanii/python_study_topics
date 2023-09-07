import time

class FiboIter():

    def __iter__(self): # se ejecuta al instaciar la clase en una variable
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self): # se ejecuta al iterar la clase dentro de un for

        # si es la primera vuelta o iteracion entonces retorne el valor de n1 y sume 1 al contador
        if self.counter == 0:
            self.counter += 1
            return self.n1
        
        # si es la segunda vuelta o iteracion entonces retorne el valor de n2 y sume 1 al contador
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        
        else:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux

            self.counter += 1
            
            return self.aux

if __name__ == '__main__':
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.1)