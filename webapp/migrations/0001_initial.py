# Generated by Django 3.0.6 on 2020-05-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('application_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='firstName', max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, db_column='lastName', max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('application_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'careers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('enquiry_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('enquiry_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'contact_us',
                'managed': False,
            },
        ),
    ]
