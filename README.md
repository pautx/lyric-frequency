# Lyric Frequency Script
Scrapes through AZLyrics to find an artist's lyrics and counts them

Usage: `./run.py [ARTIST] [SONGS]...`
Example: `./run.py`

Modules
* requests
* bs4

If only artist is passed, then it will scrape all their main songs.
Multiple songs may be passed, but will slow down after 5 to avoid being blocked.

Current Issues
* Beat tags and singer identifiers are still detected as lyrics
* Features are still detected as lyrics
* Need to add proper help page
* Option for sorting, song limits, etc.
