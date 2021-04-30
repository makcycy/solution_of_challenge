from credential import setEnv
from speech_to_text import SpeechToText

def main():
    setEnv()
    stt = SpeechToText()
    result = stt.transcribe_file(speech_file='dataset/flac_example.flac')
    for key in result.keys():
        print(f"{key}: {result[key]}")

if __name__ == '__main__':
    main()