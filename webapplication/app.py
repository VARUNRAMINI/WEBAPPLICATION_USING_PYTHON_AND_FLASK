from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

@app.route('/')
def index():
    return render_template('index.html', translations={})

@app.route('/translate', methods=['POST'])
def translate():
    source_text = request.form['source_text']
    target_language = request.form['target_language']
    translation = translate_text(source_text, target_language)
    return render_template('index.html', translations={target_language: translation})

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0',port=5000)
