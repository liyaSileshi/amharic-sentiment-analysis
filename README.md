# Sentiment Analysis for Amharic Language

# Project Description

Amharic is one of the 86 languages spoken in Ethiopia. It is the "working language" of the federal government. 

The goal of this project is to have a more accurate sentiment analysis for Amharic language. The data that I will be using is an annotated data (tweet_ID with label of Positive, Negative or Neutral).

The potential value is that there isn't a robust sentiment classifier for low-resource languages such as Amharic, so by working on a model hopefully I will improve the accuracy of the model.

## Dataset

The dataset I will be using is composed of 9.4k Amharic tweets that are pre-classified as Positive, Negative or neutral. 

[Link to data & description](https://github.com/uhh-lt/ASAB/tree/main/data)

## MVP

A more accurate classification/NLP model that predict new Amharic tweets as Positive, Negative or Neutral.

Input: A tweet written in Amharic

Output: Positive, Negative or Neutral

## Goals

The Amharic language is one of the low-resource languages and there have been some researches done in sentiment analysis. The goal of this project is to have a more accurate sentiment analysis for Amharic sentences by improving upon techniques used by previous researchers and also using pre-trained models that have a similar language structure with Amharic but with a high resource by utilizing transfer learning. 

## Stretch Goals

- Add a feature for sarcasm detection

### Justification that the scope of your project is appropriate for 6 weeks with respect to learning curve, compute and storage resources

In order to successfully implement this project, I will do more research on NLP models, measuring and improving accuracy of NLP models. I will be using Google Colab notebook for running my model with GPU runtime.

# Articles and Research Papers

## Research Papers

[https://www.aclweb.org/anthology/2020.coling-main.91.pdf](https://www.aclweb.org/anthology/2020.coling-main.91.pdf)

[https://www.hilcoe.net/wp-content/uploads/2020/08/V2N2Paper12.pdf](https://www.hilcoe.net/wp-content/uploads/2020/08/V2N2Paper12.pdf)

[http://etd.aau.edu.et/bitstream/handle/123456789/3029/Selama Gebremeskel.pdf?sequence=1&isAllowed=y](http://etd.aau.edu.et/bitstream/handle/123456789/3029/Selama%20Gebremeskel.pdf?sequence=1&isAllowed=y)

[https://arxiv.org/pdf/2104.02516v1.pdf](https://arxiv.org/pdf/2104.02516v1.pdf)

[https://www.researchgate.net/publication/331673959_DEEP_LEARNING_APPROACH_FOR_AMHARIC_SENTIMENT_ANALYSIS_UNIVERSITY_OF_GONDAR](https://www.researchgate.net/publication/331673959_DEEP_LEARNING_APPROACH_FOR_AMHARIC_SENTIMENT_ANALYSIS_UNIVERSITY_OF_GONDAR)

### Summary #1

Research: [https://www.aclweb.org/anthology/2020.coling-main.91.pdf](https://www.aclweb.org/anthology/2020.coling-main.91.pdf)

This research focused on the development of an annotation tool for Amharic tweets and the sentiment analysis for the data gathered. Since the annotation tools that already exist don't support Amharic, they made a user-friendly annotation tool using a telegram bot. They used this bot to annotate each tweet. Each tweet is annotated by 3 different telegram users. The 3 choices to annotate was Positive, Negative or Neutral. They then used different deep learning text classifiers and supervised classifiers. Their research shows FLAIR deep learning model outperforms the other models that they've experimented on.

### Summary #2

Research: [https://www.hilcoe.net/wp-content/uploads/2020/08/V2N2Paper12.pdf](https://www.hilcoe.net/wp-content/uploads/2020/08/V2N2Paper12.pdf)

They used SVM model to classify Amharic online posts as Positive or Negative. Because of its morphological complexity of Amharic, it was difficult to find data to work with. The preprocessing included converting the transliteration from Latin to Ethiopic, manually annotating the corpus using polarity scales instead of binary values of Positive and Negative. The scaling values were integers from -2 up to +2. -2 being more negative and +2 being more positive. A value of 0 is neutral. They also had to change words to their base form by removing the inflectional morphemes. For this, they used a python tool called [HornMorpho](https://github.com/hltdi/HornMorpho) that converts a given word into its morphological analysis form. They used the Naïve Bayes machine learning algorithm and used unigram, bigram, and hybrid variants as features. 

### Summary #3

Research: [http://etd.aau.edu.et/bitstream/handle/123456789/3029/Selama Gebremeskel.pdf?sequence=1&isAllowed=y](http://etd.aau.edu.et/bitstream/handle/123456789/3029/Selama%20Gebremeskel.pdf?sequence=1&isAllowed=y)

This research work has tried to go through the techniques of sentiment mining for opinionated
Amharic texts. To classify a given opinionated document or text into predefined classes, the
opinionated document passes through pre-processing, detection of sentiment words, weight
assignment and polarity classification processes. Pre-processing involves normalization and
tokenization. The detection of sentiment words is a process of detecting polarity words and
contextual valence shifters based on the sentiment lexicon. Weight assignment and polarity
propagation is responsible for assigning an initial weight for detected sentiment terms and
propagating polarity value of sentiment terms that are linked to contextual valence shifters. (pg 66)

### Summary #4

Research: [https://arxiv.org/pdf/2104.02516v1.pdf](https://arxiv.org/pdf/2104.02516v1.pdf)

This project focused on 3 things. 

1, incentivized the crowd-sourcing, collection and curation of language datasets through an online quantitative and qualitative challenge

2, supported research fellows for a period of 3-4 months to create datasets annotated for NLP tasks

3,  hosted competitive Machine Learning challenges on the basis of these datasets

It explains due to the low-resource of African languages, Africa has been left out of NLP advancement. And the project aims to help in increasing resources for African languages.

### Summary #5

Research: [https://www.researchgate.net/publication/331673959_DEEP_LEARNING_APPROACH_FOR_AMHARIC_SENTIMENT_ANALYSIS_UNIVERSITY_OF_GONDAR](https://www.researchgate.net/publication/331673959_DEEP_LEARNING_APPROACH_FOR_AMHARIC_SENTIMENT_ANALYSIS_UNIVERSITY_OF_GONDAR)

The two researchers in this research extracted data from Fana Broadcasting Corporation (FBC) facebook page. They chose FBC media because it's one of the top media services in Ethiopia and it covers social, economical, and political subjects. They used manual annotation for each post which was annotated by linguistic experts. They used a similar technique as Summary#2 where instead of classifying posts in binary as positive or negative, they had seven classes ranging from extremely negative to extremely positive. They also had a table that summarized what tools, models, classes, features, etc. other researchers have used which was very helpful to review. They did 3 different experiments. The dataset size they used for the first two was 600 and the third one was 1000. Their experiment and research were fairly different from the rest because they put emoji into consideration when annotating each post. The highest score that they were able to achieve was an approximately 96% and that was on their first experiment. 

## Articles

### Summary #6

[https://towardsdatascience.com/sentiment-analysis-for-low-resourced-languages-on-social-media-128bf01f2547](https://towardsdatascience.com/sentiment-analysis-for-low-resourced-languages-on-social-media-128bf01f2547)

This article is focused on how sentiment analysis was done on the Arabizi. "Arabizi is a very informal transcription of the spoken Dialectal Arabic in Latin script". The structure of the Arabic language is similar to Amharic because they're both agglutinative so it was an interesting read. One word could have many inflection points meaning it can be an origin to hundreds of other words in Arabic. And because of that, it is quite difficult to classify a sentiment as positive or negative by just seeing the word. Similar to Amharic, there is no standard way to spell some words because there are some letters in the alphabet that are phonetically similar but are different letters and they can be used interchangeably. There is also the problem of having many dialects for one language. All this and more reasons increase the lexical sparsity of the language. In addition, Arabizi is popular for its codeswitching. Codeswitching is when you are switching between two languages in your sentences. This is pretty common in social media posts according to the writer. It's also common in the Amharic language. 

# Summary of research and articles

The rise of social media has helped in collecting a lot of data for making analysis, and prediction models. Sentiment analysis is one of the popular benefits that came about due to this mass data. Languages such as English were easier to do a model on because the data was already labeled and there was many available corpus for English. 
However, there are many languages out there that are difficult to do sentiment analysis on. We call them low-resource languages. The structure of these languages makes it really hard to build a model because of lack of availability of labeled data, and because of their many dialects and how their words are structures. 

Amharic is one of the low-resource languages. Because of the scarcity of labeled data, it's been quite difficult to make an NLP model for sentiment analysis. However, recent researchers and Data Scientists are using platforms such as Telegram bots to label already existing Amharic tweets by asking users whether they are Positive, Negative or Neutral. Using this data, they were able to build models to classify Amharic tweets. But even then, it is quite difficult sometimes to classify a tweet since it's hard to tell sarcasm in tweets and their data collection didn't account for that.

# Implementation Plan

- [ ]  Exploration of the tweet datasets of ASAB
- [ ]  Start from analyzing the already built models from other researches ([models](https://github.com/uhh-lt/ASAB/tree/main/model))
- [ ]  Find a high-resource language that is similar to Amharic in its structure (Germany and Arabic is similar by their morpheme structure)
- [ ]  Start with a pre-trained model from the high-resource language and use transfer learning
- [ ]  Work on improving it's accuracy
- [ ]  Built different types of NLP models and compare their accuracies for the given data

# Resources

[https://linguaphiles.livejournal.com/716083.html](https://linguaphiles.livejournal.com/716083.html)

[https://www.findke.ovgu.de/findke/en/Research/Data+Sets/Contemporary+Amharic+Corpus+(CACO)-p-1142.html](https://www.findke.ovgu.de/findke/en/Research/Data+Sets/Contemporary+Amharic+Corpus+%28CACO%29-p-1142.html)

[https://github.com/hltdi/HornMorpho](https://github.com/hltdi/HornMorpho)