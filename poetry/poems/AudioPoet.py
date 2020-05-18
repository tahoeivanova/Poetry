from gtts.tts import gTTS
from .models import Poem
class AudioPoet:
    def __init__(self, text):
        # получаем текст на вход
        self.text = text



    def audio(self):
        # путь к файлу
        path_name = 'poems/static/poems/'
        # имя файла

        mp3_name = '1.mp3'

        # Эта строка отправляет текст для озвучивания гуглу
        tts = gTTS(text=self.text, lang='ru')

        # Получаем от гугла озвученный текст в виде mp3
        tts.save(path_name+mp3_name)

