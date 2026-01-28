# 🤖 IBM Watson Natural Language Understanding (NLU) Lab

Welcome to the Watson NLU Lab! This repository contains a collection of resources designed to teach you how to analyze text and websites using AI.

## 📁 Repository Overview

- **`NLU_Example_Enhanced.ipynb`**: An interactive Jupyter Notebook for exploring NLU features (Categories, Keywords, Sentiment, Emotion) with deep explanations and data visualization.
- **`NLU_categories_Student.py`**: A beginner-friendly Python script focused on extracting page metadata and categories.
- **`nlu_workflow.png`**: A technical diagram illustrating how data flows through the NLU pipeline.
- **`README_Categories.md`**: Dedicated documentation for the categories script.
- **`README_Example.md`**: Overview of the notebook analysis process.

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Installation
Clone this repository and install the required dependencies:
```bash
# Create a virtual environment
python -m venv .venv

# Activate the environment (Mac/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
You need an IBM Cloud API key to use the NLU service.
1. Copy the `env.sample` file and rename it to `.env`:
   ```bash
   cp env.sample .env
   ```
2. Open `.env` and fill in your credentials from the IBM Cloud Console:
   ```env
   IAM_KEY=your_api_key_here
   SERVICE_URL=your_service_url_here
   ```
   > [!IMPORTANT]
   > Do not include quotes around your API key or URL.

---

## 🛠️ Usage

### Running the Script
To analyze website metadata and categories:
```bash
python NLU_categories_Student.py
```

### Running the Notebook
To run the interactive analysis:
1. Ensure your virtual environment is active.
2. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
3. Open `NLU_Example_Enhanced.ipynb`.

---

## 🧠 Concepts Taught
- **Data Cleaning**: Using Pandas to prepare raw text for AI.
- **Sentiment Analysis**: Understanding the emotional tone of text.
- **Category Hierarchy**: Learning how Watson classifies content.
- **Visualization**: Using Matplotlib to plot 3D emotional trends.
