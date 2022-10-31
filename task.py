from RPA.Browser.Selenium import Selenium
import time 
import json


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
           


class Main:
    def launch_the_rocket():
        logged_in = Login.login()
        if logged_in:
            data = Details.get_details()
            if data == "0":
                return
            if data["do_questions_by_links"] == True:
                
                list_of_questions = data["list_of_questions"]
                for x in list_of_questions:
                    question_name = x.replace('https://leetcode.com/problems/','')
                    question_name = question_name.replace('-',' ')
                    if question_name[len(question_name)-1] == "/":
                        question_name = question_name[:len(question_name)-1]

                    f = open("answers.json", "r")
                    answers = json.load(f)
                    for z in answers:
                        if z["question_title"].lower() == question_name.lower():
                            browser.go_to(z["answer_link"])
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
