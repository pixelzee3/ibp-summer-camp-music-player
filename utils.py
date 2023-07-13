from pygame import mixer as pygamemixer

class PlayerUtils:
    def __init__(self, mixer: pygamemixer) -> None:
        self.mixer = mixer

    def play(self, path: str):
        self.mixer.music.load(path)
        self.mixer.music.play()
    
    def queue_song(self, path: str):
        self.mixer.music.queue(path)

    def pause(self):
        self.mixer.music.pause()

    def unpause(self):
        self.mixer.music.unpause()

    def rewind(self):
        self.mixer.music.rewind()
    
    def set_volume(self, volume: float):
        self.mixer.music.set_volume(volume)

class UIUtils:
    def select(selections: dict):
        for key, value in selections.items():
            print(f"{key} >>> {value}")
        while True:
            selection = input("Select an option: ")
            if selection not in selections:
                print("Please choose from the above options.")
                continue
            break
        return selection
    def lowkey_select(selections: str):
        print(selections)
        return input("> ")