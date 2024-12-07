import subprocess
import time

# Flask ilovasini ishga tushirish
def start_flask():
    subprocess.Popen(['python', 'flask_app.py'])

# Streamlit ilovasini ishga tushirish
def start_streamlit():
    subprocess.Popen(['streamlit', 'run', 'streamlit_app.py'])

if __name__ == "__main__":
    # Flask ilovasini ishga tushirish
    start_flask()
    time.sleep(5)  # Flask ilovasining ishga tushishiga vaqt berish
    # Streamlit ilovasini ishga tushirish
    start_streamlit()
