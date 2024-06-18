from flask import Flask
from views import my_view

app = Flask(__name__) #create a new app called Flask (__name__)
app.register_blueprint(my_view) #use the blueprint 'my_view', which is a separate file

if __name__ == "__main__":
  app.run(debug = True, port = 8000)