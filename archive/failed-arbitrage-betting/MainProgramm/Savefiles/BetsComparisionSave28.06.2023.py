from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from Calculations import Calculations
import time
import keyboard


def login(account_num):
    webDriver.get("https://www.tiktok.com/")
    #logInCloseButton = webDriver.find_element(By.CSS_SELECTOR, ".tiktok-lps1dn-Button-StyledLoginButton")

    """accept_button = webDriver.find_element(By.CSS_SELECTOR, "button[type='button']")
    print(accept_button)
    time.sleep(1)
    accept_button.click()"""
    time.sleep(1)
    googleLoginButton = waitDriver.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-e2e="channel-item"]')))
    print(googleLoginButton)
    googleLoginButton[3].click()
    window_handles = webDriver.window_handles
    print(window_handles)
    webDriver.switch_to.window(window_handles[1])
    un_input_field = waitDriver.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"][name="identifier"]')))
    un_input_field.send_keys(nameAndPassList[account_num][0])
    button_google_account = waitDriver.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-idom-class="nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]')))
    button_google_account.click()
    pa_input_field = waitDriver.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"].whsOnd.zHQkBf')))
    pa_input_field.send_keys(nameAndPassList[account_num][1])
    button_google_account_login = waitDriver.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button')))
    print(button_google_account_login)
    button_google_account_login.click()
    webDriver.switch_to.window(window_handles[0])
    """googleLoginButton[1].click()
    logInViaUsernameAndMail = waitDriver.until(EC.presence_of_element_located((By.LINK_TEXT, "Mit E-Mail-Adresse oder Benutzernamen anmelden")))
    logInViaUsernameAndMail.click()
    userName = waitDriver.until(EC.presence_of_element_located((By.NAME, "username")))
    userName.send_keys(nameAndPassList[0][0])
    password = waitDriver.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
    password.send_keys(nameAndPassList[0][1])
    logInButton = waitDriver.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[data-e2e="login-button"]')))
    if systemready:
        logInButton.click()"""

def on_key_press(event):
    if event.name == 'q':
        keyboard.unhook(on_key_press)

def human_solving():
    keyboard.hook(on_key_press)
    keyboard.wait('q')      #If human solved puzzle, he presses "q"


def cookies():
    webDriver.get("https://chrome.google.com/webstore/detail/i-still-dont-care-about-c/edibdbjcniadpccecjdfdjjppcpchdlm")
    #time.sleep(1)
    #element = webDriver.find_element(By.CSS_SELECTOR, 'div.h-e-f-Ra-c.e-f-oh-Md-zb-k [aria-label="Hinzufügen"]')
    cookieButton = waitDriver.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.h-e-f-Ra-c.e-f-oh-Md-zb-k [aria-label="Hinzufügen"]')))
    #print(element)
    cookieButton.click()

def get_list_pinnacle():
    #webDriver.get("https://www.pinnacle.com/de/")
    #pinnacle_tennis_liste = pinnacle_tennis()
    pinnacle_tennis_liste = """HEUTE
(39)
ATP EASTBOURNE - R1
MONEYLINE
HANDICAP
ÜBER
UNTER
Ryan Peniston (Sätze)
Marc-Andrea Huesler (Sätze)
18:00
2.000
1.892
+1.5
1.390
-1.5
3.180
2.5
2.220
2.5
1.714
+11
Ryan Peniston (Spiele )
Marc-Andrea Huesler (Spiele )
18:00
+0.5
1.900
-0.5
1.970
23
1.869
23
2.000
+7
WTA BAD HOMBURG - R1
MONEYLINE
HANDICAP
ÜBER
UNTER
Iga Świątek (Sätze)
Tatjana Maria (Sätze)
18:00
1.129
6.830
-1.5
1.416
+1.5
3.050
2.5
3.620
2.5
1.319
+11
Iga Świątek (Spiele )
Tatjana Maria (Spiele )
18:00
-5.5
1.892
+5.5
1.980
19
1.892
19
1.980
+7
WTA EASTBOURNE - R1
MONEYLINE
HANDICAP
ÜBER
UNTER
Madison Keys (Sätze)
Tereza Martincova (Sätze)
18:00
1.404
3.060
-1.5
2.120
+1.5
1.763
2.5
2.410
2.5
1.606
+11
Madison Keys (Spiele )
Tereza Martincova (Games)
18:00
-3.5
1.925
+3.5
1.925
22
1.990
22
1.869
+7
ATP CHALLENGER MEDELLIN - R1
MONEYLINE
HANDICAP
ÜBER
UNTER
Tristan Schoolkate (Sätze)
Eduardo Ribeiro (Sätze)
21:00
2.040
1.806
+1.5
1.454
-1.5
2.810
2.5
2.560
2.5
1.531
+11"""
    pinnacle_tennis_string_converter(pinnacle_tennis_liste)


