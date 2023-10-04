def moviereview(mname):
        from signup import doSignUp
        import signup
        import signinsignup
        import pysimplepassword
        import PySimpleGUI as sg
        from datetime import date
        import random
        import mysql.connector as mysql
        mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
        mycur=mydb.cursor()
        def getmovieid(movie):
                mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
                mycur=mydb.cursor()
                qry=("SELECT movieid FROM movies WHERE moviename= %s")
                data=(movie,)
                mycur.execute(qry, data)
                rows=mycur.fetchall()
                mydb.close()
                if len(rows)==0:
                        return 0
                else:
                        movieid=rows[0][0]
                        return movieid
                
        def insertmovie(movid=0, mname='', lang='',genre='', rev='', rating=0, user=''):
                
                curdate =date.today()
                curdate=str(curdate)
                yyyy=int(curdate[:4])
                mm=int(curdate[5:7])
                dd=int(curdate[8:10])
                revid=random.randint(10000, 1000000)
                revid=mname[0:5]+str(revid)
                mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
                mycur=mydb.cursor()
                qry=("INSERT INTO moviereview(revid,movieid, moviename, language, genre, review, rating,user ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)")
                data=(revid, movid, mname, lang, genre, rev, rating, user)
                mycur.execute(qry, data)
                mydb.commit()
                mydb.close()
                
        def getuser(u):
                
                mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
                mycur=mydb.cursor()
                qry=("SELECT * FROM users WHERE emailadd= %s or userid= %s")
                data=(u,u)
                mycur.execute(qry, data)
                rows=mycur.fetchall()
                mydb.close()
                if len(rows)==0:
                        return False
                else:
                        return True
        if type(mname)==list:
                movid=mname[0]
                movname=mname[1]
                movname=movname.upper()
                movlang=mname[2]
                movgenre=mname[3]
        else:
                movname=mname
        
        sg.ChangeLookAndFeel('Dark Brown')
        
        
        line1=[[sg.Text('Movie Name: ', justification ='left', size=(10,1), font='Any 20'), sg.Text('XXX', size=(30,1), font='Any 20',relief=sg.RELIEF_SUNKEN,key='-NAME-')]]
        line2=[[sg.Text('Language: ', justification ='left', size=(10,1), font='Any 20'), sg.Text('XXX', size=(30,1), font='Any 20',relief=sg.RELIEF_SUNKEN, key='-LANG-')]]
        line3=[[sg.Text('Genre: ', justification ='left', size=(10,1), font='Any 20'), sg.Text('XXX', size=(30,1), font='Any 20',relief=sg.RELIEF_SUNKEN, key='-GENRE-')]]
        line4=[[sg.Text('User id or email: ', justification ='left', size=(10,1), font='Any 20'), sg.Input('XXX', size=(30,1), font='Any 20', key='-USER-')]]
        reviewline=[[sg.Text('Review', size=(10,1), justification='left', font='Any 20')]]
        reviewbox=[[sg.MLine(default_text=' ', size=(100, 15),autoscroll=True, key='-REVIEW-')]]
        ratings=[[sg.Radio(u'\u2605','-RATINGS-', default=False, size=(10, 1), key='-R0-'), sg.Radio(u'\u2605'+u'\u2605', '-RATINGS-',default=False, size=(10,1), key='-R1-'), sg.Radio(u'\u2605'+u'\u2605'+u'\u2605', '-RATINGS-',default=False, size=(10,1), key='-R2-'),\
              sg.Radio(u'\u2605'+u'\u2605'+u'\u2605'+u'\u2605','-RATINGS-', default=False, size=(10, 1), key='-R3-'),sg.Radio(u'\u2605'+u'\u2605'+u'\u2605'+u'\u2605'+u'\u2605','-RATINGS-', default=False, size=(10, 1), key='-R4-') ]]
        buttons=[[sg.Text('', size=(15,1)),sg.Button('  Done  ', size=(10,1),font='Any 20', key='-DONE-'), sg.Button('Cancel', size=(10,1), font='Any 20', key='-CANCEL-')]]
        col=line1+line2+line3+line4+reviewline+reviewbox+ratings+buttons
             
        
                     
        layout=[[sg.Text('WRITE REVIEW',justification='center', size=(11,1), font='Any 20')],
                [sg.Column(col)]
               ]
        window = sg.Window('WRITE REVIEW WINDOW', layout, font='Courier 12', finalize=True)
        window['-NAME-'].update(movname)
        window['-LANG-'].update(movlang)
        window['-GENRE-'].update(movgenre)
                     
    
        while True:
                event, values = window.read()
                if event is None or event=='-CANCEL-':
                        break
                elif event=='-GENRELIST-':
                    genre=values['-GENRELIST-']
                    window['-GENRE-'].update(genre)
                elif event=='-LANGLIST-':
                    lang=values['-LANGLIST-']
                    window['-LANG-'].update(lang)
                elif event=='-DONE-':
                    mname=movname
                    lang=movlang
                    genre=movgenre
                    rev=values['-REVIEW-']
                    r=False
                    for i in range(5):
                        r=values['-R'+str(i)+'-']
                        if r==True:
                            rating=i+1
                            break
                    if r==False:
                        g=sg.popup_yes_no('You have not entered the rating \n Do you want to add rating?',font='Any 15')
                        if g=="Yes":
                                sg.popup_auto_close('You can rate the movie in a second....', button_type=5,font='Any 15')
                                continue
                        else:
                                rating=0
                                             
                    user=values['-USER-']
                    
                    if getuser(user):
                            if not (len(mname)==0 or len(lang)==0 or len(genre)==0 or len(rev)==0):
                                    insertmovie(movid, mname, lang,genre[0], rev, rating, user)
                                    break
                            else:
                                    sg.popup("     Please enter all fields   ",font='Any 15')
                    else:
                            user=signinsignup.signinsignup()
                            print(user)
                            if user=='':
                                    break
                            else:

                                    #user=user[0]
                                    window['-USER-'].update(user)
                                    insertmovie(movid, mname, lang, genre[0], rev, rating, user)
                                    break
                            
            
        window.close()
        del window
                
