# import random as r
# l=['hello','hi','apple','mango','orange',1,2,3,4,5]
# print(l)
# a=r.shuffle(l)
# print(l)
# print(a)
# print(l)

# import random
# print("First Pass:")
# random.seed(5)
# print(random.random()) # A specific decimal
# print("Second Pass (Restarting):")
# random.seed(5)
# print(random.random()) # The EXACT same decimal as above

# import getpass
# a=getpass.getpass("Enter name- ")
# print(a)


import json
import os
import time
import urllib.request
from datetime import datetime
from dotenv import load_dotenv

# --- CONFIGURATION ---
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(ROOT_DIR, ".env"))
API_KEY = os.getenv("API_KEY", "")
MODEL = "gemini-2.5-flash-preview-09-2025"

# --- DATA STRUCTURES ---
ZODIAC_DATA = {
    'Aries': {"element": "Fire", "planet": "Mars", "traits": "Bold, pioneering, courageous, and energetic."},
    'Taurus': {"element": "Earth", "planet": "Venus", "traits": "Reliable, patient, musical, and grounded."},
    'Gemini': {"element": "Air", "planet": "Mercury", "traits": "Versatile, expressive, curious, and kind."},
    'Cancer': {"element": "Water", "planet": "Moon", "traits": "Intuitive, sentimental, compassionate, and protective."},
    'Leo': {"element": "Fire", "planet": "Sun", "traits": "Dramatic, outgoing, self-assured, and fiery."},
    'Virgo': {"element": "Earth", "planet": "Mercury", "traits": "Loyal, analytical, kind, and hardworking."},
    'Libra': {"element": "Air", "planet": "Venus", "traits": "Social, fair-minded, diplomatic, and gracious."},
    'Scorpio': {"element": "Water", "planet": "Pluto", "traits": "Passionate, stubborn, resourceful, and brave."},
    'Sagittarius': {"element": "Fire", "planet": "Jupiter", "traits": "Generous, idealistic, great sense of humor."},
    'Capricorn': {"element": "Earth", "planet": "Saturn", "traits": "Responsible, disciplined, self-control, good managers."},
    'Aquarius': {"element": "Air", "planet": "Uranus", "traits": "Progressive, original, independent, humanitarian."},
    'Pisces': {"element": "Water", "planet": "Neptune", "traits": "Compassionate, artistic, intuitive, gentle, wise."}
}

NUMEROLOGY_DATA = {
    1: "The Leader: Independent, original, and courageous.",
    2: "The Diplomat: Sensitive, tactful, and diplomatic.",
    3: "The Creative: Expressive, social, and imaginative.",
    4: "The Builder: Practical, disciplined, and reliable.",
    5: "The Adventurer: Versatile, freedom-loving, and curious.",
    6: "The Nurturer: Responsible, loving, and community-minded.",
    7: "The Seeker: Analytical, spiritual, and investigative.",
    8: "The Powerhouse: Ambitious, authoritative, and success-oriented.",
    9: "The Humanitarian: Compassionate, generous, and idealistic.",
    11: "The Visionary: Highly intuitive and spiritually insightful.",
    22: "The Master Builder: Capable of turning grand dreams into reality.",
    33: "The Master Teacher: Devoted to the spiritual uplifting of others."
}

# --- LOGIC FUNCTIONS ---

def get_zodiac(dob_str):
    """Determines the Western Zodiac sign based on birth date."""
    try:
        date = datetime.strptime(dob_str, "%d-%m-%Y")
        day, month = date.day, date.month
        if (month == 3 and day >= 21) or (month == 4 and day <= 19): return "Aries"
        if (month == 4 and day >= 20) or (month == 5 and day <= 20): return "Taurus"
        if (month == 5 and day >= 21) or (month == 6 and day <= 20): return "Gemini"
        if (month == 6 and day >= 21) or (month == 7 and day <= 22): return "Cancer"
        if (month == 7 and day >= 23) or (month == 8 and day <= 22): return "Leo"
        if (month == 8 and day >= 23) or (month == 9 and day <= 22): return "Virgo"
        if (month == 9 and day >= 23) or (month == 10 and day <= 22): return "Libra"
        if (month == 10 and day >= 23) or (month == 11 and day <= 21): return "Scorpio"
        if (month == 11 and day >= 22) or (month == 12 and day <= 21): return "Sagittarius"
        if (month == 12 and day >= 22) or (month == 1 and day <= 19): return "Capricorn"
        if (month == 1 and day >= 20) or (month == 2 and day <= 18): return "Aquarius"
        return "Pisces"
    except ValueError:
        return "Aries"

