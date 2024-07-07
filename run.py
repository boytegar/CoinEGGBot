import random
import requests
import time
import urllib.parse
import json
import base64
import socket
from datetime import datetime

def load_credentials():
    # Membaca token dari file dan mengembalikan daftar token
    try:
        with open('query_id.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        # print("Token berhasil dimuat.")
        return queries
    except FileNotFoundError:
        print("File query_id.txt tidak ditemukan.")
        return [  ]
    except Exception as e:
        print("Terjadi kesalahan saat memuat token:", str(e))
        return [  ]
    
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
    'content-length': '0',
    'priority': 'u=1, i',
    'Origin': 'https://app-coop.rovex.io',
    'Referer': 'https://app-coop.rovex.io/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
}

def profile(query):
    url = "https://egg-api.hivehubs.app/api/login/tg"
    data = {
          'init_data': query,
          'referrer': ""
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, json=data, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None
    
def assets(token):
    url = "https://egg-api.hivehubs.app/api/user/assets"
    data = {
          'token': token,
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, json=data, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def info(token):
    url = "https://egg-api.hivehubs.app/api/scene/info"
    data = {
          'token': token,
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, json=data, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def reward(token, uid):
    url = "https://egg-api.hivehubs.app/api/scene/egg/reward"
    data = {
        'egg_uid': uid,
        'token': token,
    }

    # {"token":"4c34a8ba5b434f95ac9baae2a4374ffa","code":"ba29e69e120e4cb18a27cffe49d3de4e"}

    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, json=data, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def redpacket():
    url = "https://egg-api.hivehubs.app/api/red/get"

def mainclaim():
     
    while True:
        queries = load_credentials()

        for query in queries:
            _profile = profile(query)
            if _profile is not None:
                data = _profile.get('data')
                user = data.get('user')
                token = data.get('token')
                print(f"ID : {user.get('id')} - NAME : {user.get('display_name')}")
                tokens = token.get('token')

                _assets = assets(tokens)
                data    = _assets.get('data')
                if _assets.get('data') != {}:
                    diamond = 0
                    if data.get('diamond') != None:
                        diamond = data['diamond']['amount']
                    egg = 0
                    if data.get('egg') != None:
                        egg = data['egg']['amount'] 
                    usdt = 0
                    if data.get('usdt') != None:
                        usdt = data['usdt']['amount']

                    print(f'assets [ egg : {egg} | usdt: {usdt} | diamond: {diamond} ]')
                    print()
                
                _info = info(tokens)
                if _info is not None:
                    data = _info.get('data')
                    for d in data:
                        scene = d.get('scene_type')
                        print(f'======= FLOOR {scene+1} =======')
                        eggs = d.get('eggs')
                        if eggs != 0:
                            for egg in eggs:
                                uid = egg.get('uid')
                                _reward = reward(tokens, uid)
                                if _reward is not None:
                                    data_reward = _reward.get('data')
                                    type = data_reward.get('a_type')
                                    amount = data_reward.get('amount')
                                    print(f"id {uid} | type : {type} | amount : {amount}")
                                    time.sleep(2)

        delay = random.randint(600, 800)
        printdelay(delay)
        time.sleep(delay)

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

def main():
    print(r"""
        
            Created By Snail S4NS Group
    find new airdrop & bot here: t.me/sanscryptox
              
        select this one :
        1. claim Auto Egg all floor
          
          """)

    selector = input("Select the one ? (default 1): ").strip().lower()

    if selector == '1':
        mainclaim()
    else:
        exit()

def printdelay(delay):
    now = datetime.now().isoformat(" ").split(".")[0]
    hours, remainder = divmod(delay, 3600)
    minutes, sec = divmod(remainder, 60)
    print(f"{now} | Waiting Time: {hours} hours, {minutes} minutes, and {sec} seconds")


def print_welcome_message(serial=None):
    print(r"""
              
            Created By Snail S4NS Group
    find new airdrop & bot here: t.me/sansxgroup
              
          """)
    print()
    if serial is not None:
        print(f"Copy, tag bot @SnailHelperBot and paste this key in discussion group t.me/sansxgroup")
        print(f"Your key : {serial}")

def read_serial_from_file(filename):
    serial_list = []
    with open(filename, 'r') as file:
        for line in file:
            serial_list.append(line.strip())
    return serial_list

serial_file = "serial.txt"
serial_list = read_serial_from_file(serial_file)


def get_serial(current_date, getpcname, name, status):
    formatted_current_date = current_date.strftime("%d-%m-%Y")
    # Encode each value using base64
    getpcname += "knjt"
    name    += "knjt"
    encoded_getpcname = base64.b64encode(getpcname.encode()).decode().replace("=", "")
    encoded_current_date = base64.b64encode(formatted_current_date.encode()).decode().replace("=", "")
    encoded_name = base64.b64encode(name.encode()).decode().replace("=", "")
    encoded_status = base64.b64encode(str(status).encode()).decode().replace("=", "")

    # Calculate the length of each encoded value
    getpcname_len = len(encoded_getpcname)
    current_date_len = len(encoded_current_date)
    name_len = len(encoded_name)
    status_len = len(encoded_status)

    # Concatenate the encoded values with their lengths
    serial = "S4NS-"
    serial += str(getpcname_len).zfill(2) + encoded_getpcname
    serial += str(current_date_len).zfill(2) + encoded_current_date
    serial += str(name_len).zfill(2) + encoded_name
    serial += str(status_len).zfill(2) + encoded_status
    return serial

def decode_pc(serial, getpcname, name, current_date):
    try:
        getpcname_len = int(serial[5:7])
        encoded_getpcname = serial[7:7+getpcname_len]
        current_date_len = int(serial[7+getpcname_len:9+getpcname_len])
        encoded_current_date = serial[9+getpcname_len:9+getpcname_len+current_date_len]
        name_len = int(serial[9+getpcname_len+current_date_len:11+getpcname_len+current_date_len])
        encoded_name = serial[11+getpcname_len+current_date_len:11+getpcname_len+current_date_len+name_len]
        status_len = int(serial[11+getpcname_len+current_date_len+name_len:13+getpcname_len+current_date_len+name_len])
        encoded_status = serial[13+getpcname_len+current_date_len+name_len:13+getpcname_len+current_date_len+name_len+status_len]

        # Decode each value using base64
        decoded_getpcname = base64.b64decode(encoded_getpcname + "==").decode()
        decoded_current_date = base64.b64decode(encoded_current_date + "==").decode()
        decoded_name = base64.b64decode(encoded_name + "==").decode()
        decoded_status = base64.b64decode(encoded_status + "==").decode()
        
        dates = compare_dates(decoded_current_date)

        if decoded_status != '1':
            print("Key Not Generated")
            return None
            
        elif decoded_getpcname.replace("knjt", "") != getpcname:
            print("Different devices registered")
            return None
        
        elif decoded_name.replace("knjt", "") != name:
            print("Different bot registered")
            return None
        
        elif dates < 0:
            print("Key Expired")
            return None
        else:
            print(f"            Key alive until : {decoded_current_date} ")
            return dates
    except Exception as e:
        print(f'Key Error : {e}')

def compare_dates(date_str):
    tanggal_compare_dt = datetime.strptime(date_str, '%d-%m-%Y')
    tanggal_now = datetime.now()
    perbedaan_hari = (tanggal_compare_dt - tanggal_now).days
    return perbedaan_hari

def started():
    getpcname = socket.gethostname()
    name = "COINEGG"
    current_date = datetime.now() # Get the current date
    status = '0'

    if len(serial_list) == 0:
        serial = get_serial(current_date, getpcname, name, status)
        print_welcome_message(serial)
    else:
        serial = serial_list[0]
        if serial == 'S4NS-XXWEWANTBYPASSXX':
            main()
        else:
            decodeds = decode_pc(serial, getpcname, name, current_date)
            if decodeds is not None:
                    print_welcome_message()
                    time.sleep(10)
                    main()         
            else:
                serial = get_serial(current_date, getpcname, name, status)
                print_welcome_message(serial)
                print("Please submit the key to bot for get new key")
            


if __name__ == "__main__":
     started()
