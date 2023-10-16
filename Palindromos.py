#Programa de Mendoza Chávez José Alberto
import unicodedata

def esPalindromo(s):
    # Convertir la cadena a minúsculas y eliminar los espacios en blanco
    s = s.lower().replace(" ", "")
    # Eliminar los acentos en las palabras
    s = ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    # Verificar si la cadena es igual a su reverso
    return s == s[::-1]

while True:
    # Pedir al usuario que ingrese una palabra o frase
    string = input("Ingrese una palabra o frase: ")

    # Verificar si la cadena es un palíndromo
    if esPalindromo(string):
        print("La cadena es un palíndromo")
    else:
        print("La cadena no es un palíndromo")