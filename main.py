from flask import *  
app = Flask(__name__)  
  
  
@app.route('/')  
def home():

    return render_template("main.html")

 
@app.route('/postmethod', methods=['POST'])
def postmethod():
    data = request.get_json()
    print(data)
    return jsonify(data)

if __name__ == '__main__':  
   app.run(debug = True)  