import time

def delay(seconds):
    time.sleep(seconds)

def five_minute_timer():
    total_seconds = 5 * 60  # 5 minutes in seconds
    for remaining in range(total_seconds, 0, -1):
        minutes, seconds = divmod(remaining, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end='\r')
        delay(1)
    print("Time's up!")

# Call the function to start the timer
five_minute_timer()