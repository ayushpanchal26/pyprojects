from csv import DictWriter,DictReader
with open('file4.csv','r') as rf:

    with open('last.csv','w') as f:
        csv_reader = DictReader(rf)
        csv_writer  = DictWriter(f,fieldnames=['firstname','lastname','age'])
        for row in csv_reader:
           fname ,lname , age = row['firstname',row['lastname'],row['age']]
           csv_writer.writerow({
               'firstname':fname.upper(),
               'last_name':fname.upper(),
               'age':age
           })