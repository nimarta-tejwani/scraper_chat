from flask import Flask, render_template, request
from scrape import scrape_data_from_url
import response

app = Flask(__name__)

data = "No data"
url = ""


@app.route('/', methods=['GET', 'POST'])
def index():
    global data
    global url
    if request.method == 'POST':
        url = request.form['url']
        data = scrape_data_from_url(url)
        print(data)
        return render_template('chat.html', data=data, url=url)
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.json.get('user_input')  # Use .get() to avoid KeyError
        bot_response = response.get_response(user_input, data)
        print(bot_response)
        return {'bot_response': bot_response}
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
