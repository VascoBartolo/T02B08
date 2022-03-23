import mfrc522
import random
from os import uname
from machine import Pin
from utime import sleep
botao_d = Pin(35, Pin.IN, Pin.PULL_UP)
botao_e = Pin(23, Pin.IN, Pin.PULL_UP)
led_1=Pin(5,Pin.OUT)
led_2=Pin(32,Pin.OUT)
led_4=Pin(33,Pin.OUT)
led_6=Pin(2,Pin.OUT)
led_7=Pin(4,Pin.OUT)
led_9=Pin(18,Pin.OUT)
led_10=Pin(26,Pin.OUT)
led_am=Pin(19,Pin.OUT)
led_vm = Pin(21, Pin.OUT)


def do_write():

	rdr = mfrc522.MFRC522(14, 12, 13, 5, 27)
	led_1.value(1)
	led_2.value(1)
	led_7.value(1)
	led_9.value(1)
	led_10.value(1)
	print("")
	print("Em espera para escrever address 0x08")
	print("")

	try:
		dados=[]
		dados.append('b"')
		while botao_d.value(): #pressionar botao direito para sair
			led_1.value(0)
			led_2.value(0)
			led_4.value(0)
			led_6.value(0)
			led_7.value(0)
			led_9.value(0)
			led_10.value(0)
			print('Em espera para escrever no cartao - pressionar botao esquerdo para continuar')
			n = random.randint(1,5)
			print(n)
			led_1.value(1)
			led_2.value(1)
			led_7.value(1)
			led_9.value(1)
			led_10.value(1)
			while botao_e.value(): #aguarda confirmacao com botão esquerdo
				sleep(0.05)
				led_vm.value(0)
				sleep(0.05)
				led_vm.value(1)
			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
					led_1.value(0)
					led_2.value(0)
					led_4.value(0)
					led_6.value(0)
					led_7.value(0)
					led_9.value(0)
					led_10.value(0)
					if n==1:
						led_1.value(1)
						led_9.value(1)
					if n==2:
						led_1.value(1)
						led_2.value(1)
						led_6.value(1)
						led_7.value(1)
						led_10.value(1)
					if n==3:
						led_2.value(1)
						led_4.value(1)
						led_6.value(1)
						led_7.value(1)
						led_10.value(1)
					if n==4:
						led_4.value(1)
						led_6.value(1)
						led_9.value(1)
						led_10.value(1)
					if n==5:
						led_2.value(1)
						led_4.value(1)
						led_7.value(1)
						led_9.value(1)
						led_10.value(1)
					sleep(2)
					print("Novo cartao encontrado")
					print("  - tag type: 0x%02x" % tag_type)
					print("  - uid	 : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
					print("")

					if rdr.select_tag(raw_uid) == rdr.OK:

						key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

						if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
							if n==1:
								stat = rdr.write(8,b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f")
							if n==2:
								stat = rdr.write(8,b"\x0f\x01\x0e\x03\x0d\x05\x0c\x07\x0b\x09\x0a\x00\x02\x06\x08\x05")
							if n==3:
								stat = rdr.write(8,b"\x0f\x0e\x0d\x0c\x0b\x0a\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09")
							if n==4:
								stat = rdr.write(8,b"\x00\x0a\x01\x0b\x02\x0c\x03\x0d\x04\x0e\x05\x0f\x06\x07\x08\x09")
							if n==5:
								stat = rdr.write(8,b"\x03\x07\x0a\x01\x0c\x0e\x01\x09\x08\x0b\x05\x0d\x02\x04\x0f\x06")
							rdr.stop_crypto1()
							if stat == rdr.OK:
								print("Guardado com sucesso")
							else:
								print("Erro a guardar")
						else:
							print("Authentication error")
					else:
						print("Failed to select tag")
			print('Fim - pressionar botao esquerdo para continuar')
			led_1.value(0)
			led_2.value(0)
			led_4.value(0)
			led_6.value(0)
			led_7.value(0)
			led_9.value(0)
			led_10.value(0)
			led_1.value(1)
			led_2.value(1)
			led_7.value(1)
			led_9.value(1)
			led_10.value(1)
			led_vm.value(0)
			while botao_e.value():
				sleep(0.05)
				led_am.value(0)
				sleep(0.05)
				led_am.value(1)
			led_am.value(0)
			
			sleep(1.8)
	except KeyboardInterrupt:
		print("Bye")