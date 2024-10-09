# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:25:00 2024

@author: Jonathan Stroud
"""

import pandas as pd
import numpy as np

#Use the file that I have in the git account
df = pd.read_csv([ENTER THE FILE HERE])


## The average star_rarity for the Characters
avg_rarity = df.star_rarity.mean()
avg_rarity = round(avg_rarity, 2)
print("The average star rarity for the chracters is ",avg_rarity,".\n")

## This has the most in the same region and the Unique regions
region_most = df.pivot_table(index = ['region'], aggfunc=['size']).sort_values(by='size', ascending=False)
print("The list of regions with the most to the least:\n",region_most)

most_members_region = df.loc[df['region'] == region_most.index[0]]
most_members_region = most_members_region.character_name
print("This is the list of Characters from the most populatred area:\n",most_members_region)

## This deals with the most weapons and who uses those weapons
weapon_most = df.pivot_table(index = ['weapon_type'], aggfunc=['size']).sort_values(by='size', ascending=False)
print("List of the most weapons used",weapon_most)

most_weapons = df.loc[df['weapon_type'] == weapon_most.index[0]]
most_weapons = most_weapons['character_name']
print("This is the list of Chracters with the same weapon:\n",most_weapons)

#Characters by their release date
character_release = df.sort_values(by=['release_date'])
print("This is the list of the characters by their release date\n",character_release['character_name'])

#Looking at the model heights
height = df.groupby(by=['model']).sum()
print("The most used height in the game:",height.index[0])

#Birthday in the order of their birth
char_birthday = df.sort_values(by=['birthday'])
print(char_birthday)


