from itertools import count
import os

def obtenerStringArchivo(raiz_archivo):
    lineas = ''
    try:
        with open(raiz_archivo) as arhivoPlano:
            lineas = arhivoPlano.read()
            #esta funcion solo existe para no repetir tanto este codigo
            

    except FileNotFoundError:
        print('al parecer has escrito mal la direccion del archivo.')
    return lineas
        

def contarLineas(raiz_archivo):
    texto = obtenerStringArchivo(raiz_archivo)
    if texto != '':
            numero =texto.splitlines()
            #la funcion splitlines cuenta cuantos saltos de linea
            # ('\n') hay en un string. Guarda el resultado en una lista
            return str(len(numero))
    else:
        print('ha ocurrido un error con el archivo')
        return str(-1)

   
def contarPalabras(raiz_archivo):
    texto = obtenerStringArchivo(raiz_archivo)
    if texto != '':    
            numeroPalabras =texto.split()
            #la funcion splitlines cuenta cuantas palabras
            # hay en un string. Por defecto seprara las palabras
            #con caracteres vacios ' '.
            return str(len(numeroPalabras))
    else:
        print('ha ocurrido un error con el archivo')
        return str(-1)
   

def contarCaracteres(raiz_archivo):
    texto = obtenerStringArchivo(raiz_archivo)
    lista_palabras = texto.split()
    numero = 0
    if texto != '':
        for palabra in lista_palabras:
            #este for recorre toda la lista
            for letra in palabra:
            #este for nos recorre cada caracter en la palabra
                if letra != '':
                    numero+=1
                    #cada vez que encuentre un caracter distinto a ''
                    #lo cuenta como tal.
            
    return str(numero)

def numeroVecesPalabra(raiz_archivo):
    #esta funcion guarda el numero de veces que aparece una palabra en
    #un diccionario
    #para eso se utiliza la funcion count y un ciclo for que recorre todas las palabras
    texto = obtenerStringArchivo(raiz_archivo)
    palabrasVeces = {}
    if texto != '':
        #si no hubo problemas al traer el archivo:
        lista_palabras = texto.split()
        for palabra in lista_palabras:
            #si la palabra no estaba en el diccionario
            #la mete, si ya estaba continua el ciclo.
            if palabra not in palabrasVeces:
                numero = lista_palabras.count(palabra)
                palabrasVeces[palabra] = numero
            else:
                continue
                  

    return palabrasVeces


def run():
    palabrasContadas = contarPalabras('./archivoPrueba.txt')+ ' palabras.'
    lineasContadas = contarLineas('./archivoPrueba.txt')+' Lineas.'
    caracteresContados = contarCaracteres('./archivoPrueba.txt')+ ' caracteres.'
    diccionarioPalabras = numeroVecesPalabra('./archivoPrueba.txt')
    nombreArchivo = os.path.basename('./archivoPrueba.txt')
    #una vez tenemos todos los datos, lo que hacemos es escribirlos en un archivo de texto
    
    try:
        with open('analisisArchivo.txt', 'w') as f:
            #si no encuentra el archivo, lo crea y lo abre
            #with proporciona un código más limpio y permite utilizar 
            #excepciones como lo es este try catch
            f.writelines(['El archivo de nombre "',nombreArchivo,'" tiene: ','\n',palabrasContadas,'\n',lineasContadas,'\n',caracteresContados,'\n','Numero de veces que aparece cada palabra (en formato clave valor): ','\n',str(diccionarioPalabras)])
            
    except FileNotFoundError:
        print("no se ha encontrado el archivo, por favor revisa el codigo")

if __name__ == '__main__':
    run()