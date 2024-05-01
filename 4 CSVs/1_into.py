from csv import reader

with open('book_1.csv','r') as f:
    csv_reader = reader(f)
    print(type(csv_reader))
    for row in csv_reader:
        print(row)
