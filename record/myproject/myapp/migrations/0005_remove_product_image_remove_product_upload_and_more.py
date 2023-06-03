# Generated by Django 4.2.1 on 2023-06-03 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_product_description_alter_product_english_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='upload',
        ),
        migrations.AddField(
            model_name='product',
            name='asuraku',
            field=models.BooleanField(default=False, verbose_name='あす楽'),
        ),
        migrations.AddField(
            model_name='product',
            name='attention_text',
            field=models.TextField(blank=True, null=True, verbose_name='注意文'),
        ),
        migrations.AddField(
            model_name='product',
            name='bottle_comment',
            field=models.TextField(blank=True, null=True, verbose_name='ボトルコメント'),
        ),
        migrations.AddField(
            model_name='product',
            name='bottle_image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='ボトル画像'),
        ),
        migrations.AddField(
            model_name='product',
            name='catch_copy',
            field=models.TextField(blank=True, null=True, verbose_name='キャッチ文'),
        ),
        migrations.AddField(
            model_name='product',
            name='catch_image1',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='キャッチ画像01(ロゴ)'),
        ),
        migrations.AddField(
            model_name='product',
            name='catch_image2',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='キャッチ画像02(キャッチ)'),
        ),
        migrations.AddField(
            model_name='product',
            name='content_volume',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='内容量'),
        ),
        migrations.AddField(
            model_name='product',
            name='delivery_method_set',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='配送方法セット'),
        ),
        migrations.AddField(
            model_name='product',
            name='directory_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ディレクトリID'),
        ),
        migrations.AddField(
            model_name='product',
            name='grape_variety',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ブドウの品種'),
        ),
        migrations.AddField(
            model_name='product',
            name='in_stock_delivery_time',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='在庫あり時の納期'),
        ),
        migrations.AddField(
            model_name='product',
            name='jan_code',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='JANコード'),
        ),
        migrations.AddField(
            model_name='product',
            name='link_category',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='リンクカテゴリ'),
        ),
        migrations.AddField(
            model_name='product',
            name='main_category',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='メインカテゴリ'),
        ),
        migrations.AddField(
            model_name='product',
            name='option_master',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='オプションマスタ'),
        ),
        migrations.AddField(
            model_name='product',
            name='out_of_stock_delivery_time',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='在庫切れ時の納期'),
        ),
        migrations.AddField(
            model_name='product',
            name='producer',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='生産者'),
        ),
        migrations.AddField(
            model_name='product',
            name='production_location',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='生産地'),
        ),
        migrations.AddField(
            model_name='product',
            name='production_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='生産年'),
        ),
        migrations.AddField(
            model_name='product',
            name='rakuten_product_image1',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='楽天商品画像1'),
        ),
        migrations.AddField(
            model_name='product',
            name='rakuten_product_image2',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='楽天商品画像2（ラベルアップ）'),
        ),
        migrations.AddField(
            model_name='product',
            name='rakuten_product_image3',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='楽天商品画像3'),
        ),
        migrations.AddField(
            model_name='product',
            name='rakuten_product_image4',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='楽天商品画像4'),
        ),
        migrations.AddField(
            model_name='product',
            name='rakuten_product_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='商品名(楽天ページTOP部分)商品名'),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_setting',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='送料設定'),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='在庫数'),
        ),
        migrations.AddField(
            model_name='product',
            name='tag_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='タグID'),
        ),
        migrations.AddField(
            model_name='product',
            name='wine_taste',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ワインのテイスト'),
        ),
        migrations.AddField(
            model_name='product',
            name='wine_type',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ワインのタイプ'),
        ),
        migrations.AddField(
            model_name='product',
            name='yahoo_product_image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='yahoo商品画像'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='商品名(楽天以外)'),
        ),
    ]
