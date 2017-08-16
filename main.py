from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjP04zj3dzVAhUP7WMKHUUlBi0QjBwIBA&url=http%3A%2F%2Fcdn2-www.dogtime.com%2Fassets%2Fuploads%2Fgallery%2Fcorgi-puppies%2Fcorgi-puppy-3.jpg&psig=AFQjCNHCSuZPOydvXHIku2dfGY45hGwNQQ&ust=1503006527000697">
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
