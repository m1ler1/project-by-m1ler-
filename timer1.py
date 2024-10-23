import time

def timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = f'{mins:02d}:{secs:02d}'
        print(timer_format, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Время вышло!")
if __name__ == "__main__":
    seconds = int(input("Введите время в секундах: "))
    timer(seconds)
