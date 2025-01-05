#La función input sirve para leer una cadena de carácteres, el argumento que recibe es el texto que se
#mostrará en pantalla para leer dicho dato.
input("Introduce tu nombre: ") #En este caso solo lee el dato, pero no lo almacena en ningún lugar

#Las funciones se ejecutan de adentro hacia afuera, lo que puede hacer cosas como esta:
print("Tu nombre es: " + input("Introduce tu nombre de nuevo por favor: ") + " " + input("Dime tu apellido: "))