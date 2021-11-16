from flask import Flask, render_template

app = Flask(__name__)


donos = [
    {'name': 'mister braus man sir', 'amount':200, 'charity': 'JDRF'},
    {'name': 'Mitchell Hudson', 'amount':6000, 'charity':'Cats in Need'}
]
@app.route('/')
def dono_index():
    """Show all donations."""
    return render_template('dono_index.html', donos=donos)


















if __name__ == '__main__':
    app.run(debug=True)