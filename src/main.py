from flask import Flask, request, abort

from src.document import discount

from src.transfer.create_transfer import transfer


app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    response = request.get_json()
    amount = discount(response)
    result = transfer(amount) 
    return 200, abort(400)
        



app.run()