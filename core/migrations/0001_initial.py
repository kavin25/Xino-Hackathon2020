# Generated by Django 3.1 on 2020-08-13 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isGuide', models.BooleanField(default=False)),
                ('interestCount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='InterestsActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('general_price', models.FloatField(null=True)),
                ('currency', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hiring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay', models.FloatField(null=True)),
                ('guide', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hiring_guide', to='core.customuser')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hiring_place', to='core.places')),
                ('traveller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hiring_traveller', to='core.customuser')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='interests',
            field=models.ManyToManyField(related_name='InterestsActivities', to='core.InterestsActivities'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='place_of_stay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guide_play_of_stay', to='core.places'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='places_of_interest',
            field=models.ManyToManyField(related_name='user_places_of_interest', to='core.Places'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='searching_for',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.customuser'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
