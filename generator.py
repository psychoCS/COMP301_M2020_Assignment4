"""

Assignment 4 - Comp301

Student: Thiago Luiz Batista

Student Number: 301110966

Program: generator.py

Purpose: Generates and displays sentences using simple grammar and vocabulary. Words are chosen at random.

"""

import csv

import random



articles = ("A","AN", "THE")

nouns = ("BOY", "GIRL", "BAT", "BALL","MAN","OCEAN","HOUSE","BIRD","BED","CAT","MILK",)

verbs = ("HIT", "SAW", "LIKED")

prepositions = ("WITH", "BY")



with open('data.txt') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')



    # Lets create the Header Row    

    print

    print(f"\n\t\t\tAvengers Worked Hours")

    print(f"\n\t-----------------------------------------------")

    print(f"\t|Employee Number|Employee Name\t|Hours Worked\t|")

    print("\t-----------------------------------------------")



    # Finaly one loop that goes line by line od the data file, putting it in a formatted table.

    employees = 0

    for avenger in csv_reader:

        print(f'\t|\t{avenger[0]}\t|\t{avenger[2]}\t|\t{avenger[3]}\t|')

        print("\t-----------------------------------------------")

        employees += 1



    # And just for fun lets count the number of 'Employees' found on the payroll

    print(f'\n\t\t\tFound {employees} avengers.\n')







class GetWords():



    # lets take the 2 user imputs 

    def copier(self,firstFile,secondFile):

        print()



    # Open the first file and save its lines on a variable

    with open(firstFile,'r')as fileData:

        firstFileContent= fileData.readlines()

        print("Reading the content on the first file...")

        print()



    # Open the second file and save its lines on a variable

    with open(secondFile,'r')as fileData:

        secondFileContent= fileData.readlines()

        print("Reading the content on the second file...")

        print()



    # Pick each line of the second file and add it to the first one

    for eachline in firstFileContent:

        secondContent = open(secondFile,'a')

        secondContent.write(eachline)

    print("Done. Content from the first file transfered to the second one")

    print()





def sentence():

    """Builds and returns a sentence."""

    return nounPhrase() + " " + verbPhrase()



def nounPhrase():

    """Builds and returns a noun phrase."""

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