#!/usr/bin/env python3

import argparse

Version = "1.0"

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
description="\nLeet Mutator is a simple script to generate every leet variation of a wordlist.\n" + 
    "Written by Conor Moening - Version " + Version + "\n")
parser.add_argument('wordlist', help="Wordlist to create leet list from")
parser.add_argument('keyspace', help="Keyspace to use for substitutions\n" +
    "Ex) e3a5 will sub 3 for e and 5 for a")
parser.add_argument('-o', default="leet.txt", help="File to output mutations to (Default leet.txt)")
args = parser.parse_args()

def replaceN(word, char, n):
    return word[:n] + str.encode(char) + word[n+1:]

def leet( word, keyspace, strings ):
    for i in range( 0, len( keyspace ) ):
        for j in range( 0, len(word) ):
            if( chr(word[j]) == keyspace[i][0] ):
                first = replaceN( word, keyspace[i][1], j )
                if first in strings:
                    return
                strings.add( first )
                leet( first, keyspace, strings )

def main():
    keyspace = []
    strings = set()

    for i in range( 0, len( args.keyspace ), 2 ):
        keyspace.append( ( args.keyspace[i], args.keyspace[i + 1] ) )

    f = open( args.wordlist, "rb" )

    print( "[Leet] Running on " + args.wordlist )
    print( "[Leet] This may take a while depending on the size of wordlist used" )

    for word in f:
        if( len( word ) != 0 ):
            strings.add( word )
            leet( word, keyspace, strings )

    errors = 0
    print( "[Leet] Mutations done. Saving to " + args.o )
    f = open( args.o, "w")
    for i in strings:
        try:
            f.write( i.decode().strip() + "\n")
        except:
            errors += 1
    print( "[Leet] Failed mutations: " + str(errors) )
    print( "[Leet] " + str(len(strings)) + " mutations written" )
    print( "[Leet] Finished. May take a moment to close")

if __name__ == '__main__':
    main()