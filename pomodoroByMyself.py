import time
import pygame

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
for x in range(4):
    print('TRABALHO')
    myTimer(1500)
    print('Pausa Curta')
    myTimer(300)
print('Pausa longa')
myTimer(900)