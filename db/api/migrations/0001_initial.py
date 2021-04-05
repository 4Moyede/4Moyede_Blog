# Generated by Django 2.2.12 on 2021-04-04 13:13

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Introduce',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, db_column='_id', primary_key=True, serialize=False)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, db_column='_id', primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('name', models.TextField()),
                ('thumbnail', models.TextField()),
                ('detail', models.TextField()),
                ('techStack', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TechStack',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, db_column='_id', primary_key=True, serialize=False)),
                ('tech', models.TextField()),
                ('skill', models.IntegerField()),
            ],
        ),
    ]