import re
import json
from googletrans import Translator

def extract_telugu_sentences(file_path):
    print(f"📥 Reading input file: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ File not found.")
        return []

    blocks = re.split(r'\n\s*\n', content.strip())
    telugu_sentences = []
    for block in blocks:
        lines = block.strip().split('\n')
        sentence_lines = [line for line in lines if not re.match(r'^\d+$', line) and '-->' not in line]
        if sentence_lines:
            telugu_sentence = ' '.join(sentence_lines).strip()
            telugu_sentences.append(telugu_sentence)
    
    print(f"✅ Extracted {len(telugu_sentences)} Telugu lines.")
    return telugu_sentences

def translate_telugu_to_english(sentences):
    print("🌐 Translating to English...")
    translator = Translator()
    translations = []
    for sentence in sentences:
        try:
            translation = translator.translate(sentence, src='te', dest='en')
            translations.append({ "en": translation.text, "te": sentence })
        except Exception as e:
            print(f"❌ Translation error: {e}")
    print(f"✅ Translated {len(translations)} sentences.")
    return translations

def write_output(translations, output_file='output.jsonl'):
    print(f"💾 Writing output to {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in translations:
            json_line = json.dumps(item, ensure_ascii=False)
            f.write(json_line + '\n')
    print("✅ Output file written successfully.")

def main():
    input_file = 'input.srt'
    telugu_sentences = extract_telugu_sentences(input_file)
    if not telugu_sentences:
        print("⚠️ No sentences to process.")
        return

    translations = translate_telugu_to_english(telugu_sentences)
    if not translations:
        print("⚠️ No translations completed.")
        return

    write_output(translations)

if __name__ == "__main__":
    print("🚀 Starting translation process...")
    main()
