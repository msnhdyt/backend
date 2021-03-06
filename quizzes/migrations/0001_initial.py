# Generated by Django 3.2.6 on 2021-08-23 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topic', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quizzes',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='topic.topic')),
            ],
        ),
    ]
