>16-noyabr

Backend python Framework:
Rest API:

- API lar json farmatida ma'lumot almashadi;
- Rest API dan foydalanish uchun, avval buni o'rnatib olish kerak;
- Swagger: Bu sayt API dan foydalanish haqida ba'zi malumotlarni taqdim etadi;
- __schema_view__ bu tizimni nomi, versiyasi, emaili va boshqa ma'lumotlar bilan ishlaydi, Ushbu parameter configning urls qismida yoziladi;
- urls dagi sozlamalarni berib qo'yish orqali, ishni osonlashtirish mumkin. Agar yozilmasa FrontEnd dasturchiga tushunturish berib o'tib ketishga to'g'ri keladi;
- Asosiysi urls PI dagi sozlamalar yozib qo'yilsa bo'ldi. Shunda tushunarli dastur bo'lishiga xizmat qiladi;
- __api-auth/__ ushbu buyruq orqali yo'lni, o'rnatilgan rest_framework imizdagi __urls__ ga yo'naltirishimiz mumkin bo'ladi;
- __drf_yasg__ - Installed appsga qo'shiladigan app;
- __schema_view__ bilan saytga kirgan vaqtda ma'lumot beradi, Agar urlsga yozib qo'yilsa;
- Books-> list_view, detail_view, search
- Urls ga api yozayotganda uni versiyasini ham yozib ketish ma'qul, Agar u bitta versiyada ishlamasa. Bo'lmasa yozish shart emas;
- API da ma'lumotlarni chiqarish uchun, uning parameterlarini __models__ da yoziladi(class sifatida);
- Misol uchun Model: Books-> book_title, book_author, book_price, book_desc;
- __Meta class__ ushbu class model ichidan yoziladi. Agar ma'lumotlar berilmasa nom berish uchun qat'iy yo'riqnoma o'rnatiladi;
- __Pillow__ modeli rasmlar bilan ishlash va url bilan ochish uchun qo'llaniladigan package;
- Admin da model qo'shish uchun, models da class yozish kerak;
- from __rest_framework.serializer__ import ModelSerializer;
- from __rest_framework.generic__ import ListAPIView;
- DEFAULT_PERGINATION_
- serializer fayli yaratiladi. Ushbu fayl ModelSerializerni yaratishga xzmat qiladi. Unda Meta class da model va field attributlari bo'ladi;
- __ModelSerializer__ modeldan kelgan ma'lumotlarni json formatga o'girib olish uchun qo'llaniladi;
- ?name=book -> queryparam;
- Dasturda search qismini yozish uchun app dagi views dan foydalanishimiz mumkin. Unda get_queryset funksiyasi yoziladi;
- get_querysetda __if 'book' in self.request.GET__ degani queryparam 'book' dan so'ng yozilgan ma'lumot bormi yoki yo'q degan so'rovga javob bo'ladi. Bu usul True yoki False qaytaradi;
- Agar yuqoridagi usul True qaytarsa __key_word = self.request.GET['book']__ yozish orqali o'zimizga kerakli so'rovni natijasini qabul qilib olishimiz mumkin bo'ladi;
- pk -> primary key;
- BookDetailAPIView class si bitta primary key oladi. 

---
To'liq tushuntirish fayllar:
-
- Settings ga yozildi;
- config/urls ga yozildi;
- app_books/urls ga yozildi;
- app_books/model ga yozildi;
- app_books/admin ga ro'yxaga olindi;
- # Keyin modelga admin sayt orqali modellar yoziladi;
- app_market/serializer.py fayli yoziladi -new
- app_market/views yoziladi;

# Jami 7 ta faylga yozildi;

- ## Import qilingan modullar:
- rest_framework;
- drf_yasg.