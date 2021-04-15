from rtttl import *

mono_esc = 'JurassicRing:d=4,o=5,b=230:g,e,8f,8e,d,c,e,c6,c'

multi_esc = [
'dotTest:d=4,o=5,b=80:c.,d.,e.,f.,g.,a.,b.',
'dotTest:d=4,o=5,b=80:c,d,e,f,g,a,b'
]

my_tune = RTTTL(multi_esc)
print(my_tune)
my_tune.exportWAV()