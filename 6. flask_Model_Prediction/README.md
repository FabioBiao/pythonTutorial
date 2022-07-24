# Model_Deployment

This a demo for a machine learning model deployment using flask both locally and on a public server.
Kindly refer to the following blog for detialed explanation
https://towardsdatascience.com/model-deployment-using-flask-c5dcbb6499c9


# create and start activate
```console
# Creating and setting virtual env
py -m venv env
. env/scripts/activate


# install dependencies
pip install flask numpy pandas sklearn joblib nltk
pip install -r requirements.txt

```
# run 
- python app.py

# requirements.txt : 
This file contains all the dependencies/libraries that would be used in the project (whenever a virtual environment is created it can use this requirements file directly to download all the dependencies you need not to install all the libraries manually, you just need to put all of them in this file)

# model.pkl :
This is our classification model, that we would be using, in this cases it is a Logistic Regression Model, which I had trained already.

# vectorizer.pkl :
This is vectorizer file that is used to convert text into a vector for the model to process, in this case we have used a tf-idf vectorizer