def calculate_life_path(dob_str):
    """Calculates Life Path Number, respecting Master Numbers 11, 22, and 33."""
    digits = [int(d) for d in dob_str if d.isdigit()]
    total = sum(digits)
    while total > 9:
        if total in [11, 22, 33]:
            return total
        total = sum(int(d) for d in str(total))
    return total

def call_celestial_oracle(prompt):
    """
    Connects to the Gemini 2.5 Flash API to generate a professional synastry report.
    Implements exponential backoff for reliability.
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "systemInstruction": {
            "parts": [{"text": "You are a world-renowned master of Synastry, Astrology, and Numerology. Your task is to provide a highly detailed, poetic, and accurate compatibility analysis. Use sections like 'Elemental Harmony', 'The Numerological Bridge', 'Potential Shadow Work', and 'A Final Cosmic Verdict'. Be profound and insightful."}]
        }
    }
    
    # Exponential backoff: 1s, 2s, 4s, 8s, 16s
    for delay in [1, 2, 4, 8, 16]:
        try:
            req = urllib.request.Request(
                url, 
                data=json.dumps(payload).encode('utf-8'), 
                headers={'Content-Type': 'application/json'}
            )
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode('utf-8'))
                return result['candidates'][0]['content']['parts'][0]['text']
        except Exception:
            time.sleep(delay)
            
    return "The cosmic energies are currently turbulent, master. Please check your connection or try again later."

# --- MAIN PROGRAM ---

def run_compatibility_analysis():
    print("✨ WELCOME TO THE COSMIC SYNASTRY ENGINE, MASTER ✨")
    print("--------------------------------------------------")

    # Person 1 Data
    name1 = input("Enter First Name: ")
    dob1 = input("Enter Date of Birth (DD-MM-YYYY): ")
    
    # Person 2 Data
    name2 = input("Enter Second Name: ")
    dob2 = input("Enter Date of Birth (DD-MM-YYYY): ")

    # Basic Validations/Calculations
    z1 = get_zodiac(dob1)
    lp1 = calculate_life_path(dob1)
    z2 = get_zodiac(dob2)
    lp2 = calculate_life_path(dob2)

    # Individual Profile Analysis
    print(f"\n[READING THE HEAVENS FOR {name1.upper()}...]")
    time.sleep(0.5)
    print(f" > Zodiac: {z1} ({ZODIAC_DATA[z1]['element']} Element, Ruled by {ZODIAC_DATA[z1]['planet']})")
    print(f" > Life Path {lp1}: {NUMEROLOGY_DATA.get(lp1, 'A unique vibrational frequency.')}")

    print(f"\n[READING THE HEAVENS FOR {name2.upper()}...]")
    time.sleep(0.5)
    print(f" > Zodiac: {z2} ({ZODIAC_DATA[z2]['element']} Element, Ruled by {ZODIAC_DATA[z2]['planet']})")
    print(f" > Life Path {lp2}: {NUMEROLOGY_DATA.get(lp2, 'A unique vibrational frequency.')}")

    # Prepare Synastry Prompt
    ai_prompt = (
        f"Generate a deep compatibility report for {name1} and {name2}. "
        f"{name1} info: {z1} sun sign, {ZODIAC_DATA[z1]['element']} element, Life Path {lp1}. "
        f"{name2} info: {z2} sun sign, {ZODIAC_DATA[z2]['element']} element, Life Path {lp2}. "
        f"Include a final compatibility percentage score."
    )

    print("\n[INITIATING DEEP COSMIC CONNECTION... PLEASE WAIT...]")
    oracle_verdict = call_celestial_oracle(ai_prompt)

    print("\n" + "═"*60)
    print("              COMPLETE SYNASTRY REPORT")
    print("═"*60)
    print(oracle_verdict)
    print("═"*60)
    print(f"\nThe stars have revealed their secrets for you, master.")

if __name__ == "__main__":
    run_compatibility_analysis()