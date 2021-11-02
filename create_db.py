import csv  

header = ['id', 'title', 'category', 'quantity', 'price']

data1 = [1, 'How to get a good grade in DOS in 40 minutes a day', 'distributed systems',  4, 60]
data2 = [2, 'RPCs for Noobs',                                     'distributed systems',  7, 50]
data3 = [3, 'Xen and the Art of Surviving Undergraduate School',  'undergraduate school', 6, 25]
data4 = [4, 'Cooking for the Impatient Undergrad',                'undergraduate school', 6, 35]


with open('db.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data1)
    writer.writerow(data2)
    writer.writerow(data3)
    writer.writerow(data4)