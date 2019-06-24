from flask import Flask, request, make_response
from flask_cors import CORS, cross_origin
import io
from Kmeans import compress_image, resize

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return "Welcome to the k-means API! Documentation will be added here shortly!"

@app.route('/upload', methods=['POST'])
def handle_upload():
    # return "hello"
    image = request.files['file']
    data = io.BytesIO(image.read())
    data = data.read()
    # compressed_buffer = compress_image(image.filename, data)
    return "hello world"
    # return make_response(compressed_buffer.tobytes())

@app.route('/resize', methods=['POST'])
def resize_upload():
    image = request.files['file']
    data = io.BytesIO(image.read())
    data = data.read()
    resized = resize(image.filename, data)
    return make_response(resized.tobytes())