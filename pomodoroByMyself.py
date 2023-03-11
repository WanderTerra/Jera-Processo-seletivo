import time

for y in range(4):
    for x in range(1500,0,-1):
        segundos = x % 60
        minutos = int(x / 60) % 60
        print(f'{minutos:02}:{segundos:02}', end="\r")
        time.sleep(1)

    print('Hora do Break')
    time.sleep(5)

    for x in range(300,0,-1):
        segundos = x % 60
        minutos = int(x / 60) % 60
        print(f'{minutos:02}:{segundos:02}', end="\r")
        time.sleep(1) 
        
    print('Hora de voltar para o trampo')
    time.sleep(5)
print('Você fez 4 Pomodoros')