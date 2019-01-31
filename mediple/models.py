from tortoise.models import Model
from tortoise import fields


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
