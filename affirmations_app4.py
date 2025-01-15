import streamlit as st
import random
import pandas as pd

def load_affirmations():
    try:
        df = pd.read_csv('possitive_affirmation.csv')
        return df['Affirmation'].tolist()
    except Exception as e:
        st.error(f"Error loading the CSV file: {e}")
        return []

affirmations = load_affirmations()

if not affirmations:
    affirmations = [
        "I trust the universe remains in control even when I'm not.",
        "I am quietly positive.",
        "I am able to stop my train of thoughts before they overwhelm me.",
        "I allow myself to feel positive under challenging circumstances.",
        "I allow self-care to transform my mindset.",
        "I grow and move on in peace.",
        "I live each moment with a positive heart and a peaceful mind.",
        "I relax my shoulders, unclench my jaw, and take a deep, calming breath before reacting.",
        "I trust the outcome even when I can't see it clearly.",
        "I approach stressful situations with peace and clarity.",
        "I prioritize self-kindness and self-care.",
        "I feel my entire body relax when I practice self-care.",
        "I believe in my body's innate ability to heal all wounds: physical, emotional, and spiritual.",
        "When others' lack of planning makes a crisis, it is my choice if I want to engage.",
        "I am relaxed and refreshed.",
        "I build new structures within my mind to convert it into a more peaceful place.",
        "Anxiety is a part of life and it holds no weight over me.",
        "I never have to settle before I'm ready.",
        "I have everything I need to heal already within me.",
        "I enjoy the peace I feel through self-care.",
        "I am completely present in the moment.",
        "I know my stress is merely a reaction, and I can control it.",
        "I become tranquil, relaxed.",
        "I am filled with inner peace and serenity.",
        "I feel great.",
        "I release anxieties and stress.",
        "I am worthy and deserving of self-love.",
        "I trust that what is meant for me will be.",
        "I embrace a life of peace and serenity.",
        "I am beautiful inside and out.",
        "I release any thought that makes me feel uncomfortable or stressed.",
        "I set my fears and worries loose.",
        "I take deep breaths and always maintain my composure.",
        "I can handle these challenges that come with recovery.",
        "I am still and calm.",
        "I am strong enough to get through this.",
        "I choose happiness over any other emotion that shows up.",
        "I see the good in everyone.",
        "I am able to tune out of negativity.",
        "I welcome serenity into my sacred space.",
        "I retain complete control over how I feel.",
        "I am able to find happiness in the little things.",
        "I choose to maintain a positive mindset.",
        "I place my heart on my hand and feel it calming.",
        "I focus on the joys of the present and avoid worrying about the future.",
        "I consciously seek moments of stillness.",
        "I am in a good place.",
        "I choose to feel uplifting emotions.",
        "I deserve to stop worrying and start trusting.",
        "I choose to envelop myself with peace.",
        "I lean into my positive thoughts.",
        "I focus on my emotional well-being.",
        "I am at peace with myself.",
        "I refuse to give in to anxieties and worries.",
        "I am grateful for the person that I am today.",
        "I manage my stress so that it doesn't manage me.",
        "I know that I can handle anything that comes my way."
    ]

