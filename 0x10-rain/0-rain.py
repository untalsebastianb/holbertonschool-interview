#!/usr/bin/python3
"""
Rain
"""


def rain(walls):
    """
    calculate how much water can be trapped
    @walls: walls
    Return: amount of water which can be trapped
    """
    if(not len(walls)):
        return 0

    size = len(walls) - 1
    prev = walls[0]
    prev_index = 0
    tmp = 0
    rainwater = 0

    for i in range(1, size + 1):
        if (walls[i] >= prev):
            prev = walls[i]
            prev_index = i
            tmp = 0
        else:
            rainwater += prev - walls[i]
            tmp += prev - walls[i]

    if (prev_index < size):
        rainwater -= tmp
        prev = walls[i]

        for i in range(size, prev_index - 1, -1):
            if (walls[i] >= prev):
                prev = walls[i]
            else:
                rainwater += prev - walls[i]

    return rainwater
