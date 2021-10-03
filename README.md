# Python-Block-chain

Simplified network construction project for mining and generating a blockchain.

# How to run:
Clone the repository with: <br/>
``` https://github.com/rhaymisonbetini/Python-Block-chain.git ```

After this process start the four different servers (eddens) one in each terminal <br/>
with the command:<br/>

``` $env:FLASK_APP = "app.py" ``` <br/>
``` flask run ``` <br/>

After this process, you must inform each server of the communication host between them.
through the CONNECT_NODES route that will receive the following parameter.

Where each host must be subsisted and added to its peers in JSON. <br>
The example below is connected to eden 5002 and updating my nodes <br/>

```
{
    "nodes": [
        "http://127.0.0.1:5001",
        "http://127.0.0.1:5003",
        "http://127.0.0.1:5000"
    ]
}
```

After this process you are able to mine, carry out transactions and update the blockchain chain on your network. <br/>

# Creating Transactions
To create transactions we will use the POST ADD_TRANSACTIONS route.

```
{
    "sender": "JULIO CAZAGRANDE",
    "receiver": "ANDRÉ CAVALEIRA",
    "amount": 0.0002
}
```
<br/>

All right. You will receive a message telling you which block your transaction will be added to once it is mined. <br/>

# Routes:
```[GET] get_chain ```: Route returns status 200 with entire blockchain chain up to last block mined

```[GET] is_valid```: Check blockchain chain integrity

```[GET] replace_chain``` : Route that scans with others
checking block updates in the block chain chain for
updating and validation of chains and new blocks

