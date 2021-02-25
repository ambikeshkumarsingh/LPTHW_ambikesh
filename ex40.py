#  Keep revisiting this exercise...

class Song(object):
    def __init__(self, lyrics):
        self.lyrics =lyrics  #what this line is doing??

    def sing_me_a_parody(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy Birthday to you",
                   "I don't want to get sued",
                   " So I'm singing this song"])

happy_bday.sing_me_a_parody()
