from flask import Flask, request, jsonify
import openai
import os
from PIL import Image
import io

app = Flask(__name__)

# Load your OpenAI API key
openai.api_key = 'your-openai-api-key-here'  # Replace with your actual API key

@app.route('/ask', methods=['POST'])
def ask():
    try:
        # Get the user query from the POST request
        user_query = request.form.get('query')
        image_file = request.files.get('image')

        # Process the image if provided
        if image_file:
            # Read the image file
            image = Image.open(image_file.stream)
            # You can add your image processing logic here (e.g., OCR, object detection)
            # For now, let's say we are extracting text from the image
            extracted_text = "extracted text from image"  # Placeholder for image processing result
        else:
            extracted_text = ""

        # Combine user query with extracted text
        combined_input = f"{user_query} {extracted_text}".strip()

        # Call the OpenAI API using the chat completion endpoint
        response = openai.chat.Completion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": combined_input}
            ]
        )

        # Extract the assistant's reply
        assistant_reply = response["choices"][0]["message"]["content"]

        # Return the assistant's reply as a JSON response
        return jsonify({"text": assistant_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
