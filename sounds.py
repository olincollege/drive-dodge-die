"""Contains car racing sounds"""

import pygame

pygame.mixer.init()

BACKGROUND_MUSIC = "media/car_sounds.wav"
CRASH_SOUND = pygame.mixer.Sound("media/crash_sound.wav")
CRASH_SOUND.set_volume(0.5)


def play():
    """Plays background music"""
    pygame.mixer.music.load(BACKGROUND_MUSIC)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)


def pause_sound():
    """Pauses music"""
    pygame.mixer.music.pause()


def unpause_sound():
    """Resumes music"""
    pygame.mixer.music.unpause()


def stop_sound():
    """Stops music"""
    pygame.mixer.music.stop()


def collision_sound():
    """Plays collision sound"""
    pygame.mixer.music.stop()
    CRASH_SOUND.play()
