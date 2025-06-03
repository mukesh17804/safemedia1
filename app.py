import os
from flask import Flask, render_template, request
from stegano import lsb
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def detect_steganography(image_path):
    try:
        hidden_data = lsb.reveal(image_path)
        return hidden_data is not None
    except:
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            if detect_steganography(file_path):
                message = "🚨 ALERT: This image contains hidden/malicious data!"
            else:
                message = "✅ This image is clean and safe."

            return render_template('index.html', message=message, filename=filename)
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
