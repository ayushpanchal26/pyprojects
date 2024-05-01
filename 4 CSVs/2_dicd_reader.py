from csv import DictReader
with open('book1 - Copy.csv' ,'r') as f:
    csv_reader = DictReader(f,delimiter='|') # if the file is not seperated by ',' than the sign should be defined in delimeter

    for row in csv_reader:
        print(row['email'])