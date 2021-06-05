#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt


# Есть словарь координат городов
def task_1():
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
        'Luxemburg':(543,345)
    }

    # Составим словарь словарей расстояний между ними
    # расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
    distances = {
    }

    for counter in sites:
        # distances = {}
        for key in sites:

            if counter == key or distances.get(key + ' ' + counter):
                continue
            value =  sqrt((sites[counter][0] - sites[key][0])**2 + (sites[counter][1] + sites[key][1])**2)
            distances.update({counter+' '+key : value})
    print(" TASK 0")
    for countries in distances:
        print(countries+'\t:', distances[countries], end=' \n')