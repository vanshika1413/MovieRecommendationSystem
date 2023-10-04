import PySimpleGUI as sg
import mysql.connector as mysql
import moviereviewwrite as mrvwrite
import moviereviewread as mrvread
import movies
import signinsignup
import signup
import pysimplepassword
import movieinfo
import adminsigninsignup
import moviesusersoption
sg.ChangeLookAndFeel('Dark Brown')

def domain():
    movlist=[]
    L2=[]
    langlist=[]
    outputlist=[]
    genrelist=[]
    retlist=[]
    topmovies=[]
    movieid=0
    movie=''
    lang=''
    genre=''
    review=''
    user=''

    def gettopmovies():
        topmovies=[]
        mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
        mycur=mydb.cursor()
        qry=("select moviename, max(rating) as 'Highest rating' from moviereview group by moviename having count(rating)>=4")
        mycur.execute(qry)
        rows=mycur.fetchall()
        mydb.close()
        mycur.close()
        templist=[]
        if len(rows)==0:
            return topmovies
        else:
            x=1
            for row in rows:
                templist.append((row[0]))
                templist.append((row[1]))
                topmovies.append(templist)
                templist=[]
                if x>=5:
                    break
                x=x+1
        return topmovies
        
    def showmovies():
        outputlist=[]
        mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
        mycur=mydb.cursor()
        qry=("SELECT m.movieid, m.moviename, m.lang, m.genre FROM movies m, moviereview mr where m.movieid=mr.movieid group by mr.movieid")
        mycur.execute(qry)
        rows=mycur.fetchall()
        mydb.close()
        Vlist=[]
        if len(rows)==0:
            return outputlist
        Vlist=[]
        x=1
        for row in rows:
            Vlist.append((row[0]))
            Vlist.append((row[1]))
            Vlist.append((row[2]))
            Vlist.append((row[3]))
            outputlist.append(Vlist)
            Vlist=[]
            if x>=10:
                break
            x=x+1
        return outputlist
    
    def checkmovie(movie):
        
        mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
        mycur=mydb.cursor()
        qry=("SELECT movieid,lang, genre,duration, trailerlink, releaseyear  FROM movies WHERE moviename= %s")
        data=(movie,)
        mycur=mydb.cursor()
        mycur.execute(qry, data)
        rows=mycur.fetchall()
        mydb.close()
        if len(rows)==0:
            return ''
        for row in rows:
            mid=row[0]
            lang=row[1]
            genre=row[2]
            duration=row[3]
            trailerlink=row[4]
            releaseyear=row[5]
        return mid, lang, genre, duration, trailerlink, releaseyear
    def getmovies(gen='', lang=''):
        print(gen, lang)
        L=[]
        mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
        mycur=mydb.cursor()
        if gen=='-NONE-' and lang=='-NONE-':
            print("Hello")
            qry=("SELECT movieid, moviename, lang, genre FROM movies ")
            mycur.execute(qry,)
            rows=mycur.fetchall()
            mydb.close()
        elif (len(gen)==0 or gen=='-NONE-') and len(lang)>=1:
            print("Yeeesssssss")
            qry=("SELECT movieid, moviename, lang, genre FROM movies WHERE lang= %s")
            data=(lang,)
            mycur.execute(qry, data)
            rows=mycur.fetchall()
            mydb.close()
        elif (len(lang)==0 or gen=='-NONE-')  and len(gen)>=1:
            print("Wohooo")
            qry=("SELECT movieid, moviename, lang, genre FROM movies WHERE genre= %s")
            data=(gen,)
            mycur.execute(qry, data)
            rows=mycur.fetchall()
            mydb.close()
        elif len(gen)>=1 and len(lang)>=1:
            print("This is the problem")
            qry=("SELECT movieid, moviename, lang, genre FROM movies WHERE genre= %s and lang= %s")
            data=(gen,lang)
            mycur.execute(qry, data)
            rows=mycur.fetchall()
            mydb.close()
        
        print(len(rows))
        Vlist=[]
        if len(rows)==0:
            return ''
        x=1
        for row in rows:
            Vlist.append(row[0])
            Vlist.append(row[1])
            Vlist.append(row[2])
            Vlist.append(row[3])
            L.append(Vlist)
            Vlist=[]
            if x>=10:
                break
            x+=1
            
        return L
      
    def getreview(mname):
        revw=()
        rating=()
        user=()
        mydb=mysql.connect(host="localhost",user="root", password="vanshi14",database="911movies")
        mycur=mydb.cursor()
        qry1=("SELECT review FROM moviereview WHERE moviename= %s")
        data1=(mname,)
        mycur.execute(qry1, data1)
        rows1=mycur.fetchall()
        qry2=("SELECT rating FROM moviereview WHERE moviename= %s")
        data2=(mname,)
        mycur.execute(qry2, data2)
        rows2=mycur.fetchall()
        qry3=("SELECT user FROM moviereview WHERE moviename= %s")
        data3=(mname,)
        mycur.execute(qry3, data3)
        rows3=mycur.fetchall()
        mydb.close()
        if len(rows1)==0:
            return 
        for r in range(len(rows1)):
            revw=revw+rows1[r]
        for i in range(len(rows2)):
            rating=rating+rows2[i]
        for i in range(len(rows3)):
            user=user+rows3[i]
    
        return revw, rating, user
    
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
    def clearmovielist():
        m=0
        for x in range(10): 
            for y in range(4):
                window[y,m].update('')
            m=m+1

    def updatemovielist():
        m=0
        for x in range(len(outputlist)): 
            for y in range(4):
                window[y,m].update(outputlist[x][y])
                L2.append((y,m))
            m=m+1
    def updatetop5():
        n=0
        i=0
        for x in range(len(topmovies)): 
            for y in range(200000,200002):

                window[y,n].update(topmovies[x][i])
                i=i+1
            if(n>=5):
                break
            n=n+1
            i=0
    topmovies=gettopmovies()
    outputlist=showmovies()
    r=0
    q=0
    if not len(outputlist)==0:
        r=len(outputlist)
    if not len(topmovies)==0:
        q=len(topmovies)
    getlang()
    getgenres()
    genrelist=['-NONE-']+ genrelist
    langlist=['-NONE-']+langlist
    colGenre=[[sg.Text('Enter the Genre', font='Any 10')],
            [sg.Combo(genrelist, size=(15,1), font='Any 10',background_color='black',key='-GENRE-')]]
    colLang=[[sg.Text('Enter the Language', font='Any 10')],
            [sg.Combo(langlist, size=(15, 1), font='Any 10',background_color='black',key='-LANGUAGE-')]]
    buttons=[[sg.Button('Show', size=(12,1),font='Any 15', key='-SHOW-'),sg.Button("Read Review", size=(12,1), font='Any 15', key='-READREVIEW-'),sg.Button("Write Review", size=(12,1), font='Any 15', key='-WRITEREVIEW-'),sg.Button('Cancel', size=(12,1),font='Any 15', key='-CANCEL-'), sg.Button('ADMIN',size=(12,1),font='Any 15', key='-ADMIN-')]]
    headings = ['MOVIEID' ,'MOVIENAME', 'LANGUAGE','GENRE']
    header =  [[sg.Text('  ' + h, size=(25,1),font='Any 10',pad=(0,0),relief=sg.RELIEF_SUNKEN) for h in headings]]
    rows = [[sg.Text('  ', size=(25,1), font='Any 10', pad=(0,0),relief=sg.RELIEF_SUNKEN,key=(i,j), enable_events=True) for i in range(4)] for j in range(10)]
    headingstop5=['Top Movies', 'Max Rating']
    headertop5=[[sg.Text('  ' + h, size=(50,1),font='Any 10',pad=(0,0),relief=sg.RELIEF_SUNKEN) for h in headingstop5]]
    top5=[[sg.Text('  ', size=(50,1), font='Any 10', pad=(0,0), justification='c', key=(i,j),relief=sg.RELIEF_SUNKEN) for i in range(200000, 200002)] for j in range(5)]
    
    topmost=[[sg.Listbox(topmovies, size=(75, len(topmovies)), font='Any 15',background_color='black',key='-TOPMOVIES-', enable_events=True)]]
    
    headingtopmost=[[sg.Text('Top Movies based on Rating', size=(30,1), font='Any 15')]]
    
    col=header+rows + headingtopmost+ headertop5 + top5+ buttons
    
    layout=[[sg.Text('911MOVIES', size=(20,1), font='Any 20'),sg.Image(filename='logo.PNG', size=(150,150))],
            [sg.Text('Enter Movie name to read or write reviews: ', size=(40,1),  font='Any 10')],
            [sg.Input('', size=(50,1), font='Any 10',key='-MOVIENAME-'),sg.Button("Check", size=(12,1), font='Any 15', key='-CHECK-')],
            [sg.Column(colGenre), sg.Column(colLang)],
    
                  
            [sg.Text('Movies reviewed! Click on Movie name to read or write review', size=(50,1), font='Any 10', key='-MOVIESLISTLABEL-')],
            [sg.Column(col)],
            [sg.Text("                                       ", size=(50,1), font='Any 10', key='-STATUS-')]
            ]
    
    window = sg.Window('911Movies', layout, font='Courier 12', finalize=True)
    updatemovielist()
    updatetop5()
    yval=0
    while True:
        event, values = window.read()
        if event is None or event=='-CANCEL-':
            break
                       
        elif event=='-SHOW-':
            genre=values['-GENRE-']
            lang=(values['-LANGUAGE-'])
            if(len(genre)==0 and len(lang)==0):
                sg.popup("Select genre or language from the appropriate list boxes.",font='Any 10')
                continue
            else:
                outputlist=getmovies(genre, lang)
                print(genre, lang)
                if len(outputlist)==0:
                    sg.popup("No movies matching the genre and language selected",font='Any 10')
                    continue
                else:
                    sg.popup("Showing movies with the selected genre and language",font='Any 10')
                    clearmovielist()
                    updatemovielist()
                    r=len(outputlist)
                    continue
        
        elif event=='-CHECK-':
            movie=values['-MOVIENAME-']
            if len(movie)==0:
                sg.popup("Invalid entry or blank.\nPlease enter movie in database,font='Any 10'")
                continue
            elif checkmovie(movie)=='':
                sg.popup("This movie does not exist in the database!\nPlease enter movie in database",font='Any 10')
                try:
                    movies.movieEntry()
                    movieid, lang, genre, duration, trailerlink, releaseyear=checkmovie(movie)
                    window['-LANGUAGE-'].update(lang)
                    window['-GENRE-'].update(genre)
                    movlist=[ movieid, values['-MOVIENAME-'],lang, genre]
                except:
                    sg.popup_auto_close("Operation canceled or failed!")
            else:
                movieid, lang, genre, duration, trailerlink, releaseyear=checkmovie(movie)
                window['-LANGUAGE-'].update(lang)
                window['-GENRE-'].update(genre)
                movlist=[ movieid, values['-MOVIENAME-'],lang, genre]
                
                movieinfo.info(movie,lang, genre,  duration, trailerlink, releaseyear)
                
        elif event=='-READREVIEW-':
            movie=values['-MOVIENAME-']
            if not (movieid==0 and movie=='' and lang=='' and genre==''):
                    movlist=[movieid, movie,lang, genre]
            if len(movie)>0 or len(movlist)>0:
                if getreview(movie) is None:
                    sg.popup("No reviews available for this movie.",font='Any 10')
                    movie=''
                    continue
                else:
                    movlist=[ movieid, movie,lang, genre]
                    rewu, rating,user=getreview(movie)
                    mrvread.moviereview(movlist,rewu, rating,user)
                    window[(1,yval)].update(text_color=('khaki'))
                    movlist=[]
                    yval=0
               

            else:
                sg.popup_auto_close("Please enter movie name or select movie from the list of movies", font='Any 10')
            movlist=[]
        elif event=='-WRITEREVIEW-':
                movie=values['-MOVIENAME-']
                if not (movieid==0 and movie=='' and lang=='' and genre==''):
                    movlist=[movieid, movie,lang, genre]
                if len(movlist)>0 or len(movie)>0:
                    mrvwrite.moviereview(movlist)
                    outputlist=showmovies()
                    if not len(outputlist)==0:
                        r=len(outputlist)
                    updatemovielist()
                    window[(1,yval)].update(text_color=('khaki'))
                    movlist=[]
                    yval=0
                else:
                   sg.popup("Please enter movie name or select movie from list ", font='Any 10')
                movlist=[]       
        elif event in L2:
            w=str(event)
            x=int(w[1:2])
            y=int(w[4:5])
            movieid=(outputlist[y][0])       
            movie=(outputlist[y][1])
            lang=(outputlist[y][2])
            genre=(outputlist[y][3])
            movlist.append(movieid)
            movlist.append(movie)
            movlist.append(lang)
            movlist.append(genre)
            window['-STATUS-'].update(movie)
            window['-MOVIENAME-'].update(movie)
            window['-GENRE-'].update(genre)
            window['-LANGUAGE-'].update(lang)
            window[1,y].update(text_color=('red'))
            if y!=yval:
                window[1,yval].update(text_color=('khaki'))
            yval=y
        elif event=='-ADMIN-':
            stat=adminsigninsignup.signinsignupadmin()
            if stat=='ADMIN' or stat=='admin' or stat=='Admin':
                moviesusersoption.movieusers()
                continue
        
    window.close()
    del window
if __name__=='__main__':
    domain()

'''
sg.popup("The details of this movie:                 \nDuration: ", duration, "\nTrailerlink: ",
                         trailerlink, "\nRelease year: ", releaseyear, font='Any 15')
'''
