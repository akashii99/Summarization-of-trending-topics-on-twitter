# Summarization-of-trending-topics-on-twitter

Automatically summarizing, the most widely discussed topics on Twitter each hour. The summary would be short but adequate to understand. Any person appearing in between on Twitter would be able to read and understand the most trending topic of the hour. 

LDA is used for topic detection on the tweets, extracting keywords for better scrapping of web documents.

NLP Techniques applied- Stemming, Lemmatization, Stop words removal, text document summarization, tf-idf weighing and similarity scores like cosine and Jaccard.

### For extracting tweets of a particular - Run tweetexport.py
### For preprocessing of tweets and implementation of LDA  - LDA/lda_mission.ipynb

<img src="https://github.com/akashii99/Summarization-of-trending-topics-on-twitter/blob/master/lda2.png">

### Results of LDA implementation on our dataset
5 Topics related to Mission Shakti:
  1. Missile
  2. Satellite
  3. अंत रक्ष
  4. Space
  5. India

5 Topics related to World Poetry Day:
  1. Beautiful
  2. Sound
  3. Rhythm
  4. poem
  5. tread
### For Tweet Clustering  - Tweet_Clustering.ipynb

#### Experiment - 
Evaluated Tweet Clustering on 3 different topic using K-means and generated keywords related to each topic.

Topics - Politics, Sports and Entertainment.

### For Web Scraping and Extractive Summarization  - 
1. Demo_WebScraping&Summary.ipynb 
2. Short_Scrapping&ExtSummarization.ipynb 
3. Scrapping&ExtSummarization.ipynb

<img src="https://github.com/akashii99/Summarization-of-trending-topics-on-twitter/blob/master/Summarization%20Flowchart.png">

### Steps :
1. Perform Extractive Summarization using Topic Representation technique. Works by selecting a subset of existing words, phrases, or sentences in the original text to form the summary.
2. Compute the similarity scores of summaries generated in first step to reduce the contribution of an unrelated article in the final summarization step by dropping those summaries with similarity less than 50% (score < 0.5).
3. TSES - 
### Follow the paper - Al-Hashemi, R. (2010). Text Summarization Extraction System (TSES) Using Extracted Keywords.
Extract relevant words and phrases : 

  ○ Term Frequency (TF) & Inverse Document Frequency (IDF)
  
  ○ Existence in Document Title and Font Type
  
  ○ Part of Speech(POS) - Discover new set of pattern that are frequent. Extract phrases matching the pattern
  
  ○ Document Classification into categories
  
Sentence Filtering using Sentence positioning, Sentence Length cut-off score, Post-Processing by removing redundant sentences, removing sentences having similarity > 65%, replace phrases using KFIDF measurement.


### For Checking the similarity between two documents - TFIDF_&_Cosine_Similarity.ipynb

## Evaluation
Comparison of our summary with Google and Microsoft Word Summarizer. Can also be compared with author’s summary.
Compute Similarity Score between both of them which can be used to compare the performance of our system. Cosine Similarity and Jaccard Similarity are most common measures used for this purpose.

Cosine Similarity Score of our summary with Microsoft Word Summarizer
#### Similarity Score = 0.893
