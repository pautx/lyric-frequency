#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
from collections import Counter
from sys import argv
from time import sleep

# Check for necessary amount of arguments
if len(argv) > 1:
    print("Scraping lyrics...")

    artist = argv[1].lower().replace(' ', '') # Get artist name 
    words = ""
    
    i = 2 # Counter for songs after first argument
    
    # If only artist name, scrape all their main songs
    if len(argv) < 3:
        URL = "https://www.azlyrics.com/" + artist[0:1] + "/" + artist + ".html"
        html = requests.get(URL).content

        parseHTML = BeautifulSoup(html, 'html.parser')

        for link in parseHTML.find_all('a'):
            if "lyrics/" + artist in str(link.get('href')):
                song = link.get('href')[11 + len(artist):]
                argv.append(song.replace('.html', ''))
    
    if (len(argv) > 5):
        print("More than 5 songs, slowing requests to avoid detection...")
        print("ETA: " + str(len(argv) * 30 / 60) + " minutes for " + str(len(argv)) + " songs.")

    # Scrape all artist's songs using azlyrics
    while i < len(argv):
        song = argv[i].lower().replace(' ', '').replace('&', '').replace(' and ', '')

        URL = "https://www.azlyrics.com/lyrics/" + artist + "/" + song + ".html"
        html = requests.get(URL).content

        if (len(argv) < 6):
            sleep(1)
        else:
            sleep(30)

        parseHTML = BeautifulSoup(html, 'html.parser')
        title = parseHTML.title.string
        
        if (title[0:8] == "AZLyrics"):
            print("Song not found")
        else:
            print(title.replace(' Lyrics | AZLyrics.com', ''))
            divs = parseHTML.find_all('div')

            lyrics = str(divs[20]).replace('<br/>', '').replace(',', '').replace('(', '').replace(')', '').split('\n')
            lines = lyrics[2:len(lyrics) - 1]

            for line in lines:
                words += line + " "

        i += 1

    # Gather and count all words
    words = words.lower().split(' ')
    wordFreq = Counter(words)

    # Print word frequencies in nice format
    for word in wordFreq:
        print(str(wordFreq[word]) + ": " + word)

else:
    print("Usage: ./run [ARTIST] [SONGS]...")




