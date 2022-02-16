#!/usr/bin/env python
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time

pygame.mixer.init(48000)
clock = pygame.time.Clock()

pygame.mixer.music.load("wgo.ogg")

CLEAR = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RED = "\033[38;2;201;35;32m"
ORANGE = "\033[38;2;219;58;0m"
YELLOW = "\033[38;2;219;175;0m"
GREEN = "\033[38;2;7;130;5m"
BLUE = "\033[38;2;29;120;194m"
INDIGO = "\033[38;2;149;62;176m"
VIOLET = "\033[38;2;13;0;219m"
MAGENTA = "\033[38;2;209;13;127m"
PINK = "\033[38;2;194;85;121m"

lyrics = [
    (2800, "And so I cry   some   times   when I'm lying   in   bed".split(' ')),
    (6000, f"just   to   {ITALIC}get it all out{CLEAR}".split(' ')),
    (7900, "What's   in   my   head".split(' ')),
    (9000, f"And  {ITALIC}I   I   I{CLEAR}".split(' ')),
    (11000, "I'm feeling          a little    peculiar".split(' ')),

    (16000, [""]),
    (16500, f"And so I wake    in the morning   and I step  {UNDERLINE}outside{CLEAR}".split(' ')),
    (19900, f"And I   take a {ITALIC}deep breath{CLEAR}".split(' ')),
    (21500, f"And   get   {ITALIC}realllll   high{CLEAR},   and I".split(' ')),
    (24500, f"Scream from-the top of my lungs,     {UNDERLINE}{BOLD}WHAT'S    GOING    ON?{CLEAR}".split(' ')),
    
    (29000, [""]),
    (29500, f"And  I   said,    {RED}H{ORANGE}E{YELLOW}E{GREEN}Y{BLUE}Y{INDIGO}Y{MAGENTA}Y{PINK}Y{RED}Y      {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H     {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H    {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}H   {INDIGO}Y{MAGENTA}E{PINK}A{RED}H".split(' ')),
    (34300, f"{RED}H{ORANGE}E{YELLOW}E{GREEN}Y{BLUE}Y{INDIGO}Y{MAGENTA}Y{PINK}Y{RED}Y      {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H     {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H{CLEAR}        I said {ORANGE}H{YELLOW}E{GREEN}Y{CLEAR}".split(' ')),
    (39700, f"{UNDERLINE}WHAT'S    GOING    ON?{CLEAR}".split(' ')),
    (43300, f"And  I   said,    {RED}H{ORANGE}E{YELLOW}E{GREEN}Y{BLUE}Y{INDIGO}Y{MAGENTA}Y{PINK}Y{RED}Y      {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H     {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H    {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}H   {INDIGO}Y{MAGENTA}E{PINK}A{RED}H".split(' ')),
    (48000, f"{RED}H{ORANGE}E{YELLOW}E{GREEN}Y{BLUE}Y{INDIGO}Y{MAGENTA}Y{PINK}Y{RED}Y      {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H     {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H{CLEAR}        I said {ORANGE}H{YELLOW}E{GREEN}Y{CLEAR}".split(' ')),
    (53500, f"{UNDERLINE}WHAT'S    GOING    ON?{CLEAR}".split(' ')),
    
    (57000, [""]),
    (57500, f"{RED}And  he  tries...{CLEAR}".split(' ')),
    (60000, f"{UNDERLINE}OH  MAH   GOD   DO I TRY!{CLEAR}            {ITALIC}I try     all  the   time".split(' ')),
    (67200, f"in  this   institution{CLEAR}".split(' ')),
    (71000, f"{RED}AND    HE   PRAYS!!!{CLEAR}".split(' ')),
    (73500, f"{UNDERLINE}OH  MAH   GOD   DO I PRAY!{CLEAR}             I pray every   single     day".split(' ')),
    (79650, f"{RED}NYAAAAAAA!!!{CLEAR}".split(' ')),
    (81100, f"{BOLD}{UNDERLINE}FOR  A   REEEEVVVVOLUTION!!!{CLEAR}".split(' ')),

    (84000, [""]),
    (84300, f"And  I   said,    {RED}H{ORANGE}E{YELLOW}E{GREEN}Y{BLUE}Y{INDIGO}Y{MAGENTA}Y{PINK}Y{RED}Y      {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H     {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H    {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}H   {INDIGO}Y{MAGENTA}E{PINK}A{RED}H".split(' ')),
    (89000, f"{RED}H{ORANGE}E{YELLOW}E{GREEN}Y{BLUE}Y{INDIGO}Y{MAGENTA}Y{PINK}Y{RED}Y      {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H     {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H{CLEAR}        I said {ORANGE}H{YELLOW}E{GREEN}Y{CLEAR}".split(' ')),
    (94600, f"{UNDERLINE}WHAT'S    GOING    ON?{CLEAR}".split(' ')),
    (98000, f"And  I   said,    {RED}H{ORANGE}E{YELLOW}E{GREEN}Y{BLUE}Y{INDIGO}Y{MAGENTA}Y{PINK}Y{RED}Y      {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H     {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H    {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}H   {INDIGO}Y{MAGENTA}E{PINK}A{RED}H".split(' ')),
    (103000, f"{RED}H{ORANGE}E{YELLOW}E{GREEN}Y{BLUE}Y{INDIGO}Y{MAGENTA}Y{PINK}Y{RED}Y      {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H     {ORANGE}Y{YELLOW}E{GREEN}A{BLUE}A{INDIGO}H{MAGENTA}H{PINK}H{RED}H{CLEAR}        I said {ORANGE}H{YELLOW}E{GREEN}Y{CLEAR}".split(' ')),
    (108600, f"{ITALIC}and  learn  how  to  hide       your    feelings{CLEAR}".split(' ')),

    (112500, [""]),
    (113000, f"{ITALIC}heeyyyyyy      yeaahhhh     yeaahhhh     yeah   yeah".split(' ')),
    (116500, f"heeyyyyyy      yeaahhhh{CLEAR}     A  {RED}Y{ORANGE}E{YELLOW}A{GREEN}H  {BLUE}Y{INDIGO}E{MAGENTA}A{PINK}H  {RED}Y{ORANGE}E{YELLOW}A{GREEN}H{CLEAR}  I said {BLUE}H{INDIGO}E{MAGENTA}Y{CLEAR}".split(' ')),
    (122000, f"{BOLD}{UNDERLINE}WHAT'S    GOING    ON?{CLEAR}".split(' ')),

    (128000, ["ABORT_THE_PROGRAM"]),
]

cur_pos = 0
next_line = lyrics[0]
cur_pos += 1

# test variables to set the song and lyrics part way in
test = False
test_line = 24
start_time = 0
if test == True:
    next_line = lyrics[test_line]
    cur_pos = test_line + 1
    start_time = next_line[0]

pygame.mixer.music.play(0, start_time / 1000)
while True:
    if pygame.mixer.music.get_busy() == False:
        break
    pos = pygame.mixer.music.get_pos() + start_time
    if pos >= next_line[0]:
        for word in next_line[1]:
            if word != "":
                print(f"{word} ", flush=True, end='')
            time.sleep(0.15)
        print()
        next_line = lyrics[cur_pos]
        cur_pos += 1
    else:
        # print(pos)
        pass
    
    clock.tick(60)

pygame.quit()
