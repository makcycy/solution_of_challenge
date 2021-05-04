from google.cloud import storage
from audio_preprocessing.audio_denoiser import model_denoise
from pydub import AudioSegment

class ToCloud:
    def __init__(self, dataset_path, denoise = True):
        self.dataset_path = dataset_path
        self.denoise = denoise

    def call(self, output_path = None, model_path = None, config_path = None):
        if self.denoise:
            self._denoise_with_model(
                output_path=output_path,
                model_path=model_path,
                config_path=config_path
            )

    def frame_rate_channel(audio_file_name):
        with wave.open(audio_file_name, "rb") as wave_file:
            frame_rate = wave_file.getframerate()
            channels = wave_file.getnchannels()
            return frame_rate, channels

    def upload_blob(bucket_name, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

    @staticmethod
    def _stereo_to_mono(audio_file_name):
        sound = AudioSegment.from_wav(audio_file_name)
        sound = sound.set_channels(1)
        sound.export(audio_file_name, format="wav")

    @staticmethod
    def mp3_to_wav(audio_file_name):
        if audio_file_name.split('.')[1] == 'mp3':
            sound = AudioSegment.from_mp3(audio_file_name)
            audio_file_name = audio_file_name.split('.')[0] + '.wav'
            sound.export(audio_file_name, format="wav")

    @staticmethod
    def _denoise_with_model(output_path = None, model_path = None, config_path = None):
        model_denoise(
            output_path = output_path,
            model_path = model_path,
            config_path = config_path
        )

