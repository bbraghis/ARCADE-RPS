from enum import Enum
import pygame


class Entity(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class Player:
    entity = None
    name = None

    def __init__(self, name):
        self.name = name

    def pick(self, entity):
        self.entity = entity

