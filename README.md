# Pirate Adventures
> I created this application as a fun learning tool that would allow the user to login and register and interact with the application. It's purpose is to help organize the pirates. A user can join an adventure that has previously been created. They can also create and host an adventure. And they can edit adventure details such as dates and the name of the adventure and additional text describing the adventure. 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
- This project solves the problem of organizing and keeping track of pirates! It keeps track of adventures they are going on and which adventures they are hosting. 
- The purpose of my project is to provide a fun interaction for the user to create names of adventures and add creative details of their adventure.  
- I undertook this project to teach myself more about create/remove/update/delete operations and to further solidify my understanding of one to many relationships in a database. 

## Technologies Used
- Tech 1 - python 2.7.16
- Tech 2 - django 1.11.29
- Tech 3 - bcrypt 3.1.7


## Features
- Awesome feature 1: Allows user to login and register with an email and password. 
- Awesome feature 2: User can join an adventure from a list of adventures and can remove themself from an adventure by clicking 'cancel'. 
- Awesome feature 3: User can create and host an adventure-and it is automatically added to the 'Attending Adventure' list for that user.  


## Setup
how to get started with the project.
1. `install python 2.7.16`
2. `pip install django == 1.11.29`
3. `pip install bcrypt == 3.1.7`


## Usage
How does one go about using it?
1. from command line terminal please run:
 `python.exe manage.py runserver`
2. Please copy the url that comes up in the terminal window and paste into your browser. 
3. The login registration should come up. Please provide a name, alias, email address, password and birthday to register.The email address is not validated, it is only for logging into the app. 
4. Once you login you will be welcomed to your dashboard. 
5. On the dashboard, you will see Adventures You are Attending, Adventures You are Hosting, and Other Pirate Adventures you can join. 
6. Please join an adventure from the list of adventures by clicking on "Join Adventure". 
7. Please host an adventure by clicking on "Create Adventure" at the top of the screen. 
8. Please give your adventure a name and add dates for the adventure. If you add a date in the past it will reset the page and remove entered details. Please add a brief description of what your adventure will entail.   
9. You can edit an adventure by clicking "Edit"-this will allow you to edit the dates of the adventure, name and details. 
10. You can remove yourself from an adventure by clicking "Cancel".

Thank you for participating in Pirate Adventures!

## Project Status
Project is: complete at this time. I would like to add the improvements and features at a later time. 


## Room for Improvement
Areas I believe could be improved. And TODOs for future development.

Room for improvement:
- Improvement to be done 1: Have a prompt for user if the date for the adventure is invalid instead of just resetting the screen.
- Improvement to be done 2: Use the name from the alias as welcoming name instead of full name. 

To do:
- Feature to be added 1: Using Pirates Attack project add feature to keep track of number of attack wounds each pirate has sustained. 
- Feature to be added 2: Display list of pirates and their total number of attack wounds along with which adventures they are attending. 


## Acknowledgements
- This project was inspired by the Pirates of the Carribean movie. 
- This project was based on assignments at Coding Dojo boot camp in python for learning create/remove/update/delete.
- Many thanks to Coding Dojo instructors and TAs!


## Contact
Created by natasha nay -[natashanay](natashanay@gmail.com) feel free to contact me!
