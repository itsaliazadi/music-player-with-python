import os
import pygame
import pygame.mixer
from tkinter import *
from tkinter import Tk

directory = "C:\\Users\\User\\Downloads"
audios = [i for i in os.listdir(directory) if '.mp3' in i]
paths = [os.path.abspath(os.path.join(directory, i)) for i in audios]


new_audios = list()
running = True
while running:
    new_audios.extend([audios[0:4]])
    for i in audios[0:4]:
        audios.remove(i)
    if len(audios) < 4:
        new_audios.extend([audios])
        running = False
new_audios_index = 0
playing_audios = new_audios[new_audios_index]


def open_music_player() :
    screen = Tk()
    pygame.mixer.init()

    def resume_the_audio() :

        if pygame.mixer.music.get_busy() :
            pygame.mixer.music.pause()
            resume = Button(screen, text='resume', height=3, width=10, bg='red',command=create_stop_button)
            resume.place(x=200, y=480)

    def create_stop_button() :

        pygame.mixer.music.unpause()
        stop = Button(screen, text='||', height=3, width=10, bg='red', command=resume_the_audio)
        stop.place(x=200, y=480)

    def play_the_audio(audio) :

        while pygame.mixer.music.get_busy():
            pass
        pygame.mixer.music.load(open(audio, 'rb'))
        pygame.mixer.music.play()

    def handle_the_audio(audio_name) :

        for i in paths:
            if audio_name in i:
                play_the_audio(i)
                create_stop_button()
                mainloop()

    def make_buttons(window,files) :

        try :
            audio_1 = Button(window,text=files[0],height=4,width=40,bg='magenta',command=lambda : handle_the_audio(files[0]))
            audio_1.config(font=("Cooper Black",10))
            audio_1.place(x=65,y=160)
        except :
            pass

        try :
            audio_2 = Button(window,text=files[1],height=4,width=40,bg='magenta',command=lambda : handle_the_audio(files[1]))
            audio_2.config(font=("Cooper Black",10))
            audio_2.place(x=65,y=240)
        except :
            pass

        try :
            audio_3 = Button(window,text=files[2],height=4,width=40,bg='magenta',command=lambda : handle_the_audio(files[2]))
            audio_3.config(font=("Cooper Black", 10))
            audio_3.place(x=65,y=320)
        except :
            pass

        try :
            audio_4 = Button(window,text=files[3],height=4,width=40,bg='magenta',command=lambda : handle_the_audio(files[3]))
            audio_4.config(font=("Cooper Black", 10))
            audio_4.place(x=65,y=400)
        except :
            pass

        def open_the_next_window() :

            for i in screen.winfo_children() :
                i.destroy()
            if pygame.mixer.music.get_busy() :
                pygame.mixer.music.pause()
            for i in new_audios  :
                if files[len(files) - 1] in i :
                    try :
                        make_buttons(screen,new_audios[new_audios.index(i)+1])
                    except :
                        pass
                    
        next_page = Button(screen,text='next page',height=3,width=10,bg='green',command=open_the_next_window)
        next_page.place(x=120,y=480)

        def open_the_previous_window() :

            for i in screen.winfo_children() :
                i.destroy()
            if pygame.mixer.music.get_busy() :
                pygame.mixer.music.pause()
            for i in new_audios :
                if files[len(files) - 1] in i :
                    try :
                        make_buttons(screen,new_audios[new_audios.index(i)-1])
                    except :
                        pass

        previous_page = Button(screen,text='previous page',height=3,width=10,bg='green',command=open_the_previous_window)
        previous_page.place(x=280,y=480)
    def make_label() :

        screen.geometry("500x600")
        guide_message = "Choose your favourite music!"
        guide = Label(screen,text=guide_message,bg='cyan')
        guide.config(width=50,height=5)
        guide.config(font=("Arial CYR",10))
        guide.pack()

        make_buttons(screen,playing_audios)
        screen.mainloop()

    make_label()

open_music_player()



