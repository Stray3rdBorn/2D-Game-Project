import os
import threading

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("ARENA_API_URL", "http://127.0.0.1:8000")
API_KEY = os.getenv("ARENA_API_KEY")


def _post_score(score, wave_reached, won):
    try:
        requests.post(
            f"{API_URL}/scores",
            json={"score": score, "wave_reached": wave_reached, "won": won},
            headers={"X-API-Key": API_KEY},
            timeout=3,
        )
    except requests.RequestException:
        pass


def submit_score(score, wave_reached, won):
    if not API_KEY:
        return
    threading.Thread(target=_post_score, args=(score, wave_reached, won), daemon=True).start()