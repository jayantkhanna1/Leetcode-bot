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
                            # copy_commands = "CTRL+a CTRL+c"
                            # browser.press_keys("xpath:/html/body/pre", copy_commands)
                            time.sleep(10)
                            code = browser.get_text("tag:pre")
                            
                            # browser.press_keys("tag:pre","\ue009+a \ue009+c")
                            browser.go_to(x)
                            time.sleep(10)
                            # select python 3
                            #browser.click_element("class:ant-select-selection-selected-value")
                            # not selecting for some reason check this

                            #browser.click_element("xpath:/html/body/div[6]/div/div/div/ul/li[1]")
                            #time.sleep(5)
                            # select editor

                            # paste new code in correct formatting
                            # subm
                            # select_commands = "SHIFT+RIGHT"
                            # for x in range(0,1000):
                            #     browser.press_keys("class:CodeMirror-sizer", select_commands)
                            select_commands = "CTRL+a Backspace"
                            browser.press_keys("class:CodeMirror-sizer", select_commands)
                            import pyperclip
                            pyperclip.copy(code)
                            paste_commands = "CTRL+v"
                            browser.press_keys("class:CodeMirror-sizer", paste_commands)
                            # Code error
                            # for x in code:
                            #     browser.press_keys("class:CodeMirror-sizer", x)
                            time.sleep(20)

                            browser.click_element("class:submit__2ISl")
                            time.sleep(10)
                            try:
                                if browser.get_text("class:success__3Ai7") == "Success":
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
