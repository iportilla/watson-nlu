# 🏷️ Watson NLU: Categories & Metadata Guide

This script demonstrates how to extract high-level information from any website using IBM Watson Natural Language Understanding.

## 📖 Key Concepts

### 1. Metadata
Metadata is "data about data." In the context of a webpage, it refers to the basic identity of the page:
- **Title**: What is the name of the page?
- **Language**: What language is it written in?
- **Image**: What is the main representative image (thumbnail) for the page?
- **Authors & Date**: Who wrote it and when?

### 2. Categories
Categories use a hierarchy (like a tree) to define what a webpage is about. 
- **Example**: `/Technology and Computing / Hardware / Computer`
- **Score**: Watson provides a confidence score (0 to 1). A score of `0.8` means Watson is very sure!

---

## 🚀 How to Run

1.  **Activate your environment**:
    ```bash
    source .venv/bin/activate
    ```
2.  **Run the script**:
    ```bash
    python NLU_categories_Student.py
    ```

---

## 💻 Code Highlights

### Why `{}` for Metadata?
In the Python SDK, most features (like Categories or Sentiment) have a dedicated "Options" class (e.g., `CategoriesOptions`). However, **Metadata** is a standard feature that doesn't require any additional configuration settings from you. 
Passing an empty dictionary `{}` tells Watson: *"Just give me the default metadata for this page."*

### Pretty Printing
We use `json.dumps(response, indent=2)` to make the output look organized. Without this, the result would be one long, messy line of text!

---

## 🛠️ Troubleshooting

- **Missing Credentials**: Ensure your `.env` file contains `IAM_KEY` and `SERVICE_URL`.
- **Import Error**: If you see `ModuleNotFoundError: No module named 'dotenv'`, run:
  ```bash
  pip install python-dotenv
  ```
