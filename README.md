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

- [x] DERS 38. <br>
* Django Shell ORM
* HTML Cheatsheet

- [x] DERS 39. <br>
* Staticfiles (https://docs.djangoproject.com/en/4.0/howto/static-files/)
* Template Inheritance (https://levelup.gitconnected.com/django-template-inheritance-and-reusability-e97b0fed8bcc)
* Bootstrap (https://getbootstrap.com/)
* Navbar
* Haqqimizda sehifesi
* Context, Template-Views elaqesi

- [x] DERS 40. <br>
* App URL ve Include mentiqi
* User App yaratmaq
* Form Class'larinin istifadesi
* Yeni User Qeydiyyati 

- [x] DERS 41. <br>
* Django mesajlari (https://docs.djangoproject.com/en/4.0/ref/contrib/messages/)
* Sayta Login olmaq 
* Crispy Formlar (https://django-crispy-forms.readthedocs.io/en/latest/)
* Saytadan Logout olmaq
* User sessiyasinin kontrolu
* Dashboard sehifesinin yaradilmasi
* Article ucun ModelForm yaradilmasi (https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/)
* Article'lari database'e yazmaq
* commit=False problemi

- [x] DERS 42. <br>
* Article'lari dashboard'da gostermek
* bootstrap tablelar
* Article Silmek ve Redakte etmek ucun views ve urls
* Article Silmek funksiyasinin islemesi
* Article Detail sehifesi
* Bootstrap Post Detail sehifesi (https://github.com/StartBootstrap/startbootstrap-blog-post/blob/master/dist/index.html)
* get_object_or_404
* Boostrap fayllarini static hala getirmek 
* CSS/JS (https://getbootstrap.com/docs/4.0/getting-started/download/)
* Jquery (https://code.jquery.com/jquery-3.6.0.min.js)
* collectstatic (https://docs.djangoproject.com/en/4.0/howto/static-files/)
* ckeditor (https://github.com/django-ckeditor/django-ckeditor)

- [x] DERS 43. <br>
* File Upload in Django
* Article Redakte etmek funksiyasinin islemesi
* delete funksiyasini get_object_or_404 ile duzeltmek
* login_required
* Article sehifesinde dizayn isleri
* Django template filters (https://docs.djangoproject.com/en/4.0/ref/templates/builtins/)
* Search funksiyanalligi
* Dynamic urls

- [x] DERS 44. + yarim ders <br>
* Comment Modeli ve Comment formu(html)
* Article'lara comment elave etmek
* reverse funksiyasi
* Article'larin commentlerini gostermek
* Comment ve Article'lari tarixe gore siralamaq (https://docs.djangoproject.com/en/4.0/ref/models/options/)
* TODO Project yaratmaq sifirdan ve onun uzerinde islemek

- [x] DERS 45. <br>
* TODO Project yaratmaq sifirdan ve onun uzerinde islemek (davami)
