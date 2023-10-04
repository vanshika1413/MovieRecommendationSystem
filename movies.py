def movieEntry():
        import PySimpleGUI as sg
        import mysql.connector as mysql
        import random
        from datetime import date
        sg.theme('Dark Brown')
        
        genrelist=[]
        langlist=[]
        mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
        mycur=mydb.cursor()
        genre=''
        mname=''
        lang=''
        duration=''
        rating=''
        descrip=''
        trailerlink=''
        releaseyear=''
        curdate =date.today()
        curdate=str(curdate)
        yyyy=int(curdate[:4])
        mm=int(curdate[5:7])
        dd=int(curdate[8:10])
        Randid=random.randint(10000, 1000000)
        getclicked=False
        mId=''

        def getmovies(mid):
                
                mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
                mycur=mydb.cursor()
                qry=("SELECT * FROM movies WHERE movieid= %s ")
                data=(mid,)
                mycur.execute(qry, data)
                rows=mycur.fetchall()
                mydb.close()
                
                if len(rows)==0:
                        return None, None, None, None, None
                for row in rows:
                        mId=str(row[0])
                        mname=str(row[1])
                        genre=str(row[2])
                        lang=str(row[3])
                        duration=str(row[4])
                        trailerlink=str(row[5])
                        releaseyear=str(row[6])
                        
                return mname, genre, lang, duration, trailerlink,releaseyear
        def clearfields():
                if getclicked==False:
                        window['-MID-'].update(visible=False)
                window['-MID-'].update('')
                window['-MNAME-'].update('')
                window['-GN-'].update('')
                window['-LANG-'].update('')
                window['-DUR-'].update('')
                window['-TL-'].update('')
                window['-RY-'].update('')
                   
        def insertinmovies(mname, genre, lang, duration, trailerlink,releaseyear):
                mid=mname[:5]+str(Randid)
                
                mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
                mycur=mydb.cursor()
                qry=("INSERT INTO movies (movieid,moviename,genre, lang,duration,trailerlink,releaseyear)VALUES(%s, %s, %s, %s, %s, %s,%s)")
                data=(mid,mname, genre,lang, duration, trailerlink, releaseyear)
                mycur.execute(qry,data)
                mydb.commit()
                qry2=("Select*from genres where genre=%s")
                data2=(genre,)
                mycur.execute(qry2,data2)
                rows=mycur.fetchall()
                if len(rows)==0:
                        gid=random.randint(100,10000)
                        gid=genre[0:2]+str(gid)
                        qry3=("Insert into genres(genreid,genre) values(%s,%s)")
                        data3=(gid,genre)
                        mycur.execute(qry3,data3)
                        mydb.commit()


                qry4=("Select*from lang where language=%s")
                data4=(lang,)
                mycur.execute(qry4,data4)
                rows=mycur.fetchall()
                if len(rows)==0:
                        lid=random.randint(100,10000)
                        lid=lang[0:2]+str(lid)
                        qry5=("Insert into lang(langid,language) values(%s,%s)")
                        data5=(lid,lang)
                        mycur.execute(qry5,data5)
                        mydb.commit()
                mydb.close()
                window['-MID-'].update(visible=True)
                window['-MID-'].update(mid)
                
                sg.popup("           One record inserted        Movie Id: ", mid,font='Any 15')
  
          
        def getlang():
                langlist.clear()
                mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
                mycur=mydb.cursor()
                qry=("SELECT distinct language FROM lang")
                mycur.execute(qry,)
                rows=mycur.fetchall()
                mydb.close()
                if len(rows)==0:
                    return None
                for row in rows:
                    langlist.append(row[0])
                return langlist
        def getgenres():
                mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
                mycur=mydb.cursor()
                genrelist.clear()
                qry=("SELECT distinct genre FROM genres")
                mycur.execute(qry,)
                rows=mycur.fetchall()
                mydb.close()
                if len(rows)==0:
                    return None
                for row in rows:
                    genrelist.append(row[0])
                return genrelist
        genrelist=getgenres()
        langlist=getlang()
        layout=[[sg.Text("Movie Entry", font='Any 25')],
                [sg.Text("Movieid     :", font='Any 14', size=(20,1)),  sg.Text('', size=(20,1), font='Any 14', visible=False, key='-MID-')],
                [sg.Text("Movie name  :", font='Any 14', size=(20,1)),  sg.Input('', size=(20,1), font='Any 14', key='-MNAME-')],
                [sg.Text("Genre       :", font='Any 14', size=(20,1)), sg.Combo(genrelist, size=(20,1), font='Any 14', key='-GN-')],
                [sg.Text("Language    :", font='Any 14', size=(20,1)), sg.Combo(langlist, size=(20,1), font='Any 14', key='-LANG-')],
                [sg.Text("Duration    :", font='Any 14', size=(20,1)), sg.Input('', size=(20,1), font='Any 14', key='-DUR-')],
                [sg.Text("Trailer link:", font='Any 14', size=(20,1)), sg.Input('', size=(20,1), font='Any 14', key='-TL-')],
                [sg.Text("Release year:", font='Any 14', size=(20,1)), sg.Input('', size=(20,1), font='Any 14', key='-RY-')],
                [sg.Button('SAVE', key='-SAVE-'), sg.Button('CANCEL', key='-CANCEL-')]
                ]
        window=sg.Window('movie entry', layout, finalize=True)
        x=0
        while True:
            window['-MID-'].update(visible=False)
            event, values=window.read()
                      
            if event is None or event=='-CANCEL-':
                x=0
                break  
            elif event=='-SAVE-':
                    window['-MID-'].update(visible=True)
                    mname=values['-MNAME-']
                    genre=values['-GN-']
                    lang=values['-LANG-']
                    duration=values['-DUR-']
                    trailerlink=values['-TL-']
                    releaseyear=values['-RY-']
                    insertinmovies(mname, genre, lang, duration, trailerlink,releaseyear)
                    clearfields()
                    continue
                    
            
                                     

        
        mycur.close()
        mydb.close()
        window.close()
        del window
        return x
            
#movieEntry()






