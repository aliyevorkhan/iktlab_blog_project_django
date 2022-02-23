# File Upload In Django

### Bu basliqda Django'da Fayl yuklemek ucun zeruri addimlar qeyd edilib

1. Fayllari idare edebilmek ucun (en esasi sekil fayllarini) Pillow modulu yuklenmelidir
    * pip install Pillow

2. settings.py icinde MEDIA_URL ve MEDIA_ROOT setirler elave edilmelidir (asagidaki kimi)
    * MEDIA_URL = '/media/'
    * MEDIA_ROOT = BASE_DIR / 'media'

3. Proyektde (herhansi bir app'in urls.py faylinda YOX) urls.py fayli icinde asagidaki setir elave edilmelidir
    * urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

4. Yuxaridaki setirin isleyebilmesi ucun altdaki import'lari etmek lazimdir
    * from django.conf import settings
    * from django.conf.urls.static import static

5. media'lara her yerde elcatanliq yaratmaq ucun context_processors deyerini settings.py icinde TEMPLATES icideki context_processors siyahisina elave etmek lazimdir
    * 'django.template.context_processors.media'

6. add_article.html icindeki form tagina asagidaki elementi elave etmek lazimdir
    * enctype="multipart/form-data"

7. Article app'inin models.py faylinda yeni bir Field yaratmaq lazimdir
    * article_image = models.FileField(blank=True, null=True, verbose_name="Şəkil")

8. Post elave etmek ekraninda bu Field'i gorebilmek ucun Article app'i icinde forms.py faylinda fields hissesine 'article_image' Field'ini da elave etmek lazimdir.

9. Herhasi post silidikde oz sahib oldugu faylin da media/ qovlugu altindan silinmesini avtomatiklesdirmek ucun django-cleanup modulu yuklenmelidir
    * pip install django_cleanup

10. Modul yuklendikden sonra INSTALLED_APPS icine elave edilmelidir
    * 'django_cleanup' seklide

11. Butun addimlar yerine yetirildikden sonra frontendden yuklenen fayli backendden alabilmek ucun add_article() methodunun icindeki ilk setir asagidaki kimi berpa edilir
    * form = ArticleForm(request.POST or None, request.FILES or None)

#### https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
#### https://docs.djangoproject.com/en/4.0/topics/http/file-uploads/