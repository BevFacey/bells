# pip3 install pygame
# sudo apt install install libsdl2-mixer-2.0-0

from datetime import datetime
import schedule
import time as time_module
import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound('bell.mp3')

def ring_bell():
    """Play the bell sound"""
    try:
        playing = sound.play()
        while playing.get_busy():
            time_module.sleep(0.1)
        #print(f"Bell rung at {datetime.now().strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"Error playing bell sound: {str(e)}")

# Define dates to skip (e.g. holidays)
# maybe this should be an online file that we fetch from Google Sheets every day at 6:00 am
# we could also have a sheet that has custom bell schedules for special days
dates_to_skip = [
    '2025-02-21',  # Labor Day
]

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
        today_str = datetime.now().strftime('%Y-%m-%d')
        if today_str in dates_to_skip:
            time_module.sleep(60)
        else:
            schedule.run_pending()
        time_module.sleep(1)    
except KeyboardInterrupt:
    print("\nShutting down bell scheduler...")
