from datetime import datetime, time
import schedule
import time as time_module
from playsound import playsound

def ring_bell(sound_file="bell.mp3"):
    """Play the bell sound"""
    try:
        playsound(sound_file)
        print(f"Bell rung at {datetime.now().strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"Error playing bell sound: {str(e)}")


# Define bell times (24-hour format)
bell_times = [
    (8, 30),
    (8, 35),
    (10, 2),
    (10, 7),
    (11, 36),
    (12, 11),
    (12, 16),
    (13, 43),
    (13, 50),
    (15, 17)
]

wednesday_bell_times = [
    (8, 30),
    (8, 35),
    (9, 46),
    (9, 53),
    (11, 4),
    (11, 48),
    (12, 55),
    (12, 59),
    (13, 6),
    (14, 17)
]

for hour, minute in bell_times:
    schedule_time = f"{hour:02d}:{minute:02d}"
    schedule.every().monday.at(schedule_time).do(ring_bell)
    schedule.every().tuesday.at(schedule_time).do(ring_bell)
    schedule.every().thursday.at(schedule_time).do(ring_bell)
    schedule.every().friday.at(schedule_time).do(ring_bell)
for hour, minute in wednesday_bell_times:
    schedule_time = f"{hour:02d}:{minute:02d}"
    schedule.every().wednesday.at(schedule_time).do(ring_bell)

# Run the scheduler
try:
    print("Bell scheduler is running. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time_module.sleep(1)    
except KeyboardInterrupt:
    print("\nShutting down bell scheduler...")
