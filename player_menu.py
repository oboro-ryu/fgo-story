from flask import Flask, render_template, redirect, url_for, send_from_directory, jsonify
app = Flask(__name__,static_folder='templates')

actions = [
    ("エレキシュガル", "ここが　がっこう、？", "img/b.png", True),
    ("エレキシュガル", "とても明るいのに、なんだか落ち着くわ","img/b.png", True),
    ("エレキシュガル", "..........", "img/c.png", True),
]

current_message_index = 0
#@app.route('/three')
#def threejs_page():
    #return render_template("card.html") 

# メニューを表示
@app.route("/")
def menu():
    return render_template("menu.html")
@app.route("/walk")
def walk():
    global current_message_index
    player, message_suffix, image_path, _ = actions[current_message_index]

    if message_suffix.startswith(player):
        message = message_suffix[len(player):].lstrip() 
    else:
        message = message_suffix

    current_message_index = (current_message_index + 1) % len(actions)
    return render_template("action.html", player=player, message=message, image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)