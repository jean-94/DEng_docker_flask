from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'status code = 200'

@app.route('/mean', methods = ['GET'])
def mean():
    values_str = request.args.get('values', type=str)
    print(values_str, type(values_str))
    try :
        values = values_str.split(',')
        values = map(float, values)
        values = list(values)
        mean = sum(values)/len(values)
        return f'Mean({values_str}) = {str(mean)}'
    except ValueError :
        return 'List of values is empty or is not numbers. :c \n Enter a proper list of value to compute the mean'