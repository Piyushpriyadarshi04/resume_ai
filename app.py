from flask import Flask, request, jsonify, render_template
import os
from analyzer import analyze_resume

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return jsonify({'error': 'No resume file provided'}), 400

    file = request.files['resume']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    filepath = os.path.join('resumes', file.filename)
    file.save(filepath)

    result = analyze_resume(filepath)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
