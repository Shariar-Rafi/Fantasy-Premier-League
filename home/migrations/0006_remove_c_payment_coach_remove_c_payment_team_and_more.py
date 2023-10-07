# Generated by Django 4.1.7 on 2023-05-27 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_g_payment_c_payment_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c_payment',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='c_payment',
            name='team',
        ),
        migrations.RemoveField(
            model_name='coach',
            name='userprofile',
        ),
        migrations.RemoveField(
            model_name='g_payment',
            name='GA',
        ),
        migrations.RemoveField(
            model_name='g_payment',
            name='team',
        ),
        migrations.RemoveField(
            model_name='ground',
            name='g_admin',
        ),
        migrations.RemoveField(
            model_name='groundadmin',
            name='userprofile',
        ),
        migrations.RemoveField(
            model_name='player',
            name='User_profile',
        ),
        migrations.RemoveField(
            model_name='team',
            name='C',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='C_payment',
        ),
        migrations.DeleteModel(
            name='Coach',
        ),
        migrations.DeleteModel(
            name='G_payment',
        ),
        migrations.DeleteModel(
            name='Ground',
        ),
        migrations.DeleteModel(
            name='GroundAdmin',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]