from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import random
import requests
import webbrowser
import os
import keyboard
from colorama import Fore
from pystyle import Center, Colors, Colorate
import time


os.system(f"title Kichi779 - Spotify Streaming bot v1 ")

url = "https://github.com/Kichi779/Spotify-Streaming-Bot/"


def check_for_updates():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Spotify-Streaming-Bot/main/version.txt")
        remote_version = r.content.decode('utf-8').strip()
        local_version = open('version.txt', 'r').read().strip()
        if remote_version != local_version:
            print(Colors.red, Center.XCenter("A new version is available. Please download the latest version from GitHub"))
            time.sleep(2)
            webbrowser.open(url)
            return False
        return True
    except:
        return True


def print_announcement():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Spotify-Streaming-Bot/main/announcement.txt", headers={"Cache-Control": "no-cache"})
        announcement = r.content.decode('utf-8').strip()
        return announcement
    except:
        print("Could not retrieve announcement from GitHub.\n")

def main():
    if not check_for_updates():
        return
    announcement = print_announcement()
    print(Colorate.Vertical(Colors.white_to_green, Center.XCenter("""
           
                       ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                       ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                       ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                      ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                     ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                       ███▐██▄   ███   ███    █▄    ███    ███   ███  
                       ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                       ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                       ▀                                             
 Improvements can be made to the code. If you're getting an error, visit my discord.
                             Discord discord.gg/AFV9m8UXuT    
                             Github  github.com/kichi779    """)))
    print("")
    print(Colors.red, Center.XCenter("ANNOUNCEMENT"))
    print(Colors.yellow, Center.XCenter(f"{announcement}"))
    print("")

    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ["enable-automation", 'enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument("--window-size=1366,768")
    chrome_options.add_argument("--lang=en-US,en;q=0.9")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option('prefs', {
        'profile.default_content_setting_values.notifications': 2
    })

    delay = random.uniform(2, 6)
    delay2 = random.uniform(5, 14)

    with open('accounts.txt', 'r') as file:
        accounts = file.readlines()

    proxies = []

    use_proxy = input(Colorate.Vertical(Colors.green_to_blue, "Do you want to use proxies? (y/n):"))

    if use_proxy.lower() == 'y':
        print(Colors.red, Center.XCenter("The proxy system will be added after 50 stars. I continue to process without a proxy"))
        with open('proxy.txt', 'r') as file:
            proxies = file.readlines()
        time.sleep(3)
    
    spotify_song = input(Colorate.Vertical(Colors.green_to_blue, "Enter the Spotify song URL (e.g https://open.spotify.com/track/5hFkGfx038V0LhqI0Uff2J?si=bf290dcc9a994c36):"))

    drivers = []

    for account in accounts:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        username, password = account.strip().split(':')


        try:
            driver.get("https://www.spotify.com/us/login/")

            username_input = driver.find_element(By.CSS_SELECTOR, "input#login-username")
            password_input = driver.find_element(By.CSS_SELECTOR, "input#login-password")

            username_input.send_keys(username)
            time.sleep(3)
            password_input.send_keys(password)

            driver.find_element(By.CSS_SELECTOR, "button[data-testid='login-button']").click()

            time.sleep(delay)

            driver.get(spotify_song)

            driver.maximize_window()

            keyboard.press_and_release('esc')

            time.sleep(10)

            try:
                cookie = driver.find_element(By.XPATH, "//button[text()='Accept Cookies']")
                cookie.click()
            except NoSuchElementException:

             try:
                button = driver.find_element(By.XPATH, "//button[contains(@class,'onetrust-close-btn-handler onetrust-close-btn-ui')]")
                button.click()
             except NoSuchElementException:
         

              time.sleep(delay2)

            playmusic_xpath = "(//button[@data-testid='play-button']//span)[3]"
            playmusic = driver.find_element(By.XPATH, playmusic_xpath)
            playmusic.click()

            time.sleep(1)

            print(Colors.green, "Username: {} - Listening process has started.".format(username))

        except Exception as e:
            print(Colors.red, "An error occurred in the bot system:", str(e))

        drivers.append(driver)

        time.sleep(5)

    print(Colors.blue, "Stream operations are completed. You can stop all transactions by closing the program.")

    while True:
        pass

if __name__ == "__main__":
    main()

# ==========================================
# Copyright 2023 Kichi779

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==========================================