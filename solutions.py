""""""
"""
Ejercicio 1
Dado un string s, devolver el string dado la vuelta
Ejemplo:
reverse("Hola")
Devuelve "aloH"
"""
def reverse(s):
    return s[::-1]




"""
Ejercicio 2
Dado un diccionario d, devolver True si existe la key k
y False en caso contrario
Ejemplo:
contains({"hola": 1}, "hola")
Devuelve 1
"""
def contains(d, k):
    return k in d





"""
Ejercicio 3
Dado un string s, contar cuantas letras mayusculas y minusculas tiene
El resultado se tiene que devolver como una tupla
Ejemplo:
upperlower("Hola")
Devuelve: (1, 3)
"""
def upperlower(s):
    return (
        len([x for x in s if x.isupper()]),
        len([x for x in s if x.islower()])
    )






"""
Ejercicio 4
Dado un numero n, imprimir una piramide de altura (hacia la derecha) n
Ejemplo:
pyramid(4)
Imprime:
X
XX
XXX
XXXX
XXX
XX
X
"""
def pyramid(n):
    i = 1
    while i < n:
        print('X'*i)
        i += 1
    while i > 0:
        print('X'*i)
        i -= 1
    pass




"""
Ejercicio 5
Dado un string s, quitar todas las mayúsculas
Ejemplo:
low("John Doe")
Devuelve:
"ohn oe"
"""

def low(s):
    return ''.join([x for x in s if x.islower()])



"""
Ejercicio 6
Dado un string, devolver el valor en int si es un int, y sino devolver false (hint: try/except)
Ejemplo:
toint("3")
Devuelve 3
toint("hola")
Devuelve False
"""
def toint(s):
    try:
        return int(s)
    except:
        return False





"""
Ejercicio 7
Dado un string devolver un diccionario con el numero de veces que aparece cada letra
Ejemplo:
letters("monty python")
Devuelve:
{'t': 2, 'h': 1, 'n': 2, 'p': 1, 'o': 2, 'm': 1, 'y': 2, ' ': 1}
"""
def letters(s):
    d = {}
    for l in s:
        if l in d.keys():
            d[l] += 1
        else:
            d[l] = 1
    return d



"""
Ejercicio 8
Imprimir el abecedario en una lista (usando range)
Ejemplo:
abc()
Devuelve:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

"""

def abc():
    l = []
    for x in range(26):
        l.append(chr(ord("a")+x))
    return l


"""
Ejercicio 9
Contar las vocales de un string s
Consideramos que las vocales son "aeiou"
Ejemplo:
vowels("thequickbrownfoxjumpsoverthelazydog")
Devuelve: 11
"""
def vowels(s):
    r = 0
    v = ['a', 'e', 'i', 'o', 'u']
    for l in v:
        r += len([x for x in s if x == l])
    return r

"""
Ejercicio 10
Dada una lista l, descartar todos los numeros mayores de 30 y los impares (usando list comprehensions)
Ejemplo:
listfilter([5,31,4,8,20])
Devuelve
[4, 8, 20]
"""
def listfilter(l):
    return [x for x in l if x <= 30 and x % 2 == 0]


"""
Ejercicio 11
Dado un numero, imprimir la tabla de multiplicar de ese numero
Ejemplo:
tabla(6)
Imprime:
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60

"""
def tabla(n):
    for i in range(1, 11):
        print(n, 'x', i, '=', n*i)


"""
Ejercicio 12 (* Complicado)
Dado un numero n, devovler una FUNCION que sume 3 a un numero
Ejemplo:
add3 = generate_addn(3)
add3(5) #  devuelve 8
"""
def generate_addn(n):
    def adder(x):
        return x + n
    return adder

"""
Ejercicio 13
Hacer una funcion que devuelva el numero de argumentos que se le han pasado
Ejemplo:
argcount("a", 1)
Devuelve 2
argcount(1,2,3)
Devuelve 3
argcount([1,2,3])
Devuelve 1
"""
def argcount(*args):
    return len(args)



"""
Ejercicio 14
Dada una lista de strings y un numero, imprimir la salida del ejemplo:
printlist(3, ["p", "q"])
Imprime
p1
q1
p2
q2
p3
q3
"""
def printlist(n, l):
    r = []
    for i in range(0, n):
        for j in l:
            r.append(str(j + str(i+1)))
    print(r)
    # alternativa pro:
    # return [val + str(i+1) for i in range(0,n) for val in l]


"""
Ejercicio 15
Crea una clase Animal que reciba como constructor un nombre n y un sonido s
Tiene que tener la funcion sonido() que imprimirá un mensaje como el del ejemplo
Ejemplo:
pato = Animal("Pato", "Cuack")
pato.sonido()
Imprime: "Soy un Pato y hago Cuack"
gato = Animal("Gato", "Miau")
gato.sonido()
Imprime: "Soy un Gato y hago Miau"
"""
class Animal:
    def __init__(self, n, s):
        self.n = n
        self.s = s
    def sonido(self):
        print("Soy un", self.n, "y hago", self.s)

"""
Ejercicio 16
Con la clase Animal de antes, añadir una funcion patas() que al llamarla imprima
"No tengo patas"
Ejemplo:
gato = Animal("Gato", "Miau")
gato.patas()
Imprime: "No tengo patas"
"""
class Animal:
    def __init__(self, n, s):
        self.n = n
        self.s = s
    def sonido(self):
        print("Soy un", self.n, "y hago", self.s)
    def patas(self):
        print("No tengo patas")


"""
Ejercicio 17
Crear la clase Gato, subclase de Animal, que al llamar a patas()
imprima "Tengo 4 patas"
"""
class Gato(Animal):
    def patas(self):
        print("Tengo 4 patas")


