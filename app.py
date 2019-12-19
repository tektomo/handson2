# -*- coding: utf-8 -*-

import random
import sys
import time
import pygame


def select_word():
    word_list = [
        ["ringo", "りんご"],
        ["banana", "ばなな"],
        ["budou", "ぶどう"],
        ["kaki", "かき"],
        ["mikan", "みかん"],
        ["neko", "ねこ"],
        ["inu", "いぬ"],
        ["uma", "うま"],
        ["saru", "さる"],
        ["tori", "とり"]
    ]
    # ワードをランダムで抽出し、抽出したワードは最後尾になる
    i = random.randint(0, len(word_list)-1)
    selected_word = word_list.pop(i)
    word_list.append(selected_word)
    # 選んだワードのリストを返す
    return selected_word


def cut_head_char(word):
    # 先頭をカットした引数を返す
    return word[1:]


def is_empty_word(word):
    # WordがNoneならTrueを、そうでないのならFalseを返す
    return not word


def in_title():
    print("In title")
    # 文字列をレンダリングする
    start_ap = font_en.render("Press Enter or Space to Start", True, (0, 0, 0))
    end_ap = font_en.render("Press ESC to Quit", True, (0, 0, 0))
    flag = True
    while flag:
        # 画面描画を行う
        screen.fill((200, 200, 200))
        screen.blit(start_ap, (0, 0))
        screen.blit(end_ap, (0, 200))
        pygame.display.update()
        # イベントを取得し、特定のキーが押されたときのみ動作を行う
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE or \
                        event.key == pygame.K_RETURN:
                    flag = False


def in_game():
    flag = True
    count = 1
    score = 0
    mistake = 0
    print("In game")
    # 最初のワードをとってきて、それをそれぞれ変数に代入
    word = select_word()
    word_roma = word[0]
    word_ja = word[1]
    # 3秒前のカウントダウンを表示
    for i in range(3):
        screen.fill((200, 200, 200))
        now_ap = font_en.render(str(3-i), True, (0, 0, 0))
        screen.blit(now_ap, (0, 200))
        pygame.display.update()
        time.sleep(0.9)
    while flag:
        # 画面を描画する
        screen.fill((200, 200, 200))
        word_ja_ap = font_ja.render(word_ja, True, (0, 0, 0))
        word_roma_ap = font_en_big.render(word_roma, True, (0, 0, 0))
        screen.blit(word_ja_ap, (0, 0))
        screen.blit(word_roma_ap, (0, 200))
        pygame.display.update()
        # イベントを取得し、正しいキーが押されていれば先頭文字をカット、もう文字がない（=完答した）ときは新しい文字列を探す（ただし回数制限で終了）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if chr(event.key) == word_roma[0]:
                    score += 1
                    word_roma = cut_head_char(word_roma)
                    if is_empty_word(word_roma):
                        count += 1
                        if count > num_word:
                            flag = False
                        word = select_word()
                        word_roma = word[0]
                        word_ja = word[1]
                else:
                    mistake += 1
    return [score, mistake]


def in_result(point):
    print("In result")
    score = point[0]
    mistake = point[1]
    score_ap = font_en.render("Your score is "+str(score), True, (0, 0, 0))
    mistake_ap = font_en.render("Your mistakes are "+str(mistake),
                                True, (0, 0, 0))
    flag = True
    while flag:
        screen.fill((200, 200, 200))
        screen.blit(score_ap, (0, 0))
        screen.blit(mistake_ap, (0, 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    flag = False



num_word = 10
screen_size_x = 720
screen_size_y = 480
pygame.init()
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
font_en_big = pygame.font.SysFont(None, 128)
font_ja = pygame.font.SysFont('yugothic', 128)
font_en = pygame.font.SysFont(None, 64)
while True:
    in_title()
    point = in_game()
    in_result(point)
