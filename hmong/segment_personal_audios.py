from pydub import AudioSegment
import os
import pandas as pd
import librosa
import soundfile as sf

input_file= '1.mp3'
speech, rate = librosa.load(input_file)
print(rate)
segment_duration = 30  # Duration of each segment in seconds
total_duration = len(speech)
segment_duration_ms = segment_duration * rate

# Initialize start and end time for the first segment
start_time = 0
end_time = segment_duration_ms

counter = 0
# Segment the audio until the end of the audio is reached
while end_time <= total_duration:
    segment = speech[start_time:end_time]

    # Move to the next segment
    start_time += segment_duration_ms
    end_time += segment_duration_ms

    segment_path = 'audio_segments_larger/' + str(counter) + '.wav'
    sf.write(segment_path, segment, rate)
    counter += 1

# path = 'audio_segments/' + str(df['file_name'][0]) + '.wav'
# sf.write(path, speech, rate)

# ['ENYOU COUGH ALL JUDAHAR BENUMBEN THOMAS OWNER THE LITTLE JOUDAL A LITTLE HOW ZELONG HALL', 'FRCALLOUIS JEAN LUI ALLER LA LAMUE ALI AMINA DE AMINA DEUX ALLI NA SHOW', 'ENNACHO ALI SHALAMY LAHA UNED THE LITTLE SALAMO ABY BOZA NOTÁ UNDER THE BOSAL AUDDER', 'ENYOU SHOULD ONLY SOME PART OF BEING THE GOBILE AT THE SOLUBLE SULABLE ABOUT', 'FROULIA FOUSA IL MET SOLA MOT À LIT LE HOBAND LES HOBBES ALLÍ ARBI', 'ENA BIOALLY AS HOW AS HOW A LITTLE HOSH HAPPER GIHOSE A POWER A LI', 'ENA CALLED EARLY HIS HEART HIS HEART EARLY MONOSIE MONOSIEURLY', 'PTAMOU A LIVO SHI', 'ENCHEWZAR YECOMBE A HAMMY NO MAN WHO ARE IS OILAND TO HER THE BABULANY OR BE', 'ENTHE CONVILLE ARE YOUR MOCONY AND CALL YOU TO ME DO BULLOW ME CORPING', 'ENHOW ARE YOUR BETTER THE TOWN CLEAR TO YOUR HIM WHERE HE COMMUTE ONLY', 'FRCHARTILA CHATILA ALLEZ ZENUBA DE LA SE LUBA BELAND ALLER À BIOUX', 'FRPIRE AUX ALLÉS ÉLICONS ELLE COMMENT ALLÉE À SOUR EN SOUR À LES ZADO', 'PTZADÓ ALLÉ ACHOUND ACHOU ALER ELE O ELE O ALI ELA LAZAR', 'ENIT WAS ALL ALI BAKAR', 'ENWOULD BE THE CARLOS YOUNG COULD MET TURCH MY PUNSIE ON THE CANYON COULDNT CITY MET THE CHANGED', 'FRQUAND IL UM AMBAMNA MON SHOW YOU SOMMIER BEDARME ZARTELLER DE KO UHA JOHAR JOS', 'PTA QUE O GÓGÁGOU LEOR HUBUA E OBENDO A PIRAMIO SÃO VALEON CHOGO QUATRADUCIA AIULACE', 'PTO CHÃO É SOM MINHA PADANNA É MER AO ALETE LICITÉ A LINCOLÍO USУЛЯНО МИЛАНА UM ELAGRAMA', 'ENA YOUR CHAIR OF THE RAW BURL OF HUECO FOR DOMIRD THE OUT', 'ENPAPA MILLION ARE YOU GOED TO THE DOOR SO HARD OR WHO ARE TRAILED AT YOUR LANE', 'ESYO EL LET LECHE DE AL DICUNEO Y MANULA LE NOTIA']
