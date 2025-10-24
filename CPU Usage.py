import psutil
import time

print("Checking your CPU usage... (Press Ctrl + C to stop)\n")

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU usage: {cpu_usage}%")
    time.sleep(1)