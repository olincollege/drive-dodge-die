import pygame

def play():
    """Plays car racing sounds"""
    pygame.mixer.init()
    pygame.mixer.music.load('media/car_sounds.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def pause_sound():
    """Pauses sound"""
    pygame.mixer.music.pause()

def unpause_sound():
    """Resumes sound"""
    pygame.mixer.music.unpause()

def stop_sound():
    """Stops sound"""
    pygame.mixer.music.stop()
