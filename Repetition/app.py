from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) # Creating Flask app



@app.route("/") # Home route 
def home(): # Home function
    return render_template("index.html")


@app.route("/about") # About route
def about(): # About function
    return "About page"


@app.route("/contact")
def contact():
    return "Contact page"


@app.route("/greet/<name>") # Route with string function argument (can also be <int:id>)
def user(name):
    return render_template("greet.html", name=name) # Template with input - we are passing data to html


@app.route("/greet/<name>/<int:id>") # Route with string function argument and int argument
def id(name, id):
    return f"Hello, {name} - {id}!"


# Route with forms
@app.route("/login", methods=["GET", "POST"]) 
def login():
    if request.method == "POST":
        username = request.form["username"]
        return render_template("greet.html", name=username)
    
    return render_template("login.html")


@app.route("/gogo")
def go():
    return redirect(url_for("home")) # Redirects url to function home



if __name__ == "__main__":
    app.run(debug=True) # Runs app and debug in browser


'''
1. Created app
2. App routes
3. Function and return response for each route

"/" -> Home (only URL with styling)
"/login" -> Input name (with login.html) -> Display result using greet.html
"/greet/<name>" -> Argument in URL, greets user
"/gogo" -> Redirects to home function (going to home URL and respond)

4. Runs app with debug in browser
'''