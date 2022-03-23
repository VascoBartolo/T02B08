# boot.py - - runs on boot-up

from machine import Pin, SPI
from utime import sleep
import read
import write

led_vm = Pin(21, Pin.OUT)
led_vd=Pin(22, Pin.OUT)
led_am=Pin(19,Pin.OUT)

led_1=Pin(5,Pin.OUT)
led_2=Pin(32,Pin.OUT)
led_4=Pin(33,Pin.OUT)
led_6=Pin(2,Pin.OUT)
led_7=Pin(4,Pin.OUT)
led_9=Pin(18,Pin.OUT)
led_10=Pin(26,Pin.OUT)

#sequencia de inicializacao
#Iniciar os comandos
botao_e = Pin(23, Pin.IN, Pin.PULL_UP)
botao_d = Pin(35, Pin.IN, Pin.PULL_UP)
led_vd.value(1) #Se led verde acender -> ok
sleep(1)
led_vm.value(0)
led_vd.value(0)
led_am.value(0)
#fim de sequencia
