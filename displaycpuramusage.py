#pip install psutil

import time
import psutil

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  ", end="")
    print(f"\rRAM Usage: |{mem_bar}| {mem_usage:.2f}%  ", end= "\r")

while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5)