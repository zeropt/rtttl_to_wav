#!/usr/bin/env python
import sys, os
import rtttl

#opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
#args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

def main():
    print(sys.argv)
    if ('-h' in sys.argv) or ('--help' in sys.argv):
        print('RTTTL to WAV')
        print('Usage:')
        print(f'\t{sys.argv[0]} <inputfile>')
        print(f'\t{sys.argv[0]} <inputfile> <outputfile>')
        sys.exit()

if __name__ == '__main__':
    main()