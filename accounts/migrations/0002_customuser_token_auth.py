<<<<<<< HEAD
# Generated by Django 4.2.5 on 2023-09-06 18:06
=======
# Generated by Django 4.2.5 on 2023-09-07 08:09
>>>>>>> 8b0d891e9d584c70be0572167e6e5128ed5d8fc5

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='token_auth',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
