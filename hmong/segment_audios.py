from pydub import AudioSegment
import os
import pandas as pd
import librosa
import soundfile as sf


data_path = 'hmong.csv'
df = pd.read_csv(data_path)

segment_names =df['segment_name'].tolist()
start_times = df['start'].tolist()
end_times = df['end'].tolist()

input_file= '1.mp3'
speech, rate = librosa.load(input_file)
print(rate)
for x in range(len(segment_names)):
  file_name = segment_names[x]
  start_second = int(start_times[x] * rate)
  end_second = int(end_times[x] * rate)
  current_segment = speech[start_second:end_second]
  print(f"Segment {x+1} duration: {len(current_segment) / rate} seconds")
  segment_path = 'audio_segments/' + str(file_name) + '.wav'
  sf.write(segment_path, current_segment, rate)

path = 'audio_segments/' + str(df['file_name'][0]) + '.wav'
sf.write(path, speech, rate)
# # ['ENSHOW EE JANNA JOHAT SO HIS SO', 'ENHE THOUGHT YOUR CONTEMBEY YES YOU DAVIDO', 'ENTHIR DA VILLA ABLAHA SINZU ZITHOU ABLAHR MOTSORVANZUDALE', 'ENJESU TOYO CONMULINÓ ABLAHAJO IS SATTI HIS SAJOJA COOCY JACOW', 'ESYO UNA AQUEABAN INMEDIATO CULTICIÓN DE JASE EN LAZI GRABAN EL AYO TAMBAN EL PELLOUDO EN LA PELLOUDO DE LA VIDA', 'PTAMBINA DA JO NA SOM FIE NASHÃO', 'RUОН В ЕСУ ЖЕ СОВТЁ ЙОКО МОЛЕНО', 'ENYEAH HOW JACK CAN YOU SEE AT THE INDIE SEAT THING YOUR SAY LOMBAN', 'ESSE LOMBAN BENJO AMBIUTI AMBIO HUYÓ EL LI AQUENCIE AQUELLO A SANCÍAS A OJO A SADUCÍO DE OJO ADADULO', 'ENHE SEE ACQUILO ELIOT SEE ELIOYA ELEAZAZI', 'ITSTAGLIO MATTRAZÍ MA TAYLOR YA COLTÍ JACOGLIO SETTI MA LE OLI SOLIA GEOLOSE DOPONNIER', 'ENWHAT DO YOU WANT TO PLAY TO THE WHOLE WHAT THROW MY IN SENT TOLD MANY YOUR YOUTH MEETAL', 'ENTHEY TOO MAKE UNDER A BABY WAR YOUR SAW THROUGH FARMING YOUR TO WORK', 'ENYOURE HIGH NIGHT FOR LOADING THE LUZY AND NOW MORE TILL THEY LOW WHAT TO TWO THOUGHT TO GAVE A TILL LOWER HATY AT THE DOOR']