import csv
if __name__=="__main__":
    f = open('q3.csv')
    data = csv.reader(f)
    header=next(data)
    line1=0
    line2=0
    line3=0
    line4=0
    line5=0
    line6=0
    line7=0
    line8=0
    line9=0
    
    
    usemx1line=''
    usemx2=0
    usemx2line=''
    usemn1=999
    usemn1line=''
    usemn2=999
    usemn2line=''
    for row in data:
        row[4]=int(row[4])
        row[5]=int(row[5])
        if row[1]=='1호선':
            line1+=row[4]+row[5]
        if row[1]=='2호선':
            line2+=row[4]+row[5]
        if row[1]=='3호선':
            line3+=row[4]+row[5]
        if row[1]=='4호선':
            line4+=row[4]+row[5]
        if row[1]=='5호선':
            line5+=row[4]+row[5]
        if row[1]=='6호선':
            line6+=row[4]+row[5]
        if row[1]=='7호선':
            line7+=row[4]+row[5]
        if row[1]=='8호선':
            line8+=row[4]+row[5]
        if row[1]=='9호선':
            line9+=row[4]+row[5]
    
    a = [line1,line2,line3,line4,line5,line6,line7,line8,line9]
    mx2nd=0
    mn2nd=max(a)
    for i in range(0,8):
        if a[i]>mx2nd:
            if a[i]!=max(a):
                mx2nd=a[i]
                mx2ndline=a.index(a[i])+1
    for i in range(0,8):
        if a[i]<mn2nd:
            if a[i]!=min(a):
                mn2nd=a[i]
                mn2ndline=a.index(a[i])+1         
    print("***Subway REport for Seoul on March 2023***")
    print("1st Busiest Line: Line",a.index(max(a))+1,'(',max(a),')')
    print("2nd Busiest Line: Line",mx2ndline,'(',mx2nd,')')
    print("1st Least used Line: Line",a.index(min(a))+1,'(',min(a),')')
    print("2nd Least used Line: Line",mn2ndline,'(',mn2nd,')')
