# Generated by Django 3.0.7 on 2020-07-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20200730_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
