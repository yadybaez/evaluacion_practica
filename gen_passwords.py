#este código genera contraseñas a partir de listas
#de diferentes caracteres

import random

#las tuplas nos sirven por que ninguna de estas listas cambiaran
posibilidadesCaracteres = {
1:('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z'),
2:('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z'),
3:('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'),
4:('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"')
}

def gen_pass(longitud):
    #bien, lo primero es que escogerá aleatoriamente entre mayusculas:1,minus:2,num:3 y char:4
    contrasena = ''
    while(len(contrasena)<=longitud):
        tupla = random.randint(1,4)
        #escogemos una tupla, y de esa un caracter aleatorio
        tupla_aux = posibilidadesCaracteres[int(tupla)]
        #seleccionamos un elemento aleatoriamente
        char_anadir = tupla_aux[random.randint(0,len(tupla_aux)-1)]
        #si el ultimo elemento es igual al que se va a añadir, escogemos otro
        if(len(contrasena)==0):
            #sin embargo, si es el primer elemento lo añadimos sin mas.
            contrasena+= char_anadir
        else:
            if(contrasena[-1]!=char_anadir):
                contrasena+= char_anadir
            else:
                while(contrasena[-1] == char_anadir):
                    #el indice negativo nos permite entrar al ultimo elemento
                    #de la string
                    char_anadir = tupla_aux[random.randint(0,len(tupla_aux)-1)]
                    #basicamente selecciona aleatoriamente varios caracteres hasta encontrar
                    #uno diferente al ultimo.
                    if(contrasena[-1] != char_anadir): 
                        contrasena+=char_anadir
                        #terminamos el ciclo
                        break
        
        
    return contrasena

def run():
    numero = int(input('dime el numero de caracteres del cual quieres tu contraseña: \n'))
    password = gen_pass(numero)
    print(password)
    #se genera el archivo en el mismo lugar donde esté este código
   
    try:
        with open('contrasenia.txt', 'w') as f:
            #si no encuentra el archivo contrasenia, lo crea y lo abre
            #with proporciona un código más limpio y permite utilizar 
            #excepciones como lo es este try catch
           
            f.writelines(['Hola, esta es la contraseña\n',password,'\n'])
            
    except FileNotFoundError:
        print("no se ha encontrado el archivo, por favor revisa el codigo")


if __name__ == '__main__':
    run()