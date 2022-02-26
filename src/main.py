from flask import Flask, request, Response

from src.document import discount
from src.transfer.create_transfer import transfer


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        response = request.get_json()
        amount = discount(response)
        result = transfer(amount)
        [print(r) for r in result]
        return Response('OK', status=200)
        

app.run()
