
from flask import render_template
from app import app
# views
@app.route('/movie/<int:movie_id>')
def index(movie_id):
    '''
    view root page function that returns the index page and its data
    '''
   
    return render_template('movie.html',id=movie_id)