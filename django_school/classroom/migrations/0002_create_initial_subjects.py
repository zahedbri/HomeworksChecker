# Generated by Django 2.0.1 on 2018-01-18 18:07

from django.db import migrations


def create_subjects(apps, schema_editor):
    Subject = apps.get_model('classroom', 'Subject')
    Subject.objects.create(name='PIU', color='#343a40')
    Subject.objects.create(name='PCLP1', color='#007bff')
    Subject.objects.create(name='PCLP2', color='#28a745')
    Subject.objects.create(name='RF', color='#17a2b8')
    Subject.objects.create(name='TehnologiiWEB', color='#ffc107')


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_subjects),
    ]
