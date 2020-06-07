from tinydb import TinyDB, Query
import random
import json
from datetime import datetime
path='./data.json'
path2='./db.json'
def new_entry():
    print('-------------------------------------------------------------')
    print('Opening database for new entry...')
    name=input('Enter name of student-') 
    nof=input("Enter name of student's father-") 
    nom=input("Enter name of student's mother-") 
    dob=input('Enter Date Of Birth of the student-') 
    y=input('Enter Year of Birth...') 
    bg=input("Enter student's Blood-group-") 
    cl= input('Enter class in which the student is being enrolled in. -')
    ph=input('Enter phone no.-')
    doa=datetime.date(datetime.now())
    ids=customid()
    admn=entryno()+1
    db=TinyDB(path)
    now=datetime.now()
    age=now.year-int(y)
    try:
        db.insert({'Admission no.':admn,'Name':name,'id':ids,\
"Father's Name":nof,"Mother's Name":nom,'Date of Birth':dob,'Age':age,\
'Blood Group':bg,'Class':cl,'Date of Admission':str(doa),'Phone':ph})
        print('Added the student to database...')
    except Exception as e:
        print('A minor error occured...')
        print(e)
    db2=TinyDB(path2)
    m=Query()
    if not db2.contains(m['Admission no.']):
        db2.insert({'Admission no.':0})
    else:
        docs=db2.search(m['Admission no.'])
        for doc in docs:
            doc['Admission no.']+=1
        db2.write_back(docs)
    
def entryno():
    print('-------------------------------------------------------------')
    db2=TinyDB(path2)
    usr=Query()
    if not db2.contains(usr['Admission no.']):
        db2.insert({'Admission no.':0})
        return 0
    else:
        docs=db2.search(usr['Admission no.'])
        for doc in docs:
            m=doc['Admission no.']
        return m

def records():
    print('-------------------------------------------------------------')
    print('Do you have an argument by which you can\
search for a particular student?')
    inp=input('If you want to search by Name, press1\n\
If you want to search by Admission No., press2\n\
If you want to search by id, press3\n\
If you want to search by Name of Father, press4\n\
If you want to search by Name of Mother, press5\n\
If you want to searchby Phone no., press6\n\
If you want to return to previous menu, press7.\n>')
    db=TinyDB(path)
    usr=Query()
    inp=int(inp)
    print('-------------------------------------------------------------')
    if inp==1:
        nm=input('Enter name of Student-')
        try:
            docs=db.search(usr['Name']==nm.lower())
            for doc in docs:
                print(json.dumps(doc,sort_keys=True, indent=4))
        except:
            print('Argument not found in database')
            return
    elif inp==2:
        inu=int(input('Enter Admission No. of Student-'))
        try:
            docs=db.search(usr['Admission no.']==inu)
            for doc in docs:
                print(json.dumps(doc,sort_keys=True, indent=4))
        except:
            print('Argument not found in database')
            return
    elif inp==3:
        id=input("Enter Student's ID-")
        try:
            docs=db.search(usr['id']==id)
            for doc in docs:
                print(json.dumps(doc,sort_keys=True, indent=4))
        except:
            print('Argument not found in database')
            return

    elif inp==4:
        nof=input("Enter name of Student's Father-")
        try:
            docs=db.search(usr["Father's Name"]==nof.lower())
            for doc in docs:
                print(json.dumps(doc,sort_keys=True, indent=4))
        except:
            print('Argument not found in database')
            return
    elif inp==5:
        nom=input("Enter name of Student's Mother-")
        try:
            docs=db.search(usr["Mother's Name"]==nom)
            for doc in docs:
                print(json.dumps(doc,sort_keys=True, indent=4))
        except:
            print('Argument not found in database')
            return 
    elif inp==6:
        phon=input('Enter Phone No.-')
        try:
            docs=db.search(usr['Phone']==phon)
            for doc in docs:
                print(json.dumps(doc,sort_keys=True, indent=4))
        except:
            print('Argument not found in database')
            return
        
    elif inp==7:
        interface()
    else:
        print('Please enter a valid no.')
        records()
    
def customid():
    ls=[0,1,2,3,4,5,6,7,8,9]
    lp=[]
    for i in range(9):
        p=random.choice(ls)
        lp.append(str(p))
    lp=''.join(lp)
    db=TinyDB(path)
    usr=Query()
    docs=db.search(usr['id']==lp)
    if docs:
        customid()
    else:
        return lp

