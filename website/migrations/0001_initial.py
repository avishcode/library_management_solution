# Generated by Django 4.2.3 on 2023-07-15 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0002_recordpayment_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('lead_id', models.AutoField(primary_key=True, serialize=False)),
                ('lead_name', models.CharField(max_length=100)),
                ('lead_phone', models.CharField(max_length=15)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.membership')),
            ],
        ),
    ]