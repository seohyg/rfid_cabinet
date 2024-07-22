from fastapi import FastAPI, HTTPException
import gpiod  # RPi.GPIO 대신 gpiod 사용
import time

app = FastAPI()

# GPIO 핀 설정
LED_PIN = 17   # 17번 핀

@app.post("/open_solenoid")  # 엔드포인트 경로 변경
def open_solenoid():
    try:
        chip = gpiod.Chip('gpiochip4')
        led_line = chip.get_line(LED_PIN)
        led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
        led_line.set_value(1)
        print("open complete!!")
    finally:
        time.sleep(10)
        led_line.set_value(0)
        led_line.release()

    print("closed!!")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
