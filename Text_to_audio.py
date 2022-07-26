import time
from gtts import gTTS
import os

myText1 = "Can you read this sentence."
language= 'en'
output= gTTS(text=myText1, lang=language, slow=False)
output.save("speak.mp3")
os.system("start speak.mp3")

L = [1, 2, 3, 4, 5, 6, 7, 8]
for i in L:
    time.sleep(-time.time()%1)          # Countdown
    print (i)


myText2 = "If first sentence is successful read this"
language= 'en'
output= gTTS(text=myText2, lang=language, slow=False)
output.save("speak2.mp3")
os.system("start speak2.mp3")
