from flask import Flask, url_for, render_template
app = Flask(__name__)



article_templates:dict[int, str] = {
    1: "index.html" ,
    2: "hitler.html",
    3: "Salvini.html"
}

@app.route('/')
def home() -> str:
    return f""" <h1>Hello!</h1>
    <a href = {url_for("name", name = "Marco")}>Nome Utente1</a>
    <br />
    <a href = {url_for("name", name = "Mario")}>Nome Utente2</a>
    <br />
    <a href = {url_for("name", name = "Giorgio")}>Nome Utente3</a>
    <br />
    <a href = {url_for("name", name = "Giorgio")}>Nome Utente4</a>
    <br />
    <a href = {url_for("name", name = "Flavio")}>Nome Utente5</a>
    <br />
    <a href = {url_for("square", b = 3**2)}>Quadrato del numero</a>
    <br />
    <a href = {url_for("somma", a = 3, b= 2)}>Somma</a>

"""



# @app.route('/user/<string:username>/<int:age>')
# def show_user_profile(username: str, age:int ) -> str:
#     return f"Profilo di {username}: {age} anni"


# @app.route('/post/<int:post_id>')
# def show_post(post_id: int) -> str:
#     return f"Post {post_id}"


# # Test: genera URL solo per route esistenti
# with app.test_request_context():
# 	print(url_for('home'))
# 	print(url_for('show_user_profile', username='John Doe', age = 30))
# 	print(url_for('show_post', post_id=42))



# @app.route('/about/<string:description>/<string:name>')
# def text_html(description: str, name:str)-> str:
#     return f"<h3>Questa è {description} di {name}</h3>"


#1. Creare un percorso  /user/<nome> che restituisca “Benvenuto, <nome>!”.

@app.route('/user/<string:name>')
def name(name: str)-> str:
    return f"<h3>Bentornato {name}!</h3>"

# 2. Definire /square/<int:n> che ritorni il quadrato di n.
@app.route('/square/<int:b>')
def square(b:int)-> str:
    return f"<p>Il quadrato di {b} è: {b**2}</p>"



# 3. Creare /sum/<int:a>/<int:b> che restituisca la somma dei due numeri.
@app.route('/sum/<int:a>/<int:b>')
def somma (a:int, b:int)->str:
    som:int = a+b
    return f"<p>La somma tra{a} e {b} è: {som}</p>"




@app.route('/posts')
def show_posts()->str:
    return f""" 

    <a href = {url_for('show_post', id =1)}>Adinolfi Gay</a>
    <a href = {url_for('show_post', id =2)}>Hitler al Berghain</a>
    <a href = {url_for('show_post', id =3)}>Perché Salvini parla</a>
"""
@app.route('/post/<int:id>')
def show_post(id:int)->str:
    template = article_templates.get(id)
    if template: 
        return render_template(template)
    else: 
        return f"<h3>Articolo non trovato</h3>"

""" 
=======================
Esercizi su url_for()
=======================

"""
# Usare url_for per creare automaticamente i link alle route definite, 
# ed esporli in una pagina principale (homepage con link a /about, /user/..., ecc.).


# print(url_for('home'))
# print(url_for('name', name = 'Mario'))
# print(url_for('square',b = 3**2))
# print(url_for('sum',a = 3, b = 4))



if __name__ == '__main__':
    app.run(debug=True)

