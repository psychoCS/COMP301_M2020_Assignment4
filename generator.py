"""
Assignment 4 - Comp301
Student: Thiago Luiz Batista
Student Number: 301110966
Program: generator.py
Purpose: Generates and displays sentences using simple grammar and vocabulary. Words are chosen at random.
"""

import csv
import random

# articles = ("A","AN", "THE") - Random version working
# nouns = ("BOY", "GIRL", "BAT", "BALL","MAN","OCEAN","HOUSE","BIRD","BED","CAT","MILK",)

verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def sentence():

    """Builds and returns a sentence."""

    return nounPhrase() + " " + verbPhrase()

def nounPhrase():

    """Builds and returns a noun phrase."""

    with open('articles.txt') as a:
        article = csv.reader(a)
        articles = random.choice(list(article))

    with open('nouns.txt') as n:
        noun = csv.reader(n)
        nouns = random.choice(list(noun))       

    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():

    """Builds and returns a verb phrase."""

    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():

    """Builds and returns a prepositional phrase."""

    return random.choice(prepositions) + " " + nounPhrase()

def main():

    """Allows the user to input the number of sentences
    to generate."""

    number = int(input("Enter the number of sentences: "))

    for count in range(number):
        print(sentence()) 

main()