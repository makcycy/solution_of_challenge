from credential import setEnv
from speech_to_text import SpeechToText
from audio_denoiser import model_denoise
from split_audio import SplitWavAudio
import os

def stt_by_file(stt_model, root_path, files):
    if isinstance(files, list):
        fileList = []
        transcriptsList = []
        for subFile in files:
            transcript = stt_model.transcribe_file(speech_file=os.path.join(root_path, subFile))
            fileList.append(subFile)
            transcriptsList.append(transcript)
        return fileList, transcriptsList

    elif isinstance(files, str):
        transcript = stt_model.transcribe_file(speech_file=os.path.join(root_path, files))
        return files, transcript
    else:
        raise TypeError('Invalid datatype passed to files, only list & str are available.\n'
                        f'{type(files)} is passed')
def main():
    setEnv('../credentials/speech-analysis-312306-6aedd9ae798f.json')
    model_denoise(
        output_path='dataset/output'
    )
    # stt = SpeechToText()
    # result = {'filename': [],
    #           'stt_result':[]}
    # root_path = 'dataset/output/enhanced'
    #
    # for file in os.listdir(root_path):
    #     swa = SplitWavAudio(root_path, file)
    #     if swa._get_duration()>50:
    #         swa.multiple_split(50)
    #         os.remove(os.path.join(root_path, file))
    #         subFileList = [_file for _file in os.listdir(root_path) if _file[:-len(file)] == file]
    #         fileList, transcriptsList = stt_by_file(stt, root_path, subFileList)
    #         result['filename'] += fileList
    #         result['stt_result'] += transcriptsList
    #     else:
    #         file, transcript = stt_by_file(stt, root_path, file)
    #     result['filename'].append(file)
    #     result['stt_result'].append(transcript)
    # print(result)


if __name__ == '__main__':
    main()