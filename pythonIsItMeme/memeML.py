import scikit
import tree
import nltk

#Features are weight and bumbpiness
#features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# Corresponding labels (apple or orange) for the weights
#labels = [0, 0, 1, 1]

#Create our features and lables
#1 for meme, 0 for not meme
features = []
labels = []

#Read in our meme training data
memeTrainList = [];

with open('trainingDataMeme', 'r') as f:
    for line in f:
        memeTrainList.append(line)

#Now use NLP to the strings
memeTrainTokens = [];
for meme in memeTrainList:
    memeTrainTokens.append(nltk.pos_tag(nltk.word_tokenize(meme)))

#Add our memes to our trainindgdata
for i in range(0, len(memeTrainList) - 1):
    tempArray = {memeTrainList[i], memeTrainTokens[i]}
    features.append(tempArray)
    labels.append(1)

#Read in our non-meme training data
noMemeTrainList = [];

with open('trainingDataNoMeme', 'r') as f:
    for line in f:
        noMemeTrainList.append(line)

#Now use NLP to the strings
noMemeTrainTokens = [];
for meme in memeTrainList:
    noMemeTrainTokens.append(nltk.pos_tag(nltk.word_tokenize(meme)))

#Add our non-memes to our trainindgdata
for i in range(0, len(noMemeTrainList) - 1):
    tempArray = {noMemeTrainList[i], noMemeTrainTokens[i]}
    features.append(tempArray)
    labels.append(0)

#Using a decision tree classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

#Read in our testing
testingList = [];

with open('testingData', 'r') as f:
    for line in f:
        testing.append(line)

#Now use NLP to the strings
testingTokens = [];
for meme in testingList:
    testingTokens.append(nltk.pos_tag(nltk.word_tokenize(meme)))

#Test the testing data!
for i in range(0, len(testingList) - 1):
    tempArray = {testingList[i], testingTokens[i]}
    print clf.predict(tempArray)
