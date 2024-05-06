import csv

def create_csv_from_text(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove leading/trailing whitespaces and split by whitespace
    data = [line.strip().split() for line in lines]

    # Define the header and column names
    header = ['file_name', 'segment_name', 'start', 'end']

    # Prepend the header to the data
    data.insert(0, header)

    # Write the data to a CSV file
    with open('hmong.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

# Usage example
create_csv_from_text('hmong_mat_01.txt')