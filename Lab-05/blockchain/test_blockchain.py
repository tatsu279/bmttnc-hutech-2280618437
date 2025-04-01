from blockchain import Blockchain

my_blockchain = Blockchain()

my_blockchain.add_transaction(sender="Alice", recipient="Bob", amount=50)
my_blockchain.add_transaction(sender="Bob", recipient="Charlie", amount=30)
my_blockchain.add_transaction(sender="Charlie", recipient="David", amount=20)

#mine a block
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction(sender="Miner", recipient="Alice", amount=10)
new_block = my_blockchain.create_block(new_proof, previous_hash)

# Print the blockchain  
for block in my_blockchain.chain:
    print(f"Block Index:", block.index)
    print("Block Timestamp:", block.timestamp)
    print("Block Transactions:", block.transactions)
    print("Block Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    
# Check if the blockchain is valid
print("Is the blockchain valid?", my_blockchain.is_chain_valid(my_blockchain.chain))


