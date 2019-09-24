import os

import requests
from flask import Flask, send_file, Response, redirect
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def get_pig_latin(text_string):
    request_url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    input_text = {"input_text": text_string}
    response = requests.post(request_url, data=input_text, allow_redirects=False)

    return response.headers.get('location')


@app.route('/')
def home():
    new_fact = get_fact().strip()
    link_url = get_pig_latin(new_fact)
    # body = f"<a href={link_url}>{link_url}</a>"
    return redirect(link_url)
    # return Response(response=body)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
