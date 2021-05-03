from pydub import AudioSegment
import math
import os


class SplitWavAudio():
    def __init__(self, root_path, filename):
        self.root_path = root_path
        self.filename = filename
        self.filepath = os.path.join(self.root_path, self.filename)
        self.audio = AudioSegment.from_wav(self.filepath)

    def _get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_sec, to_sec, split_filename):
        t1 = from_sec * 1000
        t2 = to_sec * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.root_path + '\\' + split_filename, format="wav")

    def multiple_split(self, sec_per_split):
        total_seconds = math.ceil(self._get_duration())
        for i in range(0, total_seconds, sec_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i + sec_per_split, split_fn)
            # print(str(i) + ' Done')
            # if i == total_seconds - sec_per_split:
                # print('All splited successfully')