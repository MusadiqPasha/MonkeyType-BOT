from selenium import webdriver
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # add ur webdriver path here webdriver.Chrome(r"C:\chromedriver_win32\chromedriver.exe")

def login():

    driver.get('https://monkeytype.com/')

    driver.set_window_position(0, 0)
    pyautogui.FAILSAFE = True

    user = pyautogui.prompt("Enter the username : ")
    pasw = pyautogui.password("Enter the password : ")

    time.sleep(2)

    pyautogui.click(x=827, y=818) #accept cookies
    time.sleep(2)

    pyautogui.click(x=1223, y=268) #login logp
    time.sleep(1)

    pyautogui.click(x=942, y=470) # email
    pyautogui.write(user)
    time.sleep(1)

    pyautogui.click(x=942, y=523) # pass
    pyautogui.write(pasw)
    time.sleep(1)

    pyautogui.click(x=942, y=607) #sign in
    time.sleep(1)


def writee(delay):
    try:
        while len(driver.find_elements(By.CLASS_NAME, "word")) != 0:
            active_word = driver.find_element(By.CSS_SELECTOR, ".word.active")
            letters = [letter.text for letter in active_word.find_elements(By.TAG_NAME, "letter")] + [' ']
            pyautogui.write(letters, interval=delay)
    except Exception as e:
        pass

def playy(delay):
    time.sleep(3)
    pyautogui.doubleClick(x=222, y=258) # monekytype
    pyautogui.doubleClick(x=222, y=258)  # monekytype

    time.sleep(1)
    # just telling the user to select his diff modes
    pyautogui.alert("Please select the mode and the time you want and THEN press OK !")

    time.sleep(1)

    driver.set_window_position(0, 0)
    time.sleep(4)

    writee(delay)

def display():
    # Print keys in the first line
    keys = list(data.keys())
    print(*keys, sep='\t')

    # Print corresponding values on subsequent lines
    for i in range(len(next(iter(data.values())))):
        values = [str(data[key][i]) for key in keys]
        print(*values, sep='\t\t')

    print("--------------------------------------")


# main shit

ans = "YES"
login()
data = {"wpm":[], "accu" :[] , "consis":[] ,"delay":[]}
while ans == "YES":
    pyautogui.scroll(1000)
    pyautogui.scroll(1000)
    pyautogui.doubleClick(x=222, y=258)

    delay = float(pyautogui.prompt(text='Enter the delay(seconds)\n    0 is instantaneous',default='0.1'))
    playy(delay)

    # to get the wpm , acc values a store it in a dict
    wpm = driver.find_element(By.CSS_SELECTOR, ".group.wpm").find_element(By.CLASS_NAME, "bottom").text
    acc = driver.find_element(By.CSS_SELECTOR, ".group.acc").find_element(By.CLASS_NAME, "bottom").text
    consistency = driver.find_element(By.CSS_SELECTOR, ".group.flat.consistency").find_element(By.CLASS_NAME,
                                                                                               "bottom").text
    data["wpm"].append(wpm)
    data["consis"].append(consistency)
    data["accu"].append(acc)
    data["delay"].append(delay)
    display()
    ans = pyautogui.confirm(text='Wanna Type again??', title='yup?', buttons=['YES', 'NO'])


driver.quit()
