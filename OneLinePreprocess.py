
def extract_features(document):
   features={}
   for word in set(document.split()):
       if len(word) > 2:
          features['contains(%s)' % word.lower()] = True
   return features

documents=[]
f = open("train_data.csv","r")
for document in f.readlines():
   parts= document.strip().split("\t")
   documents.append((parts[1],bool(int(parts[0]))))

print documents[0]


import random
random.seed(1234)
random.shuffle(documents)
import nltk
n_train = int(0.8*len(documents))
training_set = nltk.classify.apply_features(extract_features,documents[:n_train])
test_set = nltk.classify.apply_features(extract_features,documents[n_train:])

print training_set[0]

classifier = nltk.NaiveBayesClassifier.train(training_set)
nltk.classify.accuracy(classifier, test_set)

print classifier.classify(extract_features("that was not a bad movie"))




