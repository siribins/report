import mysql.connector

def New():
    createtable="create table if not exists student(admissionno varchar(10) primary key, rollno varchar(5), name varchar(30), fname varchar(30), mname varchar(30), phone varchar(12), address varchar(100), sclass varchar(5), section varchar(2))"
    cursor.execute(createtable)
    admissionno=input("Enter student's admission number: ")
    rollno=input("Enter student's roll number: ")
    name=input("Enter student's  name: ")
    fname=input("Enter father's name: ")
    mname=input("Enter mother's name: ")
    phone=input("Enter contact number: ")
    address=input("Enter address: ")
    sclass=input("Enter class: ")
    section=input("Enter section: ")
    insert="insert into student (admissionno, rollno, name, fname, mname, phone, address, sclass, section) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values=(admissionno, rollno, name, fname, mname, phone, address, sclass, section)
    cursor.execute(insert, values)
    cursor.execute("commit")
    print("Student data added")
    cursor.close()

def Display():
    cursor.execute("select * from student")
    data=cursor.fetchall()
    print(data)
    cursor.close()

def Update():
    admission_no=input("Enter student's admission number: ")
    sql="select * from student where admissionno=%s"
    cursor.execute(sql,(admission_no,))
    data=cursor.fetchall()
    if data:
        print('''Press 1 to change name
Press 2 to change phone number
Press 3 to change address''')
        choice=int(input("Enter your choice: "))
        if choice==1:
            name=input("Enter name of student: ")
            sql="update student set name= %s where admissionno =%s"
            cursor.execute(sql,(name,admission_no))
            cursor.execute("commit")
            print("Name updated")
        elif choice==2:
            phoneno=input("Enter phone number: ")
            sql="update student set phone= %s where admissionno=%s"
            cursor.execute(sql,(phoneno,admission_no))
            cursor.execute("commit")
            print("Phone number updated")
        elif choice==3:
            address=input("Enter address: ")
            sql="update student set address= %s where admissionno= %s"
            cursor.execute(sql, (address, admission_no))
            cursor.execute("commit")
            print("Address updated")
    else:
        print("Something went wrong")
    cursor.close()

def Marks():
    createtable="create table if not exists marks (admissionno varchar(10) primary key, english int, math int, physics int, chemistry int, computer int, total int, average int)"
    cursor.execute(createtable)
    admission_no=input("Enter student's admission number: ")
    english=int(input("Enter marks scored in English: "))
    math=int(input("Enter marks scored in Math: "))
    physics=int(input("Enter marks scored in Physics: "))
    chemistry=int(input("Enter marks scored in Chemistry: "))
    computer=int(input("Enter marks scored in Computer: "))
    total=english+math+physics+chemistry+computer
    average=total/5
    sql="insert into marks (admissionno, english, math, physics, chemistry, computer, total, average) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    values= (admission_no, english, math, physics, chemistry, computer, total, average)
    cursor.execute(sql,values)
    cursor.execute("commit")
    cursor.close()

def AllReport():
    cursor.execute("select * from marks")
    data=cursor.fetchall()
    for i in data:
        print(i,"\n")
    cursor.close()

def OneReport():
    admission_no=input("Enter admission number of student: ")
    sql="select * from marks where admissionno=%s"
    cursor.execute(sql,(admission_no,))
    data=cursor.fetchall()
    if data:
        print(data)
    else:
        print("Record not found")
    cursor.close()

def Details():
    admission_no=input("Enter the student's admission number: ")
    sql="select * from student, marks where student.admissionno=marks.admissionno and student.admissionno=%s"
    cursor.execute(sql,(admission_no,))
    data=cursor.fetchall()
    print(data)
    cursor.close()
    
while True:
    db=mysql.connector.connect(host='localhost', user='root', passwd='root', database='exam')
    cursor=db.cursor()
    print("*"*20,"MENU","*"*20)
    print('''1. To add a student record
2. To display student record
3. To update student record
4. Add student's marks
5. To generate all student's report card
6. To generate one student's report card
7. To see all details of one student
8. Exit''')
    print("*"*45)
    choice=int(input("Enter your choice: "))
    if choice==1:
        New()
    elif choice==2:
        Display()
    elif choice==3:
        Update()
    elif choice==4:
        Marks()
    elif choice==5:
        AllReport()
    elif choice==6:
        OneReport()
    elif choice==7:
        Details()
    elif choice==8:
        print("Exiting...")
        cursor.close()
        break
    else:
        print("Invalid choice")
