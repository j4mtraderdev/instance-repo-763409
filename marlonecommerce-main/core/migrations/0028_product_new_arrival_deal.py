# Generated by Django 4.2.2 on 2024-07-18 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_product_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_arrival',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('expiration_date', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals', to='core.product')),
            ],
            options={
                'verbose_name_plural': 'Deals',
            },
        ),
    ]
