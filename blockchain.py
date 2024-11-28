import hashlib 
import json 
from time import time 
 
class Blockchain: 
    def __init__(self): 
        self.chain = [] 
        self.pending_votes = [] 
        self.create_block(previous_hash="0", proof=1)  # Genesis block 
 
    def create_block(self, proof, previous_hash): 
        block = { 
            "index": len(self.chain) + 1, 
            "timestamp": time(), 
            "votes": self.pending_votes, 
            "proof": proof, 
            "previous_hash": previous_hash, 
        } 
        self.pending_votes = []  # Clear pending votes 
        self.chain.append(block) 
        return block 
 
    def add_vote(self, voter_id, candidate_id): 
        self.pending_votes.append({ 
            "voter_id": voter_id, 
            "candidate_id": candidate_id 
        }) 
 
    def proof_of_work(self, previous_proof): 
        new_proof = 1 
        while True: 
            hash_operation = hashlib.sha256( 
                str(new_proof**2 - previous_proof**2).encode() 
            ).hexdigest() 
            if hash_operation[:4] == "0000": 
                return new_proof 
            new_proof += 1 
 
    def hash(self, block): 
        encoded_block = json.dumps(block, sort_keys=True).encode() 
        return hashlib.sha256(encoded_block).hexdigest()
