def signinsignupadmin():
    import pysimplepassword
    import PySimpleGUI as sg
    import mysql.connector as mysql
    sg.theme('Dark Brown')
   
    dont_open=False
    n=None
    layout = [  
                [sg.Text('                                                                                                                   ')],
                [sg.Text('                                                                                                                   ')],
                [sg.Text('     ADMIN SIGN-IN    ', font='Any 20')],
                [sg.Button('CANCEL', size=(20,1), font='Any 15', key='-CANCEL-'), sg.Button('SIGN-IN',size=(20,1),font='Any 15',key='-SIGNIN-')]
                
            ]
    window = sg.Window('Signin Signup', layout, return_keyboard_events=True)
    def getuser(pwd):
        
        u=''
        mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
        mycur=mydb.cursor()
        qry=("SELECT status FROM users WHERE password=%s")
        data=(pwd,)
        mycur=mydb.cursor()
        mycur.execute(qry, data)
        rows=mycur.fetchall()
        
        mydb.close()
        if len(rows)>0:
            adm=rows[0]
        return adm
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
    
    while True:
        event, values = window.read()
        
        if event is None or event=='-CANCEL-':
            dont_open=True
            n=None
            break
        if event=='-SIGNIN-':
            pdch,p=pysimplepassword.doSignIn()
            if pdch==True:
                n=getuser(p)
                n=n[0]
                print(n)
                dont_open=False
                break
        
    window.close()
    del window
    return n

#signinsignupadmin()
