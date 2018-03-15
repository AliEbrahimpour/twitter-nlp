<div dir=rtl>
این مخزن کد برای تمرینات درس بازیابی اطلاعات - [دانشگاه بزرگمهر قائنات](http://buqaen.ac.ir) در نظر گرفته شده است.
# تمرین اول
هدف از این تمرین، اشنایی اولیه با مفاهیم پایه **پردازش زبان طبیعی در زبان فارسی با استفاده از داده های توئیتر** است. 
برای خواندن توئیت از کتابخانه
```
tweepy
```
استفاده شده است و مشخصات اتصال به توئیتر در فایل 
```
twitter_config.py
```
قرار گرفته است که در صورت نیاز به کار کردن با اکانت شخصی خودتان، می توانید با مراجعه به سایت [توئیتر](https://apps.twitter.com)، یک App جدید ساخته، مشخصات اتصال آنرا در این فایل وارد کنید.
با توجه به فیلتر بودن سایت توئیتر برای انجام این تمرین از نرم افزارهایی مانند [سایفون](https://s3.amazonaws.com/0ubz-2q11-gi9y/fa.html#rtl) استفاده کنید و دقت کنیدکه گزینه Use VPN Mode را در تنظیمات این نرم افزار تیک بزنید تا تمام ترافیک ویندوز از جمله ترافیک مورد نیاز برای اتصال به توئیتر هنگام اجرای برنامه ها از طریق این نرم افزار صورت بگیرد.
## قبل از شروع
دقت کنید که پای چارم و نسخه 3 پایتون روی سیستم شما نصب باشد.
پروژه جاری را ابتدا فورک نمایید تا به اکانت شما در گیت هاب منتقل شود. سپس، آنرا دانلود و یا به کمک گیت، Clone نمایید تا به سیستم شما منتقل گردد. سایفون را اجرا و تنظیمات آنرا انجام دهید. 

## گام صفر
در این گام، تنها به اجرای برنامه و مشاهده توئیت ها و اطلاعات مختلفی که هنگام دریافت یک توئیت به دست ما می رسد، می پردازیم. 
فایل 
```
twitter-step-0.py
```
 را باز کرده، محتویات آنرا بررسی کنید. 
در این فایل، کلاسی داریم با نام
 ```
 TweetListener
 ```
  که از کلاس
   ```
   StreamListener
   ```
   
    ارث بری دارد . کلاس
    ```
    StreamListener
    ```
     برای خواندن جریانی (خواندن مداوم جریان داده های توئیتر) استفاده می شود که متد 
     ```
     on_data
     ```
      آن، هنگام دریافت هر توئیت که با پارامتر دیتا که به آن ارسال می شود،فراخوانی می شود و بنابراین پردازش های خود را در این متد انجام می دهیم. 
با دستور 
```
 json.loads(data)
 ```
 رشته دریافت شده را به جی سان تبدیل نموده و برای تبدیل یک دیکشنری (جی سان) به یک رشته برای ذخیره در فایل از 
 ```
 json.dumps(data)
 ```
  استفاده خواهیم کرد.
برخی از اطلاعات
 ```
 json_data 
 ```
 که همان توئیت دریافت شده است را چاپ کرده ایم . مهم ترین این اطلاعات، متن توئیت یا
  ```
  json_data["text"] 
  ```
   است. 
در انتهای فایل با دو دستور زیر : 

```
twitter_stream = Stream(auth, TweetListener()) 
twitter_stream.filter(languages=['fa'], track=['با' , 'از','به','در'])
```

شروع به پردازش جریانی از توئیت های فارسی که در آنها کلمات **با، از ، به ، در** به کار رفته است، خواهیم کرد. یعنی به ازای بخشی از توئیت های فارسی که در آنها این کلمات به کار رفته است ( نه همه آنها)،توئیتها را دریافت خواهیم کرد و با متد
```
on_data
```
به پردازش آنها خواهیم پرداخت.
**نکته** : اگر کل توئیت دریافتی را پرینت کنید یعنی دستور
    ```
    print(data)
    ```
     حروف فارسی به صورت کدشده (با علامت یوی انگلیسی که کد یونیکد هر حرف است) خواهید دید اما اگر هر بخش از اطلاعات را به صورت جداگانه پرینت کنید، آنها را فارسی خواهید دید. 
     
## گام اول
در این مرحله، هر توئیت دریافتی را در پوشه
 tweets‌
 txt‌
  ذخیره خواهیم کرد. برای اینکه مدیریت این فایلها راحت تر باشد، آنها را در پوشه ای به تاریخ روز دریافت شدن توئیت، ذخیره کرده ایم. 
فایل 
```
twitter-step-1.py
```
   را اجرا کنید تا این فایلهای متنی ساخته شوند. حدود هزار عدد توئیت را حتما ذخیره کنید.
توضیح اینکه با کتابخانه 
```
pathlib
```
 پوشه های لازم برای ذخیره توئیت ها را می سازیم و
  ```
  codecs.open
  ```
   فایل مربوط به ذخیره هر توئیت را به صورت یونیکد ایجاد کرده و متن توئیت را در آن ذخیره می کنیم. 

## گام دوم 
در این مرحله، به حذف علائم نگارشی ، آدرسهای ایمیل ، آدرسهای اشخاص و مانند آن می پردازیم.
با دستورات : 
```
for dirpath, dirs, files in os.walk('tweets'):    
           for filename in fnmatch.filter(files, '*.txt'):        
                  with codecs.open(os.path.join(dirpath, filename),'r',encoding="utf-8")as f:

```
تمام فایلهای موجود در تمام پوشه های قرار گرفته در آدرس 
```
tweets
```
را باز کرده و مرحله به مرحله پردازش می کنیم. 
برای حذف یک الگوی خاص از کتابخانه معروف 
```
re
```
که مخفف عبارات با قاعده است استفاده کرده ایم. مثلا در کد زیر : 

```
tweet= re.sub(r'@[A-Za-z0-9_]+', '',tweet)

```
 ابتدا الگو  را مشخص کرده ایم : تمام کلماتی که با 
 @ 
 شروع شوند و بعد از آنها یکی از حروف الفبا یا اعداد یا آندرلاین به تعداد یک یا بیشتر به کار رود را با رشته خالی درون متغیر 

```
 tweet 
```

 جایگزین کرده ایم و نتیجه را هم در همین متغیر ذخیره نموده ایم.
 ضمنا با دستور : 

```
 tweet = " ".join(tweet.split())
```

 برای اینکه تمام متن یک توئیت را در یک خط ذخیره کنیم، ابتدا آنها را اسپلیت کرده و سپس با دستور جوین به یکدیگر چسبانده ایم. کاراکتر ابتدای این دستور و قبل از دستور جوین، مشخص کننده کاراکتری است که بین عناصر لیست قرار خواهد گرفت. 
 پوشه ای با نام 
 ```
 step2
 ```
 درون پوشه 
 ```
 nlp
 ```
 ایجاد کرده ایم و خروجی این مرحله که پاکسازی اولیه متن توئیت هاست درون این پوشه ذخیره خواهد شد.
**نکته مهم** : 
تمام خروجی های مراحل بعدی تمرین، مشابه با این مرحله درون پوشه ای به صورت مجزا قرار خواهد گرفت تا عملیات قابل پیگری به صورت مرحله به مرحله باشد. 
 
## گام سوم
اولین تمرین ، گام سوم این فرآیند است که هدف آن، شمارش تمامی کلمات موجود در تمامی توئیت ها و ***ذخیره آنها در یک فایل*** در پوشه 
```
step3
```
به صورت مرتب شده است. خروجی این مرحله فایلی با ساختار زیر خواهد بود : 
```
و : 396
از : 143
به : 128
....
```
یعنی از پرتکرارترین کلمه به کم تکرارترین کلمه .
برای این منظور می توانید از کد زیر استفاده کنید :‌
```
file=open("D:\\zzzz\\names2.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print k,v
file.close();
```

## گام چهارم 
در این مرحله ، می خواهیم کلمات پرتکرار یا 
```
stop words
```
یا ایست واژه ها را حذف کنیم. 
فایل خروجی مرحله 
