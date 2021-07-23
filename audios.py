import os


# Collecting the musics in the computer via the Downloads folder
directory = "C:\\Users\\User\\Downloads"
dir_audios = [i for i in os.listdir(directory) if '.mp3' in i]
paths = [os.path.abspath(os.path.join(directory, i)) for i in dir_audios]

# Classifing the musics into fours member groups
audios = list()
running = True
while running:
    audios.extend([dir_audios[0:4]])
    for i in dir_audios[0:4]:
        dir_audios.remove(i)
    if len(dir_audios) < 4:
        audios.extend([dir_audios])
        running = False
audios_index = 0
playing_audios = audios[audios_index]
