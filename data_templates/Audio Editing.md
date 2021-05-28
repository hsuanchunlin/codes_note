# Audio Editing
## Pydub

Before use pydub, install ffmpeg by
```
brew install ffmpeg
```
Install pydub

```
pip install pydub
```

### Convert m4a to wav
```python
from pydub import AudioSegment
sound = AudioSegment.from_file('./data/output/sample3.m4a')
sound.export("./data/output/output.wav", format="wav")
```
### Split wav file to multiple wav files

```python
from pydub import AudioSegment
import math

class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '/' + filename

        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_sec, to_sec, split_filename):
        t1 = from_sec * 1000
        t2 = to_sec * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '/' + split_filename, format="wav")

    def multiple_split(self, sec_per_split):
        total_secs = math.ceil(self.get_duration())
        for i in range(0, total_secs, sec_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+sec_per_split, split_fn)
            print(str(i) + ' Done')
```

### Combind multiple wav files into one

```python
from pydub import AudioSegment
import os
from glob import glob

playlist_songs = glob('*.wav')
combined = AudioSegment.empty()

for song in playlist_songs:
    print(song)
    inputs = AudioSegment.from_file(song)
    combined += inputs

combined.export("output.wav", format="wav")
```