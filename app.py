from flask import Flask, render_template, request 
from blockchain import Blockchain  # Added Blockchain class 

app = Flask(__name__) 
blockchain = Blockchain() 
@app.route('/') 
def index(): 
 return render_template("index.html") 
  
@app.route('/vote', methods=['POST']) 
def vote(): 
 voter_id = request.form['voter_id'] 
 candidate_id = request.form['candidate_id'] 
 blockchain.add_vote(voter_id, candidate_id)  # Add vote to the blockchain 
 # Placeholder for vote handling 
 return render_template("success.html", voter_id=voter_id, candidate_id=candidate_id) 
   
@app.route('/mine', methods=['GET']) 
def mine_block(): 
    if not blockchain.pending_votes: 
        return render_template("error.html", message="No votes to mine. Please cast votes first!") 
    previous_block = blockchain.chain[-1] 
    proof = blockchain.proof_of_work(previous_block["proof"]) 
    previous_hash = blockchain.hash(previous_block) 
    block = blockchain.create_block(proof, previous_hash) 
    return render_template("block_mined.html", block=block) 
 
@app.route('/chain', methods=['GET']) 
def view_chain(): 
    return render_template("view_chain.html", chain=blockchain.chain) 
 
if __name__ == '__main__': 
app.run(debug=True)


