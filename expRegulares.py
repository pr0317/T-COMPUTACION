from cgitb import text
import re
import string
from textwrap import fill
import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x400")
etiqueta = tkinter.Label(ventana, text = "Identificador de datos", bg = "yellow")
etiqueta.pack(fill = tkinter.BOTH, expand = 1)


ventana.mainloop()


##!expresiones regulares para verificación de:
##1.1. entero
##1.2. real
##1.3. Notación Científica
#1.4. Correo Electrónico

cadena = input("Ingrese un número entero:  ")
print(cadena)

#Expresión regular [+] simbol opcional, ? caracter que precede debe conincidir una vez con el tipo de dato,
#                  \d cualquier cifra de 0 a 9, $ fin de la validación

if re.match('[+]?\d$',cadena):
	print("Si es Número entero")
else:
	print("No es Número entero")

cadena = input("Ingrese un número Real:  ")
print(cadena)

#Expresión regular \. simbolo de punto y "+" que concatena la validación"

if re.match('[+-]?\d+(\.\d)$',cadena):
	     print("Si es Número Real")
else:
	     print("No es Número Real")

cadena = input("ingrese un número para mostrar en notación cientifica:  ")

if re.match('[-+]?\d?(\.\d)+([eE][+-]\d)$',cadena):
	print("Si es Notación Cientifica")
else:
	print("No es Notación Cientifica")

cadena = str(input("Ingrese su correo electronico:  "))
print(cadena)

# Funcion de validación
# @autor https://www.lawebdelprogramador.com/codigo/Python/2040-Validar-cuenta-de-correo.html
# Adaptado para uso educativo.
# Apoyo de sintaxis https://support.google.com/a/answer/1371415?hl=es && https://relopezbriega.github.io/blog/2015/07/19/expresiones-regulares-con-python/

             # user            @  organization     . type
if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',cadena.lower()):
	print("Correo correcto")
else:
	print("Correo incorrecto")



