import pygame
from datetime import datetime
pygame.init()

def getCurrentHour():
    rawTime = datetime.now().strftime("%H:%M:%S")
    currentHour = rawTime.split(':')[0]
    return currentHour

def playTrackForHour(hour):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(f'./tracks/acnl-default-{hour}.mp3')
    pygame.mixer.music.play()

def hourSwitchOccursShortly():
    rawTime = datetime.now().strftime("%H:%M:%S")
    min = int(rawTime.split(':')[1])
    sec = int(rawTime.split(':')[2])

    print(f"{min}:{sec}")
    if min >= 59 and sec >= 50:
        print("true!")
        return True
    return False

# Startup    
currentlyPlayingHour = getCurrentHour() 
playTrackForHour(currentlyPlayingHour)
fadeOutSeconds = 10

# Main loop
while True:
    pygame.time.Clock().tick(1)
    currentHour = getCurrentHour()
    
    if (hourSwitchOccursShortly()):
        pygame.mixer.music.fadeout(fadeOutSeconds * 900)
    
    # Skips loop, unless nothing is playing or a the next hour is detected
    if (currentlyPlayingHour == currentHour and pygame.mixer.music.get_busy()):
        continue
    
    playTrackForHour(currentHour)
    currentlyPlayingHour = currentHour

    
    