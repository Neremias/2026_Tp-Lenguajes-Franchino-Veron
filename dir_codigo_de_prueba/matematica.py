def sumar(a, b):
    return a + b

def promedio(numeros):
    total = 0
    for n in numeros:
        total += n
    return total / len(numeros)
    
def restar(a, b):
    return a - b

def sumar_2(a, b):
    num1 = a
    num2 = b
    return num1 + num2

def estadisticas(numeros):
    suma = 0
    cantidad = 0
    maximo = numeros[0]
    for n in numeros:
        suma += n
        cantidad += 1
        if n > maximo:
            maximo = n
    promedio = suma / cantidad
    return promedio, maximo

def estadisticas2(numeros):
    suma = 0
    cantidad = 0
    maximo = numeros[0]
    for n in numeros:
        cantidad += 1
        suma+= n
        if n>maximo:
            maximo = n
    promedio = suma / cantidad
    return promedio, maximo

def wh():  
    i=0  
    while i<10:
        print("hola")
        i+=1
    
def fh():
    for i in range(10):
        print("hola")
