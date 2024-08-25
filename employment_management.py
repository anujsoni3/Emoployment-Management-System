import pymysql as pm
import sys
from pygame import mixer              
import prettytable as pt
import time


#_______________________________________________________________________jai shreee ram _________________________________________________________________________________________________

def getmaxeno():
    maxid=''                                                                                              
    try:
        con=pm.connect(user="root",password="root",host='localhost',database="emp")                      
        cur=con.cursor()
        qry="select max(eno) from emp"
        cur.execute(qry)                                                                                 
        row=cur.fetchone() #(None,)                                                                     
        #print(row)    
        if row[0]==None:
            maxid=1   
        else:
             maxid=row[0]+1    
    except pm.DatabaseError as e:
        con.rollback()
        print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
        return maxid
def getmaxjid():
    maxid=''
    try:
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        qry="select max(jid) from job"
        cur.execute(qry) 
        row=cur.fetchone() #(None,)
        #print(row)    
        if row[0]==None:
            maxid=1
            
        else:
            maxid=row[0]+1
        
               
    except pm.DatabaseError as e:
        con.rollback()
        print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
        return maxid
    
def getmaxdno():
    maxdno=''
    try:
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        qry="select max(dno) from dept"
        cur.execute(qry) 
        row=cur.fetchone() #(None,)
        #print(row)    
        if row[0]==None:
            maxdno=1
            
        else:
            maxdno=row[0]+1
        return maxdno
        
               
    except pm.DatabaseError as e:
        con.rollback()
        print(' '*gapvalue,'Database Error : ',e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
        return maxdno

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
mwd="8737"
def add():
    try:
        
        eno=getmaxeno()
        print("EMPLOYE ID:" , eno)
        fname=input("enter first name")
        lname=input("enter  last name") 
        dno=int(input("ENTER dpt no."))
        gender=input("enter gender m/male/f/female")
        doj=input("enter doj")
       
        jid=int(input("ENTER JOB ID OF EMPLOYE "))
       
        qry= f"""
            INSERT INTO emp
            VALUES
            ({eno},"{fname}","{lname}",{dno}, "{gender}","{doj}",{jid})
    """
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        con.commit()
        print("EMPLOYE ADDED SUCCESFULLY")
    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input()
    

def update():
   
    try:
        eno=int(input("ENTER EMLOYE ID YOU WANT TO UPDATE"))
        qry=f"""
            select * from emp
            WHERE eno={eno}
    """
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        data=cur.fetchone()
        if data == None:
            print( "DATA NOT FOUND")
            return
        else:
            print(data)
        qrydel=f"""
               DELETE
               FROM emp                             
               where eno={eno}
    """

        cur.execute(qrydel)
        con.commit()
        #addnewdetails
    #________________________________        ___
        print("DO YOU WISH TO UPDATE EMPLOYE  ENTER Y/N ?")
     
        
        
        
        fname=input("enter first name")
        lname=input("enter  last name") 
        dno=int(input("ENTER dpt no."))
        gender=input("enter gender m/male/f/female")
        doj=input("enter doj")
       
        jobid=int(input("jobid"))
       
        qry= f"""
            INSERT INTO emp
            VALUES
            ({eno},"{fname}","{lname}",{dno}, "{gender}","{doj}" ,{jobid})
    """
      

      
        cur.execute(qry)
        con.commit()
        
        print("DATA UPDATED")
    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input() 


def showall():
  
    try:
        qry="""
            select *
            from emp,dept,job
            where emp.dno=dept.dno and emp.jid=job.jid
    """
        r=['eno','fname','lname','dno','gender','doj','jobid' , "departmentno","department","manager","jid","jobname","salary","commision"]
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        if con==None :
            print("ERROR OCCURED")
        cur=con.cursor()
        cur.execute(qry)
        data=cur.fetchall()
        t=pt.PrettyTable(r)
        if data==():
            print( "DATA NOT FOUND")
            pass
        else:
            print("EMPLOYE DETAILS")
            for i in data:
                t.add_row(i)
            print(t)
            print("ENTER ANY KEY TO MAIN MENU ")
            input()


    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
    

        if cur:
            
            cur.close()
        if con:
            
            con.close()
        

def searchbyeno():
    
    
    
    try:
        

        eno=int(input("ENTER EMLOYE ID YOU WANT TO SEE"))
        qry=f"""
            select *
            from emp,dept,job
            where emp.dno=dept.dno and emp.jid=job.jid and eno={eno} 
    """
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        data=cur.fetchone()
        r=['eno','fname','lname','dno','gender','doj','jobid' , "departmentno","department","manager","jid","jobname","salary","commision"]
        t=pt.PrettyTable(r)
        if data ==None:
            print( "DATA NOT FOUND")
            return
        else:
            print("DESIRED EMPLOYE")
            t.add_row(data)
            print(t)
            
    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input()
def delete():      
    try:      
        eno=int(input("ENTER EMLOYE ID YOU WANT TO UPDATE"))
        qry=f"""

            select * from emp
            WHERE eno={eno}
    """
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        data=cur.fetchone()
        r=['eno','fname','lname','dno','gender','doj','jobid' , "departmentno","department","manager","jid","jobname","salary","commision"]
        t=pt.PrettyTable(r)
        if data == None:
            print( "DATA NOT FOUND")
            pass
        else:
            print("DESIRED EMPLOYE")
            t.add_row(data)
            print(t)
            t.add_row(i)
            print(t)
        qrydel=f"""
               DELETE
               FROM emp                             
               where eno={eno}
            
    """
        print("ARE YOU SURE TO DELETE EMPLOYE  ENTER Y/N ?")
        IN=input()
        if IN.lower()in ["y","yes"]:
             con=pm.connect(user="root",password="root",host='localhost',database="emp")
             cur=con.cursor()
             cur.execute(qrydel)
             con.commit()
             print(":EMP DELETED SUCCESFULLY 🙂 ")
            
       
        else:
            print("WORK ABORTED 🙂 ")
            pass
   
    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input()

#=====================================================================================================================================================================
#=======================================================================================================================================================================
def searchbydept():
    try:
        
        dno=int(input("ENTER DEPARTMENT NUMBER"))
        qry=f""" select *
                 from emp,dept,job
                 where emp.dno=dept.dno and emp.jid=job.jid and dept.dno={dno}

            """
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        data=cur.fetchone()
        r=['eno','fname','lname','dno','gender','doj','jobid' , "departmentno","department","manager","jid","jobname","salary","commision"]
        t=pt.PrettyTable(r)
        if data==None:
            print("NO EMPLOYE FOUND")
        else:
            print("EMPLOYE DETAILS BASED ON DEPARTMENT")
            
            t.add_row(data)
            print(t)
            print("ENTER ANY KEY TO MAIN MENU ")
            input()
      
    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input()
#searchbydept()

def insertnewdept():
    try:
            
        dno=getmaxdno()
        print("DEPARTMENT NUMBER :",dno)
        dname=input("NAME OF THE DEPARTMENT")
        man=input("ENTER MANAGER OF dept")
        qry=f""" INSERT INTO dept
                 values
                 ({dno},"{dname}","{man}")

        """
        
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        con.commit()
    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input()


def viewalldept():
    try:
        
        qry=f""" select *
                 from dept
        """
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        data=cur.fetchall()
        r=[ "departmentno","department","manager"]
        t=pt.PrettyTable(r)
        if data==():
            print("NO DEPARTMENT FOUND")
        else:
            
            for i in data:
                t.add_row(i)
            print(t)
            

        
    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input()
#viewalldept()
def updatedept():
    try:
            
        dno=int(input("ENTER DEPARTMENT NUMBER:"))
        qry=f""" select *
                 from dept
                 where dno={dno}    
    """
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        data=cur.fetchone()
        r=[ "departmentno","department","manager"]
        t=pt.PrettyTable(r)
        if data == None:
            print( "DATA NOT FOUND")
            return
        else:
            t.add_row(data)
            print(t)
           
      
        qrydel=f"""
               DELETE
               FROM dept                         
               where dno={dno}
        """

        cur.execute(qrydel)
        con.commit()

         #enter new details
        dname=input("NAME OF THE DEPARTMENT")
        man=input("ENTER MANAGER OF dept")
        qry=f""" INSERT INTO dept
                 values
                 ({dno},"{dname}","{man}")

        """
        
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        con.commit()
    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input()
        

#mwd="8737"
def deldept():
    try:
            
        dno=int(input("ENTER DEPARTMENT NUMBER:"))
        qry=f""" select *
                 from dept
                 where dno={dno}    
    """
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        
        data=cur.fetchone()
        r=[ "departmentno","department","manager"]
        t=pt.PrettyTable(r)
        if data == None:
            print( "DATA NOT FOUND")
            return
        else:
            t.add_row(data)
            print(t)
            
        qrydel=f""" DELETE
                    FROM dept                            
                    where dno={dno}
        """
        
        print("ARE YOU SURE TO DELETE DEPARTMENT ENTER Y/N ?")
        IN=input()
        if IN.lower()in ["y","yes"]:
             con=pm.connect(user="root",password="root",host='localhost',database="emp")
             cur=con.cursor()
             cur.execute(qrydel)
             con.commit()
             print(":DEPARTMENT DELETED SUCCESFULLY 🙂 ")
            
       
        else:
            print("WORK ABORTED 🙂 ")
            pass
    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input()

#deldept()    
            
#=========================================================================================================================================================================

def viewalljob():
    try:
        
        qry=f""" select *
                 from job
        """
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        data=cur.fetchall()
        r=["jid","jobname","salary","commision"]
        t=pt.PrettyTable(r)
        if data==():
            print("NO JOB FOUND")
        else:
            for i in data:
                t.add_row(i)
            print(t)
           

    except pm.DatabaseError as e:
        
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input()
#viewalljob()        
def searchbyjobid():
    
    try:

        jid=int(input("ENTER JOBID OF EMPLOYE"))
        qry=f""" select *
                from emp NATURAL JOIN job
                WHERE jid={jid}
            """
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        data=cur.fetchone()
        r=['eno','fname','lname','dno','gender','doj','jobid' ,"jobname","salary","commision"]
        t=pt.PrettyTable(r)
        if data==None:
            print("NO EMPLOYE FOUND")
        else:
            t.add_row(data)
            print(t)
    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input()

#searchbyjobid()
def insertnewdJOB():
    try:
            
        jobid=getmaxjid()
        print("JOBID:",jobid)
        jobname =input("ENTER NAME OF NEW JOB")
        basicsal=float(input("ENTER BASIC  SALARY OF NEW JOB"))
        comm=float(input("ENTER COMMISION "))
        qry=f""" INSERT INTO job
                 values
                 ({jobid},"{jobname}",{basicsal},{comm})

        """
        
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        con.commit()
    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input()


    
def updatejob():
    try:
            
        jid=int(input("ENTER job number:"))
        qry=f""" select *
                 from job
                 where jid={jid}    
    """
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        data=cur.fetchone()
        r=['jid' ,"jobname","salary","commision"]
        t=pt.PrettyTable(r)
        if data == None:
            print( "DATA NOT FOUND")
            return
        else:
            t.add_row(data)
            print(t)
            
        qrydel=f"""
               DELETE
               FROM job                         
               where jid={jid}
        """

        cur.execute(qrydel)
        con.commit()
      #enter new details
        
        jobname =input("ENTER NAME OF NEW JOB")
        basicsal=float(input("ENTER BASIC  SALARY OF NEW JOB"))
        comm=float(input("ENTER COMMISION "))
        qry=f""" INSERT INTO job
                 values
                 ({jid},"{jobname}",{basicsal},{comm})

        """

        
        
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        con.commit()
        print("DATA UPDATED SUCCESFULYY")
    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input()
        
    
 

def deljob():
    try:
        jid=int(input("ENTER job number:"))
        qry=f""" select *
                 from job
                 where jid={jid}    
    """
        con=pm.connect(user="root",password="root",host='localhost',database="emp")
        cur=con.cursor()
        cur.execute(qry)
        data=cur.fetchone()
        r=['jid' ,"jobname","salary","commision"]
        t=pt.PrettyTable(r)
        if data == None:
            time.sleep(1)
            print( "DATA NOT FOUND")
            return
        else:
            t.add_row(data)
            time.sleep(1)
            print(t) 
            
        qrydel=f"""
                   DELETE
                   FROM job                         
                   where jid={jid}
            """
        print("ARE YOU SURE TO DELETE EMPLOYE  ENTER Y/N ?")
        IN=input()
        if IN.lower()in ["y","yes"]:
             con=pm.connect(user="root",password="root",host='localhost',database="emp")
             cur=con.cursor()
             cur.execute(qrydel)
             con.commit()
             time.sleep(1)
             print(":EMP DELETED SUCCESFULLY 🙂 ")
            
       
        else:
            time.sleep(1)
            print("WORK ABORTED 🙂 ")
            pass
    except pm.DatabaseError as e:
        con.rollback()
        print("ERROR OCCURED :", e)
    finally:
        if cur:
            cur.close()
        if con: 
            con.close()
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        input()
def password():
    time.sleep(1)
    ch=input("ENTER PASSWORD TO ACCESS FILE")
    if ch==mwd:
        time.sleep(1)
        
        print("UNLOCKED :")
        
    else:
        time.sleep(1)
        print("PLEASE ENTER CORRECT PASSWORD")
        
        sys.exit()
        
def addcom():
    time.sleep(1)
    r=input("OUT OF 5")
    time.sleep(1)
    message=input( " ENTER COMMENTS  ")
    print("STANDARD - RATING+COMMENT")
    s=r+message
    f=open("improve.txt" ,"a")
    f.write(s)
    print("COMMENT ADDED ")
    f.close()
def showcom():
    f=open("improve.txt", "r")
    print((f.read()).split())

    
    
#__________________________________________________________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________________________________________________________
        
#IMPORTING AND LOADING THE MUSIC
mixer.init()
mixer.music.load(r"C:\Users\ANUJ\Downloads\Tere Nainon Mein - (Raag.Fm).mp3")
mixer.music.set_volume(3.0)


#================================================================================ END OF CODE ================================================================================
menu= """
    ***********************************************************************************************************************************************************
    |           _ॐ_  ॐ      E M P L O Y E E     M A N A G E M E N T      S Y S T E M     ==>      M A I N     M E N U         ॐ _ॐ_                       |
    ***********************************************************************************************************************************************************
    | * |  DEPARTMENT  MODULE   | 1 | NEW  DEPARTMENT    | 2 |  VIEW ALL DEPT.   | 3 | MODIFY DEPT.   | 4 | DELETE DEPT.   |     
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    | * |       JOB MODULE              | 5 |    NEW  JOB            | 6 |  VIEW ALL JOBS     | 7 |  MODIFY JOBS      | 8 | DELETE  JOBS        | 
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    | * |   EMPLOYEE   MODULE     | 9 |    NEW   EMP.        | 10 |  VIEW ALL EMP.   | 11 |  MODIFY  EMP.      | 12 | DELETE EMP.      |
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    | * |        REPORTS            | 13 |   DEPT WISE EMP.         | 14 | JOB DEGIGNATION WISE EMP     | 15 |  VIEW EMP BY ENO.       |
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    | * |        SETTINGS              | 0 |     E  X  I  T                                      | 16 |    M U S I C / S O U N D      | 17 | ABOUT US |                                               |
    ***********************************************************************************************************************************************************
     





"""
menu2="""
    ***********************************************************************************************************************************************************
    |           _ॐ_  ॐ      E M P L O Y E E     M A N A G E M E N T      S Y S T E M     ==>      M A I N     M E N U         ॐ _ॐ_                       |
    ***********************************************************************************************************************************************************
    
                                                                   |1| NEW DEPARTMENT
                                 DEPARTMENT MODULE                 |2| VEIW ALL DEPARTMENT
                                                                   |3| MODIFY DEPARTMENT
                                                                   |4| DELETE DEPARTMENT
                                                                   
                        ----------------------------------------------------------------------------------------------------------------
                         
                                                                   |5| NEW JOB
                                                                   |6| VIEW ALL JOBS
                                 JOB MODULE                         |7| MODIFY JOBS
                                                                   |8| DELETE JOBS
                                                                   
                        ----------------------------------------------------------------------------------------------------------------
                         
                                                                   |9| NEW EMPLOYEE
                                                                   |10| VIEW ALL EMPLOYEE
                                 EMPLOYEE MODULE                   |11| MODIFY EMPLOYEE
                                                                   |12| DELETE EMPLOYE
                                                                   
                        ----------------------------------------------------------------------------------------------------------------                                         

                                                                   |13| DEPARTMENT WISE EMPLOYEE
                                 REPORTS                           |14| JOB DESIGNATION WISE EMPLOYEE
                                                                   |15| VIEW EMPLOYEE BY EMPLOYEENUMBER
                                                                   
                       -----------------------------------------------------------------------------------------------------------------

                                                                   |16| MUSIC /SOUND 
                                                                   |0|  EXIT
                                                                   
     ***********************************************************************************************************************************************************
     |                                                                                                                                                         |
     ***********************************************************************************************************************************************************
     

     


"""
    

while(1):
    print(" "*50 , "WELCOME TO MAIN MENU OF EMPLOYEE MANAGEMENT SYSTEM")
    
    print(menu)
    ch=int(input("ENTER YOUR CHOISE BETWEEN 0-17"))

    if ch==1:
        print(" INSERT NEW DEPARTMENT  ")
        time.sleep(1)
        print("ENTER ANY KEY TO CONTINUE")
        input()
        insertnewdept()

    elif ch==2:
        print("VIEW ALL DEPT")
        time.sleep(1)
        print("ENTER ANY KEY TO CONTINUE")
        input()
        viewalldept()

    elif ch==3:
        print("MODIFY DEPTARTMENT")
        time.sleep(1)
        print("ENTER ANY KEY TO CONTINUE")
        input()
        updatedept()  

    elif ch==4:
        print("DELETE A DEPARTMENT")
        print("ENTER ANY KEY TO CONTINUE")
        input()
        deldept()  

    elif ch==5:
        print("INSERT A JOB ")
        time.sleep(1)
        print("ENTER ANY KEY TO CONTINUE")
        input()
        insertnewdJOB()  

    elif ch==6:
        print("VIEW ALL JOBS")
        time.sleep(1)
        print("ENTER ANY KEY TO CONTINUE")
        input()
        viewalljob()  

    elif ch==7:
        print("MODEIFY A JOB")
        time.sleep(1)
        print("ENTER ANY KEY TO CONTINUE")
        input()
        updatejob()  

    elif ch==8:
        print("DELETE A JOB")
        time.sleep(1)
        print("ENTER ANY KEY TO CONTINUE")
        input()
        deljob()  

    elif ch==9:
        print("ADD AN EMPLOYEE")
        time.sleep(1)
        print("ENTER ANY KEY TO CONTINUE")
        input()
        add()

    elif ch==10:
        print("VIEW ALL EMPLOYEE")
        time.sleep(1)
        print("ENTER ANY KEY TO CONTINUE")
        input()
        showall()

    elif ch==11:
        print("UPDATE AN EMPLOYEE")
        print("ENTER ANY KEY TO CONTINUE")
        input()
        update()

    elif ch==12:
        print("DELETE AN EMPLOYEE")
        time.sleep(1)
        print("ENTER ANY KEY TO CONTINUE")
        input() 
        delete()

    elif ch==13:
        print("SEARCH EMPLOYEES BY DEPARTMENT")
        time.sleep(1)
        print("ENTER ANY KEY TO CONTINUE")
        input()
        searchbydept()
    elif ch==14:
        print("SEARCH EMPLOYEES BY JOB")
        time.sleep(1)
        print("ENTER ANY KEY TO CONTINUE")
        input()
        searchbyjobid()
        

    elif ch==15:
        print("SERCH EMPLOYE BY EMPLOYEE ID:")
        time.sleep(1)
        print("ENTER ANY KEY TO CONTINUE")
        input()
        searchbyeno()

    elif ch==16:
        print(' '*50 , "RELAX AND LISTEN TO tere naino mein  !")
        time.sleep(1)
        print('''PRESS Y/YES TO PLAY MUSIC
                                   OR
                     PRESS ANY OTHER KEY  TO STOP MUSIC''')
        CH = input()
        if CH.lower() in  ['y','yes'] :
            mixer.music.play()
        else:
            mixer.music.stop()
            
    elif ch==0:
        print("ARE YOU SURE YOU WANT TO EXIT:")
        time.sleep(1)
        print("ENTER ANY KEY TO EXIT ")
        input()
        print("""                                                             ~~THANKYOU FOR USING APPLICATION~~
""")
        break
    elif ch==17:
        print("WELCOME IN ABOUT US SECTION ")
        time.sleep(1)
        print("AUTHORITY - SHREY OMER , ANUJ SONI , PAWAN GUPTA ")
        time.sleep(1)
        print("SPECIAL THANKS TO DHIRENDRA SIR AND SAIF CLASSES BANDA :")
        time.sleep(1)
        print(""" WE ARE UPCOMING FUTURE PROGRAMMERS FROM BANDA DISTRICT OF UTTAR PRADESH INDIA
                  WE DESIGNED THIS PROJECT TO MAKE EMPLOYEMENT MANAGEMENT EASY
                  IF YOU LIKED OUR WORK PLEASE RATE US AND GIVE US SUGGESTIONS TO IMPROVE THIS WORK YOUR INVOLVEMENT WILL BE RESPECTED """)
        time.sleep(1)
        CH=input(" DO YOU WISH TO  RATE US| ENTER Y OR YES ")
        if CH.lower() in ["y" ,"yes"]:
            
            M="""----------------------------
                    1 - ADD COMMENTS 
                    2 - SHOW ALL COMMENTS
                    3 - EXIT
                 ----------------------------
            """
            while 1:
                time.sleep(1)
                print(M)
                ch=int(input("ENTER YOUR CHOISE"))
                if ch==1:
                    
                    addcom()
                elif ch==2:
                    showcom()
                elif ch==3:
                    break
                else:
                    time.sleep(1)
                    print("ENTER VALID CHOISE")
        else:
             time.sleep(1)
             print("THANKS FOR USING THIS APPLICATION")
            
            
            
            
            
        
        
    else:
        print("PLEASE ENTER A VALID CHOISE BTWEEN =>[0-16] ")
        print("PRESS ANY KEY TO ENTER MAIN MENU")
        break

                                                    
              

#================================================================================ END OF CODE =================================================================================




