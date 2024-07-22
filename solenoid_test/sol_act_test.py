import gpiod
import time

######필독!! 솔레노이드가 트리거 된 상태로 터미널 종료 후 방치되면 과열로 코일 손상 및 연기가 발생할 수 있음. (직접 겪어 봄)######
#라즈베리 파이 sd카드 다룰 때는 항상 전원이 꺼진 후에 

LED_PIN = 17
chip = gpiod.Chip('gpiochip4')
led_line = chip.get_line(LED_PIN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT) #이름만 led로 조작
try:
   # 1초에 한번씩 딸깍 거리는 작동.
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

#작동하지 않는 경우
#릴레이에서 틱,틱,틱 소리는 나는 경우 : 솔레노이드 고장 및 소렐노이드 부근 배선 및 단선 확인
#릴레이에서 틱,틱,틱 소리는 안나지만 릴레이 led는 잘 작동하는 경우 : GND 확인 및 PSU 전원 확인
#릴레이가 작동하지 않는 경우 : 라즈베리 파이로 부터 오는 신호선 확인. 코드에 'gpiochip4' 이 부분 'gpiochip0' ~ 'gpiochip4' 으로 하나씩 바꿔보기.
