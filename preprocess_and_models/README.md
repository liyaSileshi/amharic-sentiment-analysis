This folder contains the script for preprocessing the extracted twitter data and the 4 models built on the twitter dataset.


The 4 models I used for my sentiment analysis was Naive Bayes with Count Vectorizer, Naive Bayes model with TFIDF vectorizer, Text blob sentiment, and SVM. 
Both the Naive Bayes had an accuracy of ~21%, but when the Mixed sentiments were removed from the datasets, the accuracy increased to ~32%. 
The text blob sentiment model has an accuracy of ~45.9%. A lot higher than the Naive Bayes model. 
The last working model I currently have is the SVM model. It has an accuracy of 50.7% with mixed sentiments removed. The model further improves to 70% when the classification is binary (positive/ negative). This shows that the model performs well when the dataset is composed of only 2 classifications. 