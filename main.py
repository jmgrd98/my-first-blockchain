import hashlib

def generateHash(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self, hash, data, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash

class BlockChain:
    def __init__(self):
        hashLast = generateHash("last_gen")
        hashFirst = generateHash("first_gen")
        self.chain = []
        self.genesis_block()

    def genesis_block(self):
        genesis = Block(generateHash("Genesis"), "Genesis", None)
        self.chain.append(genesis)

    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        hash = generateHash(data + prev_hash)
        block = Block(hash, data, prev_hash)
        self.chain.append(block)

    def print_chain(self):
        for block in self.chain:
            print("Data: " + block.data)
            print("Hash: " + block.hash)
            print("Previous Hash: " + str(block.prev_hash))
            print()

if __name__ == "__main__":
    blockchain = BlockChain()
    blockchain.add_block("First Block")
    blockchain.add_block("Second Block")
    blockchain.add_block("Third Block")
    blockchain.print_chain()
