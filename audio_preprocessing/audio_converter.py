import os
from os import path
from pydub import AudioSegment

def converter():
    src = '../dataset/raw'
    for file in os.listdir(src):
        if file[-4:] == '.ogg':
            sound = AudioSegment.from_ogg(os.path.join(src,file))
            sound.export(os.path.join(src,f"{file[:-4]}.wav"), format='wav')
            os.remove(os.path.join(src, file))
        else:
            print(f"{os.path.join(src,file)} failed! Only ogg file is available!")



if __name__ == '__main__':
    # for converting raw file from ogg to wav only
    converter()