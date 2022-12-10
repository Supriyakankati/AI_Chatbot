# skincarebot

# Project Overview:
The Main goal of this conversational Ai chatbot is assist in recommending the best skin care routine on a daily basis. The motivation behind this concept comes with taking good care of your skin is important for more than just your appearance. As the largest organ you have, your skin is essential to your general health. If you take care of it, it can help take care of you. This is why it is so important to have a well-thought-out skin care routine. It is absolutely worth the time and energy to take care of your skin on a daily basis. Even due to the change in weather conditions will be facing problems with the extreme dry skin. By using skincare we can keep our skin clear and soft by avoiding skin problems like acne, blackheads, skin burns and dark spots. This bot helps in suggesting video recommendations for the cause and treatment for skin problems like acne, dark pigmentation, pimples, sunburns and blackheads etc.. It also helps in suggesting best brands to use from the top rated.

# Conversational responses from chatbot:

Mainly, Chatbot is designed to answer the questions related to skincare routine, skin problems, best brands, usage of products, steps to use. For decision making process, bot collects the data from user and based on the data, it will provide the response to user. For example, if user is interested in getting best skincare routine then bot asks for some information (filters) about the user regarding skin types based on that it will suggest suitable categories with brands. And also if the user have skin problems then  bot suggests the video recommendations by calling the Youtube Api.
Below is the sample conversation between user and chatbot makes the user to understand the nature of the response from the chatbot
 
# Sample Conversation for best skincare routine:
 
 ![sample conversarion](https://user-images.githubusercontent.com/120232768/206873834-ab210e9a-c74c-4366-895b-ca86ff820133.png)


# Technology stack:
Rasa Version    :         3.3.1
Minimum Compatible Version: 3.0.0
Rasa SDK Version :         3.3.0
Python Version   :         3.8.15
Operating System  :         Windows-10-10.0.19044-SP0
Python Path      :         C:\Users\Checkout\anaconda3\envs\install_demo\python.exe


# Steps performed:

1. Clone the repository
    ```
       Git clone: https://github.com/Supriyakankati/skincarebot.git 
    ```
2. Setup a environment for Rasa
    2.1 Install python 3.8
    ```
        sudo apt-get install python3.8, python3.8-dev, python3.8-venv
    ```
    2.2 First create a virtual environment in your choice of directory using the following command and activate it: 
    ```
        python -m venv venv         # Create virtual env.
        source venv/bin/activate    # Activate virtual env.
    ```
    2.3 Install dependencies for Rasa using requirements.txt
    ```
        pip install -r requirements.txt
    ```
3. Run the rasa server and actions server
    ```
        rasa run actions
    ```
4. Setup ngrok to expose the local server to the internet
    ```
    Ngrok.exe http 5005
    ```
5. Integrate slack channel with rasa server
    ```
    https://api.slack.com/apps
    ```
6. We are now close to run the chatbot. Since the action server is up and the model has been trained, we can simply use the following command to run the chatbot. with this we can play with chatbot in the terminal.(Optional)
    ```
        rasa shell        
    ```

# Demo:
Below is the demo of the chatbot. It shows the conversation between user and chatbot. It also shows the flow of the data from user to the chatbot.

![1_Demo](https://user-images.githubusercontent.com/120232768/206873944-711bac89-e987-4367-867b-508a7ca1993e.png)
![2_Demo](https://user-images.githubusercontent.com/120232768/206873945-6a01264f-bd02-467d-be83-fc68311dbd9d.png)
![3_Demo](https://user-images.githubusercontent.com/120232768/206873947-d39f03eb-5865-42bd-9a23-325f6f8bd77d.png)
![4_Demo](https://user-images.githubusercontent.com/120232768/206873948-836ac691-d695-4e03-be3a-a9a417a27d42.png)
![5_Demo](https://user-images.githubusercontent.com/120232768/206873949-3757a6d9-f510-4997-affa-93be07a07e0a.png)


# References:
* [Rasa Docs](https://rasa.com/)
* [RASA NLU](https://rasa.com/docs/rasa/nlu/components/)
* [RASA Core](https://rasa.com/docs/rasa/core/policies/)
* [Tutorials](https://www.youtube.com/c/RasaHQ)


# Support and Contact
If you have any questions or suggestions, please contact  supriya.kankati@sjsu.edu 
I will be happy to help you. Create an issue if you find any bug. I will try to fix it as soon as possible. 



Thankyou
* [Professor Jorjeta G. Jetcheva]





