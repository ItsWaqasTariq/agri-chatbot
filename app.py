from flask import Flask, request, render_template, jsonify
from chatbot import AgricultureChatbot  # Importing the chatbot logic from chatbot.py

# Initialize Flask app
app = Flask(__name__)

# Initialize Groq API key for chatbot
api_key = "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"  # Your Groq API key
chatbot = AgricultureChatbot(api_key)  # Creating an instance of the agriculture chatbot

@app.route('/')
def home():
    return render_template('index.html')  # Serve the index.html template

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message')  # Get the user input from the request body
    if not user_input:
        return jsonify({"message": "Please ask a valid question."})

    # Get the response from the chatbot
    response_message = chatbot.agriculture_chatbot(user_input)
    return jsonify({"message": response_message})  # Return the response in JSON format

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
