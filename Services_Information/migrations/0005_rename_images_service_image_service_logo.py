# Generated by Django 4.0.4 on 2022-05-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services_Information', '0004_team_member_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='images',
            new_name='image',
        ),
        migrations.AddField(
            model_name='service',
            name='logo',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]