from credential import setEnv
from speech_to_text import SpeechToText
from audio_denoiser import model_denoise

def main():
    setEnv('../credentials/speech-analysis-312306-6aedd9ae798f.json')
    model_denoise(
        output_path='dataset/output'
    )
    stt = SpeechToText()
    result = stt.transcribe_file(speech_file='dataset/output/enhanced/d2.wav')
    for key in result.keys():
        print(f"{key}: {result[key]}")

if __name__ == '__main__':
    main()