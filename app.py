"""Pet Adoption App"""


from flask import Flask, request, redirect, render_template
from models import Pet, db, connect_db
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

with app.app_context():

    connect_db(app)
    db.create_all()


@app.route("/")
def home():
    pets = Pet.query.all()
    return render_template("list-pets.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()
    
    print("*****", form.photo_url.data)

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, age=age, species=species, photo_url=photo_url, notes=notes)
        db.session.add(pet)
        db.session.commit()
        
        return redirect("/")

    else:
        return render_template(
            "add-pet.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Pet edit form; handle editing."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.photo_url.data == "profile.png":
            form.photo_url.data = ""

    if form.validate_on_submit():
        pet.photo_url =  "profile.png" if form.photo_url.data == "" else form.photo_url.data
        pet.notes = form.notes.data
        print(form.available.data)
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit-pet.html", form=form, pet=pet)