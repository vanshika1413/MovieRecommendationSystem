def doSignUp():
        import PySimpleGUI as sg
        import mysql.connector as mysql
        import random
        from datetime import date
        sg.theme('Dark Brown')
        
        
        mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
        mycur=mydb.cursor()
        name=''
        em=''
        pwd1=''
        pwd=''
        stat=''
        curdate=date.today()
        curdate=str(curdate)
        yyyy=int(curdate[:4])
        mm=int(curdate[5:7])
        dd=int(curdate[8:10])
        Randid=random.randint(10000, 1000000)
        getclicked=False
        uId=''

        def getuser(email):
                
                mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
                mycur=mydb.cursor()
                qry=("SELECT * FROM users WHERE emailadd= %s ")
                data=(email,)
                mycur.execute(qry, data)
                rows=mycur.fetchall()
                mydb.close()
                
                if len(rows)==0:
                        return None, None, None, None, None
                for row in rows:
                        uId=str(row[0])
                        name=str(row[1])
                        em=str(row[2])
                        pwd=str(row[3])
                        stat=str(row[4])
                        
                return uId, name, em, pwd, stat
                
        def insertinusers(name, emailadd, password):
            status='ADMIN'    
            mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
            mycur=mydb.cursor()
            qry=("INSERT INTO users (userid,name, emailadd, password,status,cdate)VALUES(%s, %s, %s, %s, %s, %s)")
            uid=name+str(Randid)
            
            data=(uid,name,emailadd, password, status, date(yyyy,mm,dd))
            mycur.execute(qry,data)
            mydb.commit()
            mydb.close()
            window['-UID-'].update(visible=True)
            window['-UID-'].update(uid)
            sg.popup("           One record inserted. PLease note down your id and email id       ",keep_on_top=True,font='Any 15')
                   
        def updateusers(name,em, pwd, stat, uid):
                stat=stat.upper()
                mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
                mycur=mydb.cursor()
                qry=("UPDATE users SET name=%s, emailadd=%s, password=%s, status=%s WHERE userid=%s ")
                data=(name,em, pwd, stat, uid)
                mycur.execute(qry,data)
                mydb.commit()
                mydb.close()
                sg.popup("       One record updated         ",font='Any 15')
        
        def deleteusers(email):
                mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
                mycur=mydb.cursor()
                qry=("DELETE FROM users WHERE emailadd = %s")
                data=(email,)
                mycur.execute(qry, data)
                mydb.commit()
                rows=mycur.rowcount
                mydb.close()
                
                sg.popup("One record deleted",font='Any 15')
        def clearfields():
                window['-UID-'].update('')
                window['-NAME-'].update('')
                window['-EM-'].update('')
                window['-PWD1-'].update('')
                window['-PWD-'].update('')
                

        layout=[[sg.Text("ADMIN SIGN UP FORM", font='Any 25')],
                [sg.Text("Id     :", font='Any 14', size=(20,1)),  sg.Input('', size=(20,1), font='Any 14', key='-UID-')],
                [sg.Text("Name       :", font='Any 14', size=(20,1)),  sg.Input('', size=(20,1), font='Any 14', key='-NAME-')],
                [sg.Text("Email      :", font='Any 14', size=(20,1)), sg.Input('', size=(20,1), font='Any 14', key='-EM-')],
                [sg.Text("Password   :", font='Any 14', size=(20,1)), sg.Input('', size=(20,1), font='Any 14', key='-PWD1-')],
                [sg.Text("Confirm Password:", font='Any 14', size=(20,1)), sg.Input('', size=(20,1), font='Any 14', key='-PWD-')],
                [sg.Button('SAVE', key='-SAVE-'), sg.Button('CANCEL', key='-CANCEL-'), sg.Button('GET', key='-GET-'), sg.Button('DELETE', key='-DELETE-')]
                ]
        window=sg.Window('Sign Up Form', layout)
        x=0
        while True:
            event, values=window.read()
            
            if event is None or event=='-CANCEL-':
                x=''
                break  
            elif event=='-SAVE-':
                    name=values['-NAME-']
                    email=values['-EM-']
                    password=values['-PWD-']
                    if getclicked==False:
                            insertinusers(name, email, password)
                    else:
                            id=values['-UID-']
                            updateusers(name, email, password, id)
                            getclicked=False
                           
                    clearfields()
                    x=email
                    break
            elif event=='-GET-':
                    getclicked=True
                    email=values['-EM-']
                    uid, name,emailadd, password, status=getuser(email)
                    if uid==None:
                            sg.popup("No matching record", keep_on_top=True,font='Any 15')
                            clearfields()
                
                    else:
                            window['-UID-'].update(uid)    
                            window['-NAME-'].update(name)
                            window['-EM-'].update(emailadd)
                            window['-PWD1-'].update(password)
                            
                    x=1

            elif event=='-DELETE-':
                    email=values['-EM-']
              
                    butn=sg.popup_yes_no("Do you wish to delete the record?",keep_on_top=True,font='Any 15')
                    
                    if butn=='Yes':
                            deleteusers(email)
                            sg.popup("Proceeding to delete",keep_on_top=True,font='Any 15')
                    clearfields()
                    x=1
        
        mycur.close()
        mydb.close()
        window.close()
        del window
        return x
#doSignUp()
