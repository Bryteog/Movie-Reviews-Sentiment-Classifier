#### Overview

Built a model to classify movie reviews as one of five classes; "Negative", "Somewhat Negative", "Neutral", "Somewhat Positive", and "Positive". The dataset, "Sentiment-analysis-on-movie-reviews" is obtained from [kaggle](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews). The data directory contains a train file with the labels: "PhraseId", "SentenceId", "Phrase" and "Sentiment", a test file with labels: "PhraseId", "SentenceId" and "Phrase", and a sample submission file, all in tsv format. Data analysis is done with the Pandas library.


#### Model

Text preprocessing is done to remove punctuation signs and assign embeddings to text with the Keras library.
The data is divided into three parts, training testing and validating sets. A bidirectional LSTM with tahn activation is used along with a couple of dense layers. The last layer has 4 units with softmax activation. The model is trainined for 30 epochs and reaches a loss of 0.0350 on the training set and 0.0308 on validation set.