def doSignIn():
    
    import PySimpleGUI as sg
    import mysql.connector as mysql
    con=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
    cur=con.cursor()
    cur.execute("Select password, emailadd from users")
    rows=cur.fetchall()
    Lpword=[]
    Lemail=[]
    for row in rows:
        Lpword.append(str(row[0]))
        Lemail.append(str(row[1]))
    cur.close()
    con.close()
    pchecked=False
    layout = [  [sg.Text('Password Entry')],
                [sg.Input(key='-IN-')],
                [sg.Button('EXIT', size=(20,1), font='15,1',key='-EXIT-'), sg.Button('OK',size=(20,1), font='15,1', key='-OK-')],
                [sg.Checkbox('SHOW PASSWORD',size=(20,1), font='15,1', enable_events=True, key='-SHOWPWD-')]
            ]
    window = sg.Window('Password Entry', layout, return_keyboard_events=True)
    s=''
    p=''
    curpos=0
    chrs=0
    pwd=''
    user=''
    message='Capslock is on'
    showpwd=False
    while True:
        event, values = window.read()
    
        if event=='\r' or event=='-OK-':
            if str(s) in Lpword or str(s) in Lemail:
                pchecked=True
                sg.popup('SIGN IN SUCCESSFUL',font='Any 15')
                break
            else:
                sg.popup('WRONG PASSWORD!!!!                    \n\n',font='Any 15')
                pchecked=False
                break   
        if event in (None, '-EXIT-'):      
            break
        if event=='BackSpace:8':
            if chrs==0:
                continue
            elif curpos==chrs:
                s=s[:-1]
                p=p[:-1]
                curpos=curpos-1
                chrs=chrs-1
                
            elif curpos!=chrs:
                s=s[:curpos-1]+s[curpos:]
                p=p[:curpos-1]+p[curpos:]
                curpos=curpos-1
                chrs=chrs-1
        elif event in ['Shift_L:16','Shift_R:17']:
           s=s[:]
           p=p[:]
           chrs=chrs+1
            
        elif event == 'Left:37':
            if curpos==0:
                continue
            else:
                curpos=curpos-1
         
        elif event=='Right:39':
            if curpos==chrs:
                continue
            else:
                curpos=curpos+1
        elif event in ['Up:38', 'Down:40']:   
            continue
        elif event =='Caps_Lock:20':
            continue
        elif event=='Delete:46':
            if curpos==0 and chrs==0:
                continue
            s=s[:curpos]+s[curpos+1:]
            p=p[:-1]
            chrs=chrs-1
        elif event=='-SHOWPWD-':
            if showpwd==False:
                window['-IN-'].update(s)
                showpwd=True
            else:
                window['-IN-'].update(p)
                showpwd=False
        elif values['-SHOWPWD-']==True:
            s=s+values['-IN-'][-1]
            p=p+'*'
            curpos=curpos+1
            chrs=chrs+1
            window['-IN-'].update(s)
        
        else:
            s=s+values['-IN-'][-1]
            p=p+'*'
            curpos=curpos+1
            chrs=chrs+1
            window['-IN-'].update(p)
    window.close()
    del window
    return pchecked,s
#doSignIn()
