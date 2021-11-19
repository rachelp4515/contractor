
from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
import os
app = Flask(__name__)

from pymongo import MongoClient
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
client = MongoClient(app.config["MONGO_URI"])
db = client.get_database('dono-track')
donos = db.donos


#---------------------- / 
@app.route('/')
def dono_index():
    """Show all donations."""
    return render_template('dono_index.html', donos=donos.find())


#---------------------- / new dono
@app.route('/donos/new')
def new_dono():
    """Add a donation"""
    return render_template('new_dono.html')


#---------------------- / submit dono
@app.route('/donos', methods=['POST'])
def dono_submit():
    """Submit donation"""
    dono = {
        'name': request.form.get('name'),
        'charity': request.form.get('charity'),
        'amount': request.form.get('amount')
    }
    donos.insert_one(dono)
    return redirect(url_for('dono_index'))


#---------------------- / display one
@app.route('/donos/<dono_id>')
def donos_show(dono_id):
    """Show a single donation"""
    dono = donos.find_one({'_id': ObjectId(dono_id)})
    return render_template('show_dono.html', dono=dono)

#--------------------- / remove from display
@app.route('/donos/<dono_id>/delete', methods=['POST'])
def donos_delete(dono_id):
    """Delete one donation."""
    donos.delete_one({'_id': ObjectId(dono_id)})
    return redirect(url_for('dono_index'))

#-------------------- / edit redirect

@app.route('/donos/<dono_id>/add')
def dono_edit(dono_id):
    """Add to a donation"""
    dono = donos.find_one({'_id': ObjectId(dono_id)})
    return render_template('add_dono.html', dono=dono)


















# @app.route('/test', methods= ['POST'])
# def test():
#     dono = {
#         'name': 'uhhhhhgggjff', 'amount':1, 'charity': 'asdf'
#     }
#     donos.insert_one(dono)
#     return redirect("/")















if __name__ == '__main__':
    app.run(debug=True)