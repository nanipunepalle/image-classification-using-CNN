from flask import Flask,render_template, request
from model import predict_butterfly


app = Flask(__name__)

@app.route('/',methods=["GET"])
def sample_func():
    print("server working")
    return render_template("index.html")
    # return "server working"

@app.route('/predict',methods=["POST","GET"])
def predict():
    if request.method == "POST":
        file=request.files['image']
        img = file.read()
        butterfly = predict_butterfly(img)
        return {"message": butterfly}, 200
    return {"message": "error occured try again"}, 200

if __name__ == "__main__":
    app.run(debug=True)

