import mfrc522
from os import uname
from machine import Pin
from utime import sleep
botao_e = Pin(23, Pin.IN, Pin.PULL_UP)
led_1=Pin(5,Pin.OUT)
led_2=Pin(32,Pin.OUT)
led_4=Pin(33,Pin.OUT)
led_6=Pin(2,Pin.OUT)
led_7=Pin(4,Pin.OUT)
led_9=Pin(18,Pin.OUT)
led_10=Pin(26,Pin.OUT)

def do_read():

	rdr = mfrc522.MFRC522(14, 12, 13, 5, 27)

	print("")
	print("Em espera para leitura no endereço 0x08")
	print("")

	try:
		while botao_e.value():

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
					print("New card detected")
					print("  - tag type: 0x%02x" % tag_type)
					print("  - uid	 : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
					print("")

					if rdr.select_tag(raw_uid) == rdr.OK:

						key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

						if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
							dados=rdr.read(8)
							print("Address 8 data: %s" % dados)
							rdr.stop_crypto1()
							for dado in dados:
								led_1.value(0)
								led_2.value(0)
								led_4.value(0)
								led_6.value(0)
								led_7.value(0)
								led_9.value(0)
								led_10.value(0)
								if dado==0:
									led_1.value(1)
									led_2.value(1)
									led_4.value(1)
									led_6.value(1)
									led_7.value(1)
									led_9.value(1)
									sleep(0.8)
								if dado==1:
									led_1.value(1)
									led_9.value(1)
									sleep(0.8)
								if dado==2:
									led_1.value(1)
									led_2.value(1)
									led_6.value(1)
									led_7.value(1)
									led_10.value(1)
									sleep(0.8)
								if dado==3:
									led_2.value(1)
									led_4.value(1)
									led_6.value(1)
									led_7.value(1)
									led_10.value(1)
									sleep(0.8)
								if dado==4:
									led_4.value(1)
									led_6.value(1)
									led_9.value(1)
									led_10.value(1)
									sleep(0.8)
								if dado==5:
									led_2.value(1)
									led_4.value(1)
									led_7.value(1)
									led_9.value(1)
									led_10.value(1)
									sleep(0.8)
								if dado==6:
									led_1.value(1)
									led_2.value(1)
									led_4.value(1)
									led_7.value(1)
									led_9.value(1)
									led_10.value(1)
									sleep(0.8)
								if dado==7:
									led_4.value(1)
									led_6.value(1)
									led_7.value(1)
									sleep(0.8)
								if dado==8:
									led_1.value(1)
									led_2.value(1)
									led_4.value(1)
									led_6.value(1)
									led_7.value(1)
									led_9.value(1)
									led_10.value(1)
									sleep(0.8)
								if dado==9:
									led_4.value(1)
									led_6.value(1)
									led_7.value(1)
									led_9.value(1)
									led_10.value(1)
									sleep(0.8)
								if dado==10:
									t=0
									while t<5:
										led_1.value(1)
										led_9.value(1)
										sleep(0.08)
										led_1.value(0)
										led_9.value(0)
										sleep(0.08)
										t+=1
									t=0
									while t<5:
										led_1.value(1)
										led_2.value(1)
										led_4.value(1)
										led_6.value(1)
										led_7.value(1)
										led_9.value(1)
										sleep(0.08)
										led_1.value(0)
										led_2.value(0)
										led_4.value(0)
										led_6.value(0)
										led_7.value(0)
										led_9.value(0)
										sleep(0.08)
										t+=1
									sleep(0.5)
								if dado==11:
									t=0
									while t<5:
										led_1.value(1)
										led_9.value(1)
										sleep(0.08)
										led_1.value(0)
										led_9.value(0)
										sleep(0.08)
										t+=1
									t=0
									sleep(0.08)
									while t<5:
										led_1.value(1)
										led_9.value(1)
										sleep(0.08)
										led_1.value(0)
										led_9.value(0)
										sleep(0.08)
										t+=1
									sleep(0.5)
								if dado==12:
									t=0
									while t<5:
										led_1.value(1)
										led_9.value(1)
										sleep(0.08)
										led_1.value(0)
										led_9.value(0)
										sleep(0.08)
										t+=1
									t=0
									while t<5:
										led_1.value(1)
										led_2.value(1)
										led_6.value(1)
										led_7.value(1)
										led_10.value(1)
										sleep(0.08)
										led_1.value(0)
										led_2.value(0)
										led_6.value(0)
										led_7.value(0)
										led_10.value(0)
										sleep(0.08)
										t+=1
									sleep(0.5)
								if dado==13:
									t=0
									while t<5:
										led_1.value(1)
										led_9.value(1)
										sleep(0.08)
										led_1.value(0)
										led_9.value(0)
										sleep(0.08)
										t+=1
									t=0
									while t<5:
										led_2.value(1)
										led_4.value(1)
										led_6.value(1)
										led_7.value(1)
										led_10.value(1)
										sleep(0.08)
										led_2.value(0)
										led_4.value(0)
										led_6.value(0)
										led_7.value(0)
										led_10.value(0)
										sleep(0.08)
										t+=1
									sleep(0.5)
								if dado==14:
									t=0
									while t<5:
										led_1.value(1)
										led_9.value(1)
										sleep(0.08)
										led_1.value(0)
										led_9.value(0)
										sleep(0.08)
										t+=1
									t=0
									while t<5:
										led_4.value(1)
										led_6.value(1)
										led_9.value(1)
										led_10.value(1)
										sleep(0.08)
										led_4.value(0)
										led_6.value(0)
										led_9.value(0)
										led_10.value(0)
										sleep(0.08)
										t+=1
									sleep(0.5)
								if dado==15:
									t=0
									while t<5:
										led_1.value(1)
										led_9.value(1)
										sleep(0.08)
										led_1.value(0)
										led_9.value(0)
										sleep(0.08)
										t+=1
									t=0
									while t<5:
										led_2.value(1)
										led_4.value(1)
										led_7.value(1)
										led_9.value(1)
										led_10.value(1)
										sleep(0.08)
										led_2.value(0)
										led_4.value(0)
										led_7.value(0)
										led_9.value(0)
										led_10.value(0)
										sleep(0.08)
										t+=1
									sleep(0.5)
							led_4.value(0)
							led_6.value(0)
							led_7.value(0)
							led_10.value(0)
							led_1.value(1)
							led_2.value(1)
							led_9.value(1)
						else:
							print("Authentication error")
					else:
						print("Erro to select tag")

	except KeyboardInterrupt:
		print("Em espera")