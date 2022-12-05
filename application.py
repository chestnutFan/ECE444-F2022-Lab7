from flask import Flask, request, json, jsonify

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)


@application.route('/')
def home():
    """
    Show home page.
    """
    return "Welcome to Fake News Detector."


@application.route('/detector', methods=['GET'])
def detector():
    """
    Fake news detector model
    """
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

    output = model.predict(vectorizer.transform([text]))[0]
    output = 0 if output == "REAL" else 1
    
    response = {
        "status_code": 200,
        "output": output
    }
    return response


if __name__ == '__main__':
    application.run()