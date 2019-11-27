## Alexa Sentiment-Analysis
---
### Overview:
----
The objective of this project is to build sentiment analyzer to predict weather the review falls under positive sentiment or negative.

### DataSet:
-----
* Source: https://www.kaggle.com/sid321axn/amazon-alexa-reviews/data
* Observations: 3150
* Features: 6

### Data Visualization:
-----
![Feed_rating](https://github.com/ShehzadaAlam/Alexa-Review-Sentiment-Analysis/blob/master/Images/Distribution.png)

* Its seems that positive class is more than the negative class, which indicate imbalance of class.
* Moreover there are more people has provided rating of 5 star to Alexa product which indicate that customer is satosfied with the product.

* Wordcloud: All words, Positive and Negative
![Wordcloud](https://github.com/ShehzadaAlam/Alexa-Review-Sentiment-Analysis/blob/master/Images/Wordcloud.png)

### Model Building:
----
##### Machine Learning Model:
Model | Accuracy Score | AUC ROC Score
----- | ----- | -----
Naive Bayes + BOW | 93 % | 60 %
Naive Bayes + TFIDF | 91 % | 50 %
SVM + BOW | 93 % | 75 %
SVM + TFIDF | 93 % | 61 %


##### Deep Learning Model:
----
Model | Accuracy Score | AUC ROC Score
----- | ----- | -----
BiLSTM | 94 % | 89 % 
Multi Conv Net Architecture | 95 % | 94 % 

**Sequential Model**
!['Sequential'](https://github.com/ShehzadaAlam/Alexa-Review-Sentiment-Analysis/blob/master/Images/model.png)

**Functional API**
!['Functional API'](https://github.com/ShehzadaAlam/Alexa-Review-Sentiment-Analysis/blob/master/Images/Model_Custom.png)


### Streamlit Deployment:
----
- Model Deplayment was done using streamlit.
* If you've entred nothing.
![nothing Entered](https://github.com/ShehzadaAlam/Alexa-Review-Sentiment-Analysis/blob/master/Images/if%20you%20enter%20nothing.PNG)
* Positive Sentiment.
![positive sentiment](https://github.com/ShehzadaAlam/Alexa-Review-Sentiment-Analysis/blob/master/Images/Positive%20Sentiment.PNG)
* Negative Sentiment
![negative sentiment](https://github.com/ShehzadaAlam/Alexa-Review-Sentiment-Analysis/blob/master/Images/negative%20sentiment.PNG)


----
<p>Thank You!	
<p><!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/ShehzadaAlam" aria-label="Follow @ShehzadaAlam on GitHub">Follow @ShehzadaAlam</a>
