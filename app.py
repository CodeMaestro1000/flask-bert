
from flask import Flask, render_template, request
from forms import TextForm
from summarizer import Summarizer
# from flask_ngrok import run_with_ngrok

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# run_with_ngrok(app)

global model = None

@app.route("/")
@app.route("/home")
def home():
	model = Summarizer()
	form = TextForm()
	return render_template('index.html', form=form)

@app.route("/summarize", methods=['GET', 'POST'])
def summarize():
	if request.method == 'POST':
		text = request.form['content']
		result = model(body=text, ratio=0.2)
		summary = result.split('.')
		return render_template('summary.html', summary=summary)


if __name__ == '__main__':
	app.run()
