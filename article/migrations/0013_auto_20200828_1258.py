# Generated by Django 3.1b1 on 2020-08-28 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20200827_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='commented_post', to='article.article'),
        ),
    ]
