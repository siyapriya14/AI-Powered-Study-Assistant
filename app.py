from flask import Flask, render_template, request
import pdfplumber

app = Flask(__name__)

pdf_text = ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    global pdf_text

    file = request.files['pdf']

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            extracted_text = page.extract_text()

            if extracted_text:
                text += extracted_text

    pdf_text = text

    sentences = text.split('.')

    summary = '.'.join(sentences[:8])

    return render_template(
        'index.html',
        summary=summary,
        message="PDF uploaded successfully!"
    )

@app.route('/quiz', methods=['POST'])
def quiz():

    global pdf_text

    sentences = pdf_text.split('.')

    questions = []

    for i in range(min(5, len(sentences))):

        sentence = sentences[i].strip()

        if sentence:

            questions.append(
                f"Q{i+1}. Explain: {sentence}?"
            )

    return render_template(
        'index.html',
        questions=questions
    )

@app.route('/chat', methods=['POST'])
def chat():

    global pdf_text

    user_question = request.form['question']

    answer = ""

    if user_question.lower() in pdf_text.lower():

        answer = "Yes! This topic exists in the PDF."

    else:

        answer = "Sorry, I could not find this topic in the PDF."

    return render_template(
        'index.html',
        answer=answer
    )

if __name__ == '__main__':
    app.run(debug=True)