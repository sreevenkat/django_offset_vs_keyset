# Generated by Django 3.0.7 on 2020-06-28 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('updated_at', models.DateTimeField(null=True)),
                ('archived', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('publisher', models.CharField(max_length=128)),
                ('updated_at', models.DateTimeField(null=True)),
                ('archived', models.BooleanField(default=False)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.Library')),
            ],
        ),
    ]
