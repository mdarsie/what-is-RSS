# Generated by Django 3.0.3 on 2020-02-11 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_title', models.CharField(max_length=200)),
                ('feed_description', models.TextField(default='')),
                ('feed_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.CharField(default='none', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_link', models.CharField(max_length=200)),
                ('article_description', models.TextField(default='')),
                ('article_guid', models.TextField(max_length=200)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='rss_reader.Feed')),
            ],
        ),
    ]
