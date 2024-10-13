from flask import Flask, render_template, request
import joblib
from wordcloud import WordCloud
from nltk.sentiment import SentimentIntensityAnalyzer

model = joblib.load('./model/SVC_Model.joblib')
vectorizer = joblib.load('./model/vectorizer.joblib')
sia = SentimentIntensityAnalyzer()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def showIndex():
    return render_template('index.html')

@app.post('/predict')
def predictText():
    text = request.form['content']

    textVector = vectorizer.transform([text])
    prediction = model.predict(textVector)
    Sentiment = sia.polarity_scores(text)
    Sentiment.pop('compound')
    sentimentTag = max(Sentiment.values())

    return render_template('prediction.html', prediction=prediction, cloud=makeCloud(text), sentimentVal = Sentiment[sentimentTag], sentimentTitle = sentimentTag)

def makeCloud(text):
    wordcloud = WordCloud().generate(text)
    return wordcloud

if __name__ == '__main__':
    app.run(debug=True)
