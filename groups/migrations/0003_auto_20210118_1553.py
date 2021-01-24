# Generated by Django 3.1.3 on 2021-01-18 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0002_group_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='auther',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='auther', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]