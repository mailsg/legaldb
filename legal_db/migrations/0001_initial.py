# Generated by Django 3.0.7 on 2020-06-03 20:53

import django.contrib.postgres.fields
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license', models.CharField(blank=True, max_length=25, null=True)),
                ('license_version', models.CharField(blank=True, max_length=25, null=True)),
                ('is_ported', models.BooleanField(blank=True, null=True)),
                ('contributor_name', models.CharField(max_length=120)),
                ('contributor_email', models.EmailField(max_length=254)),
                ('contribution_credit', models.BooleanField()),
                ('link', models.URLField(max_length=2000)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('summary', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('case_no', models.CharField(blank=True, max_length=50, null=True)),
                ('jurisdiction', models.CharField(blank=True, max_length=250, null=True)),
                ('court_name', models.CharField(max_length=250)),
                ('decision_district_city_circuit', models.CharField(blank=True, max_length=250, null=True)),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
                ('decided_at', models.DateField(blank=True, null=True)),
                ('en_translation_link', models.URLField(blank=True, max_length=2000, null=True)),
                ('cc_involvement', models.CharField(blank=True, max_length=100, null=True)),
                ('cc_implication', models.TextField(blank=True, null=True)),
                ('work_type', models.CharField(blank=True, max_length=100, null=True)),
                ('issue', models.CharField(blank=True, max_length=200, null=True)),
                ('blurb', models.TextField(blank=True, null=True)),
                ('original_blurb', models.TextField(blank=True, null=True)),
                ('background', models.TextField(blank=True, null=True)),
                ('result', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('answer', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license', models.CharField(blank=True, max_length=25, null=True)),
                ('license_version', models.CharField(blank=True, max_length=25, null=True)),
                ('is_ported', models.BooleanField(blank=True, null=True)),
                ('contributor_name', models.CharField(max_length=120)),
                ('contributor_email', models.EmailField(max_length=254)),
                ('contribution_credit', models.BooleanField()),
                ('link', models.URLField(max_length=2000)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('summary', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('authors', models.CharField(blank=True, max_length=250, null=True)),
                ('published_at', models.DateField(blank=True, null=True)),
                ('elements_discussing', models.CharField(blank=True, max_length=250, null=True)),
                ('journal_or_publisher', models.CharField(blank=True, max_length=256, null=True)),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
