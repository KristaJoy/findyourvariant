# Flask App
**Loki has variants, do you?**
Inspired while watching an episode of the show Loki, I wanted to create a fun website to utilize some of the skills I have in Python, JavaScript and using an API call to interact with data. 

## How It Works
The app works by taking the user inputs of name and year of birth, creates an API call to feed into a Python function which generates a dictionary that the JavaScript d3 program writes to the website. Essentially it uses a list of jobs and location options, generates a dictionary of three variants which come together by creating random 4-digit numbers linked to the first letter of the input name for the variant id#, then three random jobs and locations, and random years based off creating a list using the user input year. You can click the Find My Variants! button repeatedly to continue to generate new options. For error handling, if you enter a year in the future or forget to input one of the fields you'll get a warning message from Miss Minutes.

## Development Process
As a test of concept, I wrote the program in a Jupyter Notebook using imported csv files of jobs and cities that I had created. Then I created the html homepage mockup of what I wanted the user interface to be, which helped me to draw the roadmap of how to get there. I then created a Flask App and connected to the Heroku site. I worked out the JavaScript code for the event handler. I spent a bit of time learning some css and getting the site to look similar to the styling of the Loki tv show. Once it was up and working locally, I connected to the sql database hosted on Heroku through pgAdmin 4 and built the databases so it was hosted online and not using the sqlite file I had made as backup. Lastly, I went back and worked on error handling for user input issues. 


