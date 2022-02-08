# iktlab_blog_app_django
IKTLAB DJANGO DERSLERI UCUN YAZILMIS BIR DJANGO BLOG PROYEKTIDIR 

### DJANGO UCUN ONEMLI ADDIMLAR
1. django-admin startproject mysite --> (django proyekti yaradir)
2. python manage.py runserver --> (django proyektini ayaga qaldirir)
3. python manage.py migrate --> (djangodaki hazir app'ler (INSTALLED_APPS) ucun database'de tablelari yaradir)
4. python manage.py createsuperuser --> (django'nun admin hissesine girebilmek ucun super user yaradir)
5. python manage.py startapp article --> (django proyekti icinde (yeni mysite) article adinda app yaradir)
6. article qovlugu altinda models.py fayli icinde Article modeli yaradilir --> (bu model database'de bir table'a qarsiliq olur)
7. mysite qovlugu altinda settings.py fayli icinde INSTALLED_APPS siyahisi icinde article app'i qeyd edilir
8. article qovlugu altinda admin.py fayli icinde admin.site.register(Article) deyilerek Article modeli qeydiyattan kecirilir. (DIQQET: Article classini import etmeyi unutma)
9. python manage.py makemigrations --> (Yaradilan Article modeli ucun database in basaduseceyi sql sorgularini yaradir)
10. python manage.py migrate --> (yaradilmis migrationlari icra edir)

BU EMELIYYATLARDAN SONRA ADMIN HISSESINDE ARTICLE GORSENMELIDIR



Bu proyekt [buradaki](https://github.com/aliyevorkhan/ikt_lab_python_module_1) derslerin davamini teskil edir.

- [x] DERS 35. <br>
* MVC/MVT haqqinda melumat
* DJANGO yuklemek
* django-admin
* django-admin startproject
* DJANGO'nun fayllari haqqinda melumat

- [x] DERS 36. <br>
* admin app haqqinda melumat
* super user yaratmaq
* article app yaratmaq

- [x] DERS 37. <br>
* Article hissesini admin panelden idare etmek
* admin hissesini fərdiləşdirmək (https://docs.djangoproject.com/en/4.0/ref/contrib/admin/)
* Django URLs

- [ ] DERS 38. <br>
* Django Shell ORM
* Staticfiles (https://docs.djangoproject.com/en/4.0/howto/static-files/)
* HTML & CSS Cheatsheet
