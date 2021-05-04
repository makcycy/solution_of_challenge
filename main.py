from credential import setEnv
from gcp_services.speech_to_text import SpeechToText
from audio_preprocessing.audio_denoiser import model_denoise
from audio_preprocessing.split_audio import SplitWavAudio
import os

def stt_by_file(stt_model, root_path, files):
    if isinstance(files, list):
        fileList = []
        transcriptsList = []
        for subFile in files:
            transcript = stt_model.transcribe_from_file(speech_file=os.path.join(root_path, subFile))
            fileList.append(subFile)
            transcriptsList.append(transcript)
        return fileList, transcriptsList

    elif isinstance(files, str):
        transcript = stt_model.transcribe_from_file(speech_file=os.path.join(root_path, files))
        return files, transcript
    else:
        raise TypeError('Invalid datatype passed to files, only list & str are available.\n'
                        f'{type(files)} is passed')

def clean_large_audio(data_path, sec_per_split):
    audioFiles = [file for file in os.listdir(data_path) if not os.path.isdir(os.path.join(data_path, file))]
    for file in audioFiles:
        SplitWavAudio(root_path=data_path, filename=file).multiple_split(sec_per_split=50)

def main():
    cred_path = '../credentials/'
    setEnv(os.path.join(cred_path, os.listdir(cred_path)[0]))

    data_path = 'dataset/'
    clean_large_audio(data_path = data_path, sec_per_split = 50)
    model_denoise(
        output_path='dataset/output'
    )
    stt = SpeechToText()
    result = {'filename': [],
              'stt_result':[]}
    root_path = 'dataset/output/enhanced'
    for file in os.listdir(root_path):
        file, transcript = stt_by_file(stt, root_path, file)
        result['filename'].append(file)
        result['stt_result'].append(transcript)
    print(result)


if __name__ == '__main__':
    main()