import time
import pygame
import threading
import os
import keyboard

def player():
    pygame.init()
    pygame.mixer.music.load('C:\\Users\\Luisa\\.vscode\\Jera\\Bells.mp3')
    pygame.mixer.music.play()
    

def myTimer(tempo):
    t=tempo
    player()
    for x in range(t,0,-1):
        segundos = x % 60
        minutos = int(x / 60) % 60
        print(f'{minutos:02}:{segundos:02}', end="\r")
        time.sleep(1)

def executaRepeticao():
    while True:
        for x in range(4):
            print('TRABALHO ----- TECLE ESPAÇO PARA PARAR')
            myTimer(1500)
            print('Pausa Curta ----- TECLE ESPAÇO PARA PARAR')
            myTimer(500)
        print('Pausa longa ----- TECLE ESPAÇO PARA PARAR')
        myTimer(900)

def paraRepeticao():
    while True:
        if keyboard.is_pressed(' '): 
            os._exit(0)
     
threading.Thread(target=executaRepeticao).start() 
threading.Thread(target=paraRepeticao).start() 