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
## wav2vec finetuning model test
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ivNAAOqhs-YKhXLosWXeBKxzC9QS67Do?authuser=2#scrollTo=GeDLkgVyk_an&line=1&uniqifier=1) (별도 세팅 없이 바로 실행 가능)

"wav2vec-base no fine-tune" 모델을 AI openAPI 내 한국인의 영어 발화 데이터셋으로 파인튜닝 후 2가지 음성 파일로 성능 체크  <br>  
학습된 모델과 토크나이저를 huggingface에 탑재 후 이를 불러와 간단하게 음성 인식 결과를 볼 수 있습니다. 직접 녹음한 wav 파일을 불러와 전처리 후 모델에 넣기 용이합니다.  
<br>
상세 코드는 추후 탑재 예정입니다.


[데이터 출처](https://aiopen.etri.re.kr/voiceModel)  
:5000개(50명*100발화)  