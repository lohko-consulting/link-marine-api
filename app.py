from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

def checkInclusion(inputString,tree):
    op = []
    for key,value in tree.items():
        if inputString in key:
            op.append(value)
            inputString = value
    return op

@app.route('/api/get_proof', methods=['GET'])
def getProof():
    wallet = request.args.get('wallet')
    with open('merkletree.json') as json_file:
        tree = json.load(json_file)
        proof = checkInclusion(wallet, tree)
        return jsonify(proof), 201

if __name__ == '__main__':
  app.run(debug=True)