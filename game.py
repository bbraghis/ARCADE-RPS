from enum import Enum
import pygame
from models import *


class GameState(Enum):
    PICKING = 0
    ENDED = 1


class GameEngine:
    player1 = None
    player2 = None
    state = None
    currentPlayer = None
    result = None

    def __init__(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.currentPlayer = self.player1
        self.state = GameState.PICKING

    def switch_player(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1

    def end_round(self, player1, player2):
        self.state = GameState.ENDED

        if player1.entity == player2.entity:
            return "Draw"

        if player1.entity == Entity.ROCK and player2.entity == Entity.SCISSORS:
            return player1

        if player1.entity > player2.entity:
            return player1
        else:
            return player2
