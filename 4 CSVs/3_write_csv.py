from csv import writer
with open('file2.csv','w',newline='') as f:
    csv_writer  = writer(f)
    # # methods  - writerow , writerows
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['ayush','USA'])
    # csv_writer.writerow(['HARSHAL','USA'] )

    csv_writer.writerows([['name','country'],['achu','usa'],['ayush','USA'],['HARSHAL','USA']])
