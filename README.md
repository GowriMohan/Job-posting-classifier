# Job_posting_classifier

This project aims to create a web app classifier using Machine learning and Streamlit that will have the capability to identify fake and real jobs. It takes input features from the user in the web page and print whether the job is real/fake.

This project uses data provided from Kaggle which contains features that define a job posting. These job postings are categorized as either real or fake. Fake job postings are a very small fraction of this dataset(i.e, it is an imbalanced dataset), which is as excepted. We are using 8 features to check whether the job posting is fraudulent or not (i.e., Fake/Real).

For this project we splitted the dataset in two ways :
1. Dataset which takes up only the numerical columns or binary features and categorical columns.
2. Dataset that would consider textual features along with other features.

The main goal to convert these attributes into two forms is to classify fraudulent job advertisements without doing any text processing and natural language processing. In this work, we have used only those categorical attributes and binary features dropping newly added feature ‘text’ which contains all the textual information provided in job ads.

The best performed model is Random Forest Classifier with an accuracy of 92%.

The link to the deployed app is here:
            https://gowrimohan-job-posting-classifier-app-m6jdsb.streamlit.app/
