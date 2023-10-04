import PySimpleGUI as sg
from datetime import date
import random
import mysql.connector as mysql
def moviereview(mname, rev, rt,u):
    movid=mname[0]
    movname=mname[1]
    movname=movname.upper()
    movlang=mname[2]
    movgenre=mname[3]
    movreview=''
    
    for i in range(len(rev)):
        movreview=movreview+str(i+1) + "." +"\n"+str(rev[i])+"Rating:"
        for j in range(rt[i]):
            movreview=movreview+ u'\u2605'
        movreview=movreview+"\tReviewer:  " + str(u[i])
        movreview=movreview+"\n\n"
        
    
    mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
    mycur=mydb.cursor()
    sg.ChangeLookAndFeel('Dark Brown')
    line1=[[sg.Text('Movie Name: ', justification ='left', size=(10,1), font='Any 17'), sg.Text('XXX', size=(30,1), font='Any 17',relief=sg.RELIEF_SUNKEN,key='-NAME-')]]
    line2=[[sg.Text('Language: ', justification ='left', size=(10,1), font='Any 17'), sg.Text('XXX', size=(30,1), font='Any 17',relief=sg.RELIEF_SUNKEN,key='-LANG-')]]
    line3=[[sg.Text('Genre: ', justification ='left', size=(10,1), font='Any 17'), sg.Text('XXX', size=(30,1), font='Any 17',relief=sg.RELIEF_SUNKEN, key='-GENRE-')]]
    reviewline=[[sg.Text('Review', size=(10,1), justification='left', font='Any 17')]]
    reviewbox=[[sg.MLine(default_text=' ', size=(65, 20),autoscroll=True, disabled=True, key='-REVIEW-')]]
    buttons=[[sg.Text('', size=(15,1)),sg.Button('  Done  ', size=(20,1),font='Any 17', key='-DONE-')]]
    col=line1+line2+line3+reviewline+reviewbox+buttons
                                                                                    
    layout=[[sg.Text('READ REVIEWS',justification='center', size=(40,1), font='Any 35')],
            [sg.Column(col)]
            ]
    window = sg.Window('READ REVIEWS WINDOW', layout, font='Courier 12', finalize=True)
    window['-NAME-'].update(movname)
    window['-LANG-'].update(movlang)
    window['-GENRE-'].update(movgenre)
    window['-REVIEW-'].update(movreview)
    while True:
        event, values = window.read()
        
        if event is None:
            break
        elif event=='-GENRELIST-':
            genre=values['-GENRELIST-']
        elif event=='-DONE-':
            break
    window.close()
    del window
