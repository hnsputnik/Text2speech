from gtts import gTTS
import traceback
import os

result = set()
with open('word.txt') as names:
    for name in names:
        result.add(name)
        try:
            language = 'vi'
            output = gTTS(text=name, lang=language, slow=False)
            print(name)
            output.save("./temp/{}.wav".format(name.rstrip()))
        except Exception as e:
            traceback.print_exc()
with open('temp.txt','w') as temp:
    temp.writelines(result)
            


