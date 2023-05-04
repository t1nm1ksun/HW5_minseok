import csv
if __name__=="__main__":
    f = open('q4.csv')
    data = csv.reader(f)
    header=next(data)
    line1stmx=''
    line1stmn=''
    line1mx=0
    line1mn=99999999999
    
    line2stmx=''
    line2stmn=''
    line2mx=0
    line2mn=99999999999
    
    line3stmx=''
    line3stmn=''
    line3mx=0
    line3mn=99999999999
    
    line4stmx=''
    line4stmn=''
    line4mx=0
    line4mn=99999999999
 
    for row in data:
        row[4]=int(row[4])
        row[5]=int(row[5])
        if row[1]=='1호선':
            if line1mx<row[4]+row[5]:
                line1mx=row[4]+row[5]
                line1stmx=row[3]
            
            if line1mn>row[4]+row[5]:
                line1mn=row[4]+row[5]
                line1stmn=row[3]
            
                
                
        if row[1]=='2호선':
            if line2mx<row[4]+row[5]:
                line2mx=row[4]+row[5]
                line2stmx=row[3]
            
            if line2mn>row[4]+row[5]:
                line2mn=row[4]+row[5]
                line2stmn=row[3]
        
        if row[1]=='3호선':
            if line3mx<row[4]+row[5]:
                line3mx=row[4]+row[5]
                line3stmx=row[3]
           
            if line3mn>row[4]+row[5]:
                line3mn=row[4]+row[5]
                line3stmn=row[3]
                
        if row[1]=='4호선':
            if line4mx<row[4]+row[5]:
                line4mx=row[4]+row[5]
                line4stmx=row[3]
            
            if line4mn>row[4]+row[5]:
                line4mn=row[4]+row[5]
                line4stmn=row[3]
            
       
        
    
          
    print("***Subway REport for Seoul on March 2023***")
    
    print("Line 1:")
    print("Busiest Station:",line1stmx,'(',line1mx,')')
    print("Least Station:",line1stmn,'(',line1mn,')')
    print("Line 2:")
    print("Busiest Station:",line2stmx,'(',line2mx,')')
    print("Least Station:",line2stmn,'(',line2mn,')')
    print("Line 3:")
    print("Busiest Station:",line3stmx,'(',line3mx,')')
    print("Least Station:",line3stmn,'(',line3mn,')')
    print("Line 4:")
    print("Busiest Station:",line4stmx,'(',line4mx,')')
    print("Least Station:",line4stmn,'(',line4mn,')')
