from flask import Flask, jsonify, request
from uuid import uuid4
from urllib.parse import urlparse
import json
from Blockchain import Blockchain
from flask import Flask, jsonify, request
from uuid import uuid4
from urllib.parse import urlparse

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

node_address = str(uuid4()).replace('-', '')

blockchain = Blockchain()


@app.route('/create-new-block', methods=['POST'])
def create_new_block():
    jso = json.loads(request.data)
    new_prof = jso['new_prof']
    user_edden = jso['USER_EDDEN']
    previous_block = blockchain.get_previous_block()
    previous_hash = blockchain.hash(previous_block)

    blockchain.add_transaction(
        sender=node_address, receiver=user_edden, amount=1)
    block = blockchain.create_block(int(new_prof), previous_hash)

    response = {'message': 'Parabens voce acabou de minerar um bloco!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions': block['transactions']
                }
    return jsonify(response), 201


@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    blockchain.add_transaction(
        sender=node_address, receiver='USER_EDDEN', amount=1)

    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Parabens voce acabou de minerar um bloco!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions': block['transactions']
                }
    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': ' Tudo certo, o blockchain e valido '}
    else:
        response = {'message': ' O blockchain nao e valido '}
    return jsonify(response), 200


@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    jso = json.loads(request.data)

    transaction_keys = ['sender', 'receiver', 'amount']
    if not all(key in jso for key in transaction_keys):
        return 'Alguns elementos estao faltando', 400
    index = blockchain.add_transaction(
        jso['sender'], jso['receiver'], jso['amount'])
    response = {'message': f'Esta tramsacao sera adicionada ao bloco {index}'}
    return jsonify(response), 201


@app.route('/connect_node', methods=['POST'])
def connect_node():

    jso = json.loads(request.data)
    nodes = jso.get('nodes', None)

    print(nodes)
    if nodes is None:
        return "Vazio", 400
    for node in nodes:
        blockchain.add_node(node)

    print(blockchain.nodes)
    response = {'message': 'Todos nos conectados, blockchain contem os seguintes nos:',
                'total_nodes': blockchain.nodes}
    return jsonify(response), 201


@app.route('/replace_chain', methods=['GET'])
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'Os nos tinham cadeias diferentes então foi substituida ',
                    'new_chain': blockchain.chain}
    else:
        response = {'message': 'Tudo certo, nao houve substituicao ',
                    'actual_chain': blockchain.chain}
    return jsonify(response), 201


app.run(host='0.0.0.0', port=5000)
