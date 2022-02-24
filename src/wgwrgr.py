from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    
    else:
        abort(400)


@app.route('/invoices', methods=['POST'])
def create_invoices():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    
    else:
        abort(400)


app.run()