# main.py

while botao_e.value() and botao_d.value():
    led_vm.value(0)
    led_vd.value(0)
    while botao_e.value() and botao_d.value():
        led_am.value(1)
    be=botao_e.value()
    bd=botao_d.value()
    t=0
    while t<5:
        sleep(0.05)
        led_am.value(0)
        sleep(0.05)
        led_am.value(1)
        t+=1
    led_am.value(0) 
    if be==0:#modo leitura
        led_vm.value(1)
        while botao_e.value():
            led_1.value(1)
            led_2.value(1)
            led_4.value(0)
            led_6.value(0)
            led_7.value(0)
            led_9.value(1)
            led_10.value(0)
            read.do_read()
			
    if bd==0:#modo escrita
        led_vd.value(1)
        while botao_d.value():
            led_1.value(1)
            led_2.value(1)
            led_4.value(0)
            led_6.value(0)
            led_7.value(1)
            led_9.value(1)
            led_10.value(1)
            write.do_write()
            
    led_1.value(0)
    led_2.value(0)
    led_4.value(0)
    led_6.value(0)
    led_7.value(0)
    led_9.value(0)
    led_10.value(0)
    led_vm.value(1)
    led_am.value(1)
    led_vd.value(1)
    sleep(0.5)

#fim
led_vm.value(0)
led_am.value(0)
led_vd.value(0)