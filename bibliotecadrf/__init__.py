from django.db import migrations, models

from livros.models import Livrob


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livrob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('editora', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=255)),
                ('descricao', models.TextField(max_length=4000)),
            ],
        ),

        migrations.CreateModel(
            name='AvaliarLivro',
            fields=[
                ('livro', models.ForeignKey(Livrob, related_name='avaliacoes', on_delete=models.CASCADE)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField()),
                ('comentario', models.TextField(blank=True, default='')),
                ('avaliacao', models.DecimalField(max_length=2, decimal_places=1)),
            ],
        ),
    ]
