#!/usr/bin/env python
import sys, os
import rtttl

debug = False

def main():
    if ('-h' in sys.argv) or ('--help' in sys.argv) or (len(sys.argv) == 1):
        print('RTTTL to WAV')
        print('Usage:')
        print(f'\t{sys.argv[0]} <inputfile>')
        print(f'\t{sys.argv[0]} <inputfile> <outputfile>')
        sys.exit()

    #Read input file
    inputfile = open(sys.argv[1], "r")
    lines = inputfile.read()

    if debug:
        print(f'rtttl data:\n{lines}\n')

    lines = lines.split()
    tune = rtttl.RTTTL(lines)
    outputfile = ''

    #produce name for output file
    if len(sys.argv) == 2:
        if not os.path.exists('output'):
            os.makedirs('output')
        outputfile = f'output/{tune.name}.wav'
    elif len(sys.argv) == 3:
        outputfile = sys.argv[2]
    else:
        print(f'Incorrect number of arguments, try:\n\t{sys.argv[0]} -h')
        sys.exit()

    #export .wav file
    tune.exportWAV(outputfile)

    if debug:
        print(f"Exported to '{outputfile}'")


if __name__ == '__main__':
    main()