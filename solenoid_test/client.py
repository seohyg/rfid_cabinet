import requests

# 라즈베리파이 IP 주소와 포트 번호를 사용하여 요청을 보냅니다.
raspberry_pi_ip = "192.168.0.134" #본인의 IP 입력

# 솔레노이드 열기
response = requests.post(f'http://{raspberry_pi_ip}:8000/open_solenoid')

print(response.json())
