from django.db import models
from ckeditor.fields import RichTextField
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlıq")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma tarixi")
    article_image = models.FileField(blank=True, null=True, verbose_name="Şəkil")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Post', related_name="comments")
    comment_author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    comment_content = models.TextField(max_length=250, verbose_name="Mezmun")
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma tarixi")
    class Meta:
        ordering = ['-comment_date']
    def __str__(self):
        return self.comment_content