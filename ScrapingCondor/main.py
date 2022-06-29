# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from itertools import count

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import winsound

def buscaMateria():
    #Física II
    url = 'https://estudiantes.portaloas.udistrital.edu.co/academicopro/index.php?index=g8e-WrLHvTv5BT8Sn-33RtAntsWNA9F6JHNBNeJb34cPogK5CLDRyAt6oDq2o6TvXR3hYPJhnCFhf-ym3CII_Yj0APuoUbK_rSKZyGhNMgn4iljw53PQMnSmMs3Y2iiLzDO2Jz6UXIYKmdPgp8BVybiUGdJidmXATa1uyedjo2hYKCc6P21g06ETSXEMlBwQeZ2Kc_l8HeR-SPTXAb254DzuRZ2h97QC367Y0pujXiFbwD6CjlTNMd6_k_9ja1E4uGxX6y-sZq5cRmy0pwJQnUxJHZ-fjyy96HPUD9679sXuTsyja_bItwcBM5xsmtUSjf4LHlN4ogKbJvv5Mcg--BGx5l1_K5S2qhyu4bmqLnSG4L0GUHdpB1PILpvQxhy1yRIC-eYEMW9di49YsUEjoZX2CNBktNJWNWPuCURBYHfF9yq33V2sHIp8pZoL8V-v5GD4-2WXOtm2uHywfov0Y4uyUvi_-VnptdqfZV4-YaYJ8a9PCyNWW_A_5qx4DyYUlLR7j0-8O-d3eytgYnUFs0RZktUwOG2KFGj3q5noU45h6hM5QuiCT6nSIDtW3bhqBLrqgzwDAWZX2nD1IZY5Lg'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    td = soup.find_all('button', class_='botonEnlacePreinscripcion')

    count = 0
    for i in td:
        count += 1

    if(count > 0):
        print(str(count) + ' Física II')
        winsound.PlaySound("Silbido", winsound.SND_FILENAME)

    # Fundamentos
    url = 'https://estudiantes.portaloas.udistrital.edu.co/academicopro/index.php?index=g8e-WrLHvTv5BT8Sn-33RtAntsWNA9F6JHNBNeJb34dJkptDwjeFSeFgp-O9WbdQt4fwV4hJ9SUizWuLqZ0cbkoPxD-o6ksCn1cY7sjfBcdsrNqTagFIoFXYc37r-FHk_8Beuksm-Cpit8hGtelzbndF1hGjjRanFsj5emC66I4ixwv3LjBzGvtjqNirgbYyUflXoHze_fYpS8QZyKoj46k107A-XdhbVSzZhndUY7XQjdoIzMYVNB4Q4amDs0ZwpOTZQM2lRKwBesLaPJ89ogAqpJZWc0eoWqACErPcT2vPmXJmZeJweq3gT9AtxN0WeNgs054wrHsIn__yhmK8eLDVZI6miGeB2_tP5zZtkAdHTIWPMYKqvIQhh1CqAEbqs9aowJ9XuRb_9-jun0SaPk5kJhFoFi3yY8v6ZBuAN9i4s9F8i4gMz0KsgfpMtS1XQOJHyHTTCt2B6g0QVKCkRui1KLEgerpIRb6ULsP9cKG0wMcTSloiwC74NEiD_vrLr0W1rOxmgqFe53Yp3JPGJoUjoromahNlSEPlFKa2ImNaP-Toi1ODi-ood3B0HObs6J7FeKq7b1-gS9HifM2GtA'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    td = soup.find_all('button', class_='botonEnlacePreinscripcion')

    count = 0
    for i in td:
        count += 1

    if (count > 0):
        print(str(count) + ' Fundamentos')
        winsound.PlaySound("Silbido", winsound.SND_FILENAME)

    time.sleep(10)

contadorDeBusquedas = 0;
while True:
    buscaMateria()
    contadorDeBusquedas += 1
    print(str(contadorDeBusquedas) + ' veces buscadas')