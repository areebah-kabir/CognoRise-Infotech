import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f'{mins:02d}:{secs:02d}'
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

seconds = int(input("Enter the countdown time in seconds: "))
countdown(seconds)
