import csv
if __name__=="__main__":
    f = open('q2.csv')
    data = csv.reader(f)
    header=next(data)
    submx=-999
    submn=999
    datemx=''
    datemn=''
   
    for row in data:
        if row[3] != '' and row[3] != '':
            row[3]=float(row[3])
            row[4]=float(row[4])
            if (row[4]-row[3])>submx:
                submx=row[4]-row[3]
                datemx=row[0]
            if (row[4]-row[3])<submn:
                submn=row[4]-row[3]
                datemn=row[0]
       
    submn=round(submn,2)
    subm=round(submx,2)
    print("***Annual Temperature Report for Seoul in 2022***")    
    print("Day with the Largest Temperature Variation :",datemx)
    print("Maximun Temperature Difference:",submx,"celsius")
    print("Day with the Smallest Temperature Variation :",datemn)
    print("Minimun Temperature Difference:",submn,"celsius")
