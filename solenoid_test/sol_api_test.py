from fastapi import FastAPI, HTTPException
import gpiod 
import time

app = FastAPI()

# GPIO 핀 설정
LED_PIN = 17

@app.post("/open_solenoid")
def open_solenoid():
    try:
        chip = gpiod.Chip('gpiochip4')
        led_line = chip.get_line(LED_PIN)
        led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
        led_line.set_value(1) #솔레오이드 작동소이 생각보다 큼
        print("open complete!!")
    finally:
        time.sleep(10) #10초 정지
        led_line.set_value(0)
        led_line.release()

    print("closed!!")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
