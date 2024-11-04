from imports import *

# Variaveis dos componentes do robô
sensorFrontal = LUMPDevice(Port.S1)
gyro = LUMPDevice(Port.S2)

# Variaveis dos 4 motores das rodas
motor1 = LUMPDevice(Port.A)
motor2 = LUMPDevice(Port.B)
motor3 = LUMPDevice(Port.C)
motor4 = LUMPDevice(Port.D)

# Variaveis do sensor frontal
MODO_SENSOR_FRONTAL = 0
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

# Variáveis de motores
KP = 0.5
KD = 0

# Variaveis antigas
# SOMAPRETO = 45
# TETO = 255
# ESQUERDO = -1
# DIREITO = 1
# COR_BRANCO = 60.5
# VERDE = 1.6
# VERMELHO = 4.5
# vezes_perdido = 0
# milliseconds = 0
# dif_ideal = 40
# DIF_SUP_IDEAL = 5
# Distacia_obstaculo = 30

