from mongoengine import Document, StringField

class User(Document):
    login = StringField(max_length=50, unique=True, required=True)
    password = StringField(max_length=50, required=True)
