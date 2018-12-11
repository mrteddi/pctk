# Password Cracking ToolKit

PCTK (Password Cracking ToolKit) is a small collection of scripts developed to aid in password cracking in capacities that standard utilities are unable to.

## Contents:
- [WLGen (Word List Generator)](README.md#WLGen])
- More coming later.

### WLGen
WLGen (Word List Generator).
Often passwords have a theme around their passwords and if you have a hint of what that may be, WLGen can help produce a wordlist to use as a dictionary.

Requirements:
```
pip3 install -r requirements
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