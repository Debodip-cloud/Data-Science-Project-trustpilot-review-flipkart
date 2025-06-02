# Data-Science-Project-trustpilot-review-flipkart
This is a data Science master project. It a comprehensive data science project involving analyzing Trustpilot reviews of Flipkart. Here, I do webscraping and analysis of trustpilot reviews on flipkart.
## Objectives

* Extract data through webscraping
* Sentiment analysis and prediction
* Predicting Rating from Content
* Visualising sentiment distribution
* Finding and Visualising top keywords in each rating
* Visualising how sentiment correlates with actual ratings


## Achievements
🔍 Project Overview:
I successfully scraped 971 Trustpilot reviews spanning around 50 pages, leveraging dynamic web scraping techniques and pagination to ensure comprehensive data extraction. My dataset included key columns: content, title, and rating.

🧹 Data Cleaning:
I meticulously cleaned the dataset by handling missing values, removing URLs, punctuation, and performing lemmatization and stopword removal for better text processing.

📊 EDA & Sentiment Analysis:
I carried out exploratory data analysis (EDA) to understand sentiment distribution and patterns. For sentiment labeling, I used polarity scores to categorize reviews into positive, neutral, and negative sentiments.

💾 Data Storage:
To ensure data integrity and remote accessibility, I created a MongoDB database and stored the cleaned dataset for backup.

🤖 Model Development:
For sentiment prediction, I built and tested several machine learning models including XGBoost, SVM, and Logistic Regression, performing hyperparameter tuning to find the optimal configuration. My final selected model achieved a high accuracy of 81% for predicting sentiment labels.

🚀 Deep Learning with TensorFlow and Keras:
I went a step further and built a Convolutional Neural Network (CNN) using TensorFlow and Keras for improved sentiment prediction.
Here’s a quick breakdown of my final model:

  Input: Tokenized and padded sequences from review content

  Embedding layer: To convert text to vector representations

  Conv1D layer: To capture local patterns in the text

  Global Max Pooling: For dimensionality reduction

  Dense layers: For final classification

  Dropout layers: To prevent overfitting

  Tuned hyperparameters using Keras Tuner’s RandomSearch for best performance

  Achieved test accuracy of 81% on sentiment prediction

🌟 Model Deployment:
I deployed the final model using Flask to create an interactive web API for real-time predictions.

📈 Rating Prediction Model:
I also built a separate machine learning model to predict ratings (1-5) from the review content.

Achieved an impressive accuracy of 99% in rating prediction!

Encountered and overcame class imbalance in the dataset using SMOTE (Synthetic Minority Over-sampling Technique) to ensure fair representation of all classes.

I built an interactive Power BI dashboard showcasing:
✅ Sentiment distribution
✅ Top keywords in each rating category
✅ The relationship between sentiment and rating
✅ Overall insights from the reviews

#DataScience #NLP #WebScraping #DeepLearning #TrustpilotReviews #Flipkart #SentimentAnalysis #MachineLearning #PowerBI #TensorFlow #Keras #Flask
