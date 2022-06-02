# Generated by Django 4.0.4 on 2022-06-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_Information', '0010_site_info_section_contact_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=255)),
                ('link', models.URLField()),
            ],
        ),
    ]
