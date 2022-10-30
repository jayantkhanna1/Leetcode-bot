from RPA.Browser.Selenium import Selenium
import time 
import json
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

browser = Selenium()
class Details:
    def get_details():
        try: 
            f = open("data.json", "r")
            data = json.load(f)
            return data
        except:
            print("Json Invalid")
            return "0"

class LoginMethods:
    def login_via_github(data):
            try: 
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
                return True
            except:
                print("Github Login Failed")
                return False

class Login:
    def login():
        # Logging in to Leetcode
        ip = "https://leetcode.com/accounts/login"
        # Getting Json
        data = Details.get_details()
        if data == "0":
            return
        login_method = data["login_method"]
        
        if login_method == "github":
                logged_in = LoginMethods.login_via_github(data)
                return logged_in
           

class Scrape:
    def scrape_and_get_answer(link):
        list_of_answers = []
        # I got number of links now somehow i have to extract links from discussion page and then go to each link and extract the answer
        no_of_links = browser.get_element_count("xpath://a")
        for i in range(1,no_of_links+1):
            browser.click_element("xpath://a["+str(i)+"]")
            print()
            time.sleep(2)
            # browser.click_link("Solution")
            # browser.click_link("Python3")
            # browser.click_link("Copy")
            # browser.click_link("Discuss")
            time.sleep(2)
        return list_of_answers

class Main:
    def launch_the_rocket():
        logged_in = Login.login()
        if logged_in:
            data = Details.get_details()
            if data == "0":
                return
            list_of_questions = data["list_of_questions"]
            for x in list_of_questions:
                link = x + "discuss/?currentPage=1&orderBy=hot&query="
                browser.go_to(link)
                list_of_answers = Scrape.scrape_and_get_answer(link)
                print(list_of_answers)
                time.sleep(5)
        else:
            return


def main():
    try:
        #automate_via_gui()
        Main.launch_the_rocket()
    finally:
        browser.close_browser()

if __name__ == "__main__":
    main()
