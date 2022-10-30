from RPA.Browser.Selenium import Selenium
from RPA.Word.Application import Application
import time 
import json

browser = Selenium()

def get_details():
    try: 
        f = open("data.json", "r")
        
        data = json.load(f)
        return data
    except:
        print("loginmethod.txt not found or is corrupted")
        return "0"

def login():
    ip = "https://leetcode.com/accounts/login"
    data = get_details()
    login_method = data["login_method"]
    if login_method == "0":
        return
    
    elif login_method == "github":
        # Login via Github
        ip = "https://leetcode.com/accounts/github/login/?next=%2F"

        # Getting Credentials
        github_username = data["github"]["username"]
        github_password = data["github"]["password"]
        browser.open_available_browser(ip)
        browser.input_text("id:login_field", github_username)
        browser.input_text("id:password", github_password)
        browser.click_button("Sign in")

        wait_time_for_authorization = data["wait_time_for_authorization"]
        # Min wait time
        if wait_time_for_authorization < 30:
            wait_time_for_authorization = 30
        # For Two Factor authentication
        time.sleep(wait_time_for_authorization)

        #Opening list of problems
        list_of_questions = data["list_of_questions"]
        for x in list_of_questions:
            link = x + "discuss/?currentPage=1&orderBy=hot&query="
            browser.go_to(link)
            #browser.click_link("/discuss/")
            print(browser.get_all_links())
            #browser.click_element("a:contains('Solution')")
            # browser.click_element("a:contains('Python3')")
            # browser.click_element("a:contains('Copy')")
            # broswer.click_link("/discuss/")
            time.sleep(50)
        #browser.click_link("/problems/height-of-binary-tree-after-subtree-removal-queries/")


def main():
    try:
        #automate_via_gui()
        login()
    finally:
        browser.close_browser()

if __name__ == "__main__":
    main()
