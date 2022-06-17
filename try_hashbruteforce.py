import hashlib,binascii

hasil1=[100]
pwd=[0]
asci=[97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,
     117,118,119,120,121,122]

i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
i7 = 0
i8 = 0
i9 = 0
i10 = 0
i11 = 0
i12 = 0

hashpwd = raw_input("Masukan Hash Password :: " )

while i1 <= 25:
    dit1 = asci[i1]
    text1 = chr (dit1)
    md4 = hashlib.new('md4', text1.encode('utf-16le')).digest()

    h_md4 = binascii.hexlify(md4)
    if h_md4 == hashpwd:
        pwd.insert(0,(h_md4))
    if pwd[0] == hashpwd:
        break
    else:
        i1 = i1 + 1

    print "Text >>> " + text1 + "||"+ "Hash ::" + h_md4

    while i2 <=25:
        dit2 = asci[i2]
        text2 = chr(dit1) + chr(dit2)
        md4 = hashlib.new('md4', text2.encode('utf-16le')).digest()
        h_md4 = binascii.hexlify(md4)
        if h_md4 == hashpwd:
            pwd.insert(0,(h_md4))
        if pwd[0] == hashpwd:
            break
        else:
            i2 = i2 + 1
        print "Text >>> " + text2 + "||"+ "Hash ::" + h_md4
    i2 = 0
i1 = 0
print "Ditemukan : %s " %(pwd[0]) + "<<<" + text1,text2
        
        
        

