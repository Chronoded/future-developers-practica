"""
Ejercicio de algoritmos: FizzBuzz
Imprimir en pantalla números del 1 a N
Reglas:
Si el número es divisible entre 3, imprimir Fizz
Si el número es divisible entre 5, imprimir Buzz
Si el número es divisible entre 3 y 5, Imprimir FizzBuzz
"""
def FizzBuzz(number):
    for i in range (1, number+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

"""
Se probó con FizzBuzz(15) y FizzBuzz(30)
Realizado a partir de los videos de ejercicios de Algoritmos
"""

