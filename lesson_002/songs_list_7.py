#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]




# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# TODO здесь ваш код

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# TODO здесь ваш код
def task_7():
    print("TASK 7")
    time_1 = 0
    time_other_1 = 0
    for song, time in violator_songs_list:
        if song == 'Halo' or song =='Enjoy the Silence' or song == 'Clean':
            time_1+=time
        else:
            time_other_1 += time

    print('All time_1 =', time_1)
    print('All time other_1 =', time_other_1)

    time_2 = 0
    time_other_2 = 0
    for key in violator_songs_dict:

        if key == 'Sweetest Perfection' or song == 'Policy of Truth' or song == 'Blue Dress':
            time_2 += violator_songs_dict[key]
        else:
            time_other_2 += violator_songs_dict[key]
    print('All time_2 =', time_2)
    print('All time other_2 =', time_other_2)

