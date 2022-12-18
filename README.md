# CS50-Final-Project
### Description:

*Introduction:*

WSID is a gui application for boring evenings when you do not know what to do. The application will give you the opportunity not to think about what to watch or what to read today if you want to occupy yourself with something new This is also not a problem the application will tell you what to do yourself. All we need to know what to do is to click on two buttons and the program will give the result without any effort 
How does it work?
We have a file which generates our data and after we formulate the data, it is sent to the main application which already generates it for the user. From there you can see how the user sees this data.
When the user enters the applications we see the main screen which has only 3 buttons

![](main.png)

*How it works:*

The "movie" button allows you to dive into the world of movies and choose something for yourself. By clicking on the genre button you will be able to select one of the five genres presented:

- action
- fantasy 
- drama
- romance
- animation
 
And by clicking Click on me, the program will give you a random name of the movie and its poster.

The "Book" button will help you choose a book to spend an enjoyable evening with. You can also choose the genre you are interested in from the four represented:

- children's literature
- novel
- poetry
- tragedy

Just as in the window for selecting a movie, when you press the button, the program will give you the author and the title of the book.
The last button will help you choose something new for you, maybe it is time to choose a new hobby


![](movie.png)
![](movie_genre.png)

In order to run the program you need to perform a few small steps:
```
git clone 
pip install -r requirements.txt
```
*Let's go through the code:*

#### What technology has been used:

1. PyQT - for GUI
2. python - core technology obviously
3. pytest - for testing programm
4. API/json - for data exchange

-project.py is the file where the data is formulated. In this file the necessary data from json is converted into a dictionary and transferred for further work with them. Also in the same file is a third-party API from which also takes the necessary data for the hobby and passed to the file main.py

-main.py - all other logic inside PYQT takes place in this file. The data from project.py is passed here for further processing and passing to the user when a certain signal is given (pressing a button). When the button is pressed the signal is passed to a class with a specific set of functions to process this signal. A function triggers and already passes the data sent from project.py, depending on the genre the user has chosen a certain condition is triggered.

Files are used to render the application:
-myWIn.py - the main window with three buttons to open the corresponding windows

-movieUi.py - movie window, here is the interface for movies, which appears statically as a result of pressing a button. This is where all the static data is located

-bookUi.py - the window with books, just like the window with movies, this window contains only static data

-hobbyUi.py - window for choosing a hobby, similar to the previous two windows

-styles.py - this file contains the basic settings for refining the look of the application

*In the future I plan to improve this project and add more options and a better look and feel.*

### I hope you enjoy my project 🙂