def edit():
    print('Welcome to the data editor menu...')
    print('First you must select the student whose data you want to edit')
    print('-------------------------------------------------------------')
    print('Do you have an argument by which you can\
search for a particular student?')
    inp=input('If you want to search by Name, press1\n\
If you want to search by Admission No., press2\n\
If you want to search by id, press3\n\
If you want to search by Name of Father, press4\n\
If you want to search by Name of Mother, press5\n\
If you want to search by Phone no., press6\n\
If you want to return to previous menu, press7.\n>')
    db=TinyDB(path)
    usr=Query()
    inp=int(inp)
    print('-------------------------------------------------------------')
    if inp==1:
        nm=input('Enter name of Student-')
        try:
            docs=db.search(usr['Name']==nm.lower())
            for doc in docs:
                print(json.dumps(doc,sort_keys=True, indent=4))
        except:
            print('Argument not found in database')
            return
    elif inp==2:
        inu=int(input('Enter Admission No. of Student-'))
        try:
            docs=db.search(usr['Admission no.']==inu)
            for doc in docs:
                print(json.dumps(doc,sort_keys=True, indent=4))
        except:
            print('Argument not found in database')
            return
    elif inp==3:
        id=input("Enter Student's ID-")
        try:
            docs=db.search(usr['id']==id)
            for doc in docs:
                print(json.dumps(doc,sort_keys=True, indent=4))
        except:
            print('Argument not found in database')
            return

    elif inp==4:
        nof=input("Enter name of Student's Father-")
        try:
            docs=db.search(usr["Father's Name"]==nof.lower())
            for doc in docs:
                print(json.dumps(doc,sort_keys=True, indent=4))
        except:
            print('Argument not found in database')
            return
    elif inp==5:
        nom=input("Enter name of Student's Mother-")
        try:
            docs=db.search(usr["Mother's Name"]==nom)
            for doc in docs:
                print(json.dumps(doc,sort_keys=True, indent=4))
        except:
            print('Argument not found in database')
            return 
    elif inp==6:
        phon=input('Enter Phone No.-')
        try:
            docs=db.search(usr['Phone']==phon)
            for doc in docs:
                print(json.dumps(doc,sort_keys=True, indent=4))
        except:
            print('Argument not found in database')
            return
        
    elif inp==7:
        interface()
    else:
        print('Please enter a valid no.\nTerminating...')
        edit()
    
    if len(docs)>1:
        print('There are multiple Entries inside the Database\
refering to that person\'s details')
        print('Consider Identifying the student from the data given \
above or using other parameters.\n\
If you find them, notice their ID \
and TYPE it in to obtain access OR \
type "db.reload" to use different parameter')
        inp=input('>')
        if inp=='db.reload':
            edit()
        else:
            try:
                db=TinyDB(path)
                usr=Query()
                docs=db.search(usr['id']==inp)
                for doc in docs:
                    print(json.dumps(doc,sort_keys=True, indent=4))
                dbs=doc
                print('-----------------------------------\
--------------------------')
                print('Now that you have identified entry,\
you can begin editing it.')
                print('The column name will start display.\
Add the addition you want to make to respective entry against it\
and then press ENTER.\n\
*If you don\'t want to edit any specific entry, press 0')
                for i in dbs:
                    k=input(f'{i}: ({dbs[i]})-')
                    if k!='0':
                        print('Editing database...')
                        for doc in docs:
                            doc[i]=k
                        db.write_back(docs)    
                
            except:
                print('Argument not found in database')
                return  
    else:
        dbs=doc
        print('-------------------------------------------------------------')
        print('Now that you have found entry, you can begin editing it.')
        print('The column name will start display.\
Add the addition you want to make to respective entry\
against it and then press ENTER.\n\
*If you don\'t want to edit any specific entry, press 0')
        for i in dbs:
            k=input(f'{i}: ({dbs[i]})-')
            if k!='0':
                print('Editing database...')
                for doc in docs:
                    doc[i]=k
                db.write_back(docs)
                

def retry():
    print('-------------------------------------------------------------')
    i= input("If you want to reuse the student database press 0-")
    if i == '0':
        print('Reopening database...')
        interface()
    else:
        pass

def interface():
    print('\t\tAmity International School, Noida-201301')
    print('Welcome to the Student Registry Database\
For New Admission Documentation')
    a=input('\t    If you want to make new entry, press-1\n\
        If you want to find total no. of registered students,press-2\n\
        If you want to access past student records, press-3\n\
        If you want to edit some past entry, press-4\n\
        If you want to exit database, press-5\n>')
    if a.isalpha():
        print('Error.Unrecognized character.')
    elif int(a)==1:
        new_entry()
    elif int(a)==2:
        a=entryno()
        print(a)
    elif int(a)==3:
        records()
    elif int(a)==4:
        edit()
    elif int(a)==5:
        pass
    else:
        print('Index out of scope.')
    retry()
interface()


