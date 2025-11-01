from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Inicialização do hub e motores
hub = PrimeHub()
me = Motor(Port.F, Direction.COUNTERCLOCKWISE)
md = Motor(Port.B)
mt_crema = Motor(Port.E)
mt_cremaII = Motor(Port.A)

# Base de movimentação
drive_base = DriveBase(me, md, wheel_diameter=57, axle_track=96)
drive_base.use_gyro(True)

# Funções de movimento
def andar(dist, velocidade=350):
    drive_base.settings(velocidade, velocidade, 220, 220)
    drive_base.straight(-dist * 10)

def turn(radius, angle):
    drive_base.settings(200, 200, 200, 200)
    drive_base.curve(radius, angle)

def rotate(graus):
    drive_base.settings(220, 220, 220, 220)
    drive_base.turn(graus)

# Funções para acionar cremalheiras individualmente
def acionar_crema(velocidade=500, angulo=360):
    mt_crema.run_angle(velocidade, angulo)

def acionar_cremaII(velocidade=500, angulo=360):
    mt_cremaII.run_angle(velocidade, angulo)

# Configurações iniciais
hub.system.set_stop_button(Button.BLUETOOTH)
drive_base.use_gyro(True)
mt_crema.brake()
mt_cremaII.brake()

# Variáveis de controle
lancamento = 1
tempo = StopWatch()

# Loop principal
while True:
    hub.display.number(lancamento)
    botoes = hub.buttons.pressed()

    # Ajuste do valor de lançamento
    if Button.LEFT in botoes:
        if lancamento > -99:
            lancamento -= 1
            hub.display.number(lancamento)
            wait(250)

    elif Button.RIGHT in botoes:
        if lancamento < 99:
            lancamento += 1
            hub.display.number(lancamento)
            wait(250)

    elif Button.CENTER in botoes:
        wait(300)
        print("Bateria:", hub.battery.voltage(), "mV")
        print("Lançamento atual:", lancamento)
        wait(1000)

        if hub.battery.voltage() < 7700:
            hub.display.text("Bateria baixa")
            wait(1500)
        else:
            wait(1000)

            if lancamento == 1:
                andar(74, 350)      # missão das pedras
                andar(-5, 350)
                turn(10, -20)       
                wait(200)
                andar(12, 350)
                turn(10, -70)       # missão virada histórica
                andar(35, 350)
                turn(10, 45)
                andar(10, 350)
                wait(200)
                andar(-35, 500)     # missão do telhado
                wait(300)
                andar(28, 350)
                turn(10, -45)
                wait(100)
                turn(10,-60)
                andar(52, 350)
                turn(1, 100)
                acionar_cremaII(500, 360)     # aciona apenas mt_crema
                andar(10,300)
                acionar_cremaII(900,-360)# missão da baleia
                andar(-5,300)
                turn(10,-40)
                andar(-10,200)
                turn(10,-15)
                acionar_cremaII(500, -600) # fazer missão da balança
                acionar_cremaII(500, 360)
                andar(10,500)
                turn(10,-30)
                andar(40)
                turn(10,27)
                andar(-15,500)
