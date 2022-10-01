#clasificar si un numero es par
clasificar2 = lambda num : num%2==0
print(clasificar2(100))

#Clasificar numeros mayores a 10 de una lista
numeros = [2,4,6,8,10,12]
for numero in numeros:
    if numero > 10:
        mayores = lambda numero : numero>10
print(mayores(numero))

#Recibir nombre, edad y ocupación de una oersona y devolverlo en un diccionario
nombre = "Jenn"
edad = 30
ocupacion = "Estudiante"

datos = {}

info = lambda nombre, edad, ocupacion : {nombre, edad, ocupacion}
print(info(nombre, edad, ocupacion))

#Sumar dos numeros
sumarNumeros=lambda num1, num2:num1+num2
print(sumarNumeros(5,20))

#Multiplicar un numero por 100
multiplicar = lambda num : num * 100
print(multiplicar(5))