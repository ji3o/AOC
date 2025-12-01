import requests

def get_aoc_input(year, day):
    
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    
    with open('SK/sk.txt') as f:
        session_key = f.read()
    
    sk = {
        'session': session_key
    }
    
    response = requests.get(url, cookies=sk)
    
    lines = response.text.strip().split('\n') #always put in list
    
    return lines