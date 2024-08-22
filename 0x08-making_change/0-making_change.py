#!/usr/bin/python3

""" The makeChange function"""


def makeChange(coins, total):
    """
    Returns: the fewest number of coins needed to meet total
        return 0, if t less than 0 or 0
        If total not met by any number of coins you have, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
