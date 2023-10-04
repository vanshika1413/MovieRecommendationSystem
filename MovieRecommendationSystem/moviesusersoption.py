def movieusers():
    import PySimpleGUI as sg
    import mysql.connector as mysql
    import moviesADMIN
    import signupADMIN
    sg.theme('Dark Brown')
    layout = [  
                [sg.Text('                                                                                                                   ')],
                [sg.Text('                                                                                                                   ')],
                [sg.Text('ADMIN LOGIN', font='Any 20')],
                [sg.Button('MOVIES', size=(20,1), font='Any 15', key='-MOVIES-'), sg.Button('USERS',size=(20,1),font='Any 15',key='-USERS-'),sg.Button('CANCEL',size=(20,1),font='Any 15',key='-CANCEL-')]
                
            ]
    window = sg.Window('ADMIN', layout, return_keyboard_events=True)
       
    while True:
        event, values = window.read()
        
        if event is None or event=='-CANCEL-':
            break
        if event=='-MOVIES-':
            moviesADMIN.movieEntry()
        elif event=='-USERS-':
            signupADMIN.doSignUp()
        
    window.close()
    del window
#movieusers()
