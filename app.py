from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

carpeta = 'static/imgs/'
ext_permitidas = ['png', 'jpg', 'jpeg', 'gif', 'webp', 'avif']
app.secret_key = b'_sdsa4582L"F4Q8z]/'
app.config['UPLOAD_FOLDER'] = carpeta

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ext_permitidas
           
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        # if 'image' not in request.files:
        #     flash('No seleccionaste imagen. Que carajo te pasa?')
            
        #     return redirect('/')
        print(request.files)
        image = request.files['image']
        if image.filename == '':
            flash('No seleccionaste imagen. Que carajo te pasa?')
            return redirect('/')
        if image and allowed_file(image.filename):
            filename = secure_filename(f"uploaded.{image.filename.rsplit('.', 1)[1].lower()}")
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html', image_name = filename)
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug = True, port=80)
    
