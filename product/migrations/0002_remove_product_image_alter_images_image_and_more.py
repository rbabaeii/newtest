# Generated by Django 4.1.2 on 2022-12-29 18:42

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to=product.models.upload_image_path, verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='product',
            name='change',
            field=models.BooleanField(default=False, verbose_name='قابل معاوضه'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('New', 'نو'), ('Used-good', 'در حد نو'), ('Old', 'کهنه')], max_length=50, verbose_name='کیفیت کالا'),
        ),
    ]