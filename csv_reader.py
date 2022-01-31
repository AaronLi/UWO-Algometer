import csv

class NormativeData():
    def __init__(self, csv_file="normative_data_1.csv"):

        with open(csv_file, 'r') as norm_data:
            csv_reader = csv.reader(norm_data)
            next(csv_reader)
            for line in csv_reader:
                print(line)


