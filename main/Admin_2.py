def admin__2(pwd,dir):
    import os,csv
    
    L=[]
    
    os.chdir(dir+"\CSVtoDB")

    files=os.listdir()
    for i in files:
        if i[-4:]=='.csv':
            L.append(i[0:len(i)-4])
    for i in L:
        temp_file=open('temp.csv','w',newline='')
        writer=csv.writer(temp_file)
        namecsv=i
        with open (namecsv+'.csv','r') as f:
            fr=csv.reader(f)
            top= ['Date','Open','High','Low','Close','Adj Close','Volume']

            writer.writerow(top)
            j=0
            
            for row in fr:
                if j==0:
                    j+=1
                    continue
                date=row[0]
                if date[2] == '-': 
                    day = int(date[0:2])
                    
                else: 
                    date=str(date[8:]+date[4:8]+date[0:4])
                    day = int(date[0:2])
                    
                for i in range(j,day):
                    if i <10:
                        writer.writerow(['0{}-08-2020'.format(i), 'n', 'n', 'n', 'n','n','n'])
                        j+=1
                    else:
                        writer.writerow(['{}-08-2020'.format(i), 'n', 'n', 'n', 'n','n','n'])
                        j+=1
                writer.writerow([date,row[1],row[2],row[3],row[4],row[5],row[6]])
                j+=1

            while j < 32:
                writer.writerow(['{}-08-2020'.format(j), 'n', 'n', 'n', 'n','n','n'])
                j+=1
            
            temp_file.flush()
            temp_file.close()
        os.remove(namecsv+'.csv')
        os.rename('temp.csv',namecsv+'.csv')
            
