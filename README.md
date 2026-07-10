# VisionQC-AI

> **AI-Based Industrial Quality Inspection System using Deep Learning**

VisionQC-AI is a web application that automatically detects defective and non-defective casting products using a Deep Learning model. Built with **TensorFlow**, **MobileNetV2**, and **Flask**, it provides real-time predictions, confidence scores, prediction history, and downloadable inspection reports.

---

## Features

- Upload casting product images
- AI-powered defect detection
- Binary classification (Good / Defective)
- Confidence score visualization
- Prediction history using SQLite
- Clear history functionality
- PDF inspection report generation
- Responsive web interface

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| TensorFlow / Keras | Deep Learning Model |
| MobileNetV2 | Transfer Learning |
| Flask | Backend Framework |
| SQLite | Database |
| HTML5 | Frontend |
| CSS3 | Styling |
| ReportLab | PDF Report Generation |
| Pillow | Image Processing |
| NumPy | Numerical Computing |

---

## Project Structure

```
VisionQC-AI/
│
├── model/
│   └── quality_model.keras
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── uploads/
│
├── templates/
│   └── index.html
│
├── app.py
├── predict.py
├── train_model.py
├── database.py
├── report_generator.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## System Workflow

```
Upload Image
      │
      ▼
Image Preprocessing
      │
      ▼
MobileNetV2 Model
      │
      ▼
Prediction
      │
      ▼
Confidence Score
      │
      ▼
Store in SQLite Database
      │
      ▼
Generate PDF Inspection Report
```

---

## AI Model

| Property | Value |
|----------|-------|
| Model | MobileNetV2 |
| Framework | TensorFlow / Keras |
| Classification | Binary |
| Classes | Good Product / Defective Product |
| Input Size | 224 × 224 Pixels |
| Validation Accuracy | 98.6% |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gouravramgopidesh/VisionQC-AI.git
cd VisionQC-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Dataset

This project uses the **Casting Product Image Dataset** for binary classification.

**Dataset Link**

https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product

> **Note:**  
> The dataset is **not included** in this repository. Download it separately and place it inside a `dataset/` folder before training the model.

Dataset Structure:

```
dataset/
├── train/
│   ├── def_front/
│   └── ok_front/
│
└── test/
    ├── def_front/
    └── ok_front/
```

To retrain the model:

```bash
python train_model.py
```

---


## Future Improvements

- Multi-class defect detection
- Live webcam inspection
- Batch image processing
- User authentication
- REST API support
- Cloud deployment
- Dashboard analytics

---

## Author

**Gourav Ram**

Computer Science Engineering (Artificial Intelligence & Machine Learning)

Jain (Deemed-to-be University)

GitHub: https://github.com/gouravramgopidesh

---

## License

This project is licensed under the **MIT License**.

---

## Acknowledgements

- TensorFlow
- Flask
- MobileNetV2
- SQLite
- ReportLab
- Kaggle Casting Product Dataset
