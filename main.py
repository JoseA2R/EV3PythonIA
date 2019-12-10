#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor, TouchSensor
from pybricks.parameters import Port ,Color
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank

ts = TouchSensor(Port.S2)

def main():
    abrir()
    testDistance_inicio()
    andar()
    direita()
    andar()
    andar()
    andar()
    esquerda()
    testDistance()
    andar_tras_inicio()
    testDistance()
    """
    abrir()
    testDistance()
    direita()
    testDistance()
    direita()
"""

def testColor_inicio():
    col = ColorSensor(Port.S3)
    x = True
    while(x):
        if(col.color() == 7):
            fechar()
            parado()
            direita()
            parado()
            andar()
            parado()
            abrir()
            parado()
            andar_tras()
            parado()
            esquerda()
            testDistance_inicio()
            x = False
        print(col.color())
        if(col.color() == 5):
            fechar()
            parado()
            direita()
            parado()
            andar()
            parado()
            abrir()
            parado()
            andar_tras()
            parado()
            esquerda()
            testDistance_inicio()
            x = False
        print(col.color())
        if(col.color() == 4):
            fechar()
            parado()
            direita()
            parado()
            andar()
            parado()
            abrir()
            parado()
            andar_tras()
            parado()
            esquerda()
            testDistance_inicio()
            x = False
        print(col.color())
        if(col.color() == 3):
            fechar()
            parado()
            direita()
            parado()
            andar()
            parado()
            abrir()
            parado()
            andar_tras()
            parado()
            esquerda()
            testDistance_inicio()
            x = False
        print(col.color())
        if(col.color() == 2):
            fechar()
            parado()
            direita()
            parado()
            andar()
            parado()
            abrir()
            parado()
            andar_tras()
            parado()
            esquerda()
            testDistance_inicio()
            x = False
        print(col.color())
        if(col.color() == 1):
            andar_tras_inicio()
            x = False
    x = True 
 

def testColor():
    col = ColorSensor(Port.S3)
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
            fechar()
            parado()
            andar_tras()
            andar_tras()
            parado()
            esquerda()
            parado()
            andar_tras_inicio()
            andar33()
            abrir()
            parado()
            andar_tras33()
            andar_tras_inicio()
            testDistance()
            x = False
        print(col.color())
        if(col.color() == 5):
            fechar()
            fechar()
            parado()
            andar_tras()
            andar_tras()
            parado()
            esquerda()
            andar()
            parado()
            direita()
            andar_tras_inicio()
            andar44()
            parado()
            abrir()
            abrir()
            parado()
            andar_tras44()
            andar_tras_inicio()
            testDistance()
            x = False
        print(col.color())
        if(col.color() == 4):
            fechar()
            fechar()
            parado()
            andar_tras()
            andar_tras()
            parado()
            esquerda()
            parado()
            andar_tras_inicio()
            andar43()
            abrir()
            parado()
            andar_tras43()
            andar_tras_inicio()
            testDistance()
            x = False
        print(col.color())
        if(col.color() == 3):
            fechar()
            fechar()
            parado()
            andar_tras()
            andar_tras()
            parado()
            esquerda()
            parado()
            andar()
            direita()
            andar_tras_inicio()
            andar34()
            parado()
            parado()
            abrir()
            abrir()
            parado()
            parado()
            andar_tras34()
            andar_tras_inicio()
            testDistance()
            x = False
        print(col.color())
        if(col.color() == 2):
            fechar()
            fechar()
            parado()
            andar_tras()
            andar_tras()
            parado()
            esquerda()
            parado()
            andar_tras_inicio()
            andar24()
            abrir()
            parado()
            andar_tras24()
            andar_tras_inicio()
            testDistance()
            x = False
        print(col.color())
        if(col.color() == 1):
            andar_tras_inicio()
            x = False
    x = True 

def testDistance_inicio():
    us = UltrasonicSensor(Port.S4)

    ola = 16
    print(ola)
    while(ola>15 ):
        ola=int(us.distance(False))/10
        print(ola)
        andar()
    if(ola<15):
        testColor_inicio()

    return ola

def testDistance():
    us = UltrasonicSensor(Port.S4)
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
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(0), 10)

def abrir():
    m = MediumMotor(OUTPUT_A)
    m.on_for_rotations(SpeedPercent(-50), 4) #Subir/Descer a garra

def andar():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(25), SpeedPercent(25), 1) #Rodar/Andar robot

def andar44():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.75)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.5)

def andar43():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.5)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 5.75)

def andar34():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 5)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.5)

def andar33():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 5)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 5)

def andar24():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 4)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.5)

def andar14():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 2.5)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.5)

def andar04():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 1)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 6.5)

def andar_tras():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(-25), SpeedPercent(-25), 1) #Rodar/Andar robot

def andar_tras_inicio():
    while not ts.pressed():
        tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
        tank_drive.on_for_seconds(SpeedPercent(-25), SpeedPercent(-25), 1) #Rodar/Andar robot

def andar_tras44():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 7)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.25)

def andar_tras43():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.25)

def andar_tras34():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 5)

def andar_tras33():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 5)

def andar_tras24():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 4)

def andar_tras14():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 2.5)

def andar_tras04():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 6.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-100), SpeedPercent(-100), 1)

def fechar():
    m = MediumMotor(OUTPUT_A)
    m.on_for_rotations(SpeedPercent(70), 5) #Subir/Descer a garra

def esquerda():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(-40), SpeedPercent(40), 1) #Rodar/Andar robot

def direita():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(40), SpeedPercent(-40), 1) #Rodar/Andar robot

if __name__== '__main__':
    main()
    