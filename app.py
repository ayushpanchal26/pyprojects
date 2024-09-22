import os
from flask import Flask, request, jsonify, render_template_string
from werkzeug.utils import secure_filename
import openai
import pytesseract
from PIL import Image

# Initialize Flask app
app = Flask(__name__)

# Configure Upload folder
UPLOAD_FOLDER = 'C:\projects\pyprojects\lang_images'
app.config['C:\projects\pyprojects\lang_images'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB upload limit

# Initialize OpenAI API
openai.api_key = 'sk-UHrOnl5OVM3_rSsyyRndKT4Ac0esIkZY87Ku2QuoTuT3BlbkFJjK4g4bC9xmwclBFyf6kqSROQLvAL2dzqj6GYq4CikA'  # Replace with your OpenAI key

# Function to translate text using GPT API
def translate_text(text, target_lang):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the appropriate model you have access to
            messages=[
                {"role": "system", "content": "You are a helpful assistant that translates text."},
                {"role": "user", "content": f"Translate the following text to {target_lang}: {text}"}
            ],
            max_tokens=500
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Route for index.html (now embedded in the Python code)
@app.route('/')
def index():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Language Converter</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: url('/static/bg.jpg') no-repeat center center fixed;
                background-size: cover;
                color: #ffffff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: rgba(0, 0, 0, 0.7);
                padding: 20px;
                border-radius: 10px;
                width: 100%;
                max-width: 600px;
            }
            textarea, input[type="file"] {
                width: 100%;
                margin-bottom: 10px;
                padding: 10px;
                font-size: 16px;
                border: none;
                border-radius: 5px;
            }
            button {
                width: 100%;
                padding: 10px;
                background-color: #fff;
                color: #000;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
            }
            button:hover {
                background-color: #000;
                color: #fff;
            }
            .output {
                margin-top: 10px;
                padding: 10px;
                background-color: #ccc;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>

    <div class="container">
        <h1>Language Converter</h1>

        <textarea id="inputText" placeholder="Paste text here..."></textarea>
        <button onclick="translateText()">Convert</button>

        <div class="output">
            <h3>Original:</h3>
            <p id="outputOriginal"></p>
        </div>
        <div class="output">
            <h3>Hindi Translation:</h3>
            <p id="outputHindi"></p>
        </div>
        <div class="output">
            <h3>Arabic Translation:</h3>
            <p id="outputArabic"></p>
        </div>
        <div class="output">
            <h3>English Translation:</h3>
            <p id="outputEnglish"></p>
        </div>

        <input type="file" id="imageUpload">
        <button onclick="uploadImage()">Upload Image</button>
    </div>

    <script>
        async function translateText() {
            const inputText = document.getElementById('inputText').value;
            const response = await fetch('/translate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: inputText }),
            });
            const data = await response.json();

            document.getElementById('outputOriginal').innerText = data.original;
            document.getElementById('outputHindi').innerText = data.hindi;
            document.getElementById('outputArabic').innerText = data.arabic;
            document.getElementById('outputEnglish').innerText = data.english;
        }

        async function uploadImage() {
            const fileInput = document.getElementById('imageUpload');
            const formData = new FormData();
            formData.append('file', fileInput.files[0]);

            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            document.getElementById('outputOriginal').innerText = data.original;
            document.getElementById('outputHindi').innerText = data.hindi;
            document.getElementById('outputArabic').innerText = data.arabic;
            document.getElementById('outputEnglish').innerText = data.english;
        }
    </script>

    </body>
    </html>
    '''
    return render_template_string(html_content)

# Route to handle text translation
@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')

    # Translate text to Hindi, Arabic, and English
    hindi_translation = translate_text(text, "Hindi")
    arabic_translation = translate_text(text, "Arabic")
    english_translation = translate_text(text, "English")

    return jsonify({
        'original': text,
        'hindi': hindi_translation,
        'arabic': arabic_translation,
        'english': english_translation
    })

# Route to handle image upload and text extraction
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract text using Tesseract
        img = Image.open(file_path)
        extracted_text = pytesseract.image_to_string(img)

        # Translate extracted text
        hindi_translation = translate_text(extracted_text, "Hindi")
        arabic_translation = translate_text(extracted_text, "Arabic")
        english_translation = translate_text(extracted_text, "English")

        return jsonify({
            'original': extracted_text,
            'hindi': hindi_translation,
            'arabic': arabic_translation,
            'english': english_translation
        })

if __name__ == '__main__':
    app.run(debug=True)
