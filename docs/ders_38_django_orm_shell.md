# Ders 38 qeydler
### Bu basliqda Django Shell vasitesi ile ORM addimlari qeyd olunacaq

1. Terminal ekraninda proyektin oldugu qovluq altinda asagidaki command yazilir:
    * python manage.py shell
2. Acilan interaktiv ekranda django kodlarimizi rahatca yazabilirik. 
   * Ilk olaraq django'nun hazir User modelini istifade edek:
      * from django.contrib.auth.models import User
   * Ikinci olaraq bizim oz yaratdigimiz Article modelini cagiraq:
      * from article.models import Article
3. Artiq bu iki classdan yeni numuneler yaradabilerik.
   * Ilk olaraq User classindan bir numune yaradaq:
      * new_user_1 = User(username="test_user_1", password="user_pass_123")
   * new_user_1 adinda bir user yaratdiq amma bunu database'e daxil etmedik. Bunun ucun:
      * new_user_1.save()
   * Artiq yeni user database'e daxil edildi. Gormek ucun admin panelde Users hissesine kecid edin
   * Database'e baxdiginiz zaman passwordun encode edilmediyini goreceksiniz.
      * new_user_2 = User(username="test_user_2")
      * new_user_2.set_password("user_pass_123")
   * Tekrardan database'e baxdiginiz zaman test_user_2 ucun parolun encode edildiyini goreceksiniz.
   * Constructor istifade etmeden de User yaratmaq mumkundur:
      * new_user_3 = User()
      * new_user_3.username = "test_user_3"
      * new_user_3.set_password("user_pass_123")
      * new_user_3.first_name = "User3"
      * new_user_3.save()

   * Ikinci addim olaraq Article classindan numuneler yaradaq:
      * article_1 = Article(title="Django Title", content="mezmun django", author=new_user_3)
      * article_1.save()
   * Yarattigimiz yeni Article numunesini django admin panelde gorebilerik.
   * Constructor istifade etmeden de User yaratmaq mumkundur. Bunu User yarattigimiz kimi edebilerik.
   * Shell hissesinden basqa bir method ile de numune yaratmagi yoxlayaq.
      * article_2 = Article.objects.create(title="Django Title objects", content="mezmun django objects", author=new_user_3)
      * article_2.save()
   * article_2 numunemizi database'e qeyd ettik. Bu numuneni istifade ederek Update emeliyyatini etmek de mumkundur.
      * article_2.title = "Django title deyisdirildi"
      * article_2.save()
   * Article Table icindeki butun article'lari getirtmek de mumkundur. Bu Select emeliyyatina beraberdir.
      * Article.objects.all()
   * Artiq terminal ekraninda Article table altindaki butun article'lari gorebilirik.
   * Spesifik Article numunesini database'den getirtmek istesek nece? Meselen bizim istediyimiz title'a gore bir Article gelsin:
      * article_3 = Article.objects.get(title="Django title deyisdirildi")
   * Artiq biz spesifik bir article numunesini getirebildik.
   * Delete emeliyyatini etmek ucun ise:
      * article_3.delete()
   * Tekrar database'i yoxladiginiz zaman artiq title'i "Django title deyisdirildi" olan article gosterilmeyecek.
   * Spesifik Select emeliyyatini id'e gore de edebilersiniz.
   * Xususi bir emeliyyat olan Filter emeliyyati da islerimizi olduqca asanlasdiracaq. Meselen title'inda "ango" sozu kecen butun record'lari(article'lari) getir.
      * Article.objects.filter(title__contains= "ango")
   * title__contains hissesinin qosa alttire(__) ile yazilmagi Djangoda xususi syntaxlardan biridir. Alttirenin solunda filter'dan kecirmek istediyiniz sutunu, saginda ise contains yazilir. Meselen:
      * Article.objects.filter(content__contains= "ango")

##### Bu movzuya dair daha cox melumat ucun
* https://docs.djangoproject.com/en/4.0/topics/db/queries/