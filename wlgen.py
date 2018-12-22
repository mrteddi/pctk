#!/usr/bin/env python3

from bs4 import BeautifulSoup
from googlesearch import search
from urllib.request import urlopen
from urllib.error import HTTPError
import re
import argparse

version = "1.0"

art = "   __        ___     ____\n"
art += "   \ \      / / |   / ___| ___ _ __\n"
art += "    \ \ /\ / /| |  | |  _ / _ \ '_ \ \n"
art += "     \ V  V / | |__| |_| |  __/ | | |\n"
art += "      \_/\_/  |_____\____|\___|_| |_|\n"

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
description=art + "\n\t   by Conor Moening" + "\n\t     Version: " + version)

parser.add_argument('theme', help="Word theme to generate a wordlist for")
parser.add_argument('-o', default="wordlist.txt", help="File to output wordlist to. (Default: wordlist.txt)")
parser.add_argument('-n', type=int, default=2, help="Sets number of websites to scrape. (Default: 2)")
args = parser.parse_args()

urls = []
words = set()

print(art)

f = open(args.o, "w+")

print("[WLGen] Searching for 'List of ", args.theme, "' in ", args.n, " websites", sep='')

for url in search('List of '+args.theme, num=args.n, stop=args.n):
    try:
        page = urlopen(url)
        baseUrl = re.search(r'\.(.*?)\.', url).group(1)
    except HTTPError as e:
        print(url + " Error: " + str(e.code))
        continue
    if baseUrl not in urls:
        urls.append(baseUrl)

        soup = BeautifulSoup(page, 'html.parser')
        lis = soup.findAll(['li', 'td'])
        for li in lis:
            line = re.sub(' \((.*)\)|[^A-Za-z\\n]', '', li.text.strip()).lower()
            if "http" not in line and "www" not in line and len(line) <= 32:
                words.add(line)

for i in sorted(words):
        f.write(i + '\n')

print("[WLGen] Scraped", len(words), "words")
print("[WLGen] Wordlist saved to file '", args.o, "'", sep='')
f.close()
