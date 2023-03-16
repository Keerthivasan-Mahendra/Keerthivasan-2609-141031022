from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://drive.google.com/file/d/1m18XfKKVRi-V9id3JpC1u6FbEUKmecjk#scrollTo=pUYnw76WSQyk', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')

if __name__== '__main__':
    app.run()