def signinsignup():
    import pysimplepassword
    import PySimpleGUI as sg
    import mysql.connector as mysql
    import signup
    sg.theme('Dark Brown')
   
    dont_open=False
    n=None
    layout = [  
                [sg.Text('                                                                                                                   ')],
                [sg.Text('                                                                                                                   ')],
                [sg.Text('If you have an account click on Signin. Otherwise sign-up ', font='Any 20')],
                
                [sg.Button('CANCEL', size=(20,1), font='Any 15', key='-CANCEL-'), sg.Button('SIGN-IN',size=(20,1),font='Any 15',key='-SIGNIN-'), sg.Button('SIGN-UP', size=(20,1),font='Any 15',key='-SIGNUP-')]
                
            ]
    window = sg.Window('Signin Signup', layout, return_keyboard_events=True)
    def getuser(pwd):
        
        u=''
        mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
        mycur=mydb.cursor()
        qry=("SELECT emailadd FROM users WHERE password=%s")
        data=(pwd,)
        mycur=mydb.cursor()
        mycur.execute(qry, data)
        rows=mycur.fetchall()
        
        mydb.close()
        if len(rows)>0:
            u=rows[0]
        return u
    def checkpassword(pwd):
        pchecked=False
        con=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
        cur=con.cursor()
        cur.execute("Select name, emailadd, password from users")
        rows=cur.fetchall()
        Lpword=[]
        for row in rows:
            Lpword.append(str(row[2]))
        cur.close()
        con.close()
        if str(pwd) in Lpword:
                pchecked=True
        return pchecked
    
    import signup
    while True:
        event, values = window.read()
        
        if event is None or event=='-CANCEL-':
            n=''
            break
        if event=='-SIGNIN-':
            pdch,p=pysimplepassword.doSignIn()
            if pdch==True:
                n=getuser(p)
                n=n[0]
                break
        elif event=='-SIGNUP-':
            n=signup.doSignUp()

            if n!='':
                sg.popup('Sign in to continue \n\n', keep_on_top=True,font='Any 15')
                pdch,p= pysimplepassword.doSignIn()
                if pdch==True:
                    break
                else:
                    sg.popup('Password incorrect!!!!\n\n', keep_on_top=True,font='Any 15')
                    continue
            else:
                break
    
    window.close()
    del window
    return n

#signinsignup()
