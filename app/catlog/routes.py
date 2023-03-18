from app.catlog import main
from flask import render_template, flash, request, redirect, url_for
from app.catlog.models import Books, Publication
from app import db
from flask_login import login_required



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



@main.route('/book/delete/<book_id>', methods=['GET','POST'])
@login_required
def delete_book(book_id):
    book = Books.query.filter(Books.id == book_id).first()
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash("Book deleted successfully")
        return redirect(url_for('main.display_book'))
    return render_template('delete_book.html', book=book, book_id=book.id)


