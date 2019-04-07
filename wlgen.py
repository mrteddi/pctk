#!/usr/bin/env python3

from bs4 import BeautifulSoup
from googlesearch import search
from urllib.request import urlopen, Request
from urllib.error import HTTPError
import re
import argparse

version = "1.2"

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
description="Written by Conor Moening - Version: " + version)

parser.add_argument('theme', help="Word theme to generate a wordlist for")
parser.add_argument('-o', default="wordlist.txt", help="File to output wordlist to. (Default: wordlist.txt)")
parser.add_argument('-n', type=int, default=2, help="Sets number of websites to scrape. (Default: 2)")
args = parser.parse_args()

def main():
    urls = []
    words = set()

    f = open(args.o, "w+")

    print("[WLGen] Searching for 'List of ", args.theme, "' in ", args.n, " websites", sep='')

    for url in search('List of '+args.theme, num=args.n, stop=args.n):
        try:
            page = urlopen( Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0)'} ) )
            baseUrl = re.search(r'\.(.*?)\.', url).group(1)
        except HTTPError as e:
            print( "[WLGen] " + url + " Error: " + str(e.code))
            continue
        except:
            print( "[WLGen] Other error" )
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

if __name__ == '__main__':
    main()