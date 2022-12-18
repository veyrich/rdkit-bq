from flask import Flask, request, jsonify, make_response
from rdkit import Chem
from rdkit.Chem import Descriptors
import random
import json
import decimal

app = Flask(__name__)


@app.route('/', methods=['POST'])
def calc_mw():

    data = request.get_data()
    results = []
    calls = request.get_json()['calls']
    print("# input rows: {}".format(len(calls)))
    for call in calls:
        molwt = mw(call[0])
        # use Decimal to convert to BQ Numeric
        if molwt:
            results.append(decimal.Decimal(molwt))
        else:
            results.append(None)

    resp = make_response(jsonify({'replies': results}))
    return resp


def mw(smi):
    m = Chem.MolFromSmiles(smi)
    if m:
        mw = Descriptors.ExactMolWt(m)
    else:
        mw = None
    return(mw)
