"""
from pydub import AudioSegment
import simpleaudio as sa


def reproduzir_mp3(caminho_arquivo):
    sound = AudioSegment.from_mp3(caminho_arquivo)
    wave_obj = sa.WaveObject.from_wave_file(io.BytesIO(sound.raw_data))

    play_obj = wave_obj.play()
    play_obj.wait_done()
"""

import pygame

def reproduzir_mp3(caminho_arquivo):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(caminho_arquivo)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        pygame.quit()

reproduzir_mp3('src/audio_aula.mp3')
