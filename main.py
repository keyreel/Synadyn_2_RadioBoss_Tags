import configparser
import os
import pathlib

import mutagen
from mutagen.apev2 import APEv2
from picard.util import encode_filename

data = configparser.ConfigParser()

WORKING_DIR = "D:\\Temp\\TAGS"
working_dir = pathlib.Path(str(WORKING_DIR))
os.chdir(working_dir)

for _ in os.listdir(working_dir):
    if _.lower().endswith(".mp3"):

        if os.path.isfile(str(_[:-4]) + ".mp3_dig"):
            mp3_dig_file = str(_[:-4]) + ".mp3_dig"
            data.read(mp3_dig_file)
            MixPoint = int(data['Audio']['msDuration']) - int(data['Audio']['msOutro'])
            CueIn = int(data['Audio']['msIntro'])
            Outro = int(data['Audio']['msDuration']) - int(data['Audio']['msVocalEnd'])
            Intro = int(data['Audio']['msVocalStart'])
            print(_)

            try:
                audio = APEv2(encode_filename(_))
            except mutagen.apev2.APENoHeaderError:
                audio = APEv2()

            # audio = APEv2(_)
            audio['MixPoint'] = str(MixPoint)
            audio['CueIn'] = str(CueIn)
            audio['Outro'] = str(Outro)
            audio['Intro'] = str(Intro)
            audio.pprint()
            audio.save(_)

            # print(data['Audio']['msDuration'])
