# Generated by Django 4.2.1 on 2023-06-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='商品説明'),
        ),
        migrations.AlterField(
            model_name='product',
            name='english_name',
            field=models.CharField(max_length=200, verbose_name='英名'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='価格'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=200, verbose_name='商品名'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_number',
            field=models.CharField(max_length=200, verbose_name='商品番号'),
        ),
        migrations.AlterField(
            model_name='product',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='アップロード'),
        ),
    ]
