from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    product_name = forms.CharField(label='商品名(楽天以外)', max_length=200, required=False)
    rakuten_product_name = forms.CharField(label='商品名(楽天ページTOP部分)商品名', max_length=200, required=False)
    english_name = forms.CharField(label='英名', max_length=200, required=False)
    description = forms.CharField(label='商品説明', widget=forms.Textarea, required=False)
    product_number = forms.CharField(label='商品番号', max_length=200, required=False)
    price = forms.DecimalField(label='価格', max_digits=5, decimal_places=2, required=False)
    production_year = forms.IntegerField(label='生産年', required=False)
    content_volume = forms.CharField(label='内容量', max_length=200, required=False)
    stock_quantity = forms.IntegerField(label='在庫数', required=False)
    producer = forms.CharField(label='生産者', max_length=200, required=False)
    production_location = forms.CharField(label='生産地', max_length=200, required=False)
    jan_code = forms.CharField(label='JANコード', max_length=13, required=False)
    wine_type = forms.CharField(label='ワインのタイプ', max_length=200, required=False)
    wine_taste = forms.CharField(label='ワインのテイスト', max_length=200, required=False)
    catch_copy = forms.CharField(label='キャッチ文', widget=forms.Textarea, required=False)
    grape_variety = forms.CharField(label='ブドウの品種', max_length=200, required=False)
    attention_text = forms.CharField(label='注意文', widget=forms.Textarea, required=False)
    option_master = forms.CharField(label='オプションマスタ', max_length=200, required=False)
    shipping_setting = forms.CharField(label='送料設定', max_length=200, required=False)
    delivery_method_set = forms.CharField(label='配送方法セット', max_length=200, required=False)
    in_stock_delivery_time = forms.CharField(label='在庫あり時の納期', max_length=200, required=False)
    out_of_stock_delivery_time = forms.CharField(label='在庫切れ時の納期', max_length=200, required=False)
    directory_id = forms.CharField(label='ディレクトリID', max_length=200, required=False)
    tag_id = forms.CharField(label='タグID', max_length=200, required=False)
    main_category = forms.CharField(label='メインカテゴリ', max_length=200, required=False)
    link_category = forms.CharField(label='リンクカテゴリ', max_length=200, required=False)
    asuraku = forms.CharField(label='あす楽',  max_length=200,required=False)
    rakuten_product_image1 = forms.ImageField(label='楽天商品画像1', required=False)
    rakuten_product_image2 = forms.ImageField(label='楽天商品画像2（ラベルアップ）', required=False)
    rakuten_product_image3 = forms.ImageField(label='楽天商品画像3', required=False)
    rakuten_product_image4 = forms.ImageField(label='楽天商品画像4', required=False)
    yahoo_product_image = forms.ImageField(label='yahoo商品画像', required=False)
    bottle_image = forms.ImageField(label='ボトル画像', required=False)
    catch_image1 = forms.ImageField(label='キャッチ画像01(ロゴ)', required=False)
    catch_image2 = forms.ImageField(label='キャッチ画像02(キャッチ)', required=False)
    bottle_comment = forms.CharField(label='ボトルコメント', widget=forms.Textarea, required=False)

    class Meta:
        model = Product
        fields = ['product_name', 'rakuten_product_name', 'english_name', 'description', 'product_number', 'price', 'production_year', 'content_volume', 'stock_quantity', 'producer', 'production_location', 'jan_code', 'wine_type', 'wine_taste', 'catch_copy', 'grape_variety', 'attention_text', 'option_master', 'shipping_setting', 'delivery_method_set', 'in_stock_delivery_time', 'out_of_stock_delivery_time', 'directory_id', 'tag_id', 'main_category', 'link_category', 'asuraku', 'rakuten_product_image1', 'rakuten_product_image2', 'rakuten_product_image3', 'rakuten_product_image4', 'yahoo_product_image', 'bottle_image', 'catch_image1', 'catch_image2', 'bottle_comment']

