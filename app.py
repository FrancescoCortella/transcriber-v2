import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import whisper

app = Flask(__name__)

# Set the folder where uploaded files will be stored temporarily
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'docx', 'csv', 'mp3', 'wav', 'ogg', 'm4a'}  # Add more allowed extensions as needed for audio files

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Call the Azure Function API here to send the file for processing
            #model = whisper.load_model("base")
            #result = model.transcribe(filename)
            #return result["text"]
            return filename
        else:
            return "Invalid file format. Allowed formats: " + ", ".join(app.config['ALLOWED_EXTENSIONS'])

if __name__ == '__main__':
    app.run(debug=True)