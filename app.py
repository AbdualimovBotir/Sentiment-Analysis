from flask import Flask, Blueprint, request, jsonify, render_template, send_from_directory
import pickle

def create_app():
    app = Flask(__name__)

    # Blueprints
    main = Blueprint('main', __name__)

    # Load model and vectorizer
    with open('models/sentiment_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    with open('models/vectorizer.pkl', 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)

    @main.route('/')
    def home():
        return render_template('index.html')

    @main.route('/favicon.ico')
    def favicon():
        return send_from_directory('static', 'favicon.ico')

    @main.route('/predict', methods=['POST'])
    def predict():
        data = request.get_json()

        if 'text' not in data:
            return jsonify({'error': 'No text provided!'}), 400

        text = data['text']

        # Vectorize the text and predict sentiment
        text_vectorized = vectorizer.transform([text])
        prediction = model.predict(text_vectorized)[0]
        sentiment = 'Positive' if prediction == 1 else 'Negative'

        return jsonify({'text': text, 'sentiment': sentiment})

    app.register_blueprint(main)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
