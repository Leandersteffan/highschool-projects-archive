from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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

def get_list_tennis():
    #webDriver.get("https://www.pinnacle.com/de/")
    pinnacle_tennis_liste = pinnacle_tennis()
    pinnacle_tennis_liste1 = """HEUTE
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
    pinnacle_matches = pinnacle_tennis_string_converter(pinnacle_tennis_liste)
    sport888_tennis_liste = sport888_tennis()
    #webDriver.quit()
    sport888_tennis_liste1 = """ATP EASTBOURNE
1
2
Wolf, JJ
4
6
5
0
Paul, Tommy
6
4
5
30
Satz 3
2.25
1.615 WTA BAD HOMBURG
1
2
Siniakova, Katerina
7
0
0
Samsonova, Liudmila
5
0
0
Satz 2
1.333
2.90 WTA EASTBOURNE
1
2
Ostapenko, Jelena
4
30
Giorgi, Camila
3
40
Satz 1
1.47
2.50 ATP MODENA CHALLENGER
1
2
Ferrari, G
1
0
0
Nava, Emilio
6
0
0
Satz 2
7.00
1.062
Kasnikowski, M
0
15
Droguet, T
2
40
Satz 1
4.00
1.20 ATP MEDELLIN CHALLENGER DOPPEL
1
2
King, E/Kirkov, V
Goldhoff, G/Soto, M
03:58
1.533
2.30
Alves, M/Couto Loureiro, J
Puttergill, C/Stevenson, K
22:12
2.05
1.667
Urrea, A/Gomez, JS
Descotte, MF/Rodriguez Taverna, SF
22:30
3.25
1.30"""
    sport888_matches = sport888_tennis_string_converter(sport888_tennis_liste)
    print("pppppppp", pinnacle_matches)
    print("ssssssss", sport888_matches)
    finale_liste_mit_booki = match_lists(pinnacle_matches, sport888_matches)
    print(abitrage_number_list_maker(finale_liste_mit_booki))



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
    i = -1       # get rid of not full match bets
    while True:
        i += 1
        if i >= len(list_of_full_game):
            break
        if "Spiele" in list_of_full_game[i]:
            list_of_full_game.pop(i)
    print(list_of_full_game)
    all_games = []# make list of players and full game bets in big list
    for i in range(len(list_of_full_game)):
        beginning = 0
        game = []
        doppelpunkt, bet_count = False, 0
        for j in range(4, len(list_of_full_game[i])):
            if "Sätze" == f"{list_of_full_game[i][j - 4]}{list_of_full_game[i][j - 3]}{list_of_full_game[i][j - 2]}{list_of_full_game[i][j - 1]}{list_of_full_game[i][j]}":
                game.append(list_of_full_game[i][beginning:j-6])
                beginning = j + 2
            if ":" == f"{list_of_full_game[i][j]}":
                doppelpunkt = True
            if " " == f"{list_of_full_game[i][j]}" and doppelpunkt == True:
                doppelpunkt = False
                beginning = j + 1
                bet_count += 1
            elif " " == f"{list_of_full_game[i][j]}" and doppelpunkt == False and bet_count == 1:
                game.append(list_of_full_game[i][beginning:j])
                beginning = j + 1
                bet_count += 1
            elif " " == f"{list_of_full_game[i][j]}" and doppelpunkt == False and bet_count == 2:
                game.append(list_of_full_game[i][beginning:j])
                bet_count += 1

        all_games.append(game)
    print(all_games)
    return all_games

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

def sport888_tennis_string_converter(content):
    #print(list[content])
    content_n_split = content.split("\n")
    #print(content_n_split)
    human_count, bet_count = 0, 0
    all_games = []
    game = []
    for i in range(len(content_n_split)):
        if "," in content_n_split[i] and human_count == 0:
            game.append(content_n_split[i])
            human_count += 1
        if "," in content_n_split[i] and human_count == 1 and content_n_split[i] not in game:
            game.append(content_n_split[i])
            human_count += 1
        if "." in content_n_split[i] and bet_count == 0 and human_count == 2:
            game.append(content_n_split[i])
            bet_count += 1
        if "." in content_n_split[i] and bet_count == 1 and human_count == 2 and content_n_split[i] not in game:
            x = content_n_split[i]
            j = 0
            while True:     # damit nächster Turniername nicht hinten dran hängt
                j += 1
                if j >= len(x):
                    break
                if " " == x[j]:
                    x = x[:j]
                    break
            game.append(x)
            all_games.append(game)
            game = []
            human_count, bet_count = 0, 0
    print(all_games)
    return all_games

    """new_beginning = 0
    games = []
    for i in range(4, len(content)):
        if "\n1\n2\n" == f"{content[i - 4]}{content[i - 3]}{content[i - 2]}{content[i - 1]}{content[i]}":
            games.append(content[new_beginning:i - 4])
            new_beginning = i + 1"""

def sport888_tennis():
    webDriver.get("https://www.888sport.de/tennis/")
    '''next_str = f"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/main/div[{13}]"
    match_box = waitDriver.until(EC.presence_of_element_located((By.XPATH, next_str)))
    """actions = ActionChains(webDriver)
    actions.move_to_element(match_box).perform()"""
    webDriver.execute_script("arguments[0].scrollIntoView();", match_box)
    print(match_box.text)'''
    time.sleep(1)
    i = 4
    all_games_string = ""
    while True:
        try:
            i += 1
            next_str = f"/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/main/div[{i}]"
            match_box = waitDriver.until(EC.presence_of_element_located((By.XPATH, next_str)))
            webDriver.execute_script("arguments[0].scrollIntoView();", match_box)
            all_games_string += " " + match_box.text
            #print(match_box.text)
        except:
            break
    print("!!!!!!!!!!!!!!!!", all_games_string)
    return all_games_string

def match_lists(liste1, liste2):      # 1. pinnacle   2. sport888
    finale_liste = []
    #liste1 = [['Lorenzo Claverie', ' Gage Brymer', '1.574', '2.300'], ['Maxwell McKennon', ' Edward Winter', '2.070', '1.704'], ['Christopher Papa', ' Isaiah Strode', '2.310', '1.571'], ['+3.0', '1.819'], ['Caroline Vernet', ' Brandy Walker', '3.180', '1.323'], ['Elise Wagle', ' Danielle Willson', '1.961', '1.787'], ['Eva Guerrero Alvarez', ' Varvara Lepchenko', '1.943', '1.800'], ['Lulu Sun', ' Valentina Ryser', '1.289', '3.390'], ['Talia Gibson', ' Alexandra Eala', '3.210', '1.316'], ['-6.5', '1.819'], ['Eudice Wong Chong', ' Anastasia Kovaleva', '1.404', '2.870'], ['Ya-Yi Yang', ' Anastasia Gasanova', '2.860', '1.404'], ['Lorenzo Claverie', ' Gage Brymer', '1.574', '2.300'], ['Maxwell McKennon', ' Edward Winter', '2.070', '1.704'], ['Christopher Papa', ' Isaiah Strode', '2.310', '1.571'], ['+3.0', '1.819'], ['Caroline Vernet', ' Brandy Walker', '3.180', '1.323'], ['Elise Wagle', ' Danielle Willson', '1.961', '1.787'], ['Eva Guerrero Alvarez', ' Varvara Lepchenko', '1.943', '1.800'], ['Lulu Sun', ' Valentina Ryser', '1.289', '3.390'], ['Talia Gibson', ' Alexandra Eala', '3.210', '1.316'], ['-6.5', '1.819'], ['Eudice Wong Chong', ' Anastasia Kovaleva', '1.404', '2.870'], ['Ya-Yi Yang', ' Anastasia Gasanova', '2.860', '1.404'], ['Lorenzo Claverie', ' Gage Brymer', '1.574', '2.300'], ['Maxwell McKennon', ' Edward Winter', '2.070', '1.704'], ['Christopher Papa', ' Isaiah Strode', '2.310', '1.571'], ['+3.0', '1.819'], ['Caroline Vernet', ' Brandy Walker', '3.180', '1.323'], ['Elise Wagle', ' Danielle Willson', '1.961', '1.787'], ['Eva Guerrero Alvarez', ' Varvara Lepchenko', '1.943', '1.800'], ['Lulu Sun', ' Valentina Ryser', '1.289', '3.390'], ['Talia Gibson', ' Alexandra Eala', '3.210', '1.316'], ['-6.5', '1.819'], ['Eudice Wong Chong', ' Anastasia Kovaleva', '1.404', '2.870'], ['Ya-Yi Yang', ' Anastasia Gasanova', '2.860', '1.404'], ['Lorenzo Claverie', ' Gage Brymer', '1.574', '2.300'], ['Maxwell McKennon', ' Edward Winter', '2.070', '1.704'], ['Christopher Papa', ' Isaiah Strode', '2.310', '1.571'], ['+3.0', '1.819'], ['Caroline Vernet', ' Brandy Walker', '3.180', '1.323'], ['Elise Wagle', ' Danielle Willson', '1.961', '1.787'], ['Eva Guerrero Alvarez', ' Varvara Lepchenko', '1.943', '1.800'], ['Lulu Sun', ' Valentina Ryser', '1.289', '3.390'], ['Talia Gibson', ' Alexandra Eala', '3.210', '1.316'], ['-6.5', '1.819'], ['Eudice Wong Chong', ' Anastasia Kovaleva', '1.404', '2.870'], ['Ya-Yi Yang', ' Anastasia Gasanova', '2.860', '1.404'], ['Lorenzo Claverie', ' Gage Brymer', '1.574', '2.300'], ['Maxwell McKennon', ' Edward Winter', '2.070', '1.704'], ['Christopher Papa', ' Isaiah Strode', '2.310', '1.571'], ['+3.0', '1.819'], ['Caroline Vernet', ' Brandy Walker', '3.180', '1.323'], ['Elise Wagle', ' Danielle Willson', '1.961', '1.787'], ['Eva Guerrero Alvarez', ' Varvara Lepchenko', '1.943', '1.800'], ['Lulu Sun', ' Valentina Ryser', '1.289', '3.390'], ['Talia Gibson', ' Alexandra Eala', '3.210', '1.316'], ['-6.5', '1.819'], ['Eudice Wong Chong', ' Anastasia Kovaleva', '1.404', '2.870'], ['Ya-Yi Yang', ' Anastasia Gasanova', '2.860', '1.404'], ['Lorenzo Claverie', ' Gage Brymer', '1.574', '2.300'], ['Maxwell McKennon', ' Edward Winter', '2.070', '1.704'], ['Christopher Papa', ' Isaiah Strode', '2.310', '1.571'], ['+3.0', '1.819'], ['Caroline Vernet', ' Brandy Walker', '3.180', '1.323'], ['Elise Wagle', ' Danielle Willson', '1.961', '1.787'], ['Eva Guerrero Alvarez', ' Varvara Lepchenko', '1.943', '1.800'], ['Lulu Sun', ' Valentina Ryser', '1.289', '3.390'], ['Talia Gibson', ' Alexandra Eala', '3.210', '1.316']]
    #liste2 = [['Siniakova, Katerina', 'Samsonova, Liudmila', '6.10', '1.091'], ['Kasnikowski, M', 'Droguet, T', '3.75', '1.222'], ['Coria, F', 'Fatic, N', '1.40', '2.80'], ['Mejia, N', 'Soriano Barrera, A', '1.10', '5.75'], ['King, E/Kirkov, V', 'Goldhoff, G/Soto, M', '1.80', '1.85'], ['Alves, M/Couto Loureiro, J', 'Puttergill, C/Stevenson, K', '2.05', '1.667'], ['Urrea, A/Gomez, JS', 'Descotte, MF/Rodriguez Taverna, SF', '3.30', '1.286'], ['Starastsenka, K', 'Otis, A', '1.25', '3.70'], ['Ramos Martin, P', 'Sepulveda, M', '2.65', '1.40'], ['Brace, Cadence', 'Sanchez, Ana Sofia', '1.30', '3.10'], ['Martinez Cirez, Carlota', 'Ansari, Carolyn', '1.10', '5.30'], ['9.50 ITF SPAIN 19A, WOMEN SINGLES', 'Savinykh, Valeria', '1.40', '2.50'], ['Gao, Xinyu', 'Paszek, Tamira', '2.30', '1.50'], ['Ishii, Sayaka', 'Perrin, Conny', '1.25', '3.40'], ['Garcia Perez, Georgina', 'Jones, Makenna', '3.10', '1.266'], ['Guerrero Alvarez, Eva', 'Lepchenko, Varvara', '2.00', '1.667'], ['Sun, Lulu', 'Ryser, Valentina', '1.266', '3.25'], ['Tan, Harmony', 'Morvayova, Viktoria', '1.062', '5.90'], ['Gibson, Talia', 'Eala, Alexandra', '3.15', '1.286'], ['Honer, Amelia', 'Schuman, Aspen', '1.60', '2.10'], ['Lu, Jia-Jing', 'Lutkemeyer Obregon, Anne Christine', '1.20', '3.65'], ['Mohamad, Shatoo', 'Cau, Alessia', '2.10', '1.615'], ['Wagle, Elise', 'Willson, Danielle', '1.85', '1.75'], ['Vernet, Caroline', 'Walker, Brandy', '2.95', '1.30'], ['2.45 ITF USA 33A, WOMEN DOUBLES', '1.727 ITF SPAIN 19A, WOMEN DOUBLES', '1.727 ITF SPAIN 19A, WOMEN DOUBLES', '1.80']]
    for i in range(len(liste1)):
        if len(liste1[i]) == 4:
            name = []
            betting_numbers = [liste1[i][2], liste1[i][3]]
            for j in range(len(liste1[i])):
                if " " in liste1[i][j]:
                    name.append(liste1[i][j].split(" "))
                    for o in range(len(name)):
                        for p in range(len(name[o])):
                            if not name[o][p]:
                                name[o].pop(p)
                                break
                    """if len(name) == 2:
                        print(name)"""
                    for k in range(len(liste2)):
                        same_count = 0
                        for l in range(len(liste2[k])):
                            for elements in name:
                                for element in elements:
                                    if element in liste2[k][l]:
                                        same_count += 1
                        if same_count >= 2:
                            name.append(betting_numbers)
                            #print(k, "!!!!!!!!!!!!", name, liste2[k])
                            finale_liste.append([name, liste2[k]])
    #print(finale_liste)
    i = 0
    while i < len(finale_liste):
        j = i + 1
        while j < len(finale_liste):
            if finale_liste[i] == finale_liste[j]:
                finale_liste.pop(j)
            else:
                j += 1
        i += 1
    #print(finale_liste)
    finale_liste_mit_booki = []
    for i in range(len(finale_liste)):
        try:
            #print(finale_liste[i])
            finale_liste_mit_booki.append([["pinnacle", [finale_liste[i][0][0], finale_liste[i][0][2]], finale_liste[i][0][3]], ["sport888", [finale_liste[i][1][0], finale_liste[i][1][1]], [finale_liste[i][1][2], finale_liste[i][1][3]]]])
        except:
            pass
    print(finale_liste_mit_booki)
    return finale_liste_mit_booki

def abitrage_number_list_maker(finale_liste_mit_booki):
    liste_best_version = []
    for i in range(len(finale_liste_mit_booki)):
        my_input = [[finale_liste_mit_booki[i][0][0], finale_liste_mit_booki[i][0][2][0], finale_liste_mit_booki[i][0][2][1]], [finale_liste_mit_booki[i][1][0], finale_liste_mit_booki[i][1][2][0], finale_liste_mit_booki[i][1][2][1]]]
        #print(my_input)
        liste_best_version.append([Calculations.best_Version(my_input), finale_liste_mit_booki[i][0][1]])
        print("hallo", finale_liste_mit_booki[i][0][1])
        #liste_best_version.append(finale_liste_mit_booki[i][0][1])
    print("111", liste_best_version)

    liste_abitrage_calc = []
    for i in range(len(liste_best_version)):
        print("!!!!", liste_best_version[i], [liste_best_version[i][0][0][1], liste_best_version[i][0][1][1]])
        to_append = []
        to_append.append(Calculations.abitrage_Calc([float(liste_best_version[i][0][0][1]), float(liste_best_version[i][0][1][1])]))
        to_append.append([liste_best_version[i][0][0][0], liste_best_version[i][0][1][0]])
        to_append.append(liste_best_version[i][1])
        liste_abitrage_calc.append(to_append)
    print(sort_list_by_float(liste_abitrage_calc))
    return sort_list_by_float(liste_abitrage_calc)


def sort_list_by_float(lst):
    sorted_lst = sorted(lst, key=lambda x: x[0])
    return sorted_lst




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


get_list_tennis()
"""cookies()
time.sleep(2)
login(0)
human_solving()"""
#time.sleep(9999)


#webDriver.quit()