from flask import *  
app = Flask(__name__)  
import pyfiglet
  
@app.route('/')  
def home():

    return render_template("main.html")

 
@app.route('/postmethod', methods=['POST'])
def postmethod():
    data = request.get_json()
    print(data)
    return jsonify(data)

if __name__ == '__main__':  
    print( "\033[96m" + pyfiglet.figlet_format("Location Tracker") + "\033[00m")
    print("\033[92m {}\033[00m\033[91m {}\033[00m".format('Developed by','Gaurav Konde'))
    app.run(debug = True)  