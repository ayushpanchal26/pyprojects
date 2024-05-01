from csv import DictWriter
with open('final.csv','w',newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['firstname','lastname','age'])
    # writerow,writerows
    csv_writer.writerow({
        'firstname':'ayush',
        'lastname': 'panchal',
        'age':19 
    })
    csv_writer.writerow({
          'firstname':'harshal',
        'lastname': 'panchal',
        'age':19 
    })

    csv_writer.writerows([
        {'firstname':'ayushh','lastname':'panchal','age':500},
        {'firstname':'slack','lastname':'panchal','age':567},
        {'firstname':'harry','lastname':'panchal','age':523}
    ])
