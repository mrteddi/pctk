#!/usr/bin/env python3

import argparse

Version = "1.2"

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
description="\nLeet Mutator is a simple script to generate every leet variation of a wordlist.\n" + 
    "Written by Conor Moening - Version " + Version + "\n")
parser.add_argument('wordlist', help="Wordlist to create leet list from")
parser.add_argument('keyspace', help="Keyspace to use for substitutions\n" +
    "Ex) e3a5 will sub 3 for e and 5 for a")
parser.add_argument('-o', default="leet.txt", help="File to output mutations to (Default leet.txt)")
parser.add_argument('-r', type=int, default="2", help="GBs of RAM to use (Default 2)")
args = parser.parse_args()

def printMutations( strings, fo, errors, total ):
    print( "[Leet] Flushing set and writing " + str( len( strings ) ) + " mutations" )
    for i in strings:
        try:
            fo.write( i.decode().strip() + "\n" )
            total += 1
        except:
            errors += 1
    strings.clear()
    print( "[Leet] Continuing... " )
    return errors, total

def replaceN(word, char, n):
    return word[:n] + str.encode( char ) + word[n+1:]

def leet( word, keyspace, strings, start ):
    for i in range( 0, len( keyspace ) ):
        for j in range( start, len( word ) ):
            if( chr( word[j] ) == keyspace[i][0] ):
                first = replaceN( word, keyspace[i][1], j )
                if first in strings:
                    return
                strings.add( first )
                leet( first, keyspace, strings, j )

def main():
    keyspace = []
    strings = set()

    total = 0
    count = 0
    errors = 0

    for i in range( 0, len( args.keyspace ), 2 ):
        keyspace.append( ( args.keyspace[i], args.keyspace[i + 1] ) )

    f = open( args.wordlist, "rb" )
    fo = open( args.o, "w" )

    print( "[Leet] Running on " + args.wordlist )
    print( "[Leet] This may take a while depending on the size of wordlist used" )

    for word in f:
        if( len( word ) != 0 ):
            strings.add( word )
            leet( word, keyspace, strings, 0 )
            count += 1
            if count % ( 3000000 * args.r ) == 0:
                errors, total = printMutations( strings, fo, errors, total )

    errors, total = printMutations( strings, fo, errors, total )
    print( "[Leet] Mutations done. Saved to " + args.o )
    print( "[Leet] Mutate errors: " + str( errors ) )
    print( "[Leet] Finished. " + str( total ) + " mutations written" )

if __name__ == '__main__':
    main()