gifs = [
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWU3N2tmNTAxMHBiZ3JkcnM5M3VzcnViZGRlNmZhYXJ5d2g1aGh1YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9rjGcdVfvzoNa/giphy.gif",
    "https://i.pinimg.com/originals/e6/60/d0/e660d003ad9e2336cc500fd2853cc2a5.gif",
    "https://cdn.pixabay.com/animation/2023/05/09/23/24/23-24-59-615_512.gif",
    "https://www.icegif.com/wp-content/uploads/icegif-5600.gif",
    "https://i.makeagif.com/media/3-18-2018/x4fpZx.gif",
    "https://c.tenor.com/x8G6MBaDjiIAAAAC/flowers-wind.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXQ4NmFzcGhldWtwZWdiYXdzZTNwMmg1MzZ4YjV0Zm5md2FqMWx3MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Pp9W9tuVF5NwQ/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGo1ZGZhZHBleTNsYmN1djB4cGZwNnZsNWs3bzg3ZnVzN29vNXA3ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/67uxmHhIF3uh6Ph8ew/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3pqdGF6Y3g0NjdsdzA0MXgyZGdlejY5YWJ0bWIzdDRkMnUyNnB1ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dU97uV3UyP0ly/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXl3NXRsMTU1ZGV5YXBheGJhdmUxbWcwend2NnMwNDg1ZGNrMmo0OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUA7aPhCAs5QRvMMJa/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3VhcHFoOW82ZTF6emQ2dzZud29reWNheW1rZWg3azIwcjBnc24zMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XcsdCc78BtNBu/giphy.gif",
    "https://pa1.narvii.com/6808/6f5fedd7dffaed239b1262b33b576c8af764d409_hq.gif",
    "https://pa1.narvii.com/6808/21a397d7938b16d1c3cc385bc691b8f11f551448_hq.gif"
]

def get_cool_background():
    pastel_shades = [
        "#F8BBD0",  # Pastel Pink
        "#D1C4E9",  # Pastel Lavender
        "#BBDEFB",  # Pastel Blue
        "#B2EBF2",  # Pastel Aqua
        "#C8E6C9",  # Pastel Green
        "#FFCCBC",  # Pastel Peach
        "#F0F4C3",  # Pastel Lime
        "#E1BEE7",  # Pastel Purple
        "#FFCDD2",  # Pastel Red
        "#B3E5FC",  # Pastel Sky Blue
        "#D7CCC8",  # Pastel Beige
        "#A5D6A7",  # Pastel Olive Green
        "#FFEB3B",  # Soft Pastel Yellow
        "#E0F7FA",  # Pastel Aqua Blue
    ]
    return random.choice(pastel_shades)

def get_new_background(previous_color):
    new_color = get_cool_background()
    while new_color == previous_color:
        new_color = get_cool_background()
    return new_color

def get_new_gif(previous_gif):
    new_gif = random.choice(gifs)
    while new_gif == previous_gif:
        new_gif = random.choice(gifs)
    return new_gif

if 'previous_background' not in st.session_state:
    st.session_state.previous_background = None

if 'previous_gif' not in st.session_state:
    st.session_state.previous_gif = None

if 'affirmation' not in st.session_state:
    if affirmations:  
        st.session_state.affirmation = random.choice(affirmations)
    else:
        st.session_state.affirmation = "No affirmations available."

background_color = get_new_background(st.session_state.previous_background)
gif = get_new_gif(st.session_state.previous_gif)

st.session_state.previous_background = background_color
st.session_state.previous_gif = gif

def is_light_color(hex_color):
    """Check if the background color is light or dark."""
    hex_color = hex_color.lstrip('#')
    rgb = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
    luminance = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2])
    return luminance > 186  

text_color = "black" if is_light_color(background_color) else "white"

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {background_color};
            color: {text_color};
        }}
        h1, h2, h3, h4, h5, h6, .stMarkdown {{
            color: {text_color};
        }}
        .css-1emrehy.edgvbvh3 {{
            color: red !important;
        }}
        .stButton button {{
            color: red !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌟 Positive Affirmations 🌟")
st.write("Welcome to your daily dose of positivity!")

if st.button("Generate Affirmation"):
    if affirmations:  
        st.session_state.affirmation = random.choice(affirmations)
    else:
        st.session_state.affirmation = "No affirmations available."
    background_color = get_new_background(st.session_state.previous_background)
    gif = get_new_gif(st.session_state.previous_gif)
    st.session_state.previous_background = background_color
    st.session_state.previous_gif = gif
st.markdown(f"<h2>{st.session_state.affirmation}</h2>", unsafe_allow_html=True)
st.image(gif, width=500)
