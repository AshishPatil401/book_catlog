from app.catlog import main
from app import db, render_template
from app.catlog.models import Books, Publication



@main.route('/')
@main.route('/home')
def display_books():
    """Description: This method is used to display all books."""
    books = Books.query.all()

    return render_template('home.html', books=books)
    


@main.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):
    """
    Description: This method is used to display all books of a publisher.
    param: publisher_id - integer 
    return: all books of specific publisher
    """
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Books.query.filter_by(pub_id = publisher.id).all()

    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)

