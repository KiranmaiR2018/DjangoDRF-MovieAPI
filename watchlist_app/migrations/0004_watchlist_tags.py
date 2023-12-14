# Generated by Django 4.2.5 on 2023-10-11 08:23

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('watchlist_app', '0003_watchlist_streamingplatform'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
