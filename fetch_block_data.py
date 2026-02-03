from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

def get_block(block_number):
    block = w3.eth.get_block(block_number, full_transactions=True)

    return {
        "block_number": block.number,
        "timestamp": block.timestamp,
        "transactions_count": len(block.transactions)
    }

if __name__ == "__main__":
    latest_block = w3.eth.block_number
    data = get_block(latest_block)

    with open("block_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Block data saved successfully.")
