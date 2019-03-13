# Password Cracking ToolKit

PCTK (Password Cracking ToolKit) is a small collection of scripts developed to aid in password cracking in capacities that standard utilities are unable to.

## Contents:
-  [WLGen (Word List Generator)](README.md#WLGen])
-  [Leet (Leet Mutator)](README.md#Leet)
- More coming later.

### WLGen
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

   __        ___     ____
   \ \      / / |   / ___| ___ _ __
    \ \ /\ / /| |  | |  _ / _ \ '_ \ 
     \ V  V / | |__| |_| |  __/ | | |
      \_/\_/  |_____\____|\___|_| |_|

	   by Conor Moening
	     Version: 1.0

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
   __        ___     ____
   \ \      / / |   / ___| ___ _ __
    \ \ /\ / /| |  | |  _ / _ \ '_ \ 
     \ V  V / | |__| |_| |  __/ | | |
      \_/\_/  |_____\____|\___|_| |_|
  
[WLGen] Searching for 'List of nouns' in 4 websites
[WLGen] Scraped 1743 words
[WLGen] Wordlist saved to file 'list.txt'
```
  
## Leet
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
usage: leet.py [-h] [-o O] wordlist keyspace

Leet Mutator is a simple script to generate every leet variation of a wordlist.
Written by Conor Moening - Version 1.0

positional arguments:
  wordlist    Wordlist to create leet list from
  keyspace    Keyspace to use for substitutions
              Ex) e3a5 will sub 3 for e and 5 for a

optional arguments:
  -h, --help  show this help message and exit
  -o O        File to output mutations to (Default leet.txt)
```
Example:
```
./leet.py rockyou.txt e3
[Leet] Running on rockyou.txt
[Leet] This may take a while depending on the size of wordlist used
[Leet] Mutations done. Saving to leet.txt
[Leet] Failed mutations: 199
[Leet] 23875008 mutations written
[Leet] Finished. May take a moment to close
```