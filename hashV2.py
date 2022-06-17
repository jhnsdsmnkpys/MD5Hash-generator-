import hashlib,datetime,MySQLdb
m = hashlib.md5()
"from dateutil.parser import *"
hasil1=[103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,
       121,122,48,49,50,51,52,53,54,55,56,57,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,
       83,84,85,86,87,88,89,90]
hasil=[97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,
       121,122,48,49,50,51,52,53,54,55,56,57,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,
       83,84,85,86,87,88,89,90]

# 0=a 1=b 2=c 3=d 4=e 5=f 6=g 7=h 8=i 9=j 10=k 11=l 12=m 13=n 14=o 15=p 16=q
# 17=r 18=s 19=t 20=u 21=v 22=w 23=x 24=y 25=z
# 26=0 27=1 28=2 29=3 30=4 31=5 32=6 33=7 34=8 35=9
# 36=A 37=B 38=C 39=D 40=E 41=F 42=G 43=H 44=I 45=J 46=K 47=L 48=M 49=N 50=O
# 51=P 52=Q 53=R 54=S 55=T 56=U 57=V 58=W 59=X 60=Y 61=Z

conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="bps")
cur= conn.cursor()
i = 0
i2 = 2
i3 = 19
i4 = 39
i5 = 1

now = datetime.datetime.now()
tanggal = now.strftime("%H:%M:%S")

now = datetime.datetime.now()
tanggal = now.strftime("%H:%M:%S")
while i <= 55 :
    letter = hasil1[i]
    plaintext = chr(letter)
    m.update(plaintext)
    x = m.hexdigest()
    i = i + 1
    #i2 = 0
    print "BPS CRACK -->>>> Text Asli : '%s'  Md5 Hash :'%s'"%(plaintext,x)
    sql1 = " insert into bpscrack (pwd,md5) values ('%s','%s')"%(plaintext,x)
    cur.execute(sql1)
    conn.commit()
    while i2 <= 61 :
        bit2 = hasil[i2]
        plaintext = chr(letter)+chr(bit2)
        m.update(plaintext)
        x = m.hexdigest()
        i2 = i2 + 1
        #i3 = 0
        print "BPS CRACK -->>>> Text Asli : '%s'  Md5 Hash :'%s'"%(plaintext,x)
        sql1 = " insert into bpscrack (pwd,md5) values ('%s','%s')"%(plaintext,x)
        cur.execute(sql1)
        conn.commit()
        while i3 <= 61 :
            bit3 = hasil[i3]
            plaintext = chr(letter)+chr(bit2)+chr(bit3)
            m.update(plaintext)
            x = m.hexdigest()
            i3 = i3 + 1
            #i4 = 0
            print "BPS CRACK -->>>> Text Asli : '%s'  Md5 Hash :'%s'"%(plaintext,x)
            sql1 = " insert into bpscrack (pwd,md5) values ('%s','%s')"%(plaintext,x)
            cur.execute(sql1)
            conn.commit()
        
            while i4 <= 61:
                bit4 = hasil[i4]
                plaintext = chr(letter)+chr(bit2)+chr(bit3)+chr(bit4)
                m.update(plaintext)
                x = m.hexdigest()
                i4 = i4 + 1
                #i5 = 0
                print "BPS CRACK -->>>> Text Asli : '%s'  Md5 Hash :'%s'"%(plaintext,x)
                sql1 = " insert into bpscrack (pwd,md5) values ('%s','%s')"%(plaintext,x)
                cur.execute(sql1)
                conn.commit()
            
                while i5 <= 61 :
                    bit5 = hasil[i5]
                    plaintext = chr(letter)+chr(bit2)+chr(bit3)+chr(bit4)+chr(bit5)
                    m.update(plaintext)
                    x = m.hexdigest()
                    i5 = i5 + 1
                
                    print "BPS CRACK -->>>> Text Asli : '%s'  Md5 Hash :'%s'"%(plaintext,x)
                    sql1 = " insert into bpscrack (pwd,md5) values ('%s','%s')"%(plaintext,x)
                    cur.execute(sql1)
                    conn.commit()
                i5 = 0
            i4 = 0
        i3= 0
    i2 = 0

now = datetime.datetime.now()
tanggal2 = now.strftime("%H:%M:%S")
print ("Start Time %s"%(tanggal))
print ("End Time %s"%(tanggal2))
print parse(tanggal2) - parse(tanggal)

