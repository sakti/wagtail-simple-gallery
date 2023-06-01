# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 09:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_simple_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='simplegalleryindex',
            options={'verbose_name': 'Gallery index', 'verbose_name_plural': 'Gallery indices'},
        ),
        migrations.AlterField(
            model_name='simplegalleryindex',
            name='collection',
            field=models.ForeignKey(help_text='Show images in this collection in the gallery view.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Collection', verbose_name='Collection'),
        ),
        migrations.AlterField(
            model_name='simplegalleryindex',
            name='images_per_page',
            field=models.IntegerField(default=8, help_text='How many images there should be on one page.', verbose_name='Images per page'),
        ),
        migrations.AlterField(
            model_name='simplegalleryindex',
            name='intro_text',
            field=wagtail.fields.RichTextField(blank=True, help_text='Optional text to go with the intro text.', verbose_name='Intro text'),
        ),
        migrations.AlterField(
            model_name='simplegalleryindex',
            name='intro_title',
            field=models.CharField(blank=True, help_text='Optional H1 title for the gallery page.', max_length=250, verbose_name='Intro title'),
        ),
        migrations.AlterField(
            model_name='simplegalleryindex',
            name='use_lightbox',
            field=models.BooleanField(default=True, help_text='Use lightbox to view larger images when clicking the thumbnail.', verbose_name='Use lightbox'),
        ),
    ]
