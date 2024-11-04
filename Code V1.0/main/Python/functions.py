from variables import *

# Atualização de valores
def atualizarSensorFrontal(modo):
    MODO_SENSOR_FRONTAL = modo
    linha4 = sensorFrontal.read(MODO_SENSOR_FRONTAL)[0] #type: ignore
    linha3 = sensorFrontal.read(MODO_SENSOR_FRONTAL)[1] #type: ignore
    linha2 = sensorFrontal.read(MODO_SENSOR_FRONTAL)[2] #type: ignore
    linha1 = sensorFrontal.read(MODO_SENSOR_FRONTAL)[3] #type: ignore

    hueEsquerda = sensorFrontal.read(0)[26] # type: ignore
    saturationEsquerda = sensorFrontal.read(0)[27] # type: ignore
    valueEsquerda = sensorFrontal.read(0)[28] # type: ignore

    hueDireita = sensorFrontal.read(0)[20] # type: ignore
    saturationDireita = sensorFrontal.read(0)[21] # type: ignore
    valueDireita = sensorFrontal.read(0)[22] # type: ignore

# Funcoes de verde
def verificarVerdeEsquerda():
    atualizarSensorFrontal(0)
    if 24 <= hueEsquerda <= 55 and saturationEsquerda >= 20 and valueEsquerda >= 9:
        return True
    return False

def verificarVerdeDireita():
    atualizarSensorFrontal(0)
    if 24 <= hueDireita <= 55 and saturationDireita >= 20 and valueDireita >= 9:
        return True
    return False

# Funcoes sensor frontal de linha
def difSensores():   
    atualizarSensorFrontal(0)
    return - linha1 - linha2 + linha3 + linha4

def pid(dif, difAnterior):
    P = dif * KP
    D = (dif - difAnterior) * KD
    return P + D


# Funcoes de movimento basico

# def moverFrente(distancia, VELOCIDADE):

def gire(angulo, direcao):
    motor1.dc(VELOCIDADE * DIRECAO)
    motor2.dc(-VELOCIDADE * DIRECAO)
    motor3.dc(VELOCIDADE * DIRECAO)
    motor4.dc(-VELOCIDADE * DIRECAO)

# def parada(milisec):    


def virar90(lado):
    atualizarSensorFrontal()
    if lado == DIREITO: 
        while linha1 and linha2 and linha3 and linha4 != 0:
            gire(50, lado)
    if lado == ESQUERDO: 
        while linha1 and linha2 and linha3 and linha4 != 0:
            gire(50, lado)

def verificar90():
    atualizarSensorFrontal()
    if linha4 and linha3 == 1:
        print("Virar 90 direito")
        virar90(DIREITO)
    
    elif linha4 and linha3 == 1:
        print("Virar 90 direito")
        virar90(ESQUERDO)
        
        


       
# def atualizarVelocidade(): 


     
# def virar_verde(lado):

        
# motor_direito = Motor(Port.A,positive_direction=Direction.CLOCKWISE)
# motor_esquerdo = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
# motor_direito2 = Motor(Port.C,positive_direction=Direction.CLOCKWISE)
# motor_esquerdo2 = Motor(Port.D,positive_direction=Direction.COUNTERCLOCKWISE)