'''def pinnacle_tennis_element_info_getter(element):
    time.sleep(10)
    webDriver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)
    element.click()'''


def pinnacle_tennis_string_converter(content):
    all_events = []
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    while True:
        i += 1
        if i == len(content) - 1:
            break
        if i < len(content) - 4:
            if "UNTER" == f"{content[i]}{content[i + 1]}{content[i + 2]}{content[i + 3]}{content[i + 4]}":
                new_segment = content[:i]
                content = content[i+4:]
                i = 0
                all_events.append(new_segment)

    all_events.pop(0)
    for k in range(2):
        for i in range(len(all_events)):
            j = len(all_events[i])
            while True:
                j -= 1
                #break
                if all_events[i][j] in numbers:
                    all_events[i] = all_events[i][:j]
                    break

    all_games = []
    x = ""
    for i in range(len(all_events)):
        x += all_events[i]
    #print(all_events, "!!!!!!!!!!!!!!!!!!!!!!!!", x)
    all_events = x
    list_all_n_parts = []
    last_i = 0
    for i in range(len(all_events)):        # split all \n
        if "\n" == f"{all_events[i]}":
            list_all_n_parts.append(all_events[last_i:i])
            last_i = i
    for i in range(len(list_all_n_parts)):      # same list without the \n at beginning
        if "\n" == list_all_n_parts[i][0]:
            list_all_n_parts[i] = list_all_n_parts[i][1:]
    print(list_all_n_parts)
    list_of_full_game = []
    next_append = ""
    wait_for_next_char = False
    for i in range(1, len(list_all_n_parts)):
        if ("Spiele" in list_all_n_parts[i - 1] or "Sätze" in list_all_n_parts[i - 1]) and ("Spiele" in list_all_n_parts[i] or "Sätze" in list_all_n_parts[i]):
            next_append += list_all_n_parts[i - 1] + " " + list_all_n_parts[i]
            wait_for_next_char = True
        elif list_all_n_parts[i][0] not in alphabet and wait_for_next_char == True:
            next_append += " " + list_all_n_parts[i]
        elif list_all_n_parts[i][0] in alphabet and wait_for_next_char == True:
            list_of_full_game.append(next_append)
            next_append = ""
            wait_for_next_char = False
    print(list_of_full_game)
    """for j in range(len(all_events)):        # algorythm to seperate games
        i = -1
        while True:
            i += 1
            if i == len(all_events[j]) - 1:
                break
            if i < len(all_events[j]) - 4:
                if "Sätze" == f"{all_events[j][i]}{all_events[j][i + 1]}{all_events[j][i + 2]}{all_events[j][i + 3]}{all_events[j][i + 4]}":
                    print("1", all_events[j][:i])
                    while True:
                        i -= 1
                        if i >= 0 and "\n" == f"{all_events[j][i]}{all_events[j][i + 1]}":
                            all_games.append(all_events[j][:i])
                            print("1", all_events[j][:i])
                            all_events[j] = all_events[j][i:]
                            i = 0
                            break
                    over_it = 0
                    while True:
                        if over_it == 2:
                            over_it = 0
                            break
                        if i < len(all_events[j]) - 4:
                            if "Sätze" == f"{all_events[j][i]}{all_events[j][i + 1]}{all_events[j][i + 2]}{all_events[j][i + 3]}{all_events[j][i + 4]}":
                                over_it += 1
                if "Spie" == f"{all_events[j][i]}{all_events[j][i + 1]}{all_events[j][i + 2]}{all_events[j][i + 3]}{all_events[j][i + 4]}":
                    while True:
                        i -= 1
                        if i >= 0 and "\n" == f"{all_events[j][i]}{all_events[j][i + 1]}":
                            all_games.append(all_events[j][:i])
                            print("2", all_events[j][:i])
                            all_events[j] = all_events[j][i:]
                            i = 0
                            break
                    over_it = 0
                    while True:
                        if over_it == 2:
                            over_it = 0
                            break
                        if i < len(all_events[j]) - 4:
                            if "Spie" == f"{all_events[j][i]}{all_events[j][i + 1]}{all_events[j][i + 2]}{all_events[j][i + 3]}{all_events[j][i + 4]}":
                                over_it += 1"""
    #print(all_events, all_games)

