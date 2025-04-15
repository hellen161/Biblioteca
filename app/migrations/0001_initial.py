# Generated by Django 5.2 on 2025-04-08 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Gênero')),
            ],
            options={
                'verbose_name': 'Gênero',
                'verbose_name_plural': 'Gêneros',
            },
        ),
        migrations.CreateModel(
            name='Leitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do leitor')),
                ('email', models.CharField(max_length=100, verbose_name='Email do leitor')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF do leitor')),
            ],
            options={
                'verbose_name': 'Leitor',
                'verbose_name_plural': 'Leitores',
            },
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do autor')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade do autor')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da editora')),
                ('site', models.CharField(max_length=100, verbose_name='Site da editora')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade da editora')),
            ],
            options={
                'verbose_name': 'Editora',
                'verbose_name_plural': 'Editoras',
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do livro')),
                ('preco', models.IntegerField(verbose_name='Preço do livro')),
                ('data_plub', models.DateField(verbose_name='Data de publicação do livro')),
                ('status', models.BooleanField(verbose_name='Status do livro')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.autor', verbose_name='Autor do livro')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.editora', verbose_name='Editora do livro')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genero', verbose_name='Gênero do livro')),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
    ]
