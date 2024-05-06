from pydub import AudioSegment
import os
import pandas as pd
import librosa
import soundfile as sf


data_path = 'thai.csv'
df = pd.read_csv(data_path)

segment_names =df['segment_name'].tolist()
start_times = df['start'].tolist()
end_times = df['end'].tolist()

input_file= '1.mp3'
speech, rate = librosa.load(input_file)
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
# ['EOPROKU MAĜA ABRAHAM ABRAHAM LI BOTIS AMIBU ĈI LA KOJA KOMIBU ĈIU DE HALEPINO KANU', 'SURSILVJUDA BIBUC CHI PER RAPS CERRAR CIN QUER CH’APMANTAMA PER RAI BUC CHI', 'ENHER SWORMI BUCHIG RAM RAHMIBUCH A MIDADA AMINADAMIBUCHI LA CHORNA', 'ENACHIBU ARE A SINKLE JACK MAN OR THAT BUT ARE NIBUCCIO BEAR SINKLEGER MAN ROOM', 'PTO BERLIBROUTE TIERCI TER SI DEBUTCHI DAL ВЕ COPEM KASA DA WITH LIBÚ TUSA ALUM', 'ITQUE CHATMANCINTE CON PENPAVRE GLI ACON URIGLIAR SALO MORNE BUCCI REHO', 'ESASA ME BUCHI DE HOCHAFA DE HOCHA FAR MI BUCHI JORAM Y URRAMO', 'ENWHAT SHE OUR CHEERE', 'CNHHAMI BU CHI HU TARM JO TAMH LI BU CHI A HHAN A HWIBU CHI HE SEH KIA', 'ENHE SEE KIJAR ME BUT TUMA LAPSEI MANA', 'PTQUE ME VOU TI ABON AMO AMOR LIBUTIO QUE O SEIAR', 'PTEU ACILIAR ME VOU TIME DESCROLIA LAPINÃO CONCÃO QUE POUR CRAR O TEMPO QUABE', 'RUЧЕРЕЛЫЙ ТЫКУМ ВАБИЛОН ЛАНЧАК ТУПЛАТ ПО ТИКРУБА ВЕЛОНИЯ У ДЛЯ КОМИНА КАМИ', 'PTCHEU CHE ANQUE ELE CHE ADI ELA ME BOU CHIM CELU BABIO', 'ENPAPER ME BOUCHING A BIT', 'PTELE ASSAR ME BUCCHIU MATAR MATAME BUCCHI A KO JAKÓ LIBUCIO SER POPREM SAME COM A PREDISO', 'ENMISSI PSYCHOQUE LENART THAT A WHITTELOMA JORN DINCROPOQUE PENCHALLERITIC ROOM', 'PTDUPROPRIÉ MANDA COM PREGUIS SONHAM DOM JOUR SER VESSE O CHORRO MANQUELEO QUANTIJADA EU QUINTE CAMPO CAPARE', 'ESTRAN LE RUE DIE PREVILLE AMBORISER DE JOSE CUMAN CONTRAPEN CON CHOPTAM MAYTON GRANJA PRINK QUAMPA EMPARE COMPLÉTÓN JA COMPAY UN PLAY', 'ENBUT THE GIPPLE ME YOU TO ME THOUGHT SO ONE OMEN', 'RUВ ЭМПРОПУ ПЕЛЬЧАЛ МАППРА КУТКЕ ЛЮСИ В МИКЛАМ ФАНУА И УСЕ УБА ВЫП', 'ENTHEY ARE UNCENT PUTTY SO THREE BACK CONFORMED TO THE BABY PROVIDED YOUNG BOWLS']