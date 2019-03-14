# Password Cracking ToolKit

PCTK (Password Cracking ToolKit) is a small collection of scripts developed to aid in password cracking in capacities that standard utilities are unable to.

## Contents:
-  [WLGen (Word List Generator)](README.md#WLGen])
-  [Leet (Leet Mutator)](README.md#Leet)
-  [Change Log](README.md#Changelog)
- More coming later.

## WLGen
wlgen.py (Word List Generator).

Often passwords have a theme around their passwords and if you have a hint of what that may be, WLGen can help produce a wordlist to use as a dictionary.

Requirements:
```
pip install -r requirements
```
Usage:
```
./wlgen.py --help
usage: wlgen.py [-h] [-o O] [-n N] theme

Written by Conor Moening - Version: 1.2

positional arguments:
  theme       Word theme to generate a wordlist for

optional arguments:
  -h, --help  show this help message and exit
  -o O        File to output wordlist to. (Default: wordlist.txt)
  -n N        Sets number of websites to scrape. (Default: 2)
```
Example:
```
We want to search for a wordlist of nouns, so the theme argument would be nouns.
Search 4 sites and output to list.txt
  
./wlgen.py nouns -n 4 -o list.txt
[WLGen] Searching for 'List of nouns' in 4 websites
[WLGen] Scraped 1743 words
[WLGen] Wordlist saved to file 'list.txt'
```
  
## Leet Mutator
leet.py (Leet Mutator)

Hashcat and other password crackers can't produce every permutation of leet code for a given word,
Leet Mutator is used to produce a leet version of a wordlist
 
Requirements:
```
None
```
Usage:
```
./leet.py --help
usage: leet.py [-h] [-o O] [-r R] wordlist keyspace

Leet Mutator is a simple script to generate every leet variation of a wordlist.
Written by Conor Moening - Version 1.2

positional arguments:
  wordlist    Wordlist to create leet list from
  keyspace    Keyspace to use for substitutions
              Ex) e3a5 will sub 3 for e and 5 for a

optional arguments:
  -h, --help  show this help message and exit
  -o O        File to output mutations to (Default leet.txt)
  -r R        GBs of RAM to use (Default 2)
```
Example:
```
This runs the first 5 million lines in rockyou (with lines > 16 stripped)
The keyspace e -> 3 o -> 0 i -> 1 is used
./leet.py rockyouStripped.txt e3o0i1
[Leet] Running on rockyouStripped.txt
[Leet] This may take a while depending on the size of wordlist used
[Leet] Flushing set and writing 21346057 mutations
[Leet] Continuing... 
[Leet] Mutations done. Saved to leet.txt
[Leet] Mutate errors: 154
[Leet] Finished. 21345903 mutations written
```

# Changelog
#### Leet Mutator 1.2
```
- Changed looping so all cases are met
- Fixed issue with RAM usage. ( See -r option )
```
#### Wordlist Generator 1.2
```
- Removed art
- Added additional error check that handles python errors
```