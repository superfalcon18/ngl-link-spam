from multiprocessing.connection import wait
import os
import time
import requests
from colorama import init, Fore

init(autoreset=False)
os.system("cls")
r = requests.Session()
print("HEHE")
target = input(f"Target: ")
question = input("Question: ")
start = input("Boom? Y/N:").upper()
def spam():
    questions_count = 0
    url = f"https://ngl.link/{target}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }

    payload = {
        "question": question
    }
    while True:
        spam = r.post(url, headers=headers, data=payload)
        questions_count += 1
        print(f"{questions_count} Questions Sent to: {target} hehe")
        time.sleep(0.5)
        
if start == "Y":
    spam()
else:
    print("eorrrorr")
    exit()
