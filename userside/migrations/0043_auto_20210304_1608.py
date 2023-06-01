# Generated by Django 3.1.5 on 2021-03-04 10:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0042_auto_20210304_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_master',
            name='id_proof',
            field=models.FileField(help_text='Any Government Approved Id(Aadhar/Driving License/PAN Card/Voter Id) <br> Must be .pdf File Only <br> Maximum Size 2MB', null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='photo',
            field=models.FileField(help_text='Image File of User <br> Must of be .jpg or .png <br> Maximum Size 1MB', null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
