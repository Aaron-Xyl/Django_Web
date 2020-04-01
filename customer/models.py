from django.db import models

# Create your models here.


from django.db.models import Model, CharField, SmallIntegerField, BigIntegerField
import json


class User(Model):
    user_id = CharField(max_length=64)
    user_pet_name = CharField(max_length=64)
    iphone = CharField(max_length=16)
    email = CharField(max_length=64)
    password = CharField(max_length=255)
    age = SmallIntegerField()
    address = CharField(max_length=255)
    info = CharField(max_length=255)
    id = BigIntegerField(primary_key=True)

    # def to_dict(self):
    #     return json.dumps({
    #         'user_id': self.user_id,
    #         'user_pet_name': self.user_pet_name,
    #         'iphone': self.iphone,
    #         'email': self.email,
    #         'password': self.password,
    #         'age': self.age,
    #         'address': self.address,
    #         'info': self.info,
    #         'id': self.id,
    #     })
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user_pet_name': self.user_pet_name,
            'iphone': self.iphone,
            'email': self.email,
            'password': self.password,
            'age': self.age,
            'address': self.address,
            'info': self.info,
            'id': self.id,
        }

    def update_dict(self):
        return {
            user_id: username,
            user_pet_name: petname,
            iphone: iphone,
            email: email,
            password: password,
            age: age,
            address: address,
            info: info,
        }

    def __str__(self):
        ms = 'name:{}'.format(self.user_id)
        return ms

    class Meta():
        db_table = 'user'
