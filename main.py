from machine import Pin, I2C
import utime
from mpu6050 import init_mpu6050, get_mpu6050_data
import time
import machine

 
i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)
init_mpu6050(i2c)

# Función para avanzar un paso en un eje dado en un sentido dado
def avanzar_motor(sentido, pin1, pin2, pin3, pin4, secuencia_pasos):
    for paso in secuencia_pasos:
        pin1.value(paso[0])
        pin2.value(paso[1])
        pin3.value(paso[2])
        pin4.value(paso[3])
        #time.sleep(0.01)  # Retardo entre pasos
        time.sleep(0.01)

# Función para mover la plataforma en un eje dado en un sentido dado
def mover_plataforma(eje, sentido, pasos):
    if eje == "X":
        pin1 = pin1_X
        pin2 = pin2_X
        pin3 = pin3_X
        pin4 = pin4_X
        secuencia_pasos = secuencia_pasos_horario if sentido == "horario" else secuencia_pasos_antihorario
    elif eje == "Y":
        pin1 = pin1_Y
        pin2 = pin2_Y
        pin3 = pin3_Y
        pin4 = pin4_Y
        secuencia_pasos = secuencia_pasos_horario if sentido == "horario" else secuencia_pasos_antihorario
    else:
        raise ValueError("Eje no válido")

    for _ in range(pasos):
        avanzar_motor(sentido, pin1, pin2, pin3, pin4, secuencia_pasos)
        
            
            

    
while True:
    data = get_mpu6050_data(i2c)
    print("Temperature: {:.2f} °C".format(data['temp']), "  Acceleration: X: {:.2f}, Y: {:.2f}, Z: {:.2f} g".format(data['accel']['x'], data['accel']['y'], data['accel']['z']), "  Gyroscope: X: {:.2f}, Y: {:.2f}, Z: {:.2f} °/s".format(data['gyro']['x'],data['gyro']['y'], data['gyro']['z']))
    #print("Acceleration: X: {:.2f}, Y: {:.2f}, Z: {:.2f} g".format(data['accel']['x'], data['accel']['y'], data['accel']['z']))
    #print("Gyroscope: X: {:.2f}, Y: {:.2f}, Z: {:.2f} °/s".format(data['gyro']['x'],data['gyro']['y'], data['gyro']['z']))
    #utime.sleep(0.01)

    
    # Configuración de los pines para el motor del eje X
    pin1_X = machine.Pin(0, machine.Pin.OUT)
    pin2_X = machine.Pin(1, machine.Pin.OUT)
    pin3_X = machine.Pin(2, machine.Pin.OUT)
    pin4_X = machine.Pin(3, machine.Pin.OUT)

    # Configuración de los pines para el motor del eje Y
    pin1_Y = machine.Pin(4, machine.Pin.OUT)
    pin2_Y = machine.Pin(5, machine.Pin.OUT)
    pin3_Y = machine.Pin(6, machine.Pin.OUT)
    pin4_Y = machine.Pin(7, machine.Pin.OUT)

    # Secuencia de pasos para el motor paso a paso en sentido horario
    secuencia_pasos_horario = [
        [1, 0, 1, 0],  # Paso 1
        [0, 1, 1, 0],  # Paso 2
        [0, 1, 0, 1],  # Paso 3
        [1, 0, 0, 1]   # Paso 4
    ]

    # Secuencia de pasos para el motor paso a paso en sentido antihorario
    secuencia_pasos_antihorario = [
        [1, 0, 0, 1],  # Paso 1
        [0, 1, 0, 1],  # Paso 2
        [0, 1, 1, 0],  # Paso 3
        [1, 0, 1, 0]   # Paso 4
    ]


    # Ejemplo de movimiento de la plataforma
    mover_plataforma("X", "antihorario", 20)  # Mover 10 pasos en el eje X en sentido antihorario
    time.sleep(0.1)  # Retardo antes de cambiar el sentido
    mover_plataforma("X", "antihorario", 20)  # Mover 10 pasos en el eje X en sentido antihorario
    time.sleep(0.1)  # Retardo antes de cambiar el sentido
    mover_plataforma("Y", "antihorario", 20)  # Mover 10 pasos en el eje Y en sentido antihorario
    time.sleep(0.1)  # Retardo antes de cambiar el sentido
    mover_plataforma("Y", "antihorario", 20)  # Mover 10 pasos en el eje Y en sentido antihorario
    time.sleep(0.1)  # Retardo antes de cambiar el sentido
    mover_plataforma("X", "horario", 20)  # Mover 10 pasos en el eje X en sentido horario
    #time.sleep(0.1)  # Retardo antes de cambiar el sentido
    mover_plataforma("Y", "horario", 20)  # Mover 10 pasos en el eje Y en sentido horario
    #time.sleep(0.1)  # Retardo antes de mover en ambos ejes
    mover_plataforma("X", "horario", 20)  # Mover 10 pasos en el eje X en sentido horario
    #time.sleep(0.1)  # Retardo antes de cambiar el sentido
    mover_plataforma("Y", "horario", 20)  # Mover 10 pasos en el eje Y en sentido horario
    #time.sleep(0.1)  # Retardo antes de mover en ambos ejes
    mover_plataforma("X", "antihorario", 20)  # Mover 10 pasos en el eje X en sentido antihorario
    #time.sleep(0.1)  # Retardo antes de mover en ambos ejes
    mover_plataforma("Y", "antihorario", 20)  # Mover 10 pasos en el eje Y en sentido antihorario
    #time.sleep(0.1)  # Retardo antes de mover en ambos ejes
    mover_plataforma("X", "horario", 20)  # Mover 10 pasos en el eje X en sentido horario
    #time.sleep(0.1)  # Retardo antes de cambiar el sentido
    mover_plataforma("Y", "horario", 20)  # Mover 10 pasos en el eje Y en sentido horario
    #time.sleep(0.1)  # Retardo antes de mover en ambos ejes

    # Detener el motor del eje X
    pin1_X.value(0)
    pin2_X.value(0)
    pin3_X.value(0)
    pin4_X.value(0)

    # Detener el motor del eje Y
    pin1_Y.value(0)
    pin2_Y.value(0)
    pin3_Y.value(0)
    pin4_Y.value(0)