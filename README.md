# 🌟 Positive Affirmations Streamlit App (With Dataset for Affirmations)

Welcome to the **Positive Affirmations** app — a calming space that serves a new uplifting affirmation with every click, beautifully paired with a soothing pastel background and a relaxing gif 🌈✨

---

## 🚀 Features

- 🎯 Randomly displays a **positive affirmation** each time the user clicks a button.
- 🎨 Pastel background changes dynamically to match the tranquil theme.
- 📸 Random **peaceful gifs** accompany each affirmation.
- 🧠 Built-in fallback affirmations list if the CSV is not found.
- 📁 Loads custom affirmations from `possitive_affirmation.csv` if available.
- 💬 Auto-adjusting text color based on background brightness for readability.

---

## 📦 Requirements
Make sure you have the following Python libraries installed:
```bash
pip install streamlit pandas
```

---

## 🛠️ How to Run the App
- Clone this repository and run the app using Streamlit:
```bash
streamlit run app.py
```
- If a possitive_affirmation.csv file exists in the same directory, it will be loaded. Otherwise, a default list of affirmations will be used.

---

## 🧘 CSV Format (Optional)
You can provide your own list of affirmations by creating a CSV file named possitive_affirmation.csv

---

## 🙌 Contributing
Feel free to submit issues or suggestions to make the app even more relaxing and joyful!
