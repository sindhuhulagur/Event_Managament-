# Generated by Django 5.1.4 on 2024-12-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0002_alter_event_options_event_category_attendee_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={},
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('business', 'Business'), ('music', 'Music'), ('sports', 'Sports'), ('tech', 'Tech')], default='business', max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]