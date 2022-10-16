
from PIL import Image
from pytesseract import *
from googletrans import Translator


def run():
    pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #insertamos la ruta donde installamos tesseract
    
    #Ahora traemos la imagen a la cual vamos a reconocer el texto
    imagen_en_ingles = Image.open('quotes.png')
    #si fuese otro idioma, image_to_string tiene un atributo en el cual
    # se puede ajustar el lenguaje
    interpretacion = pytesseract.image_to_string(imagen_en_ingles)
    print(interpretacion)
    #ya tenemos el texto en ingles, ahora vamos a traducirlo.
    #para esto utilizamos la API de google translate 
    #e importamos googletrans
    print('--------------')
    convertir_esp = Translator() 
    texto_en_esp = convertir_esp.translate(text=interpretacion,dest='es',src='en').text
    print(texto_en_esp)
    #finalmente guardamos esto en un archivo de texto plano:
    try:
        with open('traduccionFoto.txt', 'w') as f:
            #si no encuentra el archivo, lo crea y lo abre
            #with proporciona un código más limpio y permite utilizar 
            #excepciones como lo es este try catch
            f.writelines(['Este es el texto original reconocido de la imagen: ','\n',interpretacion,'\n','-----------','Aqui esta la traduccion del texto: ','\n',texto_en_esp])
            
    except FileNotFoundError:
        print("no se ha encontrado el archivo, por favor revisa el codigo")
    


if __name__ == '__main__':
    run()