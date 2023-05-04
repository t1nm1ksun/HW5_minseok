import csv
if __name__=="__main__":
    f = open('q1.csv')
    data = csv.reader(f)
    header=next(data)
    avg=0
    avgmn=0
    avgmx=0
    cnt=0
    for row in data:
        if row[2] != '' and row[3] != '' and row[4] != '':
            row[3]=float(row[3])
            row[2]=float(row[2])
            row[4]=float(row[4])
            avg+=row[2]
            avgmx+=row[4]
            cnt+=1
            avgmn+=row[3]
        
     
    avg=round(avg/cnt,2)
    avgmx=round(avgmx/cnt,2)
    avgmn=round(avgmn/cnt,2)

    print("***Annual Temperature Report for Seoul in 2022***")
    print("Average Temperature:",avg,"celsius")
    print("Average Minimum Temperature :",avgmn,"celsius")
    print("Average Maximum Temperature :",avgmx,"celsius")

