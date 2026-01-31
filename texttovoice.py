from gtts import gTTS
import os

text = "Hello, Hi kaivalya welcome and how are you?"
tts = gTTS(text=text, lang='en')
tts.save("welcome.mp3")
os.system("start welcome.mp3")  # Plays the file on Windows