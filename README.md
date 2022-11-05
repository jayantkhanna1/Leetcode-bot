# LeetCode Bot

Hola! This is a leetcode bot that can solve all your leetcode problems while you sit back and sip your coffee. Best part? It is completely free and solves questions at human speed! so you can get those coding assignements done a night before the deadline.

It is user friendly and easy to use. It is also open source and you can <a href = "#contribute">contribute</a> to it! 

If you just wanna do this as quicklly as possible read the <a href = "#tldr">TLDR</a> section. else i would recommend you to read whole Readme as it contains a lot of useful information.
## Content
 - <a href = "#tldr">TLDR (Too Long, Didn't Read)</a>
 - <a href = "#setup">Setup</a>
 - <a href = "#json">Make Json</a>
 - <a href = "#run">Run the Bot</a>
 - <a href = "#contribute">Contribute</a>
 - <a href = "#faq">FAQ</a>
 - <a href = "#contact">Contact Me</a>

# <a id="tldr"></a>TLDR

You need : 
 - Python 3.6 or above
 - Chrome Browser (Default)
 - Leetcode Account
 - A good internet connection

Install these two robocorp packages on VSC:

 - Install extension: https://marketplace.visualstudio.com/items?itemName=robocorp.robotframework-lsp

 - Install extension: https://marketplace.visualstudio.com/items?itemName=robocorp.robocorp-code


Make Json file using <a href = "#json">this</a> guide.

Run the bot using CTRL + SHIFT + P and type "Robocorp: Run Robot Task" Press Enter.

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


  - <strong>max_wrong_submissions</strong>: This is max number of wrong submissions before giving a correct one to mimic human like nature although not perfect it might help to  a certain extent. It chooses a random number betwwen 0 to number you set for number of wrong submissions

 - <strong>do_questions_by_links</strong> : This is a boolean value. If you want to solve questions by links, set it to true. If you want to solve questions by question number range, set it to false.

 - <strong>do_questions_by_range</strong>: This is a boolean value. If you want to solve questions by links, set it to false. If you want to solve questions by question number range, set it to true.

 - <strong>list_of_questions</strong> : This is a list of questions. If you want to solve questions by links, add all links in this list. If you want to solve questions by question number range, you can leave it empty.

 - <strong>list_of_questions_by_range</strong> : This is a list of questions. If you want to solve questions by links, you can leave it empty. If you want to solve questions by question number range, give range like [1,3]. This means question number 1, 2, 3 will be solved.

 - <strong>login_method</strong> : Here you can enter your login method. You can either "Github". To login via Github or "Leetcode" to login via Leetcode. If you want to login via Google currently it is not supported. But I will add it soon.

 - <strong>github</strong> : Here you can enter your Github username and password. If you want to login via Github.

 - <strong>leetcode</strong> : Here you can enter your Leetcode username and password. If you want to login via Leetcode.

 ## I am DUM DUM and don't understand JSON. HELP ME!

 Ok Ok! no worries just copy this Json data and paste it in your data.json file. Just add your username and password and you are good to go. Your questions 1 to 5 will be solved. Change range to solve others. (If you don't know how to change range, I would suggest you do not use this bot and do questions on your own :P)

```json
    {
        "wait_time_for_authorization":30,
        "wait_time_before_submitting_answer" : 600,
        "wait_time_between_submissions" : 120,
        "wait_time_for_page_load" : 10,

        "max_wrong_submissions" : 2,

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

Finally we are here. We are going to run the bot. But before that, I would like to tell you how it will work. 

 - First, it will open Chrome and go to Leetcode.com
 - Then it will login to your account
 - Then it will wait for you to grant 2FA. (wait_time_for_authorization)
 - Then it will go to the question you want to solve
 - Then it will wait for some time and do some wrong submissions if entered in data.json 
 - Then it will wait for sometime before submitting correct answer
 - Then it will submit the answer
 - Then it will wait for some time to go to next question
 - And so on...

 Only part you have to do is to grant 2FA. Rest is done by the bot. 

 <strong>Note : </strong> Depending on your PC specs/Internet speed it might slow it down so do not worry if your laptop starts hanging. You can kill this bot any time in between nothing will happen to your leetcode account everything will remian as is.

 ## Step 1:

 ```
Press CTRL + SHIFT + P 

type Robocorp: Run Robot 
```
 If you have done Robocorp setup correctly, you will see this option. If not please read <a href = "#setup">Setup</a> section again.


## Step 2: 

Make sure you have added your data in data.json file. If you have not done it yet, please read <a href = "#json">Make Json</a> section. If done <strong>press Enter</strong>

<strong>If you are running this for the first time it might take some time to install all Robocorp dependencies. So please be patient. (PS: It took 30 minutes for me to install all dependencies for the first time)</strong>


## Step 3:

You will see a new window open. It will autologin depending on your login method. If you have selected Github, it will login via Github. If you have selected Leetcode, it will login via Leetcode.

Here is the screenshot of the bot running with Github Login method.


## Step 4:

Now you have to grant 2FA. You will see a new window open. It will ask you to grant 2FA. You have to grant it. You have to do it within time allocated in wait_for_authorizaton. Minimum time will be 30 seconds. If you have not granted 2FA within that time, it will throw an error and bot will stop.

Here is the screenshot of the bot asking for 2FA running with Github Login method.


## Step 5:

Now bot will go to your selected question and start solving it. You can see the bot solving the question in the screenshot below.

## Step 6:

It may or may not make a few wrong submissions depending on your data.json file. If you have set max_wrong_submissions to 0, it will not make any wrong submissions. 

Here is a screenshot attached of the bot making wrong submissions.

## Step 7:

It will wait for some time before submitting the correct answer. You can see the bot waiting in the screenshot below.

## Step 8:

It will submit the correct answer. You can see the bot submitting the correct answer in the screenshot below.

## Step 9:

It will wait for some time before going to next question or ending. You can see the bot waiting in the screenshot below.

## Step 10:

Done! Bot ends and you will see following output in the terminal.


# <a id = "contribute"></a>Contribute

Hope you enjoyed using my bot and it helped you in solving questions. If you want to contribute to this project, you can do so by <a href= "#conatc">Contacting me </a> and telling me what more can i add to this bot/ If you faced any error while using this bot I will try to fix it as soon as possible and will add your name here.

## Contributors
<br>

<table>
    <tr>
        <td><img style="margin-left:50%;height:250px;" src = "img/jayant.jpg"></td>
        <td><p style="text-align:center;">Jayant Khanna : Like, Do I really need to add my name here? :P Anyways check out my <a href = "https://jayantkhanna.herokuapp.com/">website</a> and <a href = "https://github.com/jayantkhanna1">Github</a> profile.</p></td>
    </tr>
</table>

 <!-- <span> <img style="margin-left:50%;height:250px;margin-right:15px;" src = "img/jayant.jpg"> <p style="text-align:center;">Jayant Khanna : Like, Do I really need to add my name here? :P Anyways check out my <a href = "https://jayantkhanna.herokuapp.com/">website</a> and <a href = "https://github.com/jayantkhanna1">Github</a> profile.</p>
</span>
 <span>  <img style="margin-left:50%;height:250px;margin-left:15px;" src = "img/ananya.jpg"> 
 <p style="text-align:center;">Ananya Vishnoi : She is helping me check all answers for LeetCode in C++ language and making them Bot compatible. She is also helping me in testing the bot. She is a great friend and a great coder. You can check her Github profile <a href = "https://github.com/ananya26-vishnoi">Here</a>
 </p>

</span>

 <span > <img style="margin-left:50%;height:250px;margin-right:15px;" src = "img/ujjwal.jpg"> <p style="text-align:center;">Ujjwal Anand : He is helping me get all answers in multiple languages such as Java, Python, Javascript etc so we can add Language functionality in the future. He is a great friend and a ML Enthusiast. You can check his Github profile <a href = "https://github.com/ujjwal-anand-0207">Here</a>
</p> 
</span>

 <span> 
  <img style="margin-left:50%;height:250px;margin-left:15px;" src = "img/Liyulu.png"> 
  <p style="text-align:center;">
   Liyu Lu: A great coder and a silent helper. Thank this guy for creating such a neat repository for so many correct Leetcode answers. Without his help this project wouldn't have been possible. You can check his Github profile <a href = "https://github.com/luliyucoordinate">Here</a>
 </p>

</span> -->


# <a id = "contact"></a>Contact

You can contact me on my <a href="mailto:jayantkhanna3105@gmail.com">E - mail</a> or on my <a href="https://www.linkedin.com/in/jayant-khanna-66a274185">LinkedIn</a> profile. You can also contact me on my <a href="https://www.instagram.com/jayant_khanna1/">Instagram</a>, <a href = "https://github.com/jayantkhanna1/">Github</a>, <a href = "https://jayantkhanna.herokuapp.com/">Website</a>. I will try to reply as soon as possible.

If you have any suggestions or want to contribute to this project, you can contact me on any of the above mentioned platforms. You can also contact me if you want to collaborate for some other ideas/project or want to hire me for some freelancing projects. I am always open to new ideas and new projects.

# <a id = "faq"></a>FAQ

Allright so you have read the whole thing and still have some questions. Here are some of the most frequently asked questions. If you have any other questions, you can contact me on any of the platforms mentioned in <a href = "#contact">Contact</a> section.

Ps: I will keep updating this section as more questions are asked but tbh I don't think anyone will be actually reading this section :P

## Q1: Why did you make this bot?
 To be honest with you I didn't make this bot for cheating my way through a class or to get some marks. I made this Bot because I wanted to learn about Selenium and Robot Framework and I thought this would be a great way to learn. 

## Q2: Why did you make this bot in Robot Framework instead of Core Selenium?
 I made this bot in Robot Framework because I wanted to learn about Robot Framework. I have been learning Python for a while now and I wanted to learn about other frameworks as well. I have heard a lot about Robot Framework and I thought this would be a great way to learn about it.

## Q3: Why have you made it Free?
 Aah yes, The classic "BRO lets make this paid we will earn so much HEHEHE". The aim of the project, as i have told multiple times, is not to earn but to help Open source. I have made this bot free so that everyone can use it and everyone can contribute to it. 

## Q4: People will use it it cheat! It will hamper new-comers Learning!!
 <span style="display:flex;align-items:center;">
 <img src = "img/cat.jpg" style="height:130px;margin-right:15px;">
 I am not going to lie, I have thought about this a lot. I have thought about how people will use this bot to cheat and how it will hamper the learning of new-comers. But then I thought, if people want to cheat, they will find a way to cheat even if this bot doesn't exist.
 </span>