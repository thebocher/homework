from mongoengine import Document, StringField, connect

class OLXOffer(Document):
    offer_id = StringField(unique=True)
    author = StringField(max_length=100)
    title = StringField(max_length=100)
    price = StringField(max_length=20)
    description = StringField(max_length=1000)
    
def connect_to_mongo():
    connect(**{'host': 'mongodb+srv://mongo_user:lolon123@cluster0.xweys.mongodb.net/olx?retryWrites=true&w=majority'})
# connect_to_mongo()
# for doc in OLXOffer.objects.all():
#     doc.delete()
#     doc.save()
    
# print(OLXOffer.objects.all())    