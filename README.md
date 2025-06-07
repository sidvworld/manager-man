# Welcome to TaskForce
## This is a proof of concept for this application written in Python

At the beginning of high school, my time management quite frankly sucked and I was in desperate need for a way to keep my tasks in order. After countless scrolling through the microsoft app store for an efficient task manager, I found that none these apps truly worked for me as they were tedious and ineffective.

TaskForce was created to solve my problems, and one it's most useful features provides a way to integrate your task management into your workflow with the simple shortcut of Alt + =.

![ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/6944dab3-c87f-4338-b8b1-f4779f3d9f15)

Using a natural language processor from a python library called spacy, the application parses the users input and converts it into a task object with attributes like the task name, task deadline (mm/dd/yyy), task priority (high, medium, low), and created date.

A server will store this data in an SQLite database in which the user can easily access their upcoming tasks. In the event that a user cannot connect to the server, current and new tasks are locally saved to the computer to be later synced.

I hope to take this project into a fullstack desktop application. Thank you for taking the time to view my proof of concept!
