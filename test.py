# main.py
from app.blockchain import Blockchain

def main():
    # Blockchain 생성자를 이용해 인스턴스를 생성하고, 필요한 인자를 전달합니다.
    bitcoin = Blockchain()

    # previous_block_hash = '519619156945694516'
    # current_block_data = [
    #     {
    #         'amount' : 10,
    #         'sender' : 'BAD48461AB6',
    #         'recipient' : 'ag4a6e4g9a4w5eg',
    #     },
    #     {
    #         'amount' : 30,
    #         "sender" : '15DSGA86G4AD46GAE',
    #         'recipient' : 'aega6we16ga1we65g1',
    #     },
    #     {
    #         'amount' : 100,
    #         "sender" : 'GAWEKGAWE66GA16W1E1661',
    #         'recipient' : 'a6w191a9be156b1a',
    #     },
    # ]
    # nonce = 100


    bc1 = {
        "chain": [
            {
                "hash": "f5757e7ad64794f6510c8d81569821cf1b62fe1282a50d038c93cce5f2dabf1b",
                "index": 1,
                "merkle_root": "25294774fb9840be0cebea260ad8f3780016115f4dadc3bc240c04d56b8b659d",
                "nonce": 778,
                "previous_block_hash": "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9",
                "timestamp": 1684741214344,
                "transactions": [
                    {
                        "amount": 50,
                        "recipient": "5924c3cfa8764176a0fa388c10f65c65",
                        "sender": "0",
                        "transaction_id": "bb1ca545c0cd4c85b0ad84bd0fce528b"
                    }
                ]
            }
        ],
        "current_node_url": "http://localhost:5000",
        "genesis_nonce": 778,
        "merkle_tree_proecss": [],
        "network_nodes": [],
        "pending_transactions": [
            {
                "amount": 6.25,
                "recipient": "00",
                "sender": "00",
                "transaction_id": "40e912fcebb94d3f95e91bcf0a1295a8"
            }
        ]
    }

    

    print('VALID:', bitcoin.chain_is_valid(bc1['chain']))
    #print(bitcoin.hash_block(previous_block_hash,current_block_data,900))

if __name__ == "__main__":
    main()
