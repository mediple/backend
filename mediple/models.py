from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20)
    tel = fields.TextField()
    email = fields.TextField()
    username = fields.CharField(max_length=10, unique=True)
    password = fields.TextField()


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
