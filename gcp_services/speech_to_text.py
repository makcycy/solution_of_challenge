import io
from google.cloud import speech_v1p1beta1 as speech

class SpeechToText:
    def __init__(self):
        pass

    def _get_file_type(self):
        """detect the file type"""
        return self.speech_file.split('.')[-1]

    def _get_recognition_config_params(self, frameRate=None):
        """
        :param frameRate: int, optional
                sample rate of the speech file
        :return: dictionary
                Attributes for speech.RecongnitionConfig
        """
        fileType = self._get_file_type()
        if fileType == 'flac':
            self.recogConfig = dict(
                encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
                audio_channel_count=2
            )
        elif fileType == 'mp3':
            self.recogConfig = dict(
                encoding=speech.RecognitionConfig.AudioEncoding.MP3
            )
        elif fileType == 'wav':
            self.recogConfig = dict(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                use_enhanced=True
            )
        if frameRate is not None:
            self.recogConfig['sample_rate_hertz'] = frameRate
        self.recogConfig['use_enhanced'] = True
        self.recogConfig['max_alternatives'] = 1
        self.recogConfig['enable_automatic_punctuation'] = True
        self.recogConfig['language_code'] = 'yue-Hant-HK'

        return self.recogConfig

    def transcribe_from_file(self, speech_file, frameRate=None):
        """
        :param speech_file: str
                    relative/ full path of the speech file
        :param frameRate: int, optional
                    sample rate of the speech file
        :return: dictionary
                    transcript and confidence level
        """
        self.speech_file = speech_file
        client = speech.SpeechClient()
        with io.open(speech_file, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(self._get_recognition_config_params(frameRate))
        operation = client.long_running_recognize(config=config, audio=audio)
        # print("Waiting for operation to complete...")
        response = operation.result()
        # print(f'result length: {len(response.results)}')

        if len(response.results) >= 1:
            result = {
                'Transcript': response.results[0].alternatives[0].transcript,
                'Confidence': response.results[0].alternatives[0].confidence
            }
        else:
            result = {'Transcript': None, 'Confidence': None}
        return result

    def transcribe_gcs(self, gcs_uri, frameRate=None):
        """Asynchronously transcribes the audio file specified by the gcs_uri."""
        client = speech.SpeechClient()

        audio = speech.types.RecognitionAudio(uri=gcs_uri)
        config = speech.types.RecognitionConfig(self._get_recognition_config_params(frameRate))

        response = client.long_running_recognize(config, audio)

        print('Waiting for operation to complete...')
        response = response.result(timeout=360)
        result = {
            'Transcript': response.results[0].alternatives[0].transcript,
            'Confidence': response.results[0].alternatives[0].confidence
        }
        return result


