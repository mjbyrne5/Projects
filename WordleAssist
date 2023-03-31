import pandas as pd
import random

# build word list
df = pd.read_csv("https://raw.githubusercontent.com/mjbyrne5/Projects/main/words.csv")
#source: https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93
data1 = df['WORDS'].tolist()
reductionTrack = len(data1)

# word info
not_exist = []
in_word = []

not1 = []
not2 = []
not3 = []
not4 = []
not5 = []

yes1 = []
yes2 = []
yes3 = []
yes4 = []
yes5 = []

yesses = []

roundCount = 1

while roundCount < 6:
    count = 0
    word = input('What is your word? ').lower()
    code = input('What is your word code? ')

    for i in code:
        count += 1
        # assign yesses
        if i == '2':
            if count == 1:
                yes1.append(word[0])
                yesses.append(word[0])
            if count == 2:
                yes2.append(word[1])
                yesses.append(word[1])
            if count == 3:
                yes3.append(word[2])
                yesses.append(word[2])
            if count == 4:
                yes4.append(word[3])
                yesses.append(word[3])
            if count == 5:
                yes5.append(word[4])
                yesses.append(word[4])

        yesses = yesses + yes1 + yes2 + yes3 + yes4 + yes5

        # assign no's
        if i == '0':
            if count == 1:
                if word[0] not in (yesses or in_word):
                    if word.count(word[0]) < 2:
                        not_exist.append(word[0])
            if count == 2:
                if word[1] not in (yesses or in_word):
                    if word.count(word[1]) < 2:
                        not_exist.append(word[1])
            if count == 3:
                if word[2] not in (yesses or in_word):
                    if word.count(word[2]) < 2:
                        not_exist.append(word[2])
            if count == 4:
                if word[3] not in (yesses or in_word):
                    if word.count(word[3]) < 2:
                        not_exist.append(word[3])
            if count == 5:
                if word[4] not in (yesses or in_word):
                    if word.count(word[4]) < 2:
                        not_exist.append(word[4])

        # assign right letter in the wrong spot
        if i == '1':
            if count == 1:
                not1.append(word[0])
                in_word.append(word[0])
                yesses.append(word[0])
            if count == 2:
                not2.append(word[1])
                in_word.append(word[1])
                yesses.append(word[1])
            if count == 3:
                not3.append(word[2])
                in_word.append(word[2])
                yesses.append(word[2])
            if count == 4:
                not4.append(word[3])
                in_word.append(word[3])
                yesses.append(word[3])
            if count == 5:
                not5.append(word[4])
                in_word.append(word[4])
                yesses.append(word[4])

    # remove words with wrong letters (check grays)
    wrongLetter = []
    for i in not_exist:
        for j in data1:
            if i in j:
                wrongLetter.append(j)
    data2 = []
    for i in data1:
        if i not in wrongLetter:
            data2.append(i)


    # check if right letter not used in right spot (check greens)
    wrongSpot = []
    for i in data2:
        if len(yes1) == 1:
            if i[0] not in yes1:
                wrongSpot.append(i)
        if len(yes2) == 1:
            if i[1] not in yes2:
                wrongSpot.append(i)
        if len(yes3) == 1:
            if i[2] not in yes3:
                wrongSpot.append(i)
        if len(yes4) == 1:
            if i[3] not in yes4:
                wrongSpot.append(i)
        if len(yes5) == 1:
            if i[4] not in yes5:
                wrongSpot.append(i)
    data3 = []
    for i in data2:
        if i not in wrongSpot:
            data3.append(i)


    # remove wrong letters for specific spot
    count1 = 1
    notRight = []
    while count1 != 7:
        for i in data3:
            if count1 == 1:
                if i[0] in not1:
                    notRight.append(i)
            if count1 == 2:
                if (i[1] in not2) and (i in data1):
                    notRight.append(i)
            if count1 == 3:
                if (i[2] in not3) and (i in data1):
                    notRight.append(i)
            if count1 == 4:
                if (i[3] in not4) and (i in data1):
                    notRight.append(i)
            if count1 == 5:
                if (i[4] in not5) and (i in data1):
                    notRight.append(i)
        count1 += 1
    data4 = []
    for i in data3:
        if i not in notRight:
            data4.append(i)

    # remove words that don't have right letters
    notCorrect = []
    for i in data4:
        for j in in_word:
            if (j not in i) and (i in data4):
                notCorrect.append(i)
    data5 = []
    for i in data4:
        if i not in notCorrect:
            data5.append(i)

    if word in data5:
        data5.remove(word)
    roundCount += 1
    if len(data5) == 0:
        print("Out of Words")


    data1 = data5
    print(f'Possible: {data1}')
    bestGuesses = []
    letterTrack = 0
    for i in data1:
        check = 0
        for j in i:
            if i.count(j) > 1:
                check += 1
        if check < 1:
            bestGuesses.append(i)

    if len(bestGuesses) > 0:
        print(f'Suggestion: {random.choice(bestGuesses)}')
    if len(bestGuesses) == 0:
        print(f'Suggestion: {random.choice(data1)}')
    print(f'Total Reduction: {round((1-((len(data1))/reductionTrack))*100,4)}%')
    if roundCount == 6:
        print("Final Round")
    print('----------------------------------------------------------------------------------')
