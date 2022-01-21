from flask import Flask,render_template, request, jsonify
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
        # print(butterfly)
        return jsonify({"message": butterfly})
    return None

if __name__ == "__main__":
    app.run(port=4001)

