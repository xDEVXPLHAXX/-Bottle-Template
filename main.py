#Bottle Template created by @rediar 
#bottle is good for smale scale web applications. It is easy to quickly make API's or small personal webpage using Bottle.
import bottle

#this is the main page
@bottle.route('/') 
def index():
  return 'Hey people. Welcome to my domain.' #html tutorial is here: https://www.w3schools.com/html/ 

@bottle.route('/static_page') #no .html extension to the end of the url is needed
def static_page():
  return bottle.static_file('page.html',root="static") #displays page.html in folder static

@bottle.route('/input/<name>') #bottle can also get variables
def input(name):
  return 'Hello '+name #try it! go to /input/yourname
#Advanced Note: regex and integer filters can also be used with bottle. 

#this can only be accesed with a post request (visiting in browser will return 405 Method Not Allowed error)
@bottle.post('/post_request_only')
def post_request_only():
  return 'Post request succesful'

#A 404 page if the url doesn't exist
@bottle.error(404)
def error404(error):
  return("oops! the page you were looked for isn't here. <a href='/'>Return Home?</a>")

bottle.run(host='0.0.0.0', port=1234) #this starts the webpage. any code after this line won't be run

#Good luck programming!