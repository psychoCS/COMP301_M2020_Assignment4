"""
Assignment 4 - Comp301
Student: Thiago Luiz Batista
Student Number: 301110966
Program: generator.py
Purpose: Generates and displays sentences using simple grammar and vocabulary. Words are chosen at random.

"""

import csv
import random

# list of articles, nouns, verbs and prepositions taken from eslgrammar.org

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
    with open('verbs.txt') as v:
        verb = csv.reader(v)
        verbs = random.choice(list(verb)) 

    optional = random.choice(['yes', 'no'])
    if optional == 'yes':
        return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

    if optional == 'no':
        return random.choice(verbs) + " " + nounPhrase()

def prepositionalPhrase():

    """Builds and returns a prepositional phrase."""

    with open('prepositions.txt') as p:

        preposition = csv.reader(p)
        prepositions = random.choice(list(preposition))

    return random.choice(prepositions) + " " + nounPhrase()

def main():

    """Allows the user to input the number of sentences to generate."""
    number = int(input("Enter the number of sentences: "))

    for count in range(number):
        print(sentence())

main()