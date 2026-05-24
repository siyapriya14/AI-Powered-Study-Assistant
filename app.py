from flask import Flask, render_template, request
import pdfplumber

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['pdf']

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            extracted_text = page.extract_text()

            if extracted_text:
                text += extracted_text

    sentences = text.split('.')

    summary = '.'.join(sentences[:8])

    return render_template(
    'index.html',
    summary=summary,
    message="PDF uploaded successfully!"
)

if __name__ == '__main__':
    app.run(debug=True)