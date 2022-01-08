# Generated by Django 3.1.1 on 2022-01-08 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0007_auto_20220106_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='code_file',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('TLE', 'TLE'), ('WA', 'WA'), ('AC', 'AC'), ('processing', 'processing'), ('queue', 'queue'), ('NotExecuted', 'NotExecuted')], default='queue', max_length=20),
        ),
        migrations.AlterField(
            model_name='submissiontest',
            name='output_file',
            field=models.TextField(blank=True, null=True),
        ),
    ]
