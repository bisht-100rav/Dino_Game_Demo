# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 10:13:55 2022

@author: Saurav
"""

import cx_Freeze

build_exe_options = {
    'packages': ["pygame","random"],
    'include_files': [["sprites/racecar.png",
                     "sprites/cacti-big.png",
                     "sprites/checkPoint.wav",
                     "sprites/cloud.png",
                     "sprites/die.wav",
                     "sprites/dino.png",
                     "sprites/dino_ducking.png",
                     "sprites/game_over.png",
                     "sprites/ground.png",
                     "sprites/jump.wav",
                     "sprites/logo.png",
                     "sprites/numbers.png",
                     "sprites/offline-sprite-2x-black.png",
                     "sprites/ptera.png",
                     "sprites/replay_button.png"]]}

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Dino Bot",
    description = 'Game',
    options = {'build.exe': build_exe_options},
    executables = executables
)