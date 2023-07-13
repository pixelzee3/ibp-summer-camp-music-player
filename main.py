from pygame import mixer
from utils import PlayerUtils
from utils import UIUtils as ui

# mixer initialization
mixer.init()
mixer.music.set_volume(0.5)

# utils initialization
pu = PlayerUtils(mixer)

# define songs
songs = [
    {
    "title": "Bad Blood",
    "artist": "Taylor Swift",
    "album": "1989",
    "path": "music/1989/Bad Blood.mp3"
    },
    {
    "title": "Blank Space",
    "artist": "Taylor Swift",
    "album": "1989",
    "path": "music/1989/Blank Space.mp3"
    },
    {
    "title": "I Know Places",
    "artist": "Taylor Swift",
    "album": "1989",
    "path": "music/1989/I Know Places.mp3"
    },
    {
    "title": "New Romantics",
    "artist": "Taylor Swift",
    "album": "1989",
    "path": "music/1989/New Romantics.mp3"
    },
    {
    "title": "Shake It Off",
    "artist": "Taylor Swift",
    "album": "1989",
    "path": "music/1989/Shake It Off.mp3"
    },
    {
    "title": "Style",
    "artist": "Taylor Swift",
    "album": "1989",
    "path": "music/1989/Style.mp3"
    },
    {
    "title": "Wildest Dreams",
    "artist": "Taylor Swift",
    "album": "1989",
    "path": "music/1989/Wildest Dreams.mp3"
    },
    {
    "title": "Anaheim",
    "artist": "NIKI",
    "album": "Nicole",
    "path": "music/Nicole/Anaheim.mp3"
    },
    {
    "title": "Backburner",
    "artist": "NIKI",
    "album": "Nicole",
    "path": "music/Nicole/Backburner.mp3"
    },
    {
    "title": "Before",
    "artist": "NIKI",
    "album": "Nicole",
    "path": "music/Nicole/Before.mp3"
    },
    {
    "title": "High School in Jakarta",
    "artist": "NIKI",
    "album": "Nicole",
    "path": "music/Nicole/High School in Jakarta.mp3"
    },
    {
    "title": "Milk Teeth",
    "artist": "NIKI",
    "album": "Nicole",
    "path": "music/Nicole/Milk Teeth.mp3"
    },
    {
    "title": "Oceans & Engines",
    "artist": "NIKI",
    "album": "Nicole",
    "path": "music/Nicole/Oceans & Engines.mp3"
    },
]

# define music player commands
def select_song(pu: PlayerUtils, ui: ui):
    count = "1"
    selections = {}
    for song in songs:
        selections[count] = song
        count = int(count)
        count += 1
        count = str(count)


    selections_to_print = {key: f"{value['artist']} - {value['title']}" for key, value in selections.items()}
    selection_number = ui.select(selections_to_print)
    
    selection = selections[selection_number]
    selection_path = selection["path"]
    selection_title = selection["title"]
    selection_artist = selection["artist"]
    selection_album = selection["album"]

    pu.play(selection_path)
    print(f"""============================================================
        
        🎶 Now playing: {selection_artist} - {selection_title} 🎶 
        📂 {selection_album}

============================================================""")

def pause(pu):
    pu.pause()
    print("""============================================================
        ⏸️ Music playback paused.
============================================================""")

def unpause(pu):
    pu.unpause()
    print("""============================================================
        ⏸️ Music playback continued.
============================================================""")

def rewind(pu):
    pu.rewind()
    print("""============================================================
        ⏪ Music playback rewound.
============================================================""")

def queue(pu):
    count = "1"
    selections = {}
    for song in songs:
        selections[count] = song
        count = int(count)
        count += 1
        count = str(count)


    selections_to_print = {key: f"{value['artist']} - {value['title']}" for key, value in selections.items()}
    selection_number = ui.select(selections_to_print)
    
    selection = selections[selection_number]
    selection_path = selection["path"]
    selection_title = selection["title"]
    selection_artist = selection["artist"]
    selection_album = selection["album"]

    pu.queue_song(selection_path)
    print(f"""============================================================
        
        🎶 Playing next: {selection_artist} - {selection_title} 🎶 
        📂 {selection_album}

============================================================""")
    
def set_volume(pu):
    volume = 0
    while True:
        selection = input("Set the volume to (0-100): ")
        try:
            volume = float(selection) / 100
        except:
            print("Input a number between 0-100")
            continue
        if volume > 100 or volume < 0:
            print("Input a number between 0-100")
            continue
        break
    pu.set_volume(volume)
    print(f"""============================================================
        Volume set to {selection}%.
============================================================""")

# register commands
commands = {
    "play": {
        "description": "Play a new song.",
        "command": lambda : select_song(pu, ui)
    },
    "pause": {
        "description": "Pause music playback.",
        "command": lambda : pause(pu)
    },
    "unpause": {
        "description": "Unpause music playback.",
        "command": lambda : unpause(pu)
    },
    "rewind": {
        "description": "Rewind current song.",
        "command": lambda : rewind(pu)
    },
    "queue": {
        "description": "Add song to play after current song ends.",
        "command": lambda : queue(pu)
    },
    "volume": {
        "description": "Set playback volume.",
        "command": lambda : set_volume(pu)
    },
    "quit": {
        "description": "Exit the program.",
        "command": lambda : exit()
    },
}

# Initial program stuff (select first song)
commands["play"]["command"]()

# Command input loop
while True:
    named_selections = {key: value["description"] for key, value in commands.items()}
    ci = ui.select(named_selections)
    commands[ci]["command"]()
