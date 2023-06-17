import secrets
import string

def generadorContrasena():
    letras = string.ascii_letters #ascii_letters: concatenacion de letras mayusculas y minusculas
    digitos = string.digits #digits: contiene numeros del 0 al 9
    especial = string.punctuation #punctuation: contiene caracteres especiales

    #concadenar letras, digitos y especial
    alphabet = letras + digitos + especial

    #asignamos la longitud de la contraseña
    pass_lenght = int(input("Ingrese longitud deseadda para la contraseña: "))

    password = ''

    #genera la contraseña
    for i in range(pass_lenght):
        password += ''.join(secrets.choice(alphabet))
        #usamos join() para agregar el caracter al password
        #como no queremos tener espacio en blanco, especificamos que el separador sea ''

    print('Nueva Contraseña: {}'.format(password))  

generadorContrasena()