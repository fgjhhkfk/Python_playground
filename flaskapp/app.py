from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RezeptForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foobar.sqlite'
app.config['SECRET_KEY'] = '1243124312431243'

db = SQLAlchemy(app)


class Rezepte(db.Model):
    __searchable__ = ['titel', 'zutaten', 'zubereitung']
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(64))
    link = db.Column(db.String(64))
    bild = db.Column(db.String(64))
    thumbnail = db.Column(db.String(64))
    zutaten = db.Column(db.String(64))
    zubereitung = db.Column(db.String(64))
    kategorie = db.Column(db.String(64))
    tags = db.Column(db.String(64))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/rezept/<int:id>/')
def rezept(id):
    rezept = Rezepte.query.get_or_404(id)
    return render_template('rezept.html', rezept=rezept)


@app.route('/main', methods=['GET', 'POST'])
def main():
    rezepte = Rezepte.query.filter(Rezepte.kategorie == 'Main')
    return render_template('main.html', rezepte=rezepte)


@app.route('/dolce')
def dolce():
    rezepte = Rezepte.query.filter(Rezepte.kategorie == 'Dolce')
    return render_template('dolce.html', rezepte=rezepte)


@app.route('/saucen')
def saucen():
    rezepte = Rezepte.query.filter(Rezepte.kategorie == 'Saucen')
    return render_template('saucen.html', rezepte=rezepte)


@app.route('/beilagen')
def beilagen():
    rezepte = Rezepte.query.filter(Rezepte.kategorie == 'Beilagen')
    return render_template('beilagen.html', rezepte=rezepte)


@app.route('/search')
def search():
    rezepte = Rezepte.query.filter(Rezepte.zutaten.like
                                   ("%" + request.args.get('query') + "%"))
    return render_template('main.html', rezepte=rezepte)


@app.route('/neues_rezept', methods=['GET', 'POST'])
def neues_rezept():
    form = RezeptForm()
    if form.validate_on_submit():
        rezept = Rezepte(titel=form.titel.data,
                         zutaten=form.zutaten.data,
                         zubereitung=form.zubereitung.data,
                         kategorie=form.kategorie.data,
                         tags=form.tags.data,
                         thumbnail='./bilder/thumbnails/Piraten.png',
                         bild='./bilder/Piraten.png')
        db.session.add(rezept)
        db.session.commit()
        flash('Rezept erfolgreich erstellt!', 'success')
        return redirect('/')
    return render_template('neues_rezept.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
