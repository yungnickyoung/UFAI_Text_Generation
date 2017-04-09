from flask import Flask, render_template, request
from neural_net_1 import run_neural_net
from text_generation import run_text_generation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')


@app.route('/displaytext', methods=['GET', 'POST'])
def save_inputText():
    if request.method == 'POST':
        f = request.form['inputText']
        with open(f, "r") as g:
               rawText = g.read()
        rawText = rawText.lower()
        run_neural_net(rawText)
        output = run_text_generation(rawText)
        return render_template('displaytext.html', inputText=output)

if __name__ == '__main__':
    app.run(debug=True)
