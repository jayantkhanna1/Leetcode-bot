# LeetCode Bot

<strong style="font-size:25px;">Do not read me, I am not ready......Y..Ya...Yamate kudasai!</strong>

Hola! This is a leetcode bot that can solve all your leetcode problems while you sit back and sip your coffee. Best part? It is completely free and solves questions at human speed! so you can get those coding assignements done a night before the deadline.

It is user friendly and easy to use. It is also open source and you can <a href = "#contribute">contribute</a> to it! 

## Content
 - <a href = "#setup">Setup</a>
 - <a href = "#json">Make Json</a>
 - <a href = "#run">Run the Bot</a>
 - <a href = "#error">Error Handling</a>
 - <a href = "#contribute">Contribute</a>
 - <a href = "#faq">FAQ</a>
 - <a href = "#contact">Contact Me</a>

# <a id="setup"></a>Setup

## Requirements
 - <strong>Python 3.6 or above</strong> (Like seriously, why are you still using 2.7?)
 - <strong>Robot Framework </strong>(Don't you worry will guide you step by step)
 - <strong>Chrome </strong>(You can use any other browser but I havent tested it so I can't guarantee it will work)
 - <strong>Leetcode Account </strong>(Like...really?)


## Python

Best will be to user version 3.9.13 as it is the latest version and has the least / undiscovered bugs. You can download it from <a href = "https://www.python.org/downloads/">here</a>. Make sure to check the box that says "Add Python to PATH" while installing.

To check what version you are currently on type this in your command prompt:

```
python --version
```

If you do not have python installed, you can download it from <a href = "https://www.python.org/downloads/">here</a>. Make sure to check the box that says "Add Python to PATH" while installing.

## Robot Framework

Nothing to be afraid of! Robot Framework is a generic, Python-based, open-source automation framework. It can be used for test automation and robotic process automation (RPA). Robot Framework is supported by Robot Framework Foundation. Many industry-leading companies use the tool in their software development. If you are interested in automation of tasks I highly recommend you to read their <a href = "https://robocorp.com/docs/quickstart-guide">documentation</a>.

If not. Don't worry, I will guide you step by step.

- Step 1: To get started,<a href = "https://id.robocorp.com/signup"> create an account </a> in Robocorp Control Room if you do not have one already. 

- Step 2: Next, install Visual Studio. If you do not use VSC I would like to appologize as I don't know how to use this on another IDE

- Step 3: Install extension: https://marketplace.visualstudio.com/items?itemName=robocorp.robotframework-lsp

- Step 4: Install extension: https://marketplace.visualstudio.com/items?itemName=robocorp.robocorp-code

And Done! Thats it now you can run the bot on your local machine. 
"Why is it not on Cloud?" Read this in <a href = "#faq">FAQ</a> section.
If you face any issues, you can <a href = "#contact">Contact Me</a> .

## Chrome

You can download it from <a href = "https://www.google.com/chrome/">here</a>. Make sure to make it your default browser. If you have another default broswer.. It might or might not work on it anyways I am happy to help you if you face any issues. You can <a href = "#contact">Contact Me</a> .

## Leetcode Account

Like I said, What are you even doing here? Go and create an account <a href = "https://leetcode.com/">here</a> and then come back.

# <a id="json"></a>Make Json

So you made it till here. Do not fret my friend, we are almost there. After we make this JSON we will be done and can start our BOT.

## Understanding JSON

After you clone this repo, you will see a file called <strong>data.json</strong>. This is where you will be adding all required details 

 - <strong>wait_time_for_authorization</strong>: This is the time (in seconds) the bot will wait for you to do 2FA. You can change it to whatever you want. But minimum is 30 seconds. To see how it will work, read <a href = "#run">Run the Bot</a> section.

 - <strong>wait_time_before_submitting_answer</strong>: This is the time (in seconds) the bot will wait before submitting the answer. You can change it to whatever you want. But I would suggest you to maximize it if you want Human like speed or have slow internet. To see how it will work, read <a href = "#run">Run the Bot</a> section.

 - <strong>wait_time_between_submissions</strong>: This is the time (in seconds) the bot will wait before starting a new question. You can change it to whatever you want.

 - <strong>wait_time_for_page_load</strong>: This is the time (in seconds) the bot will wait for page to load. You can change it to whatever you want. But I would suggest you to increase it if you have slow internet. Keep it minimum to 5 seconds if you have fast internet.(Unless you want to see errors)

 - <strong>do_questions_by_links</strong> : This is a boolean value. If you want to solve questions by links, set it to true. If you want to solve questions by question number range, set it to false.

 - <strong>do_questions_by_range</strong>: This is a boolean value. If you want to solve questions by links, set it to false. If you want to solve questions by question number range, set it to true.

 - <strong>list_of_questions</strong> : This is a list of questions. If you want to solve questions by links, add all links in this list. If you want to solve questions by question number range, you can leave it empty.

 - <strong>list_of_questions_by_range</strong> : This is a list of questions. If you want to solve questions by links, you can leave it empty. If you want to solve questions by question number range, give range like [1,3]. This means question number 1, 2, 3 will be solved.

 - <strong>login_method</strong> : Here you can enter your login method. You can either "Github". To login via Github or "Leetcode" to login via Leetcode. If you want to login via Google currently it is not supported. But I will add it soon.

 - <strong>github</strong> : Here you can enter your Github username and password. If you want to login via Github.

 - <strong>leetcode</strong> : Here you can enter your Leetcode username and password. If you want to login via Leetcode.

 ## I am DUM DUM and don't understand JSON. HELP ME!

 Ok Ok no worries just copy this Json data and paste it in your data.json file. Just add your username and password and you are good to go. Ypur questions 1 to 5 will be solved.

```json
    {
        "wait_time_for_authorization":30,
        "wait_time_before_submitting_answer" : 600,
        "wait_time_between_submissions" : 120,
        "wait_time_for_page_load" : 10,

        "do_questions_by_links":false,
        "do_questions_by_range":true,

        "list_of_questions":[],
        "list_of_questions_by_range":[1,5],
        
        "login_method" : "<GITHUB/LEETCODE>",
        "github" : {
            "username" : "<Your Username>",
            "password" : "<Your Github Password>"
        },
        "leetcode" : {
            "username" : "<Your Username>",
            "password" : "<Your Leetcode Password>"
        }    
    }
```

# <a id="run"></a>Run the Bot