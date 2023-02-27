
def admin__1(pwd,dir):
    import csv,mysql.connector,os

    os.chdir(dir+"\CSVtoDB")
    cnx=mysql.connector.connect(
        database='project',
        host='localhost',
        user='root',
        password=pwd)

    cursor= cnx.cursor()

    L=[]
    folders=os.listdir()
    for i in folders:
        if i[-4:]=='.csv':
            L.append(i[0:len(i)-4])
        
            
    for i in L:
        namecsv=i
        string=''
        with open (namecsv+'.csv','r') as f:
            fr=csv.reader(f)
            j=-1
            for row in fr:
                if j == -1:
                    j+=1 
                    continue
                j+=1
                date=row[0]
                date=str(date[6:10]+date[2:6]+date[0:2])
                if row[1]=='n':                
                    price='nnnn'
                else:
                    opn=round(float(row[1]), 2)
                    high=round(float(row[2]), 2)
                    low=round(float(row[3]), 2)
                    close=round(float(row[4]), 2)
                    price=opn+high+low+close
                
                if j==31:
                    if price == 'nnnn':
                        price='NULL'
                        string+="('{}',NULL,NULL,NULL,NULL,NULL)".format(date)
                        break
                    string+="('{}',{},{},{},{},{})".format(date,round(float(price)/4, 2),opn,high,low,close)
                    break

                if price == 'nnnn':
                    price='NULL'
                    string+="('{}',NULL,NULL,NULL,NULL,NULL),".format(date)
                    opn=row[1]
                    high=row[2]
                    low=row[3]
                    close=row[4]
                    continue
                 
                string+="('{}',{},{},{},{},{}),".format(date,round(float(price)/4, 2),opn,high,low,close)

        if cnx.is_connected:
            
            cursor.execute('DROP TABLE IF EXISTS {}'.format(namecsv))
            query ='Create table {}(Dop date,Average Float(10,3),Open Float(10,3),\
                High Float(10,3),Low Float(10,3), Close Float(10,3))'.format(namecsv)
            cursor.execute(query)
            query = 'insert into {}(Dop,Average,Open,High,Low,Close) values {}'.format(namecsv,string)
            cursor.execute(query)
            cnx.commit()
            
    cnx.close()
