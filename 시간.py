#시간 측정 프로그램
import time
start_time=time.perf_counter()

#실행 구문 입력








#여기까지
end_time=time.perf_counter()
dur_time=end_time-start_time
print(f"코드 실행 시간: {int(round(dur_time, 3)*1000)}ms")
