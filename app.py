# -*- coding: utf-8 -*-

import random
import sys
import pygame

"""
def select_word():
    word_list = [
        ["apple", "あっぷる"],
        ["banana", "ばなな"]
    ]
    i = random.randint(0, 1)
    selected_word = word_list.pop(i)
    word_list.append(selected_word)
    return selected_word


def cut_head_char(word):
    return word[1:]


def is_empty_word(word):
    return not word


def in_title():
    print("In title")
    i = True
    while i:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    i = False
"""


def in_game():
    print("In game")
    # word = select_word()
    while True:
        screen.fill((200, 200, 200))

        sf_word = use_font.render("aiueo", True, (0, 0, 255))
        screen.blit(sf_word, (0, 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


num_word = 10
screen_size_x = 720
screen_size_y = 480

count = 0
pygame.init()
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
use_font = pygame.font.SysFont(None, 128)


if __name__ == "__main__":
    while True:
        # in_title()
        in_game()
        # in_result()
