import PySimpleGUI as sg
import webbrowser
def info(mname,lang, genre, dur, trailerlink,ryear):
    sg.ChangeLookAndFeel('Dark Brown')
    
    line1=[[sg.Text('Movie Name: ', justification ='left', size=(20,1), font='Any 20'), sg.Text('XXX', size=(70,1), font='Any 15',relief=sg.RELIEF_SUNKEN,key='-NAME-')]]
    line2=[[sg.Text('Language: ', justification ='left', size=(20,1), font='Any 20'), sg.Text('XXX', size=(70,1), font='Any 15',relief=sg.RELIEF_SUNKEN,key='-LANG-')]]
    line3=[[sg.Text('Genre: ', justification ='left', size=(20,1), font='Any 20'), sg.Text('XXX', size=(70,1), font='Any 15',relief=sg.RELIEF_SUNKEN, key='-GENRE-')]]
    line4=[[sg.Text('Duration in hours: ', justification ='left', size=(20,1), font='Any 20'), sg.Text('XXX', size=(70,1), font='Any 15',relief=sg.RELIEF_SUNKEN, key='-DURATION-')]]
    line5=[[sg.Text('Trailer Link: ', justification ='left', size=(20,1), font='Any 20'), sg.Text('XXX', size=(70,1), font='Any 15',relief=sg.RELIEF_SUNKEN, key='-TRAILERLINK-', enable_events=True)]]
    line6=[[sg.Text('Release Year: ', justification ='left', size=(20,1), font='Any 20'), sg.Text('XXX', size=(70,1), font='Any 15',relief=sg.RELIEF_SUNKEN, key='-RELEASEYEAR-')]]
    
    buttons=[[sg.Text('                               ', size=(15,1)),sg.Button('    Done     ', size=(20,1),font='Any 20', key='-DONE-')]]
    col=line1+line2+line3+line4+line5+line6+buttons
                                                                                    
    layout=[[sg.Text('Movie Information',justification='center', size=(40,1), font='Any 35')],
            
            [sg.Column(col)]
            ]
    window = sg.Window('Movie Info', layout, font='Courier 12', finalize=True)
    window['-NAME-'].update(mname)
    window['-LANG-'].update(lang)
    window['-GENRE-'].update(genre)
    window['-DURATION-'].update(dur)
    window['-TRAILERLINK-'].update(trailerlink)
    window['-RELEASEYEAR-'].update(ryear)
    
    while True:
        event, values = window.read()
        
        if event is None:
            break
        
        elif event=='-DONE-':
            break
        elif event =='-TRAILERLINK-':
            window['-TRAILERLINK-'].update(text_color=('green'))
            webbrowser.open_new(trailerlink)
    window.close()
    del window
