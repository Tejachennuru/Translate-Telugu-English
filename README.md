# 🗣 Telugu Subtitle Translator

A simple tool to convert `.srt` subtitle files written in **Telugu** into structured English-Telugu sentence pairs for NLP or localization tasks.

---

## 📁 Project Structure

```
telugu-translator/
├── input.srt         # Input subtitle file (Telugu)
├── en_te.py          # Python translation script
├── output.jsonl      # Output file with English-Telugu pairs
└── README.md         # Documentation
```

---

## ✅ Features

- Parses `.srt` subtitle files
- Extracts and processes only Telugu text lines
- Translates each line to English
- Outputs results in JSON Lines format
- Lightweight, no complex setup

---

## 🛠 Installation

Make sure you have Python 3.6+ installed, then install dependencies:

```bash
pip install googletrans==4.0.0-rc1
```

---

## 🚀 Usage

1. Place your input file in the same directory and name it `input.srt`.

2. Run the script:

```bash
python en_te.py
```

3. After successful execution, the translated results will be saved to:

```
output.jsonl
```

---

## 📥 Input Format

Get the subtitles from a youtube video

1. Paste the link of video you want to download subtitles.
2. Click Download button to begin extracting subtitles.
3. Select the subtitles format and language you want to download, then click Download button.

 Tricks
Add subtitle.to/ before the URL and press Enter
Or add subtitle.to/ between the URL and press Enter

Download the srt file for input.

The input should be a `.srt` file like the example below:

```
1
00:00:00,000 --> 00:00:03,520
ఏఐ ఏఐ ఏఐఏఐ ఈ పదం విని విని విని మీకు

2
00:00:03,520 --> 00:00:05,359
చిరాగ వచ్చేస్తుందని నాకు తెలుసు. కానీ

3
00:00:05,359 --> 00:00:07,919
99% ఆఫ్ ద బిగినర్స్ కి ఏఐ రిలేటెడ్

4
00:00:07,919 --> 00:00:09,519
టర్మ్స్ అయితే తెలియవు. రాగ్ అంటే ఏంటి?

5
00:00:09,519 --> 00:00:11,759
ఎల్ఎల్ఎం అంటే ఏంటి? ఏఏజెంట్ కి ఏ టూల్ కి

6
00:00:11,759 --> 00:00:13,679
డిఫరెన్స్ ఏంటి? లాంగ్ చైన్ అంటే ఏంటి?
```

> The script will ignore timestamp and numbering lines. Only Telugu dialogue is processed.

---

## 📤 Output Format

The output will be saved in `output.jsonl` (JSON Lines format), where each line represents one translation:

```json
{ "en": "AI AI AI AI you keep hearing this word", "te": "ఏఐ ఏఐ ఏఐఏఐ ఈ పదం విని విని విని మీకు" }
{ "en": "I know Chirag comes to your mind. But", "te": "చిరాగ వచ్చేస్తుందని నాకు తెలుసు. కానీ" }
{ "en": "99% of beginners don’t know AI-related terms", "te": "99% ఆఫ్ ద బిగినర్స్ కి ఏఐ రిలేటెడ్" }
{ "en": "They don't know terms. What is RAG?", "te": "టర్మ్స్ అయితే తెలియవు. రాగ్ అంటే ఏంటి?" }
```

---

## 🧠 Behind the Scenes

- Built using `googletrans` (Google Translate unofficial API)
- Auto-detects language and provides approximate translations
- Lightweight and works offline after initial translation

---

## 📌 Notes

- Requires internet access for translation.
- `googletrans` may hit rate limits if overused — avoid large file batches.
- Ideal for creating English-Telugu parallel corpora.

---

## 🤝 Contributing

Pull requests welcome. For major changes, open an issue first to discuss what you would like to change.

---

## 📄 License

MIT License © 2025

---
