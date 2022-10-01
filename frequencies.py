"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    strItems = ([str(items) for items in items])
    for i in strItems:
      frequencies[i] = strItems.count(i)
    return frequencies


