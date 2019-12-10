#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor, TouchSensor
from pybricks.parameters import Port ,Color
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from time import sleep

ts = TouchSensor(Port.S2)
col = ColorSensor(Port.S3)
us = UltrasonicSensor(Port.S4)

m = MediumMotor(OUTPUT_A)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

def main():
    abrir()
    testDistance_inicio()
    while(col.color() != 1):
        colocarPecas()
    """
    abrir()
    testDistance()
    direita()
    testDistance()
    direita()
"""

def colocarPecas():
    andar()
    direita()
    andar()
    andar()
    andar()
    esquerda()
    testDistance()
    andar_tras_inicio()
    

def testColor_inicio():
    
    x = True
    while(x):
        if(col.color() == 7):   #ccor castanho
            fechar()
            sleep(1)
            direita()
            andar()
            abrir()
            sleep(1)
            andar_tras()
            esquerda()
            testDistance_inicio()
            x = False
        print(col.color())
        if(col.color() == 5):   #cor vermelha
            fechar()
            sleep(1)
            direita()
            andar()
            abrir()
            sleep(1)
            andar_tras()
            esquerda()
            testDistance_inicio()
            x = False
        print(col.color())
        if(col.color() == 4):   #cor amarelo
            fechar()
            sleep(1)
            direita()
            andar()
            abrir()
            sleep(1)
            andar_tras()
            esquerda()
            testDistance_inicio()
            x = False
        print(col.color())  
        if(col.color() == 3):   #cor verde
            fechar()
            sleep(1)
            direita()
            andar()
            abrir()
            sleep(1)
            andar_tras()
            esquerda()
            testDistance_inicio()
            x = False
        print(col.color())
        if(col.color() == 2):   #cor azul
            fechar()
            sleep(1)
            direita()
            andar()
            abrir()
            sleep(1)
            andar_tras()
            esquerda()
            testDistance_inicio()
            x = False
        print(col.color())
        if(col.color() == 1):   #cor preto
            andar_tras_inicio()
            x = False
    x = True 
 

def testColor():
    """
    cores = []
    while(cores.len()<25):
        cores.append(col.color)
        print(cores)
    """
    x = True
    while(x):
        if(col.color() == 7):
            fechar()
            sleep(1)
            andar_tras()
            andar_tras()
            direita()
            andar_tras()
            andar_tras()
            andar_tras()
            esquerda()
            andar_tras_inicio()
            andar33()
            abrir()
            sleep(1)
            andar_tras33()
            andar_tras_inicio()
            x = False
        print(col.color())
        if(col.color() == 5):
            fechar()
            sleep(1)
            andar_tras()
            andar_tras()
            direita()
            andar_tras()
            andar_tras()
            andar_tras()
            esquerda()
            andar_tras_inicio()
            andar44()
            abrir()
            abrir()
            sleep(1)
            andar_tras44()
            andar_tras_inicio()
            x = False
        print(col.color())
        if(col.color() == 4):
            fechar()
            sleep(1)
            andar_tras()
            andar_tras()
            direita()
            andar_tras()
            andar_tras()
            andar_tras()
            esquerda()
            andar_tras_inicio()
            andar43()
            abrir()
            abrir()
            parado()
            andar_tras43()
            andar_tras_inicio()
            x = False
        print(col.color())
        if(col.color() == 3):
            fechar()
            sleep(1)
            andar_tras()
            andar_tras()
            direita()
            andar_tras()
            andar_tras()
            andar_tras()
            esquerda()
            andar_tras_inicio()
            andar34()
            abrir()
            abrir()
            andar_tras34()
            andar_tras_inicio()
            x = False
        print(col.color())
        if(col.color() == 2):
            #fechar()
            fechar()
            sleep(1)
            #parado()
            andar_tras()
            andar_tras()
            #parado()
            direita()
            andar_tras()
            andar_tras()
            andar_tras()
            esquerda()
            #parado()
            andar_tras_inicio()
            andar24()
            abrir()
            sleep(1)
            #parado()
            andar_tras24()
            andar_tras_inicio()
            x = False
        print(col.color())
        if(col.color() == 1):
            andar_tras_inicio()
            x = False
    x = True 

def testDistance_inicio():

    distancia = 16
    print(distancia)
    while(distancia > 15 ):
        distancia=int(us.distance(False))/10
        print(distancia)
        andar()
    if(distancia<15):
        testColor_inicio()

    return distancia

def testDistance():

    #abrir()
    
    ola = 16
    print(ola)
    while(ola>15):
        ola=int(us.distance(False))/10
        print(ola)
        andar()
    if(ola<15):
        testColor()

    return ola


def parado():
    tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(0), 10)

def abrir():
    m.on_for_rotations(SpeedPercent(-50), 4) #Subir/Descer a garra

def andar():
    tank_drive.on_for_seconds(SpeedPercent(25), SpeedPercent(25), 1) #Rodar/Andar robot

def andar44():
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.75)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.5)

def andar43():
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.5)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 5.75)

def andar34():
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 5)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.5)

def andar33():
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 5)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 5)

def andar24():
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 4)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.5)

def andar14():
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 2.5)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.5)

def andar04():
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 1)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.5)

def andar_tras():
    tank_drive.on_for_seconds(SpeedPercent(-25), SpeedPercent(-25), 1) #Rodar/Andar robot

def andar_tras_inicio():
    while not ts.pressed():
        tank_drive.on_for_seconds(SpeedPercent(-25), SpeedPercent(-25), 1) #Rodar/Andar robot

def andar_tras44():
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 7)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.25)

def andar_tras43():
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.25)

def andar_tras34():
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 5)

def andar_tras33():
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 5)

def andar_tras24():
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 4)

def andar_tras14():
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 2.5)

def andar_tras04():
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 1)

def fechar():
    m.on_for_rotations(SpeedPercent(70), 5) #Subir/Descer a garra

def esquerda():
    tank_drive.on_for_seconds(SpeedPercent(-40), SpeedPercent(40), 1) #Rodar/Andar robot

def direita():
    tank_drive.on_for_seconds(SpeedPercent(40), SpeedPercent(-40), 1) #Rodar/Andar robot

if __name__== '__main__':
    main()
    