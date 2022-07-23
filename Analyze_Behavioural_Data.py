#for dataset importing and visualization
import pandas as pd
## for cleaning purpose
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score


dataset = pd.read_csv('c_history.csv')
print(dataset)

## we will create an empty list where we will store the cleaned text
cleaned_data = []
for i in range(0, len(dataset)):
  review = re.sub('[^a-zA-Z]', ' ', str(dataset['texts'][i]))
  # review = str(dataset['texts'][i])
  review = review.lower()
  review = review.split()
  #Stemming the data
  stemmer = PorterStemmer()
  review = [stemmer.stem(word) for word in review if not word in set(stopwords.words('english'))]
  review = ' '.join(review)
  cleaned_data.append(review)

## printing the cleaned words line by line
for item in cleaned_data:
  print(item)

## we will create matrix of feautures from cleaned_data by converting the string list
## into 2-D matrix called as Matrix of Features by using the technique called vectorization.
cv = CountVectorizer(max_features = 1500)
x = cv.fit_transform(cleaned_data).toarray()
print(x)


y = dataset.iloc[:, -1] ## last column will be taken which consists of the interests
le = LabelEncoder()
y = le.fit_transform(y)
print(y)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train) ## here we are training the model so that we can use it later on


y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

# ## 1 - Study and 0 - Entertainment
# string = input("Enter a string-->",)
# new = []
# new.append(string)
# new = cv.transform(new).toarray()
# custom_predict = classifier.predict(new)
# if(custom_predict == 0):
#   print("User is Interested in Entertainment and fun")
# else:
#   print("User is interested in Education related content")