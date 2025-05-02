# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

def remove_common_chars(name1, name2):
    name1_list = list(name1)
    name2_list = list(name2)

    for char in name1[:]:
        if char in name2_list:
            name1_list.remove(char)
            name2_list.remove(char)

    return len(name1_list) + len(name2_list)

def flames_result(count):
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    
    while len(flames) > 1:
        split = (count % len(flames)) - 1
        if split >= 0:
            flames = flames[split+1:] + flames[:split]
        else:
            flames.pop()
    return flames[0]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        name1 = request.form["name1"].lower().replace(" ", "")
        name2 = request.form["name2"].lower().replace(" ", "")
        count = remove_common_chars(name1, name2)
        result = flames_result(count)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
