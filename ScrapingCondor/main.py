
# Librerias utilizadas
from bs4 import BeautifulSoup
import requests
import time

#La libreria windsound se usa para emitir el sonido en Linux 
from playsound import playsound
#La libreria windsound se usa para emitir el sonido en windows 
#import winsound

#Funcion encargada de localizar y monitorizar nuestro punto objetivo

def buscaCita():
  
    #Url de la pagina a monitorizar
    url = 'ingrese aqui la Url de la pagina a monitorear sin quitar las comillas'

    #Crea la sopa y obtiene el contenido de la pagina
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Encuentra el boton dentro del contenido extraido y lo guarda
    td = soup.find_all('button', class_='ingrese aqui el nombre de la clase del boton a monitorear sin quitar las comillas')
  
    #Contador que nos indica si el boton que buscamos esta activo
    count = 0
    for i in td:
        count += 1

    #If que nos avisa cuando ha encontrado la cita
    if(count > 0):
        print(str(count) + ' Cita encontrada')
        #Dependiendo de si estamos en Linux o en Windows debemos activar un reproductor de sonido u otro, Playsound en e caso de Linux y Windsound en el caso de windwos
        playsound('Silbido.mp3')
         #winsound.PlaySound("Silbido", winsound.SND_FILENAME)

    #Tiempo de descanso hasta la proxima busqueda
    time.sleep(1)

#Contador de cuantas veces se ha realizado la busqueda
contadorDeBusquedas = 0;
while True:
    buscaCita()
    contadorDeBusquedas += 1
    print(str(contadorDeBusquedas) + ' veces buscadas')