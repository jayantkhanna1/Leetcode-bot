from RPA.Browser.Selenium import Selenium
import time 
import json
import requests
from bs4 import BeautifulSoup


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
        elif login_method == "leetcode":
                print("Leetcode Login not implemented")
                return False
        elif login_method == "google":
                print("Google Login not supported yet")
                return False
        else:
                print("Invalid Login Method")
                return False

class Answer:
    def get_answer(answer_link):
        # Getting answer
        answer = requests.get(answer_link)
        return str(answer.content.decode('utf-8'))

class Main:
    def launch_the_rocket():
        # CHECKS IF LOGGED IN
        logged_in = Login.login()
        if logged_in:
            # Gets Json data
            data = Details.get_details()
            if data == "0":
                # In case of error
                return
            # Use this if we have to do question by link
            if data["do_questions_by_links"] == True:
                # Gets list of questions
                list_of_questions = data["list_of_questions"]
                # Iterates over list of questions
                for x in list_of_questions:
                    # Getting answer links by matching question name
                    question_name = x.replace('https://leetcode.com/problems/','')
                    question_name = question_name.replace('-',' ')
                    if question_name[len(question_name)-1] == "/":
                        question_name = question_name[:len(question_name)-1]

                    f = open("answers.json", "r")
                    answers = json.load(f)
                    for z in answers:
                        # If question name matches with the answer name
                        if z["question_title"].lower() == question_name.lower():
                            # Gets answer link
                            code = Answer.get_answer(z["answer_link"])

                            # Gets code and goes to question
                            browser.go_to(x)
                            time.sleep(data["wait_time_for_page_load"])

                            # Removes already present code
                            select_commands = "CTRL+a BACKSPACE"
                            browser.press_keys('xpath://*[@id="editor"]/div[4]/div[1]/div/div/div[1]/div[2]/div[1]/div[4]', select_commands)
                            delete_commands = "\ue003"
                            browser.press_keys('xpath://*[@id="editor"]/div[4]/div[1]/div/div/div[1]/div[2]/div[1]/div[4]', delete_commands)
                            time.sleep(1)
                            
                            # Copies code to clipboard
                            import pyperclip
                            pyperclip.copy(code)

                            # Pastes code in editor and sleeps
                            paste_commands = "CTRL+v"
                            browser.press_keys('xpath://*[@id="editor"]/div[4]/div[1]/div/div/div[1]/div[2]/div[1]/div[4]', paste_commands)

                            # Sleeping before submitting
                            time.sleep(data["wait_time_for_submitting_answer"])

                            # Submits answer
                            browser.click_element('xpath://*[@id="qd-content"]/div[3]/div/div[3]/div/div/div[3]/div/div/div[3]/button[3]')

                            # Sleeping before moving on to next question
                            time.sleep(data["wait_time_for_submitting_answer"])

                            # Printing answer passed or not
                            try:
                                if browser.get_text('xpath://*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/span') == "Accepted":
                                    print("Question number - "+str(z["question_number"])+" Solved")
                                else:
                                    print("Question number - "+str(z["question_number"])+" Failed")
                            except:
                                print("Question number - "+str(z["question_number"])+" Failed")
        
            elif data["do_questions_by_links"] == False:
                range_of_questions = data["list_of_questions_by_range"]
                for x in range(range_of_questions[0], range_of_questions[1]+1):
                    # Gets answer links by matching question name
                    f = open("answers.json", "r")
                    answers = json.load(f)
                    for z in answers:
                        # If question name matches with the answer name
                        if z["question_number"] == x:
                            # Gets answer link
                            code = Answer.get_answer(z["answer_link"])

                            # Gets code and goes to question
                            browser.go_to("https://leetcode.com/problems/"+z["question_title"].replace(' ','-').lower())
                            time.sleep(data["wait_time_for_page_load"])

                            # Removes already present code
                            select_commands = "CTRL+a BACKSPACE"
                            browser.press_keys('xpath://*[@id="editor"]/div[4]/div[1]/div/div/div[1]/div[2]/div[1]/div[4]', select_commands)
                            delete_commands = "\ue003"
                            browser.press_keys('xpath://*[@id="editor"]/div[4]/div[1]/div/div/div[1]/div[2]/div[1]/div[4]', delete_commands)
                            time.sleep(1)
                            # Copies code to clipboard
                            import pyperclip
                            pyperclip.copy(code)
                            
                            # Pastes code in editor and sleeps
                            paste_commands = "CTRL+v"
                            browser.press_keys('xpath://*[@id="editor"]/div[4]/div[1]/div/div/div[1]/div[2]/div[1]/div[4]', paste_commands)

                            # Sleeping before submitting
                            time.sleep(data["wait_time_for_submitting_answer"])

                            # Submits answer
                            browser.click_element('xpath://*[@id="qd-content"]/div[3]/div/div[3]/div/div/div/div/div/div[3]/button[3]')

                            # Sleeping before moving on to next question
                            time.sleep(data["wait_time_for_submitting_answer"])

                            # Printing answer passed or not
                            try:
                                if browser.get_text('xpath://*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/span') == "Accepted":
                                    print("Question number - "+str(z["question_number"])+" Solved")
                                else:
                                    print("Question number - "+str(z["question_number"])+" Failed")
                            except:
                                print("Question number - "+str(z["question_number"])+" Failed")
        else:
            return


def main():
    try:       
        Main.launch_the_rocket()
    finally:
        browser.close_browser()

if __name__ == "__main__":
    main()
