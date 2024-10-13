from flask import Flask, render_template, request
import joblib
from wordcloud import WordCloud
from nltk.sentiment import SentimentIntensityAnalyzer
from predictTag import get_category

model = joblib.load('model/svc_model_77_better.joblib')
vectorizer = joblib.load('model/vectorier.joblib')
sia = SentimentIntensityAnalyzer()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def showIndex():
    return render_template('index.html')

@app.post('/predict')
def predictText():
    text = request.form.get('text')
    print(text)
    textVector = vectorizer.transform([text])
    prediction = model.predict(textVector)
    Sentiment = sia.polarity_scores(text)
    Sentiment.pop('compound')
    sentimentTag = max(Sentiment.values())
    print(prediction)
    print(Sentiment)
    return render_template('prediction.html', prediction=get_category(prediction[0]), cloud=makeCloud(text), sentimentVal = sentimentTag, sentimentTitle = list(Sentiment.keys())[list(Sentiment.values()).index(sentimentTag)])

def makeCloud(text):
    wordcloud = WordCloud().generate(text)
    return wordcloud

if __name__ == '__main__':
    app.run(debug=True)
