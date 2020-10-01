#Created by Shelley Ophir
#Coding Dojo Oct. 1, 2020
#Create a server file that generates the specified responses for the following url requests:

#first import Flask
from flask import Flask

#create a new instance of the class Flask and name it app
app = Flask(__name__)

# localhost:5000/ - have it say "Hello World!"
@app.route("/")
def hello():
    return "Hello World!"

# localhost:5000/dojo - have it say "Dojo!"
@app.route("/dojo")
def dojo():
    return "Dojo!"

# Create one url pattern and function that can handle the following examples:
    # localhost:5000/say/flask - have it say "Hi Flask!"
    # localhost:5000/say/michael - have it say "Hi Michael!"
    # localhost:5000/say/john - have it say "Hi John!"
@app.route("/say/<name>")
def say(name):
    return ("Hi " + name.capitalize() + "!")#the .capitalize() method capitalizes the first letter


# Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
    # localhost:5000/repeat/35/hello - have it say "hello" 35 times
    # localhost:5000/repeat/80/bye - have it say "bye" 80 times
    # localhost:5000/repeat/99/dogs - have it say "dogs" 99 times   
@app.route("/repeat/<num>/<name>")
def repeat(num, name):
    return (name * int(num))#need to convert num to an int as it is passed in as a string

#  NINJA BONUS: For the 4th task, ensure the 2nd element in the URL is an integer (hint: http://exploreflask.com/en/latest/views.html#url-converters)
@app.route("/repeat2/<int:num>/<name>")
def repeat2(num, name):
    return (name * num)#took out the int() because the converter <int:> in the route definition took care of it

#  SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, they receive an error message saying "Sorry! No response. Try again."
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."


#End all server files with this debugger statement:
if (__name__ == "__main__"): #Ensures this file is being run directly and not from a different module
    app.run(debug = True) #run the app in debug mode