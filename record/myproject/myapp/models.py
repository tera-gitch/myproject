from django.db import models

class Product(models.Model):
    product_name = models.CharField('商品名(楽天以外)', max_length=200, null=True, blank=True)
    rakuten_product_name = models.CharField('商品名(楽天ページTOP部分)商品名', max_length=200, null=True, blank=True)
    english_name = models.CharField('英名', max_length=200, null=True, blank=True)
    description = models.TextField('商品説明', null=True, blank=True)
    product_number = models.CharField('商品番号', max_length=200, null=True, blank=True)
    price = models.DecimalField('価格', max_digits=5, decimal_places=2, null=True, blank=True)
    production_year = models.IntegerField('生産年', null=True, blank=True)
    content_volume = models.CharField('内容量', max_length=200, null=True, blank=True)
    stock_quantity = models.IntegerField('在庫数', null=True, blank=True)
    producer = models.CharField('生産者', max_length=200, null=True, blank=True)
    production_location = models.CharField('生産地', max_length=200, null=True, blank=True)
    jan_code = models.CharField('JANコード', max_length=13, null=True, blank=True) # Assuming JAN code is a 13 digit number
    wine_type = models.CharField('ワインのタイプ', max_length=200, null=True, blank=True)
    wine_taste = models.CharField('ワインのテイスト', max_length=200, null=True, blank=True)
    catch_copy = models.TextField('キャッチ文', null=True, blank=True)
    grape_variety = models.CharField('ブドウの品種', max_length=200, null=True, blank=True)
    attention_text = models.TextField('注意文', null=True, blank=True)
    option_master = models.CharField('オプションマスタ', max_length=200, null=True, blank=True)
    shipping_setting = models.CharField('送料設定', max_length=200, null=True, blank=True)
    delivery_method_set = models.CharField('配送方法セット', max_length=200, null=True, blank=True)
    in_stock_delivery_time = models.CharField('在庫あり時の納期', max_length=200, null=True, blank=True)
    out_of_stock_delivery_time = models.CharField('在庫切れ時の納期', max_length=200, null=True, blank=True)
    directory_id = models.CharField('ディレクトリID', max_length=200, null=True, blank=True)
    tag_id = models.CharField('タグID', max_length=200, null=True, blank=True)
    main_category = models.CharField('メインカテゴリ', max_length=200, null=True, blank=True)
    link_category = models.CharField('リンクカテゴリ', max_length=200, null=True, blank=True)
    asuraku =models.CharField('あす楽',  max_length=200, null=True, blank=True)
    rakuten_product_image1 = models.ImageField('楽天商品画像1', upload_to='products/', null=True, blank=True)
    rakuten_product_image2 = models.ImageField('楽天商品画像2（ラベルアップ）', upload_to='products/', null=True, blank=True)
    rakuten_product_image3 = models.ImageField('楽天商品画像3', upload_to='products/', null=True, blank=True)
    rakuten_product_image4 = models.ImageField('楽天商品画像4', upload_to='products/', null=True, blank=True)
    yahoo_product_image = models.ImageField('yahoo商品画像', upload_to='products/', null=True, blank=True)
    bottle_image = models.ImageField('ボトル画像', upload_to='products/', null=True, blank=True)
    catch_image1 = models.ImageField('キャッチ画像01(ロゴ)', upload_to='products/', null=True, blank=True)
    catch_image2 = models.ImageField('キャッチ画像02(キャッチ)', upload_to='products/', null=True, blank=True)
    bottle_comment = models.TextField('ボトルコメント', null=True, blank=True)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'

