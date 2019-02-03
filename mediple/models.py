from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20)
    profile_image = fields.TextField()
    tel = fields.TextField()
    email = fields.TextField()
    username = fields.CharField(max_length=10, unique=True)
    password = fields.TextField()


class UserData(Model):
    user = fields.ForeignKeyField('models.User')
    age = fields.IntField()
    height = fields.IntField()
    weight = fields.IntField()


class Medicine(Model):
    id = fields.IntField(pk=True)
    admin_method = fields.CharField(max_length=5)
    basis = fields.CharField(max_length=10)
    code = fields.TextField()
    name = fields.TextField()
    made = fields.TextField()
    how_to = fields.TextField()
    max_price = fields.IntField()
    is_specialty = fields.BooleanField()

    def __str__(self):
        return self.name
