import numpy as np
from scipy.io import wavfile
import os

frequencies = {
    'c' : 16.35,
    'c#': 17.32,
    'd' : 18.35,
    'd#': 19.45,
    'e' : 20.60,
    'f' : 21.83,
    'f#': 23.12,
    'g' : 24.50,
    'g#': 25.96,
    'a' : 27.50,
    'a#': 29.14,
    'b' : 30.87
}

class RTTTL:
    '''RTTTL class for ringtone music'''
    def __init__(self, text, samplerate=44100, volume=0.2):
        self.text = text
        self.samplerate = samplerate
        self.volume = volume
        self.soundarray = np.array([])
        self.name = 'default_name'
        if isinstance(self.text, str):
            self.__addString(self.text)
        elif isinstance(self.text, list):
            for i in self.text:
                self.__addString(i)
        else:
            raise Exception("text should be either a string or a list")

    def __addString(self, text):
        #-------------------Split Text-----------------------
        name, settings, notes = text.split(':')
        self.name = name
        settings = settings.split(',')
        notes = notes.split(',')
        #-------------Parse Settings section-----------------
        default_dur = 4
        default_oct = 5
        default_bpm = 160
        if len(settings) == 3:
            for setting in settings:
                setting = setting.strip().lower()
                if setting[0] == 'd':
                    default_dur = int(setting[2:])
                elif setting[0] == 'o':
                    default_oct = int(setting[2:])
                elif setting[0] == 'b':
                    default_bpm = int(setting[2:])
                else:
                    raise Exception(f'"{setting}" is not a recognized rtttl argument')
        else:
            raise Exception(f"{settings} RTTTL requires 3 settings arguments")
        #-----------------Create Wave Data-------------------
        localarray = np.array([])
        for note in notes:
            note = note.strip().lower()
            note_dur = default_dur
            note_oct = default_oct
            dotted = False
            if '.' in note: #if it's a dotted note, set dotted True and remove the period
                dotted = True
                note = note[:-1]
            if 'p' in note:
                #pause
                if note[:-1]: #specified duration
                    note_dur = int(note[:-1])
                #array time
                duration = 240/(default_bpm*note_dur)
                tone = np.zeros(int(self.samplerate*duration))
                localarray = np.concatenate((localarray, tone))
            else:
                #find note key
                key_str = ''
                for key in frequencies.keys():
                    if key in note:
                        key_str = key
                if not key_str:
                    raise Exception(f'"{note}" is not a recognized rtttl note')
                key_i = note.index(key_str)
                if note[:key_i]: #specified duration
                    note_dur = int(note[:key_i])
                if note[key_i+len(key_str):]: #specified octave
                    note_oct = int(note[key_i+len(key_str):])
                #array time
                duration = 240/(default_bpm*note_dur)
                if dotted:
                    duration *= 1.5
                frequency = frequencies[key_str]*2**note_oct
                t = np.linspace(0, duration, int(self.samplerate*duration))
                tone = self.volume*np.sin(frequency * 2*np.pi * t)
                localarray = np.concatenate((localarray, tone))
        #-----------------------Add Arrays------------------------
        if len(self.soundarray) < len(localarray):
            self.soundarray = np.concatenate((self.soundarray, np.zeros(len(localarray)-len(self.soundarray))))
        elif len(localarray) < len(self.soundarray):
            localarray = np.concatenate((localarray, np.zeros(len(self.soundarray)-len(localarray))))
        self.soundarray = np.add(self.soundarray, localarray)

    def exportWAV(self, filename = ''):
        if not os.path.exists('output'):
            os.makedirs('output')
        if filename: #if the filename is not empty
            wavfile.write(f'{filename}', self.samplerate, self.soundarray)
        else: #use the builtin name
            wavfile.write(f'{self.name}.wav', self.samplerate, self.soundarray)

    def __str__(self):
        return f'RTTTL {self.text} at a {self.samplerate}Hz samplerate and {self.volume} volume'

    def __repr__(self):
        return f'Vector(text={self.text}, samplerate={self.samplerate}, volume={self.volume})'

if __name__ == '__main__':
    print('running test')
    txt = "IronMan:d=4,o=5,b=80:b4,d,8d,8e,8e,8p,16g,16f#,16g,16f#,16g,16f#,8d,8d,8e,8e"
    my_tune = RTTTL(txt)
    my_tune.exportWAV('test.wav')