from flask import Flask, request
from caesar import rotate_string

app= Flask(__name__)
app.config['DEBUG']= True

form= """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}

            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}

        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form action="/ceasar" method="post">
            <label for="Rotate by">Rotate by:</label>
            <input type="text" name="rot" value= 0 /><br>
            <textarea name="text" rows="25" cols="50">{0}</textarea><br>
            <input type="submit" />
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    result= form
    return form.format("")

@app.route("/ceasar", methods=['POST'])
def encrypt():
    message= request.form["text"]
    number = request.form["rot"]
    answer = rotate_string(message,int(number))
    return form.format(answer)

app.run()    