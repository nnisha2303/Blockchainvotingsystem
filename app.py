from flask import Flask, render_template, request 
app = Flask(__name__) 

@app.route('/') 
def index(): 
 return render_template("index.html") 
  
@app.route('/vote', methods=['POST']) 
def vote(): 
 voter_id = request.form['voter_id'] 
 candidate_id = request.form['candidate_id'] 
 # Placeholder for vote handling 
 return render_template("success.html", voter_id=voter_id, candidate_id=candidate_id) 
  
if __name__ == '__main__': 
app.run(debug=True)
