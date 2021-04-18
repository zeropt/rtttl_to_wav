# RTTTL to wav file

I wrote this program to playback music writing in **Ring Tone Text Transfer Language**(RTTTL) by converting the notes into square waves that are then written to a WAV file. I was then able to play it back using Audacity. RTTTL is the same format used by the bluejay melody editor for BLHeli_S ESCs. The bluejay repository can be found [here](https://github.com/mathiasvr/bluejay).

This is one of my first attempts at python programming. The packages I used can be installed using the requirements.txt file.
```
pip install -r requirements.txt
```

RTTTL music can be stored in a text file. Multiple melodies can be played on top of each other to simulate the 4 ESCs of a quadcopter by adding new more lines to the text file. There's a great Wikipedia page on how these work.
```
LZ_S2H:d=8,o=5,b=80:a4,c,e,a,b,e,c,b,c6,e,c,c6,f#,d,a4,f#,e,c,a4,4c,e,c,a4,g4,a4,a3
LZ_S2H:d=2,o=4,b=80:a,g#,g,f#,1e,8b3,4a3
LZ_S2H:d=8,o=4,b=80:a3,c,e,a,g#,e,c,b,g,e,c,c5,f#,d,a3,f#,e,c,a3,4c,e,c,a3,g3,a3,a
LZ_S2H:d=2,o=5,b=80:1e,1a4,1a4,8d,4e
```

The **txtwav.py** file can be run through a terminal or command line. This will create an output folder where you can find the new WAV file. The default name will be that of the RTTTL header of the last line in the text file (LZ_S2H.wav for the example above).
```
python txtwav.py example.txt
```

or you could designate an output file
```
python txtwav.py example.txt example.wav
```

I had a lot of fun playing with this and I hope you enjoy it if your try it.
