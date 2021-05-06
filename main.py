from credential import setEnv
from gcp_services.speech_to_text import SpeechToText
from audio_preprocessing.audio_denoiser import model_denoise
from audio_preprocessing.split_audio import SplitWavAudio
import os
from gcp_services.sentiment_analysis import sample_analyze_sentiment
from gcp_services.entities_analysis import sample_analyze_entities
from gcp_services.text_classification_analysis import sample_classify_text


def clean_large_audio(data_path, sec_per_split):
    audioFiles = [file for file in os.listdir(data_path) if not os.path.isdir(os.path.join(data_path, file))]
    for file in audioFiles:
        SplitWavAudio(root_path=data_path, filename=file).multiple_split(sec_per_split=sec_per_split)

def main():
    cred_path = '../credentials/'
    setEnv(os.path.join(cred_path, os.listdir(cred_path)[0]))

    data_path = 'dataset/'
    output_path = os.path.join(data_path, 'output')
    clean_large_audio(data_path = data_path, sec_per_split = 50)
    model_denoise(
        output_path=output_path
    )
    stt = SpeechToText()
    results = {}
    for file in os.listdir(output_path):
        transcript = stt.transcribe_from_file(os.path.join(output_path, file))
        results[file] = transcript
    print(results)

    # print(sample_analyze_sentiment(results['stt_result'][0]['Transcript']))
    # print(sample_classify_text(results['stt_result'][0]['Transcript']))
    # print(sample_analyze_entities(results['stt_result'][0]['Transcript']))



if __name__ == '__main__':
    main()