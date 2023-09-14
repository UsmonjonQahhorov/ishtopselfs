# Generated by Django 4.2.5 on 2023-09-09 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='application_resume', to='resumes.resume')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='application_vacancy', to='vacancies.vacancy')),
            ],
        ),
        migrations.AddField(
            model_name='vacancy',
            name='applications',
            field=models.ManyToManyField(related_name='applications', through='vacancies.Application', to='resumes.resume'),
        ),
    ]
