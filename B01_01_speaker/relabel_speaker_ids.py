
def relabel(rttm_file):
    output_file = "relabel_" + rttm_file  # Path to the output file

    with open(rttm_file, "r") as rttm:
        lines = rttm.readlines()

    # Create a dictionary to map existing speaker IDs to new sequential IDs
    speaker_mapping = {}
    new_speaker_id = 0

    with open(output_file, "w") as out:
        for line in lines:
            parts = line.strip().split(" ")
            speaker_id = parts[7]  # Assuming speaker ID is at index 7

            if speaker_id not in speaker_mapping:
                speaker_mapping[speaker_id] = new_speaker_id
                new_speaker_id += 1

            # Update the speaker ID in the line
            parts[7] = "SPEAKER_0" + str(speaker_mapping[speaker_id])

            # Write the updated line to the output file
            out.write(" ".join(parts) + "\n")




relabel('akha_B01_01.rttm')
relabel('hmong_B01_01.rttm')
relabel('thai_B01_01.rttm')