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
        
                
        def insertinusers(name, emailadd, password):
                status='USER'
                mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
                mycur=mydb.cursor()
                qry=("INSERT INTO users (userid,name, emailadd, password,status,cdate)VALUES(%s, %s, %s, %s, %s, %s)")
                uid=name+str(Randid)
                data=(uid,name,emailadd, password, status, date(yyyy,mm,dd))
                mycur.execute(qry,data)
                mydb.commit()
                mycur.close()
                mydb.close()
                window['-UID-'].update(visible=True)
                window['-UID-'].update(uid)
                sg.popup("           One record inserted. PLease note down id         ",keep_on_top=True, font='Any 15')
                               
        def clearfields():
                window['-UID-'].update('')
                window['-NAME-'].update('')
                window['-EM-'].update('')
                window['-PWD1-'].update('')
                window['-PWD-'].update('')

        layout=[[sg.Text("SIGN UP FORM", font='Any 25')],
                [sg.Text("Id     :", font='Any 14', size=(20,1)),  sg.Text('', size=(20,1), font='Any 14',visible=False, key='-UID-')],
                [sg.Text("Name       :", font='Any 14', size=(20,1)),  sg.Input('', size=(20,1), font='Any 14', key='-NAME-')],
                [sg.Text("Email      :", font='Any 14', size=(20,1)), sg.Input('', size=(20,1), font='Any 14', key='-EM-')],
                [sg.Text("Password   :", font='Any 14', size=(20,1)), sg.Input('', size=(20,1), font='Any 14', key='-PWD1-')],
                [sg.Text("Confirm Password:", font='Any 14', size=(20,1)), sg.Input('', size=(20,1), font='Any 14', key='-PWD-')],
                [sg.Button('SAVE', key='-SAVE-'), sg.Button('CANCEL', key='-CANCEL-')]
                ]
        window=sg.Window('Sign Up Form', layout, keep_on_top=True)
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
                    insertinusers(name, email, password)
                    clearfields()
                    x=email
                    break
        
        window.close()
        del window
        return x
#doSignUp()
