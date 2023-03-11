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
    for x in range(t,-1,-1):
        segundos = x % 60
        minutos = int(x / 60) % 60
        print(f'      {minutos:02}:{segundos:02}', end="\r")
        time.sleep(1)

def executorDePomodoros():
        global contador_de_Pomodoro
        while True:
            for x in range(4):
                print('\n    TRABALHO ----- TECLE ESPAÇO PARA PARAR')
                myTimer(1500)
                contador_de_Pomodoro += 1
                print (' '*50,'         \|/')
                print (' '*50,f'       (_____) POMODOROS FEITOS --> {contador_de_Pomodoro}\n')
                print('\n    Pausa Curta ----- TECLE ESPAÇO PARA PARAR')
                myTimer(300) 
            print('\n    Pausa longa ----- TECLE ESPAÇO PARA PARAR')
            myTimer(600)

def executaRepeticao(): 
    global contador_de_Pomodoro
    if  contador_de_Pomodoro == 0:
        opcao=int(input('\nTECLE:\n1- PARA INICIAR O TRABALHO\n2- PARA INICIAR COM UMA PAUSA CURTA\n3- PARA INICIAR COM UMA PAUSA LONGA\n----> '))
        if opcao == 1:
            executorDePomodoros()
        elif opcao == 2:
            print('\n    Pausa Curta')
            myTimer(3)
            executorDePomodoros()
        elif opcao == 3:
            print('\n    Pausa longa')
            myTimer(9)
            executorDePomodoros()

    

def paraRepeticao():
    while True:     
        if keyboard.is_pressed(' '): 
           os._exit(0)

contador_de_Pomodoro = 0


threading.Thread(target=executaRepeticao).start() 
threading.Thread(target=paraRepeticao).start()