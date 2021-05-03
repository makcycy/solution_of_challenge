from credential import setEnv
from speech_to_text import SpeechToText
from audio_denoiser import model_denoise
from split_audio import SplitWavAudio
import os

def main():
    setEnv('../credentials/speech-analysis-312306-6aedd9ae798f.json')
    # model_denoise(
    #     output_path='dataset/output'
    # )
    SplitWavAudio('dataset/output/enhanced', 'd2.wav').multiple_split(10)
    stt = SpeechToText()
    res = []
    root_path = 'dataset/output/enhanced'
    for file in os.listdir(root_path):
        if file =='d2.wav':
            continue
        result = stt.transcribe_file(speech_file=os.path.join(root_path, file))
        res.append(result)
        print(result)
    # for key in result.keys():
    #     print(f"{key}: {result[key]}")

if __name__ == '__main__':
    main()