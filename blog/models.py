from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    # 他モデルへのリンク
    auther = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 文字数制限ありのテキスト
    title = models.CharField(max_length=200)
    # 制限なしの長文テキスト
    text = models.TextField()
    # 日付と時間
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    # blog公開メソッド
    def publish(self):
        
        self.published_date = timezone.now()
        self.save()

    # リターンするためのメソッド
    def __str__(self):
        return self.title
