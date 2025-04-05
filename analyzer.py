import fitz  # PyMuPDF
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def analyze_resume(filepath):
    text = extract_text_from_pdf(filepath)
    tokens = word_tokenize(text.lower())

    # Example skill list
    skills = ['python', 'java', 'sql', 'machine learning', 'data analysis']
    matched_skills = [skill for skill in skills if skill in tokens]

    return {
        "skills": matched_skills,
        "score": len(matched_skills) * 10,
        "summary": f"Found {len(matched_skills)} matching skills."
    }
