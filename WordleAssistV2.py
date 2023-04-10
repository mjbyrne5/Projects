import pandas as pd

# build word list
df = pd.read_csv("https://raw.githubusercontent.com/mjbyrne5/Projects/main/words.csv")
#  source: https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93
masterWordList = df['WORDS'].tolist()
reductionStats = len(masterWordList)


# word info
grayLetters = []
greenLetters = []

notIn = [[], [], [], [], []]
yesIn = [[], [], [], [], []]

roundCount = 1
doubleTrack = False
inPlay = True

while inPlay:
    if roundCount == 1:
        wordList = masterWordList
        print('WORDLE ASSIST INSTRUCTIONS: Wordle Assist is designed to be used in conjunction\n '
              'with the NYT Wordle game. Open daily NYT Wordle. Pick your first word and input\n '
              'into NYT Wordle. When prompted, input word into Wordle Assist. Input code provided\n '
              'by NYT Wordle. A gray letter = 0, yellow = 1, green = 2. Ex: 02100. Repeat with word \n'
              'suggestion or your own word.\n'
              '----------------------------------------------------------------------------------------------')
    count = 0

    if roundCount == 6:
        print("Last Round Reached")
        inPlay = False
        break
    print(f'Round: {roundCount}')
    if roundCount == 5:
        print("Final")

    word = input('What is your word? ').lower()
    while word not in masterWordList:
        word = input('Word is not valid. Input new word: ').lower()
    code = input('What is your word code? ')
    while len(code) != 5:
        code = input('Code invalid. Input new word code: ')
    print('----------------------------------------------------------------------------------------------')

    if code == '22222':
        print("You've solved the word")
        inPlay = False

    for i in code:
        count += 1
        # Assign greens
        if i == '2':
            if count == 1 and word[0] not in yesIn[0]:
                yesIn[0].append(word[0])
                if word[0] not in greenLetters:
                    greenLetters.append(word[0])
            if count == 2 and word[1] not in yesIn[1]:
                yesIn[1].append(word[1])
                if word[0] not in greenLetters:
                    greenLetters.append(word[1])
            if count == 3 and word[2] not in yesIn[2]:
                yesIn[2].append(word[2])
                if word[0] not in greenLetters:
                    greenLetters.append(word[2])
            if count == 4 and word[3] not in yesIn[3]:
                yesIn[3].append(word[3])
                if word[0] not in greenLetters:
                    greenLetters.append(word[3])
            if count == 5 and word[4] not in yesIn[4]:
                yesIn[4].append(word[4])
                if word[0] not in greenLetters:
                    greenLetters.append(word[4])

        # Assign grays
        if i == '0':
            if count == 1:
                notIn[0].append(word[0])
                if word[0] in greenLetters:
                    if word[0] not in yesIn[1]:
                        notIn[1].append(word[0])
                    if word[0] not in yesIn[2]:
                        notIn[2].append(word[0])
                    if word[0] not in yesIn[3]:
                        notIn[3].append(word[0])
                    if word[0] not in yesIn[4]:
                        notIn[4].append(word[0])
                if word[0] not in greenLetters:
                    if word[0] not in word[1]:
                        if word[0] not in word[2]:
                            if word[0] not in word[3]:
                                if word[0] not in word[4]:
                                    grayLetters.append(word[0])
            if count == 2:
                notIn[1].append(word[1])
                if word[1] in greenLetters:
                    if word[1] not in yesIn[1]:
                        notIn[1].append(word[1])
                    if word[1] not in yesIn[2]:
                        notIn[2].append(word[1])
                    if word[1] not in yesIn[3]:
                        notIn[3].append(word[1])
                    if word[1] not in yesIn[4]:
                        notIn[4].append(word[1])
                if word[1] not in greenLetters:
                    if word[1] not in word[2]:
                        if word[1] not in word[3]:
                            if word[1] not in word[4]:
                                grayLetters.append(word[1])
            if count == 3:
                notIn[2].append(word[2])
                if word[2] in greenLetters:
                    if word[2] not in yesIn[3]:
                        notIn[2].append(word[3])
                    if word[2] not in yesIn[4]:
                        notIn[3].append(word[3])
                if word[2] not in greenLetters:
                    if word[2] not in word[3]:
                        if word[2] not in word[4]:
                            grayLetters.append(word[2])
            if count == 4:
                notIn[3].append(word[3])
                if word[3] in greenLetters:
                    if word[3] not in yesIn[4]:
                        notIn[3].append(word[3])
                if word[3] not in greenLetters:
                    if word[3] not in word[4]:
                        grayLetters.append(word[3])
            if count == 5:
                notIn[4].append(word[4])
                if word[4] not in greenLetters:
                    grayLetters.append(word[4])


        # Assign yellows
        if i == '1':
            if count == 1 and word[0] not in notIn[0]:
                notIn[0].append(word[0])
                if word[0] not in greenLetters:
                    greenLetters.append(word[0])
            if count == 2 and word[1] not in notIn[1]:
                notIn[1].append(word[1])
                if word[1] not in greenLetters:
                    greenLetters.append(word[1])
            if count == 3 and word[2] not in notIn[2]:
                notIn[2].append(word[2])
                if word[2] not in greenLetters:
                    greenLetters.append(word[2])
            if count == 4 and word[3] not in notIn[3]:
                notIn[3].append(word[3])
                if word[3] not in greenLetters:
                    greenLetters.append(word[3])
            if count == 5 and word[4] not in notIn[4]:
                notIn[4].append(word[4])
                if word[4] not in greenLetters:
                    greenLetters.append(word[4])

    # Remove words with gray letters
    grayLetterWords = []
    for i in grayLetters:
        for j in wordList:
            if i in j:
                grayLetterWords.append(j)
    wordList2 = []
    for i in wordList:
        if i not in grayLetterWords:
            wordList2.append(i)

    # Check for spot in word that has a known green
    wrongLetter = []
    for i in wordList2:
        if len(yesIn[0]) == 1:
            if i[0] not in yesIn[0]:
                wrongLetter.append(i)
        if len(yesIn[1]) == 1:
            if i[1] not in yesIn[1]:
                wrongLetter.append(i)
        if len(yesIn[2]) == 1:
            if i[2] not in yesIn[2]:
                wrongLetter.append(i)
        if len(yesIn[3]) == 1:
            if i[3] not in yesIn[3]:
                wrongLetter.append(i)
        if len(yesIn[4]) == 1:
            if i[4] not in yesIn[4]:
                wrongLetter.append(i)
    wordList3 = []
    for i in wordList2:
        if i not in wrongLetter:
            wordList3.append(i)

    # Remove words with wrong letter in known spot
    notRight = []
    for i in wordList3:
        if i[0] in notIn[0]:
            if i not in notRight:
                notRight.append(i)
        if i[1] in notIn[1]:
            if i not in notRight:
                notRight.append(i)
        if i[2] in notIn[2]:
            if i not in notRight:
                notRight.append(i)
        if i[3] in notIn[3]:
            if i not in notRight:
                notRight.append(i)
        if i[4] in notIn[4]:
            if i not in notRight:
                notRight.append(i)
    wordList4 = []
    for i in wordList3:
        if i not in notRight:
            wordList4.append(i)

    # remove words that don't have green letters
    notCorrect = []
    for i in wordList4:
        for j in greenLetters:
            if j not in i:
                if i not in notCorrect:
                    notCorrect.append(i)
    wordList5 = []
    for i in wordList4:
        if i not in notCorrect:
            wordList5.append(i)

    # Check if any possible words left
    roundCount += 1
    if len(wordList5) == 0:
        print("Out of Words")

    codeTrack = 0
    doubleLetter = '0'
    doubleStore = []
    wordList6 = []
    # Check if answer has a double letter
    for i in word:
        if code[codeTrack] == '1':
            doubleStore.append(i)
        if code[codeTrack] == '2':
            doubleStore.append(i)
        codeTrack += 1
    for i in doubleStore:
        if doubleStore.count(i) > 1:
            doubleTrack = True
            doubleLetter = i
        if doubleTrack:
            for j in wordList5:
                if j.count(doubleLetter) > 1:
                    if j not in wordList6:
                        wordList6.append(j)
    if not doubleTrack:
        wordList = wordList5
    if doubleTrack:
        wordList = wordList6
        if code != '22222':
            print('Double letter detected')


    # Find letters remaining with greatest frequency
    letters = [['a', 0], ['b', 0], ['c', 0], ['d', 0], ['e', 0], ['f', 0], ['g', 0], ['h', 0], ['i', 0],
               ['j', 0], ['k', 0], ['l', 0], ['m', 0], ['n', 0], ['o', 0], ['p', 0], ['q', 0], ['r', 0],
               ['s', 0], ['t', 0], ['u', 0], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0]]
    for p in wordList:
        letters[0][1] += p.count('a')
        letters[1][1] += p.count('b')
        letters[2][1] += p.count('c')
        letters[3][1] += p.count('d')
        letters[4][1] += p.count('e')
        letters[5][1] += p.count('f')
        letters[6][1] += p.count('g')
        letters[7][1] += p.count('h')
        letters[8][1] += p.count('i')
        letters[9][1] += p.count('j')
        letters[10][1] += p.count('k')
        letters[11][1] += p.count('l')
        letters[12][1] += p.count('m')
        letters[13][1] += p.count('n')
        letters[14][1] += p.count('o')
        letters[15][1] += p.count('p')
        letters[16][1] += p.count('q')
        letters[17][1] += p.count('r')
        letters[18][1] += p.count('s')
        letters[19][1] += p.count('t')
        letters[20][1] += p.count('u')
        letters[21][1] += p.count('v')
        letters[22][1] += p.count('w')
        letters[23][1] += p.count('x')
        letters[24][1] += p.count('y')
        letters[25][1] += p.count('z')

    # sort letter frequencies in ascending order
    letters.sort(key=lambda x: x[1])

    bestLetters = []
    bestLettersCount = 25

    while len(bestLetters) < 5 - len(greenLetters):
        if letters[bestLettersCount][0] not in greenLetters:
            bestLetters.append(letters[bestLettersCount][0])
        bestLettersCount -= 1

    tier1 = []
    tier2 = []
    tier3 = []
    tier4 = []
    tier5 = []

    for q in wordList:
        if len(bestLetters) == 1:
            if bestLetters[0] in q:
                tier1.append(q)

        if len(bestLetters) == 2:
            if bestLetters[0] in q:
                tier1.append(q)
                if bestLetters[1] in q:
                    tier2.append(q)
            if bestLetters[1] in q:
                if q not in tier1:
                    tier1.append(q)

        if len(bestLetters) == 3:
            if bestLetters[0] in q:
                if q not in tier1:
                    tier1.append(q)
                if bestLetters[1] in q:
                    if q not in tier2:
                        tier2.append(q)
                    if bestLetters[2] in q:
                        if q not in tier3:
                            tier3.append(q)
                if bestLetters[2] in q:
                    if q not in tier2:
                        tier2.append(q)
            if bestLetters[1] in q:
                if q not in tier1:
                    tier1.append(q)
                    if bestLetters[2] in q:
                        if q not in tier2:
                            tier2.append(q)
            if bestLetters[2] in q:
                if q not in tier1:
                    tier1.append(q)

        if len(bestLetters) == 5:
            bestLetters.remove(bestLetters[4])

        if len(bestLetters) == 4:
            if bestLetters[0] in q:
                if q not in tier1:
                    tier1.append(q)
                    if bestLetters[1] in q:
                        if q not in tier2:
                            tier2.append(q)
                            if bestLetters[2] in q:
                                if q not in tier3:
                                    tier3.append(q)
                                    if bestLetters[3] in q:
                                        if q not in tier4:
                                            tier4.append(q)
                            if bestLetters[3] in q:
                                if q not in tier3:
                                    tier3.append(q)
                    if bestLetters[2] in q:
                        if q not in tier2:
                            tier2.append(q)
                            if bestLetters[3] in q:
                                if q not in tier3:
                                    tier3.append(q)
                    if bestLetters[3] in q:
                        if q not in tier2:
                            tier2.append(q)
            if bestLetters[1] in q:
                if q not in tier1:
                    tier1.append(q)
                    if bestLetters[2] in q:
                        if q not in tier2:
                            tier2.append(q)
                            if bestLetters[3] in q:
                                if q not in tier3:
                                    tier3.append(q)
                    if bestLetters[3] in q:
                        if q not in tier2:
                            tier2.append(q)
            if bestLetters[2] in q:  # done
                if q not in tier1:
                    tier1.append(q)
                    if bestLetters[3] in q:
                        if q not in tier2:
                            tier2.append(q)
            if bestLetters[3] in q:  # done
                if q not in tier1:
                    tier1.append(q)

    a = 0
    if len(tier4) > 0:
        a = tier4[0]
    elif len(tier3) > 0:
        a = tier3[0]
    elif len(tier2) > 0:
        a = tier2[0]
    elif len(tier1) > 0:
        a = tier1[0]

    doubleTracker = 0
    doubleList = []
    for i in wordList:
        for j in i:
            if i.count(j) > 1:
                if i not in doubleList:
                    doubleList.append(i)
                    doubleTracker += 1

    if inPlay:
        if doubleTracker/len(wordList) > 0.75:
            a = doubleList[0]
            if code != '22222':
                print('Double Letter Word Probable')

    if inPlay:
        print(f'Possible: {wordList}')
        print(f'Suggestion: {a}')
        print(f'Total Reduction: {round((1 - ((len(wordList)) / reductionStats)) * 100, 4)}%  '
              f'Total Words Remaining: {len(wordList)}')
