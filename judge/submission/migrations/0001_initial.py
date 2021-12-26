# Generated by Django 3.1.1 on 2021-12-26 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0005_auto_20211226_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_file', models.FilePathField(path='code')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('TLE', 'TLE'), ('WA', 'WA'), ('AC', 'AC'), ('procesing', 'processing'), ('queue', 'queue')], max_length=20)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission', to='question.question')),
            ],
            options={
                'verbose_name': 'Submission',
                'verbose_name_plural': 'Submissions',
            },
        ),
        migrations.CreateModel(
            name='SubmissionTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_file', models.FilePathField(path='submission_test', unique=True)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission_test', to='submission.submission')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission_test', to='question.test')),
            ],
            options={
                'verbose_name': 'Submission Test',
                'verbose_name_plural': 'Submission Tests',
            },
        ),
    ]
