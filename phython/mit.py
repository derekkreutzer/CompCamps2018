import pygame

class MIT:
    """docstring for ."""
    def __init__(self, name):
        self.name=name
        self.image = "images/" + self.name.lower() + ".jpg"
        self.img = pygame.image.load(self.image)
        self.img = pygame.transform.scale(self.img,(100,100))
