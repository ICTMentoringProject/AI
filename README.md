# AI

## 모듈 설명
모듈 이름|기능|
---|---|
audiorecorder.py| 목소리 녹음 모듈|

### [audiorecorder.py](https://github.com/EduTechProjects/AI/blob/junghyewon/audiorecording/audiorecorder.py)
: 노트북 마이크 오픈 후 사용자의 목소리를 녹음하여 .wav파일로 반환해줍니다. 내부 함수는 다음과 같습니다.

*audio_Recording(RECORD_SECONDS = 120)
  - 디폴트 마이크는 1번째 마이크입니다.(보통 노트북에서 제일 기본으로 사용하는 노트북 내장 마이크)
  - RATE는 sr을 의미하는데 이는 노트북마다 다릅니다. 안에 device()라는 함수로 1번째 마이크의 RATE를 자동으로 반환하게 구현했습니다.
  - 저장되는 파일명은 "audiofile.wav"입니다. 추후 librosa로 오디오를 변경하거나 wav2vec에 받아올 때 이 이름으로 받아오시면 됩니다.
```
#사용예시
pip install pyaudio
import audiorecorder as ar
ar.audio_Recording()
```
