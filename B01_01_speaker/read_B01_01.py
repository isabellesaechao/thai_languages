import os
def format_time(seconds):
    minutes = int(seconds // 60)
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:06.3f}"

def convert_to_minutes_seconds(time):
    minutes = int(float(time)) // 60
    seconds = float(time) % 60
    return f"{minutes:02d}:{seconds:05.2f}"

def read_rttm(rttm_file):
  output_file = 'audio_info_file.txt'

  with open(rttm_file, "r") as rttm_input, open(output_file, "a") as output:
      output.write(rttm_file + '\n')
      for line in rttm_input:
          parts = line.strip().split()
          if len(parts) >= 4 and parts[0] == "SPEAKER":
              start_time = convert_to_minutes_seconds(parts[3])
              end_time = convert_to_minutes_seconds(float(parts[3]) + float(parts[4]))
              parts[3] = start_time
              parts[4] = end_time
              updated_line = " ".join(parts)
              output.write(updated_line + "\n")
          else:
              output.write(line)
      output.write('\n')


read_rttm('relabel_akha_B01_01.rttm')
read_rttm('relabel_hmong_B01_01.rttm')
read_rttm('relabel_thai_B01_01.rttm')