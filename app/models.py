from app import db
from datetime import datetime

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    is_available = db.Column(db.Boolean, default=True, nullable=False)
    
    authors = db.relationship('Author', secondary='book_authors', backref=db.backref('books', lazy=True))

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

book_authors = db.Table('book_authors',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)

class BorrowedBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrower_name = db.Column(db.String(80), nullable=False)

    book = db.relationship('Book', backref='borrowed_books')

    @property
    def title(self):
        return self.book.title


    