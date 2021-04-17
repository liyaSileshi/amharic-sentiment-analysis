# coling_dataset
More than 300k Amharic tweets are collected using twitter API.  After preprocessing about 9000 tweets remain. 
Then the dataset is divided in a ration of 10%, 10% and 80% for test, development and training sets respectively.  
The dataset folder contain all the three files. In each file
text the tweet id and sentiment of a tweets are presented. 

Amharic Sentiment Analysis Dataset
==================================================


### Contact

anonymous

### Citation

When using the data in your research or publication, please the paper entiled: "Investigating the Challenges in Amharic Sentiment Analysis: Building Annotation Tools and Classification Models"



Datasets
--------

### Description

The dataset is based on Twitter datasource colected in the months of December 2019 and January 2020, targeting only tweets written in the 'Fidel' script.
Out of 300k tweets collected, we select tweets based Amharic sentiment lexicons (around 1200 lexicons), a tweet is selected when it contains at least one lexicon. At the end, 9389 tweets are annotated, each tweet by three annotators, using the ASAB social media based annotation tool.

### Data Format
The data is formated as comma separated value (csv) where each line contains a tweet id and the sentiment annotation. If you need the cleaned tweets, contact as:  anonymous

```
1213084822521950209,neutral
1213011490372038656,neutral
1213763702715043840,mixed
1213764224356421633,neutral
1212766574337150976,positive
```

### Data Instances

The data is split in 90:10:10. The size of the tarining, development and test set will be: 7511, 939, 939 instances



