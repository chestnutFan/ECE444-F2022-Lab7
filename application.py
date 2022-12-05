from flask import Flask, request, json, jsonify

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)

# Home page
@application.route('/')
def home():
    return "<h1>Welcome to Fake News Detector.</h1>"

# Fake news detector model
@application.route('/detector', methods=['GET'])
def detector():
    # get input
    text = request.args.get('text')

    if text is None:
        resp = jsonify({'error': 'Lack of input.'})
        resp.status_code = 400
        return resp
    
    # load and run the model
    model = None
    with open('./models/basic_classifier.pkl', 'rb') as fid:
        model = pickle.load(fid)
    vectorizer = None
    with open('./models/count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)

    pred = model.predict(vectorizer.transform([text]))[0]
    pred = 0 if pred == "REAL" else 1
    
    result = {
        "status_code": 200,
        "pred": pred
    }
    return result


if __name__ == '__main__':
    application.run()