def pinnacle_tennis():
    webDriver.get("https://www.pinnacle.com/de/tennis/matchups")

    scrollable_element = waitDriver.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/main/div/div[2]/div")))
    #scrollable_element = waitDriver.until(EC.presence_of_element_located((By.CLASS_NAME, "style_list__VpX-E")))

    # Get initial content
    initial_content = scrollable_element.text

    # Get the total scroll height of the element
    scroll_height = webDriver.execute_script("return arguments[0].scrollHeight", scrollable_element)

    # Set the segment height for scrolling
    segment_height = 300

    # Initialize the current scroll position
    current_scroll_position = 0

    loaded_content = ""
    # Scroll in segments until reaching the bottom
    while current_scroll_position < scroll_height:
        # Scroll to the current position + segment height using JavaScript
        webDriver.execute_script("arguments[0].scrollTop = arguments[1]", scrollable_element,
                                 current_scroll_position + segment_height)

        # Wait for a small delay to allow new content to load
        time.sleep(0.2)  # Adjust the delay as needed

        # Update the current scroll position
        current_scroll_position += segment_height

        loaded_content += scrollable_element.text
        print(len(loaded_content), "!!!!!!")


    # Combine the initial content and the loaded content
    complete_content = initial_content + "\n" + loaded_content

    print(len(complete_content), complete_content)
    return complete_content


