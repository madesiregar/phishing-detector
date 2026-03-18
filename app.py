from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    mode = data.get('mode', 'url')
    input_val = data.get('input', '')

    if mode == 'url':
        from detector.url_analyzer import analyze_url
        result = analyze_url(input_val)
    else:
        from detector.email_analyzer import analyze_email
        result = analyze_email(input_val)

    verdict = 'SAFE' if result['score'] < 25 else 'SUSPICIOUS' if result['score'] < 60 else 'PHISHING'
    result['verdict'] = verdict
    return jsonify(result)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)