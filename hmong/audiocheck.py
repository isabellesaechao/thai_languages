# NOTE: pip shows imcompatible errors due to preinstalled libraries but you do not need to care
!pip install -q espnet==0.10.0
!pip install -q espnet_model_zoo

#@title Choose Multilingual ASR model { run: "auto" }


import time
import torch
import string
from espnet_model_zoo.downloader import ModelDownloader
from espnet2.bin.asr_inference import Speech2Text
from google.colab import files
from IPython.display import display, Audio
import soundfile
import librosa.display
import matplotlib.pyplot as plt

lang = 'multilingual'
fs = 16000 #@param {type:"integer"}
tag = 'ftshijt/open_li52_asr_train_asr_raw_bpe7000_valid.acc.ave_10best' #@param ["	ftshijt/open_li52_asr_train_asr_raw_bpe7000_valid.acc.ave_10best"] {type:"string"}

d = ModelDownloader()
# It may takes a while to download and build models
speech2text = Speech2Text(
    **d.download_and_unpack(tag),
    device="cuda",
    minlenratio=0.0,
    maxlenratio=0.0,
    ctc_weight=0.3,
    beam_size=10,
    batch_size=0,
    nbest=1
)

def text_normalizer(text):
    text = text.upper()
    return text.translate(str.maketrans('', '', string.punctuation))



uploaded = files.upload()

for file_name in uploaded.keys():
  speech, rate = soundfile.read(file_name)
  assert rate == fs, "mismatch in sampling rate"
  nbests = speech2text(speech)
  text, *_ = nbests[0]

  print(f"Input Speech: {file_name}")
  display(Audio(speech, rate=rate))
  librosa.display.waveplot(speech, sr=rate)
  plt.show()
  print(f"ASR hypothesis: {text_normalizer(text)}")
  print("*" * 50)

# ['ENSHOW EE JANNA JOHAT SO HIS SO', 'ENHE THOUGHT YOUR CONTEMBEY YES YOU DAVIDO', 'ENTHIR DA VILLA ABLAHA SINZU ZITHOU ABLAHR MOTSORVANZUDALE', 'ENJESU TOYO CONMULINÓ ABLAHAJO IS SATTI HIS SAJOJA COOCY JACOW', 'ESYO UNA AQUEABAN INMEDIATO CULTICIÓN DE JASE EN LAZI GRABAN EL AYO TAMBAN EL PELLOUDO EN LA PELLOUDO DE LA VIDA', 'PTAMBINA DA JO NA SOM FIE NASHÃO', 'RUОН В ЕСУ ЖЕ СОВТЁ ЙОКО МОЛЕНО', 'ENYEAH HOW JACK CAN YOU SEE AT THE INDIE SEAT THING YOUR SAY LOMBAN', 'ESSE LOMBAN BENJO AMBIUTI AMBIO HUYÓ EL LI AQUENCIE AQUELLO A SANCÍAS A OJO A SADUCÍO DE OJO ADADULO', 'ENHE SEE ACQUILO ELIOT SEE ELIOYA ELEAZAZI', 'ITSTAGLIO MATTRAZÍ MA TAYLOR YA COLTÍ JACOGLIO SETTI MA LE OLI SOLIA GEOLOSE DOPONNIER', 'ENWHAT DO YOU WANT TO PLAY TO THE WHOLE WHAT THROW MY IN SENT TOLD MANY YOUR YOUTH MEETAL', 'ENTHEY TOO MAKE UNDER A BABY WAR YOUR SAW THROUGH FARMING YOUR TO WORK', 'ENYOURE HIGH NIGHT FOR LOADING THE LUZY AND NOW MORE TILL THEY LOW WHAT TO TWO THOUGHT TO GAVE A TILL LOWER HATY AT THE DOOR']