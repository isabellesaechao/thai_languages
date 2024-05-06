from pyAudioAnalysis import audioSegmentation
from sklearn.cluster import KMeans

# Set the path to your audio file
audio_file = "hmong/audio_segments/B01___01_Matthieu____MWWHDVN2DA.wav"

# Set the parameters for speaker diarization
window_size = 0.05  # Window size in seconds
hop_size = 0.025  # Hop size in seconds
num_speakers = 2  # Number of speakers to be detected

# Perform speaker diarization
segments, labels = audioSegmentation.speaker_diarization(audio_file, window_size, hop_size, num_speakers)

# Calculate the duration of each segment
segment_durations = [end_time - start_time for start_time, end_time in segments]

# Perform clustering to assign labels based on segment durations
kmeans = KMeans(n_clusters=num_speakers)
kmeans.fit([[duration] for duration in segment_durations])

# Print the diarization results
for segment, label in zip(segments, kmeans.labels_):
    start_time = segment[0]
    end_time = segment[1]
    speaker_id = label
    print(f"Speaker {speaker_id}: {start_time} - {end_time}")



