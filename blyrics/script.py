#!/usr/bin/python
# Author:   @BlankGodd

from pyfiglet import Figlet
from search import Search_Genius
from save import Save
import time


class Script:
    
    def __init__(self):
        banner = Figlet(font='standard')
        print(banner.renderText("BLyrics"))

        print()
        print("Welcome To BLyrics")
        print()
        print('If you are new to BLyrics please check the help guide by typing help')
        print('Ignore to continue')
        print()
        comd = input(": ").lower()
        if comd == 'help':
            print('Welcome to BLyrics')
            print("To go back, enter 'back'(lower case)")
            print("To return to start page, enter 'menu'(lower case)")
            print("To exit, enter 'ctrl+Z'")
            print('Follow the prompt and you should be fine :)')
            time.sleep(3)
            for i in range(2):
                print()
        self.start()

    def start(self):
        print("To get latest articles from www.genius.com, press 1")
        print("To get the chart of the top trending songs, press 2")
        print('To get information about songs and artists, get song lyrics, press #')
        print()

        command = input(': ')
        if command == 1:
            self.get_articles()
        elif command == '2':
            self.get_chart()
        elif command == '3' or command == '#':
            self.get_searching()
        elif command == 'back' or 'command' == 'menu':
            self.start()
        else:
            print("Invalid input")
            self.start()
        
    def get_articles(self):
        print()
        print('Articles')
        # call get articles module
    
    def get_searching(self):
        """To starting searchin
        
        Properties:
            Artist:
                -Name: Artist name
                -Alias: Artist aliases
                -Description: Information about artist
                -Twitter: Twitter handle
                -Instagram: Instagram handle
                -Facebook: Facebook name
                -Songs: List of top songs
            Songs:
                -Title: Song title
                -Artist: Artist name
                -Description: Song description
                -Release Date: Song release date
                -Recording Location
                -Lyrics: Song lyrics
        """
        print()
        print('Information')
        print('1: Search Artist')
        print('2: Search Song ')
        print()
        command = input('Enter 1 or 2: ').lower()
        if command == 'back' or command == 'menu':
            self.start()
            return
        print()
        response = None
        search_str = ''
        if command == '1':
            while search_str == '':
                print("Please enter valid input!")
                search_str = input('Enter Artist name: ')
            if search_str == 'back' or search_str == 'menu':
                self.start()
                return
            response = Search_Genius.search_artist(search_str)
        elif command == '2':
            while search_str == '':
                print("Please enter valid input!")
                search_str = input('Enter Song title: ')
            if search_str == 'back' or search_str == 'menu':
                self.start()
                return
            response = Search_Genius.search_song(search_str)
        else:
            print('Invalid input!')
            self.get_searching()
            return

        if not response:
            print('{} not found. Please retry!'.format(search_str))
            self.get_searching()
            return

        if command == '1':
            name = response['artist_name']
            alias = response['Aliases']
            twitter = response['Twitter Handle']
            ig = response['Instagram Handle']
            facebook = response['Facebook Name']
            description = response['Description']
            songs = response['songs']
            
            print()
            print('Artist Name: {}'.format(name))
            print('Aliases: {}'.format(alias))
            print()
            print('Twitter Handle: {}'.format(twitter))
            print('Instagram Handle: {}'.format(ig))
            print('Facebook Name: {}'.format(facebook))
            print()
            print('Description: \n{}'.format(description))
            print()
            print('Songs by {}'.format(name))
            if type(songs) == list:
                for song in songs:
                    print(song)
            else:
                for k,v in songs.items():
                    print(v)   
        else:
            {'Title' : ranked_song[0], 'Artist' : ranked_song[2], 
            'Description' : description, 'Lyrics' : lyrics, 
            'song_id' : song_id, 'lyrics_url' : ranked_song[4],
            'page_title' : page_title, 'recording_location' : recording_location,
            'release_date' : release_date}
            title = response['Title']
            artist = response['Artist']
            description = response['Description']
            lyrics = response['Lyrics']
            recording_location = response['recording_location']
            release_date = response['release_date']

            print()
            print('Song Title: {}'.format(title))
            print('Artist: {}'.format(artist))
            print()
            print('Record Location: {}'.format(recording_location))
            print('Release Date: {}'.format(release_date))
            print()
            print('Description: \n{}'.format(description))
            print()
            print('Lyrics: \n{}'.format(lyrics))
            print()
            print()

            print('Would you like to view annotations')
            an = input('y/n: ').lower()
            if an == 'back' or an == 'menu':
                self.start()
                return
            if an == 'y':
                pass
            else:
                pass

        print()
        print('Would you like to save information to file')
        sv = input('y/n: ').lower:
        if sv == 'y':
            if command == '1':
                Save.save_artist(path,response)
            else:
                Save.save_song(path, response)
        elif sv == 'back' or sv == 'menu':
            self.start()
        else:
            pass
        
        
        



