import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Take a break. 😊\n")

def pomodoro_timer():
    work_duration = 25  # minutes
    short_break = 5
    long_break = 15
    sessions = 0

    while True:
        print(f"🔔 Pomodoro {sessions + 1} started! Focus for {work_duration} minutes.")
        countdown(work_duration)
        sessions += 1

        if sessions % 4 == 0:
            print("🎉 Time for a long break!")
            countdown(long_break)
        else:
            print("☕ Take a short break.")
            countdown(short_break)

        user_input = input("Start next session? (y/n): ")
        if user_input.lower() != 'y':
            print("Good job today! 🚀")
            break

pomodoro_timer()
