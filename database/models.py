from datetime import datetime
from peewee import (SqliteDatabase, Model,
                    IntegerField, CharField,
                    TextField, DateTimeField)


db = SqliteDatabase('./real_estate.db')


class BaseModel(Model):
    class Meta:
        database = db


class Offer(BaseModel):
    offer_id = IntegerField()
    title = CharField(max_length=100)
    price = IntegerField()
    url = CharField(max_length=200)
    geo = CharField(max_length=250)
    description = TextField()
    date_pub = DateTimeField(default=datetime.now())

    class Meta:
        table_name = 'offers'


Offer.create_table(safe=True)
