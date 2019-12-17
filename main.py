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

vm = 0  #vermelho
am = 0  #amarelo
vd = 0  #verde
az = 0  #azul

def main():
    abrir()
    testDistance_inicio()
    while(col.color() != 1):
        colocarPecas()


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
        if(col.color() == 7):   #cor castanho
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
    x = True
    global vm #vermelho 5
    global am #amarelo  4
    global vd #verde    3
    global az #azul     2

    while(x):
        if(col.color() == 7):
            fechar()
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
            sleep(1)
            vm += 1
            print("vermelho") 
            if(vm == 1):
                andar44()
                abrir()
                abrir()
                parado()
                andar_tras44()
            if(vm == 2):
                andar43()
                abrir()
                abrir()
                parado()
                andar_tras43()
            if(vm == 3):
                andar42()
                abrir()
                abrir()
                parado()
                andar_tras42()
            if(vm == 4):
                andar04()
                abrir()
                abrir()
                parado()
                andar_tras04()
            andar_tras_inicio()
            x = False
        print(col.color())
        if(col.color() == 4):
            fechar()
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
            sleep(1)
            am += 1
            print("amarelo") 
            if(am == 1):
                andar34()
                abrir()
                abrir()
                parado()
                andar_tras34()
            if(am == 2):
                andar33()
                abrir()
                abrir()
                parado()
                andar_tras33()
            if(am == 3):
                andar32()
                abrir()
                abrir()
                parado()
                andar_tras32()
            if(am == 4):
                andar03()
                abrir()
                abrir()
                parado()
                andar_tras03()
            andar_tras_inicio()
            x = False
        print(col.color())
        if(col.color() == 3):
            fechar()
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
            sleep(1)
            vd += 1
            print("verde") 
            if(vd == 1):
                andar24()
                abrir()
                abrir()
                parado()
                andar_tras24()
            if(vd == 2):
                andar23()
                abrir()
                abrir()
                parado()
                andar_tras23()
            if(vd == 3):
                andar22()
                abrir()
                abrir()
                parado()
                andar_tras22()
            if(vd == 4):
                andar02()
                abrir()
                abrir()
                parado()
                andar_tras02()
            andar_tras_inicio()
            x = False
        print(col.color())
        if(col.color() == 2):
            fechar()
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
            sleep(1)
            az += 1
            print("azul") 
            if(az == 1):
                andar14()
                abrir()
                abrir()
                parado()
                andar_tras14()
            if(az == 2):
                andar13()
                abrir()
                abrir()
                parado()
                andar_tras13()
            if(az == 3):
                andar12()
                abrir()
                abrir()
                parado()
                andar_tras12()
            if(az == 4):
                andar02()
                abrir()
                abrir()
                parado()
                andar_tras02()
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
    m.on_for_rotations(SpeedPercent(-75), 4) #Subir/Descer a garra

def andar():
    tank_drive.on_for_seconds(SpeedPercent(25), SpeedPercent(25), 1) #Rodar/Andar robot

def andar44():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 7)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 7.5)

def andar43():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 7)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 5.75)

def andar42():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 7)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 4.25)

def andar41():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 7)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 2.75)

def andar40():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 7)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 1)

def andar34():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 5.30)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 7)

def andar33():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 5.30)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 5.75)

def andar32():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 5.30)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 4.25)

def andar31():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 5.30)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 2.75)

def andar30():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 5.30)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 1)

def andar24():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 4)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 7)

def andar23():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 4)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 5.75) 

def andar22():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 4)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 4.25)

def andar21():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 4)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 2.75)

def andar20():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 4)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 1)

def andar14():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 2.5)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 7)

def andar13():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 2.5)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 5.75)

def andar12():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 2.5)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 4.25)

def andar11():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 2.5)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 2.75)

def andar10():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 2.5)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 1)

def andar04():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 1)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 7)

def andar03():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 1)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 5.75)

def andar02():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 1)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 4.25)

def andar01():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 1)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 2.75)

def andar00():
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 1)
    esquerda()
    tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(70), 1)

def andar_tras():
    tank_drive.on_for_seconds(SpeedPercent(-25), SpeedPercent(-25), 1) #Rodar/Andar robot

def andar_tras_inicio():
    while not ts.pressed():
        tank_drive.on_for_seconds(SpeedPercent(-25), SpeedPercent(-25), 1) #Rodar/Andar robot

def andar_tras44():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 7)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 6.25)

def andar_tras43():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 6)

def andar_tras42():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 6)

def andar_tras41():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 3)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 6)

def andar_tras40():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 1)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 6)

def andar_tras34():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 5.75)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 5)

def andar_tras33():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 5.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 5)

def andar_tras32():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 5)

def andar_tras31():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 3)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 5)

def andar_tras30():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 1)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 5)

def andar_tras24():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 6.75)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 3.5)

def andar_tras23():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 5.75)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 3.5)

def andar_tras22():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 4.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 3.5)

def andar_tras21():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 3)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 3.5)

def andar_tras20():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 1)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 3.5)

def andar_tras14():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 6.75)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 2)

def andar_tras13():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 5.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 2)

def andar_tras12():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 4.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 2)

def andar_tras11():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 3)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 2)

def andar_tras10():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 1)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 2)

def andar_tras04():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 7)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 0.5)

def andar_tras03():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 6)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 0.5)

def andar_tras02():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 4.5)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 0.5)

def andar_tras01():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 3)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 0.5)

def andar_tras00():
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 1)
    direita()
    tank_drive.on_for_seconds(SpeedPercent(-70), SpeedPercent(-70), 0.5)

def fechar():
    m.on_for_rotations(SpeedPercent(75), 5) #Subir/Descer a garra

def esquerda():
    tank_drive.on_for_seconds(SpeedPercent(-35), SpeedPercent(35), 1) #Rodar/Andar robot

def direita():
    tank_drive.on_for_seconds(SpeedPercent(35), SpeedPercent(-35), 1) #Rodar/Andar robot

if __name__ == '__main__':
    main()
