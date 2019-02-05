# Name: Austin James
# Date: 02/04/2019

# Import os to use listdir
# Import defaultict to use defaultdict(int)
# Import sys to use arguments
import os
from collections import defaultdict
import sys

# Read in the set of reportingverbs

verbFile = open("reportingverbs.txt", "r")

# For some reason, it won't allow me to initialize an empty set,
# so I will add and remove an empty element
verbSet = {""}

for x in verbFile:
    verb = x.strip()
    verbSet.add(verb.upper())

verbSet.remove("")

# Get the list of filenames in both the StudentDataSet and the
# COCADataSet directories

# Below are the filepaths for my machine
#studentDataSetPath = "/Users/AustinJames1/Documents/GitHub/assignment01/StudentDataSet"
#cocaDataSetPath = "/Users/AustinJames1/Documents/GitHub/assignment01/COCADataSet"

studentDataSetPath = sys.argv[1]
cocaDataSetPath = sys.argv[2]

studentDataSetFilenames = os.listdir(studentDataSetPath)
cocaDataSetFilenames = os.listdir(cocaDataSetPath)

rawStudentData = []
rawCOCAData = []

# Read in the files from both data sets
for x in studentDataSetFilenames:
    filename = "/Users/AustinJames1/Documents/GitHub/assignment01/StudentDataSet/" + x
    file = open(filename, "r")
    for y in file:
        line =  y[47:len(y)].strip()
        rawStudentData.append(line)

for x in cocaDataSetFilenames:
    filename = "/Users/AustinJames1/Documents/GitHub/assignment01/COCADataSet/" + x
    file = open(filename, "r")
    for y in file:
        line =  y[62:len(y)].strip()
        rawCOCAData.append(line)

# Split the data sets into individual words
tokenizedStudentData = []
tokenizedCOCAData = []

for x in rawStudentData:
    tokenizedStudentData.append(x.split(" "))

for x in rawCOCAData:
    tokenizedCOCAData.append(x.split(" "))

# Pick out the verbs from the larger group of words, using the CLAWS tags
studentTokens = []
cocaTokens = []

studentVerbs = []
cocaVerbs = []

for x in tokenizedStudentData:
    for y in x:
        taggedPair = y.split("_")
        if len(taggedPair) > 1:
            studentTokens.append(taggedPair[0])
            if taggedPair[1].startswith("V"):
                if taggedPair[0].upper() in verbSet:
                    studentVerbs.append(taggedPair[0])

for x in tokenizedCOCAData:
    for y in x:
        taggedPair = y.split("_")
        if len(taggedPair) > 1:
            cocaTokens.append(taggedPair[0])
            if taggedPair[1].startswith("V"):
                if taggedPair[0].upper() in verbSet:
                    cocaVerbs.append(taggedPair[0])

# Count the frequency of each token and verb
studentTokenCount = defaultdict(int)
cocaTokenCount = defaultdict(int)

studentVerbCount = defaultdict(int)
cocaVerbCount = defaultdict(int)

for x in studentTokens:
    studentTokenCount[x] += 1

for x in cocaTokens:
    cocaTokenCount[x] += 1

for x in studentVerbs:
    studentVerbCount[x] += 1

for x in cocaVerbs:
    cocaVerbCount[x] += 1

# Sort that defaultdict by value
sortedStudentVerbs = sorted(studentVerbCount.items(), key=lambda(k,v): v, reverse = True)
sortedCOCAVerbs = sorted(cocaVerbCount.items(), key=lambda(k,v): v, reverse=True)

# Print out the top 10 most occurring tokens and verbs that
totalStudentTokens = len(studentTokens)
totalCOCATokens = len(cocaTokens)

out = open("output.txt", "w")

out.write("Student Data (verb, freq, freq per 1000)\n")

for x in range(10):
    verb = sortedStudentVerbs[x][0]
    freq = sortedStudentVerbs[x][1]
    per1000 = (float(freq)/float(totalStudentTokens))*1000
    if len(verb) > 6:
        out.write(verb+"\t\t"+str(freq)+"\t\t\t"+str(per1000)+"\n")
    else:
        out.write(verb+"\t\t\t"+str(freq)+"\t\t\t"+str(per1000)+"\n")

out.write("\n")
out.write("COCA Data (verb, freq, freq per 1000)\n")

for x in range(10):
    verb = sortedCOCAVerbs[x][0]
    freq = sortedCOCAVerbs[x][1]
    per1000 = (float(freq)/float(totalCOCATokens))*1000
    if len(verb) > 6:
        out.write(verb+"\t\t"+str(freq)+"\t\t\t"+str(per1000)+"\n")
    else:
        out.write(verb+"\t\t\t"+str(freq)+"\t\t\t"+str(per1000)+"\n")
