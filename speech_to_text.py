import io
from credential import setEnv
from google.cloud import speech_v1p1beta1 as speech

class SpeechToText:
    def __init__(self):
        pass

    def _get_file_type(self):
        return self.speech_file.split('.')[-1]

    def _get_recognition_config_params(self):
        fileType = self._get_file_type()
        if fileType == 'flac':
            self.recogConfig = dict(
                encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
                audio_channel_count=2,
                language_code='yue-Hant-HK'
            )
        elif fileType == 'mp3':
            self.recogConfig = dict(
                encoding=speech.RecognitionConfig.AudioEncoding.MP3,
                language_code='yue-Hant-HK'
            )
        return self.recogConfig

    def transcribe_file(self, speech_file):
        self.speech_file = speech_file
        client = speech.SpeechClient()
        with io.open(speech_file, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(self._get_recognition_config_params())
        operation = client.long_running_recognize(config=config, audio=audio)
        print("Waiting for operation to complete...")
        response = operation.result(timeout=90)
        result = {
            'Transcript': response.results[0].alternatives[0].transcript,
            'Confidence': response.results[0].alternatives[0].confidence
        }
        return result
