from rtttl import *

mono_esc = 'JurassicRing:d=4,o=5,b=230:g,e,8f,8e,d,c,e,c6,c'

multi_esc = [
'WhiteStripes:d=4,o=5,b=230:2g#5,p,g#5,b5,8p,g#5,8p,f#5,1e5,1d#5',
'WhiteStripes:d=4,o=5,b=230:2g#4,p,g#4,b4,8p,g#4,8p,f#4,1e4,1d#4',
'WhiteStripes:d=4,o=5,b=230:2g#6,p,g#6,b6,8p,g#6,8p,f#6,1e6,1d#6',
'WhiteStripes:d=4,o=5,b=230:2d#5,p,d#5,f#5,8p,d#5,8p,c#5,1b4,1a#4'
]

my_tune = RTTTL(multi_esc)
my_tune.exportWAV()