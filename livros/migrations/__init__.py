from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='descricao',
            field=models.TextField(max_length=4000),
        ),
    ]
