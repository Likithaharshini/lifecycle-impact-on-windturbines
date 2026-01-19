from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
import sqlite3, os, pickle, numpy as np
from reportlab.pdfgen import canvas
from base64 import b64encode, b64decode
from Crypto.Cipher import AES

# ---------------- Flask Setup ----------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

DB_PATH = 'database/turbine_data.db'
REPORT_PATH = 'reports/pdfs/'
MODEL_PATH = 'models/assessment_model.pkl'

# Create necessary directories
os.makedirs('database', exist_ok=True)
os.makedirs(REPORT_PATH, exist_ok=True)
os.makedirs('models', exist_ok=True)

# ---------------- Database Initialization ----------------
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS blades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    length TEXT,
    width TEXT,
    weight TEXT,
    circumference TEXT
)
''')
conn.commit()
conn.close()

# ---------------- AES Encryption/Decryption ----------------
KEY = b'Sixteen byte key'
BLOCK_SIZE = 16

def pad(s):
    pad_len = BLOCK_SIZE - len(s) % BLOCK_SIZE
    return s + chr(pad_len) * pad_len

def unpad(s):
    return s[:-ord(s[-1])]

def encrypt_data(data):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return b64encode(cipher.encrypt(pad(data).encode())).decode()

def decrypt_data(enc):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return unpad(cipher.decrypt(b64decode(enc)).decode())

# ---------------- Load FNN Model ----------------
fnn_model = None
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        fnn_model = pickle.load(f)

# ---------------- Module Functions ----------------
def solver_analysis(length, width, weight, circumference):
    cut_pieces = round(float(length) * 0.5, 2)
    heating_temp = 120 + float(weight) * 0.1
    heating_time = 30 + float(circumference) * 0.2
    return f"Cut Pieces: {cut_pieces} m | Heating Temp: {heating_temp} °C | Heating Time: {heating_time} min"

def reclamation(length, width, weight, circumference):
    fiberglass = round(float(weight) * 0.4, 2)
    carbon_fiber = round(float(weight) * 0.3, 2)
    balsa = round(float(weight) * 0.2, 2)
    bio_oil = round(float(weight) * 0.1, 2)
    return f"Fiberglass: {fiberglass} kg | Carbon Fiber: {carbon_fiber} kg | Balsa: {balsa} kg | Bio Oil: {bio_oil} kg"

def fabrication(length, width, weight, circumference):
    materials = {
        'Carbon Fiber': 50,
        'Fiberglass': 40,
        'PET Foam': 30,
        'Flax Fiber': 20,
        'Basalt Fiber': 25,
        'Pecan Resin': 15,
        'Bio Oil Solute': 10
    }
    return str(materials)

def assessment(length, width, weight, circumference):
    if fnn_model:
        input_data = np.array([[float(length), float(width), float(weight), float(circumference)]])
        result = fnn_model.predict(input_data)[0]
        metrics = [round(val, 2) for val in result]
        return f"Metric1: {metrics[0]} | Metric2: {metrics[1]} | Metric3: {metrics[2]} | Metric4: {metrics[3]}"
    else:
        return "FNN Assessment Results: Placeholder (train model for accuracy)"

# ---------------- Flask Routes ----------------
# Default landing page
@app.route('/')
def home():
    return render_template('index.html')

# Admin page
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        length = request.form['length']
        width = request.form['width']
        weight = request.form['weight']
        circumference = request.form['circumference']

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('INSERT INTO blades (length, width, weight, circumference) VALUES (?, ?, ?, ?)',
                  (encrypt_data(length), encrypt_data(width), encrypt_data(weight), encrypt_data(circumference)))
        blade_id = c.lastrowid
        conn.commit()
        conn.close()

        return redirect(url_for('module_view', blade_id=blade_id))
    return render_template('admin.html')

# Module view page
@app.route('/module/<int:blade_id>')
def module_view(blade_id):
    return render_template('admin.html', blade_id=blade_id)

# Fetch module data
@app.route('/module_data/<int:blade_id>/<module>')
def module_data(blade_id, module):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT length, width, weight, circumference FROM blades WHERE id=?', (blade_id,))
    row = c.fetchone()
    conn.close()

    if not row:
        return jsonify({'result': 'Blade not found'})

    length, width, weight, circumference = map(decrypt_data, row)

    if module == 'solver':
        result = solver_analysis(length, width, weight, circumference)
    elif module == 'reclamation':
        result = reclamation(length, width, weight, circumference)
    elif module == 'fabrication':
        result = fabrication(length, width, weight, circumference)
    elif module == 'assessment':
        result = assessment(length, width, weight, circumference)
    elif module == 'final':
        result = "Final Report includes all module data."
    else:
        result = "Invalid module"

    return jsonify({'result': result})

# PDF generation
@app.route('/download_pdf/<int:blade_id>/<module>')
def download_pdf(blade_id, module):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT length, width, weight, circumference FROM blades WHERE id=?', (blade_id,))
    row = c.fetchone()
    conn.close()

    if not row:
        return "Blade not found"

    length, width, weight, circumference = map(decrypt_data, row)

    if module == 'solver':
        content = solver_analysis(length, width, weight, circumference)
    elif module == 'reclamation':
        content = reclamation(length, width, weight, circumference)
    elif module == 'fabrication':
        content = fabrication(length, width, weight, circumference)
    elif module == 'assessment':
        content = assessment(length, width, weight, circumference)
    elif module == 'final':
        content = (
            "FINAL REPORT\n\n"
            f"SOLVER ANALYSIS:\n{solver_analysis(length, width, weight, circumference)}\n\n"
            f"RECLAMATION:\n{reclamation(length, width, weight, circumference)}\n\n"
            f"FABRICATION:\n{fabrication(length, width, weight, circumference)}\n\n"
            f"ASSESSMENT:\n{assessment(length, width, weight, circumference)}"
        )
    else:
        content = "Invalid module"

    filename = f"{REPORT_PATH}{module}_blade_{blade_id}.pdf"
    c = canvas.Canvas(filename)
    c.setFont("Helvetica", 12)
    for i, line in enumerate(content.split('\n')):
        c.drawString(50, 800 - i*20, line)
    c.save()
    return send_file(filename, as_attachment=True)

# ---------------- Run App ----------------
if __name__ == '__main__':
    app.run(debug=True)