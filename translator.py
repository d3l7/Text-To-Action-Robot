from googletrans import Translator
import pyttsx3 as tts

#Loading TTS engine
engine = tts.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 140)

#Translating text
translator = Translator()

translated_text = translator.translate('read the text below. then match the phrases to the correct translation', src='en', dest='es')
print(translated_text.text)

#TTS working
engine.say(translated_text.text)
engine.runAndWait()
engine.stop()

