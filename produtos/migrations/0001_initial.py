# Generated by Django 4.1.2 on 2022-11-01 18:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Produto",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("preco", models.DecimalField(decimal_places=2, max_digits=5)),
                ("nome", models.CharField(max_length=100)),
                ("imagem", models.TextField()),
                ("descricao", models.TextField(null=True)),
            ],
        ),
    ]