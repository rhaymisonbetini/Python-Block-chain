import datetime
import hashlib
import json
from flask import Flask, jsonify

# part one, create a new blockchain


class BlockChain:
    def __init__(self):
        
        self.chain = []

        self.create_block(proof=1, previous_hash='0')
