class RPGInfo:
    author = 'Anonymous'

    def __init__(self, game_title):
        self.game_title = game_title

    def welcome(self):
        print(f"Welcome to the {self.game_title}!")

    @staticmethod
    def info():
        print("Made using OOP principles.")

    @classmethod
    def credits(cls):
        print(f"Game developed by {cls.author}")
