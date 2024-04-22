# Generated by Django 5.0.4 on 2024-04-19 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=400, null=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='staff/')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Staff',
            },
        ),
    ]