def pinnacle_tennis_false():
    webDriver.get("https://www.pinnacle.com/de/tennis/matchups")

    scrollable_element = waitDriver.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/main/div/div[2]/div")))
    #scrollable_element = waitDriver.until(EC.presence_of_element_located((By.CLASS_NAME, "style_list__VpX-E")))

    # Get initial content
    initial_content = scrollable_element.text

    # Get the total scroll height of the element
    scroll_height = webDriver.execute_script("return arguments[0].scrollHeight", scrollable_element)

    # Set the segment height for scrolling
    segment_height = 300

    # Initialize the current scroll position
    current_scroll_position = 0

    loaded_content = ""
    # Scroll in segments until reaching the bottom
    while current_scroll_position < scroll_height:
        # Scroll to the current position + segment height using JavaScript
        webDriver.execute_script("arguments[0].scrollTop = arguments[1]", scrollable_element,
                                 current_scroll_position + segment_height)

        # Wait for a small delay to allow new content to load
        time.sleep(0.2)  # Adjust the delay as needed

        # Update the current scroll position
        current_scroll_position += segment_height

        loaded_content += scrollable_element.text
        print(len(loaded_content), "!!!!!!")


    # Combine the initial content and the loaded content
    complete_content = initial_content + "\n" + loaded_content

    print(len(complete_content), complete_content)

    """# Get initial content
    initial_content = scrollable_element.text

    # Scroll to the bottom of the element using JavaScript
    webDriver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_element)

    # Wait for a small delay to allow new content to load
    time.sleep(5)  # Adjust the delay as needed

    # Keep scrolling and waiting for new content to load until no more new content is loaded
    previous_content = ""
    loaded_content = ""
    i=0
    while True:
        i += 1
        print(i)
        # Scroll to the bottom of the element using JavaScript
        webDriver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_element)

        # Wait for a small delay to allow new content to load
        time.sleep(2)  # Adjust the delay as needed

        # Retrieve the new content
        new_content = scrollable_element.text

        # Break the loop if no new content is loaded
        if new_content == previous_content:
            break

        # Update the previous content
        previous_content = new_content
        loaded_content = loaded_content + "\n" + new_content

    # Combine the initial content and all the loaded content
    complete_content = initial_content + "\n" + loaded_content

    print(len(complete_content), complete_content)"""

    """# Scroll to the bottom of the element using JavaScript
    webDriver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_element)

    # Wait for a small delay to allow the content to load
    time.sleep(2)  # Adjust the delay as needed

    # Scroll to the top of the element using JavaScript
    webDriver.execute_script("arguments[0].scrollTop = 0", scrollable_element)

    # Retrieve the complete content
    complete_content = scrollable_element.text

    print("THIS IS IT", complete_content)"""
    #------------------
    print(scrollable_element.text)
    time.sleep(2)
    scroll_height = webDriver.execute_script("return arguments[0].scrollHeight", scrollable_element)
    #webDriver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_element)
    listen_element = waitDriver.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/main/div/div[2]/div/div[2]/div/div")))
    match_elements = []
    match_elements.append(listen_element.find_elements(By.CLASS_NAME, "scrollbar-item"))
    """all_tennis_match_elements_values = {}

    for i in range(len(match_elements[-1])):
        all_tennis_match_elements_values[match_elements[-1][i]] = match_elements[-1][i].text"""
    start_time = time.time()
    while time.time() - start_time < 5:

        match_elements.append(listen_element.find_elements(By.CLASS_NAME, "scrollbar-item"))
        """for i in range(len(match_elements[-1])):
            #try:
            all_tennis_match_elements_values[match_elements[-1][i]] = match_elements[-1][i].text
            #except:
                #pass"""

        webDriver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_element)
        time.sleep(0.1)  # Adjust the sleep duration as needed

        # Check if scrolling reached the bottom
        new_scroll_height = webDriver.execute_script("return arguments[0].scrollHeight", scrollable_element)
        if new_scroll_height == scroll_height:
            break

        scroll_height = new_scroll_height

    match_liste_Element = []
    for i in range(len(match_elements)):
        if type(match_elements[i]) == list:
            for j in range(len(match_elements[i])):
                if match_elements[i][j] not in match_liste_Element:
                    match_liste_Element.append(match_elements[i][j])
        else:
            if match_elements[i] not in match_liste_Element:
                match_liste_Element.append(match_elements[i])
    print(f"hier: {len(match_elements)}", match_elements)
    print(f"hier: {len(match_liste_Element)}", match_liste_Element)
    print(match_liste_Element[-1], match_liste_Element[-1].text)
    #print(all_tennis_match_elements_values)
    '''webDriver.execute_script("arguments[0].scrollTop = 0", scrollable_element)'''
    '''pinnacle_tennis_element_info_getter(match_liste_Element[0])'''
    """tennis_button = waitDriver.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/aside[1]/div[3]/ul/li[15]")))
    tennis_button.click()"""
    """all_matches = waitDriver.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[2]/div/div[2]/main/div/div[2]/div/div[2]/div/div/div[7]/div")))
    print(all_matches)"""
    """goes_on, i = True, 1
    while goes_on:
        i += 1
        try:
            try:
                tennis_match = waitDriver.until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[2]/div/div[2]/main/div/div[2]/div/div[2]/div/div/div[{i}]/div/div[1]/div/a/div/div")))
                webDriver.execute_script("arguments[0].scrollIntoView();", tennis_match)
                names = tennis_match.find_elements(By.CLASS_NAME, "event-row-participant")
                name_list = [name.text for name in names]
                for name in name_list:
                    print(i, name)
            except:
                i += 1
                tennis_match = waitDriver.until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[2]/div/div[2]/main/div/div[2]/div/div[2]/div/div/div[{i}]/div/div[1]/div/a/div/div")))
                webDriver.execute_script("arguments[0].scrollIntoView();", tennis_match)
                names = tennis_match.find_elements(By.CLASS_NAME, "event-row-participant")
                name_list = [name.text for name in names]
                for name in name_list:
                    print(i, name)
        except:
            goes_on = False"""
    "/html/body/div[2]/div/div[2]/main/div/div[2]/div/div[2]/div/div/div[2]/div"
    "/html/body/div[2]/div/div[2]/main/div/div[2]/div/div[2]/div/div/div[3]/div"
    "/html/body/div[2]/div/div[2]/main/div/div[2]/div/div[2]/div/div/div[4]/div"
    "/html/body/div[2]/div/div[2]/main/div/div[2]/div/div[2]/div/div/div[5]/div"
    "/html/body/div[2]/div/div[2]/main/div/div[2]/div/div[2]/div/div/div[7]/div"
    "/html/body/div[2]/div/div[2]/main/div/div[2]/div/div[2]/div/div/div[6]/div"
    "/html/body/div[2]/div/div[2]/main/div/div[2]/div/div[2]/div/div/div[7]/div"


s = Service("chromedriver_bypass.exe")

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--diable-blink-features=AutomationControlled")

webDriver = webdriver.Chrome(service=s, options=options)
waitDriver = WebDriverWait(webDriver, 7)
# path_to_chromedriver = 'chromedriver.exe'
# webDriver = webdriver.Chrome(executable_path=path_to_chromedriver)


get_list_pinnacle()
"""cookies()
time.sleep(2)
login(0)
human_solving()"""
time.sleep(9999)


webDriver.quit()