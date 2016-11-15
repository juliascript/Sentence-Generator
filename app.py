import weightedWordGenerator
from flask import Flask
app = Flask(__name__)

@app.route('/')
def generateSentence():
	sentence = weightedWordGenerator.generateSentenceFromTextfile('sampleText.txt')
    return sentence

# next step: make it possible to upload a text file then generate sentence from that corpus

if __name__ == "__main__":
	app.run()