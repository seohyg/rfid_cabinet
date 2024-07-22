import gpiod
import time
LED_PIN = 17
chip = gpiod.Chip('gpiochip4')
led_line = chip.get_line(LED_PIN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT) #이름만 led로 조작
try:
   # for _ in range(10):
   while True:
       led_line.set_value(1)
       print("1")
       time.sleep(1)
       led_line.set_value(0)
       print("0")
       time.sleep(1)
finally:
   led_line.release()
