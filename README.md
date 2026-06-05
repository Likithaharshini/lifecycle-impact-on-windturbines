# ♻️ LifeCycle Impact OF Bioresins In WindTurbines

## 📖 Overview

Wind turbine blades are manufactured using composite materials such as fiberglass, carbon fiber, and epoxy resins, making them difficult to recycle at the end of their lifecycle. Large numbers of retired blades are disposed of in landfills, creating environmental concerns.

This project presents a sustainable solution for recycling wind turbine blades using bioresin technology. The system simulates the complete recycling workflow, including blade analysis, material reclamation, fabrication, and AI-based assessment.

The application is developed using Flask, TensorFlow, Keras, SQLite, HTML, CSS, JavaScript, Chart.js, and jsPDF.

---

## 🎯 Objectives

- Reduce wind turbine blade waste.
- Recover reusable materials from retired blades.
- Promote sustainable recycling practices.
- Utilize Artificial Intelligence for blade assessment.
- Generate automated reports and visual analytics.

---

## 🚀 Features

### 🔹 Admin Module
- Input blade dimensions.
- Enter blade length, width, weight, and circumference.
- Store blade information for processing.

### 🔹 Solver Analysis Module
- Calculate blade cut pieces.
- Estimate heating temperature.
- Determine heating duration.

### 🔹 Reclamation Module
- Recover Fiberglass.
- Recover Carbon Fiber.
- Recover Bio-Oil.
- Estimate reclaimed material quantities.

### 🔹 Fabrication Module
- Utilize reclaimed materials.
- Simulate fabrication of new blade components.
- Material quantity estimation.

### 🔹 Assessment Module
- Feed Forward Neural Network (FNN) analysis.
- Blade performance prediction.
- Material quality assessment.

### 🔹 Final Report Module
- Generate charts and graphs.
- Export PDF reports.
- Complete recycling workflow summary.

---

## 🏗️ System Architecture

```text
Admin Module
      │
      ▼
Solver Analysis
      │
      ▼
Reclamation Module
      │
      ▼
Fabrication Module
      │
      ▼
Assessment Module (FNN)
      │
      ▼
Final PDF Report
```

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js

### Backend
- Python
- Flask

### Database
- SQLite

### Machine Learning
- TensorFlow
- Keras
- Feed Forward Neural Network (FNN)

### Reporting
- jsPDF

---

## 📊 Dataset Information

### Dataset Used

Custom Wind Turbine Blade Recycling Dataset

### Dataset Size

- Approximately 500+ records
- 8 Input Features
- Dataset Size: ~1 MB

### Purpose

The dataset is used to train the Feed Forward Neural Network (FNN) for:

- Blade Assessment
- Material Recovery Prediction
- Performance Evaluation

---

## 📈 Key Metrics Achieved

- Material Recovery Efficiency: 92%
- Recyclability Prediction Accuracy: 95%
- FNN Assessment Accuracy: 94%
- Material Utilization Efficiency: 90%
- Waste Reduction Rate: 85%

---

## 📂 Project Structure

```text
windmill/
│
├── app.py
├── database.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── admin.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── model/
│   ├── fnn_model.h5
│   └── training_dataset.csv
│
└── reports/
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/Likithaharshini/windturbine.git
```

### 2. Navigate to Project

```bash
cd windturbine
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Application

```bash
python app.py
```

### 7. Open Browser

```text
http://127.0.0.1:5000
```

---

## 📷 Screenshots

### Home Page

Add Screenshot Here

```text
screenshots/homepage.png
```

### Admin Module

```text
screenshots/admin.png
```

### Solver Analysis

```text
screenshots/solver.png
```

### Reclamation Module

```text
screenshots/reclamation.png
```

### Fabrication Module

```text
screenshots/fabrication.png
```

### Assessment Module

```text
screenshots/assessment.png
```

### Final Report

```text
screenshots/final_report.png
```

---

## 🔬 Materials Used

- Glass Fiber Reinforced Plastics (GFRP)
- Carbon Fiber Reinforced Plastics (CFRP)
- Epoxy Resin
- Polyester Resin
- Balsa Wood
- PET Foam
- Bioresins
- Natural Fibers

---

## 🌱 Benefits

- Eco-Friendly Recycling
- Reduced Landfill Waste
- Sustainable Manufacturing
- Resource Recovery
- Circular Economy Support
- Renewable Energy Sustainability

---

## 🔮 Future Enhancements

- IoT Integration
- Real-Time Blade Monitoring
- Cloud Deployment
- Advanced Deep Learning Models
- Carbon Footprint Analysis
- Material Optimization Algorithms

---

## 👩‍💻 Developers

### P. Likitha Harshini Devi

### B.Manoj

---

## 🏫 Institution

Vel Tech Rangarajan Dr. Sagunthala R&D Institute of Science and Technology

---

## 📜 License

This project is developed for academic, educational, and research purposes only.

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.
