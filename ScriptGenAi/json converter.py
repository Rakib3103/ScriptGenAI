import json
import re
from docx import Document

# Step 1: Extract text from DOCX file
def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Step 2: Parse dialogues into JSONL format
def parse_script_to_jsonl(text, category):
    jsonl_data = []
    lines = text.split("\n")
    prompt = ""
    context = f"Category: {category}"  # Add context like 'Cold Lead', 'Mild Lead', etc.
    
    for line in lines:
        # Match roles and dialogues
        match = re.match(r"^(.*?):\s*(.*)", line.strip())
        if match:
            role, dialogue = match.groups()
            if role == "সেক্টর স্পেশালিস্ট":
                if prompt:  # Save the previous pair if exists
                    jsonl_data.append({
                        "prompt": f"{context}\n{prompt.strip()}",
                        "completion": dialogue.strip()
                    })
                prompt = dialogue  # Set new prompt
            elif role in ["কৃষক", "আপা"]:
                jsonl_data.append({
                    "prompt": f"{context}\n{prompt.strip()}",
                    "completion": dialogue.strip()
                })
                prompt = ""  # Reset prompt for the next dialogue
    return jsonl_data

# Step 3: Save data to JSONL file
def save_as_jsonl(data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for item in data:
            json.dump(item, f, ensure_ascii=False)  # Preserve Bangla text
            f.write("\n")

# Main workflow
docx_path = "female_farmer_script.docx"  # Change to your file path
output_path = "output.jsonl"
category = "Female Farmer - Cold Lead"  # Example category

# Extract text
text = extract_text_from_docx(docx_path)

# Parse and convert to JSONL
jsonl_data = parse_script_to_jsonl(text, category)

# Save JSONL
save_as_jsonl(jsonl_data, output_path)
print(f"JSONL file saved at {output_path}")
