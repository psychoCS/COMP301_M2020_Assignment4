"""
Assignment 4 - Comp301
Student: Thiago Luiz Batista
Student Number: 301110966
Program: generator.py
Purpose: Generates and displays sentences using simple grammar and vocabulary. Words are chosen at random.
"""

import csv
import random

# A list of articles, conjunctions, nouns, prepositions and verbs were taken from eslgrammar.org. A list of adjectives was taken from https://www.paperrater.com/page/lists-of-adjectives
def sentence():

   """Randomly builds and returns a simple sentence or one with a conjunction and a second independent clause."""
    optional = random.choice(['yes', 'no'])
    if optional == 'yes':
        return nounPhrase() + " " + verbPhrase()
    if optional == 'no':
        return nounPhrase() + " " + verbPhrase() + " " +  conjunction() + " " + nounPhrase() + " " + verbPhrase()     


def nounPhrase():

    """Builds and returns a noun phrase with or without an adjective."""
    with open('articles.txt') as a:
        article = csv.reader(a)
        articles = random.choice(list(article))
    with open('adjectives.txt') as ad:
        adjective = csv.reader(ad)
        adjectives = random.choice(list(adjective))  
    with open('nouns.txt') as n:
        noun = csv.reader(n)
        nouns = random.choice(list(noun))   

    optional1 = random.choice(['yes', 'no'])
    if optional1 == 'yes':    
        return random.choice(articles) + " " + random.choice(nouns)
    if optional1 == 'no':    
        return random.choice(articles) + " " + random.choice(adjectives) + " " + random.choice(nouns)


def verbPhrase():

    """Builds and returns a verb phrase with or without a preposition."""
    with open('verbs.txt') as v:
        verb = csv.reader(v)
        verbs = random.choice(list(verb)) 

    optional = random.choice(['yes', 'no'])
    if optional == 'yes':
        return random.choice(verbs) + " " + nounPhrase() 
    if optional == 'no':
        return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()


def conjunction():

    """Choose and returns a conjunction."""
    with open('conjunctions.txt') as c:
        conjunction = csv.reader(c)
        conjunctions = random.choice(list(conjunction))
    return random.choice(conjunctions)


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