from rubpy import Message, Client, handlers, models, methods
from asyncio import run, sleep
import random
from datetime import datetime
print("**********Welcome to the robot**********")
print("**********The robot is active**********")
my_group = "g0DYTT805d6479b06dbb98445eca94d9"

my_filters = ("@", "join", "rubika.ir")
group_admins = []

silence_list = []
no_gifs = False
warning_users = []
warns_del = 3
channe_id = "..."
my_insults = (
    "کیر",
    "کص",
    "کون",
    "کس ننت",
    "کوس",
    "کوص",
    "ممه",
    "ننت",
    "بی ناموس",
    "بیناموس",
    "بیناموص",
    "بی ناموص",
    "گایید",
    "جنده",
    "جندع",
    "جیندا",
    "پستون",
    "کسکش",
    "ننه کس",
    "اوبی",
    "هرزه",
    "قحبه",
    "عنتر",
    "فاک",
    "کسعمت",
    "کصخل",
    "کسخل",
    "تخمی",
    "سکس",
    "صکص",
    "کسخول",
    "کسشر",
    "کسشعر",
)

texts_jok = [
 " الیسا و ملیسا، رفتن برن کلیسا تو راهروی کلیسا، گیر کرد به سقف کلیپسا",
 "ولی دختر بودنم سخته ها فک کن عکس خودت به اون خوشگلیو بدی عکس یه پسرو بگیری",
"نوک مداد قرمزای سوسمارنشان رو که زبون می زدی خوش رنگ تر می شد",
"طرف بعد امتحان همچین میاد بیرون سیگار می کشه که انگار شرکتش ورشکست شده",
"زن: مرد چرا کولر نمی خری ؟ به درد نمی خوره اونایی هم که دارن گذاشتن رو پشت بوم",
"یه سیب زمینی شوهرش میمیره بند نمیندازه میشه کیوی",
"چوپان دروغگو میمیره توی قبر ازش میپرسن اسمت چیه میگه دهقان فداکار",
"غضنفر می ره عروسی ‌‌‌؛ تو عروسی برف شادی می زنن ؛ سرما می خوره!!",
"غضنفر با کلید گوشش رو تمیز می کرده؛ گردنش قفل می کنه!!",
"به غضنفر می گن: شنیدم آدم شدی؟ می گه: نامردا شایعه کردن!!",
"تو امتحان دنبال این نیستن که چقد حالیته دنبال اینن که چی بلند نیستی",
"اگه تو مدرسه یه درس برامون می ذاشتن با عنوان آموزش تقلب هیچ وقت تقلب یاد نمی گرفتیم",
"بعضیا تیپ شون یه جوریه که آدم نمی دونه دارن مسخره بازی درمیارن یا واقعا مد روزه!",
"اونی که داداش نداره مثل کسیه که بدون سلاح به جنگ میره",
"یعنی درک و شعوری که استامینوفن واسه تسکین درد آدم داره؛ بعضی از آدما ندارن",
"دوست داشتن کسی که دوستت نداره مثل اینه که توی فرودگاه منتظر کشتی باشی!",
"من چاق نیستم، فقط استخوان بندی شکمم درشته",
"غضنفر میمیره، عکسشو نداشتند بذارن رو قبرش، تا گردن دفنش می‌کنند",
"چنتا پست شکست عشقی دارم رو دستم باد کرده. یکی بیاد با من ازدواج کنه بعد ولم کنه تا من اینارو بذارم",
"بعدها به بچه هام می گم شما یادتون نمیاد… یه زمانی خوشگلی خدادادی بود",
"قدر کسی یا چیزی که دارین رو بدونین، قبل از اینکه بقیه قدرشونو بدونن",
"پدر: پسرم هروقت من رو اذیت می کنی یکی از موهای سرم سفید می شه. پسر: پس برای همین بابا بزرگ تمام موهاش سفید شده؟!",
"اطلاعات من در مورد بازار بورس در این حده که سبزا بهتر از قرمزان -__",
"هم عاشقتم هم ازت متنفرم، میانگین که بگیری می‌بینی برام مهم نیستی",
"دادم هارد لپ تاپمو ریکاوری کردن‌ الان یه هفتس زنگ می‌زنن می‌گن بیا ببرش، اما روم نمیشه برم…",
"شمام مامانتون از در میاد توو، هنو منتظرید از توو کیفش بهتون خوراکی بده ؟ یا من برم یه 10 سال بزرگتر شم بعد بیام",
"‏این که نزدیک 30 سال سن داشته باشی و اجازه نداشته باشی برای خودت خونه مستقل بگیری تلخ ترین شوخی ای بود که فرهنگ ایرانی با ما کرد",
"پاييز واسه همه خاطرات عاشقانه است واسه ما معموليا همينكه مگس و پشه ها كم ميشن جای خوشحالی داره !",
"سوار ماشین شدم راننده از دست مسافر قبلی شاکی بود گفت: لعنت به این شغل که ما باید هر الاغ بیشعوری رو سوار کنیم",
"‏ما بچه بودیم کتک میخوردیم بعدش تازه باید میرفتیم از ننه بابامون عذرخواهی میکردیم که ببخشید عصبانیت کردم که تو پاشدی منو زدی 😐",
"‏رفتم اداره خون که خون اهدا کنم یارو گفت شما باید بری اداره دخانیات که نیکوتین اهدا کن",
"ﺩﻗﺖ ﮐﺮﺩﯾﻦ ﺍُﺩﮐﻠﻦ 200 ﻫﺰﺍﺭ ﺗﻮﻣﻨﯽ ﻣﯿﺰﻧﯽ 3 ﺳﺎﻋﺘﻢ ﺑﻮﺵ ﻧﻤﯿﻤﻮﻧﻪ ! ﺑﻌﺪ ﯾﻪ ﺳﯿﮕﺎﺭ 200 ﺗﻮﻣﻨﯽ ﻣﯿﮑﺸﯽ ﺗﺎ 3 ﺭﻭﺯ ﺑﻮﺵ ﻣﯿﻤﻮﻧﻪ !",
"‏دوست سلنا گومز بهش یه کلیه اهدا کرد و دوست مگان مرکل به شاهزاده هری معرفیش کرد، اونوقت رفقای ما بهمون زنگ میزنن یا قرض میخوان یا نتورک مارکتینگ میکنن",
"بابام به مامانم اس ام اس عاشقانه فرستاده، الان 2 روزه خونمون دعواست، مامانم گیر داده به بابام که این اس ام اس و کی واست فرستاده بوود",
"سالها گذشت و ما نفهمیدیم وقتی تو دستشویی هستیم کسی در میزنه باید چی جوابش بدیم؛ اینجایم، اینجا پره، من تو هستم, کار دارم، هنوز تموم نشده",
"‏فامیلای ما وقتی میان مهمونی انقدر می‌مونن که اگه خدایی نکرده تو اون مدت پدر خانواده فوت کنه اندازه بقیه تو ارث و اینا سهم دارن",
]

texts_chat5 = [
"شرکت کوکا کولا روزانه بیش از 1 میلیارد از محصولات خود را به فروش می رساند",
"اسب های دریایی تنها حیواناتی هستند که در آن ها جنس نر باردار می شود.",
"روش استفاده ی صحیح از سنجاق سر به این صورت است که قسمت شیاردار را برای نگه داشتن موها استفاده می کنند، با این روش دیگر سنجاق سر در موهای شما گیر نمی کند",
"کلاه ایمنی فضانوردان دستگاه های خاصی برای خاراندن بینی دارد",
"یونانیان باستان معتقد بودند که زندگی یک فرد در کبد متمرکز است و نه در قلب.",
"آتش هیچ سایه ای ندارد زیرا آتش خودش منبع نور است و هنگامی که پرتو نور تولید شده از آتش مسدود می شود، سایه ها ظاهر می شوند",
"قلب میگو در سرش قرار گرفته است",
"تمساح نمی تواند زبانش را از دهانش بیرون بیاورد.",
"موش ها و اسب ها هرگز نمی توانند استفراغ کنند",
"لئوناردو داوینچی قیچی را اختراع کرده است.",
"چشم های شتر مرغ بزرگتر از مغز اوست",
"ستاره دریایی مغز ندارد",
"خرس های قطبی چپ دست هستند.",
"اگر بخواهید از کره شمالی به فنلاند بروید فقط باید از یک کشور عبور کنید؛ کشور روسیه"
"قطب جنوب بزرگترین بیابان کره ی زمین است",
" پنج گونه مار در سراسر جهان وجود دارد که می توانند پرواز کنند",
" اثر زبان شما مانند اثر انگشتان شما منحصر به فرد است.",
"با یک مداد می توانید خطی به طول 61 کیلومتر بکشید.",
"حلزون های بی صدف 4 بینی دارند!",
"فیل ها تنها حیواناتی هستند که نمی توانند بپرند.",
"برای حیوانی به نام تنبل 2 هفته طول خواهد کشید تا بتواند غذای خود را هضم کند!",
"تقریبا 3 درصد از یخ های قطب جنوب ادرار پنگوئن ها می باشد",
"خفاش ها همیشه از سمت چپ غار خارج می شوند.",
"زرافه ها تارهای صوتی ندارند",
"حس چشایی پروانه ها در پاهای شان می باشد",
" نزدیک به 150 نفر در سال بر اثر افتادن نارگیل بر روی سرشان جان خود را از دست می دهند",
"چشم های شترمرغ از مغزش بزرگتر است",
"حلزون مي‌تواند 3 سال بخوابد.",
"به طور ميانگين مردم از عنكبوت بيشتر مي‌ترسند تا از مرگ!",
"ملت آمريكا بطور ميانگين روزانه 73000 متر مربع پيتزا مي‌خورند",
"سوسکها سریعترین جانوران ۶ پا می باشند با سرعت یک متردرثانیه.",
"خرگوشها و طوطی ها بدون نیازبه چرخاندن سرخود قادرند پشت سرخود را ببینند.",
"سگهای شهری بطورمتوسط ۳ سال بیشتر از سگهای روستائی عمرمی کنند.",
"درامریکا سالانه ۱۵نفر بر اثر گازگرفتگی توسط سگها جان خود را از دست می دهند.",
"مادروهمسرگراهام بل مخترع تلفن هر دو ناشنوا بودند",
"۱۰ % وزن بدن انسان (بدون آب ) را باکتریها تشکیل می دهند.",
"۱۱% جمعیت جهان را چپ دستان تشکیل می دهند",
" از هر ۱۰ نفر یک نفر در سراسر جهان در جزیره زندگی می کند",
"۹۸ % وزن آب از اکسیژن تشکیل یافته است.",
]

texts_chat10 = [
    "خوش اومدی عشقمون",
    "کاشکی نمیومدی",
    "ای جان",
    "خوب شد تاومدی",
]

texts_chat9 = [
    "مراقبت کن خدافظ",
    "بای عزیزم",
    "میموندی خوش میگذشت",
    "منم با خودت ببر",
    "نرو سمیه",
    "سیک",
    "گپ بدون تو حال نمیده",
]

texts_chat8 = [
    "توت باشه بخندی",
    "فدای خنده هات بشم",
    "تو فقط بخند",
    "ای جان عشقم خندید",
]

texts_chat7 = [
    "دسته تبر",
    "خبری نیس خبرا پیشه توعه",
    "سلامتیت دلبر",
    "به تو مربوط نیس",
]

texts_chat6 = [
    "خداروشکر",
    "شکر",
    "همیشه خوب باشی عزیزم",
    "ای جان",
    "افرین دلبرم خوب باش",
]

texts_chat4 = [
    "جانم نفسم",
    "بنال",
    "بله قربان",
    "انقدر خایمالی نکن",
    "میخای بکنمت انقدر صدا میکنی",
    "جون",
    "بمیر انقدر صدا نکن",
    "میخوام بخوابم",
]

texts_chat1 = [

      "خوبم تو خوبی",
         "مرسی ",
     "به تو مربوط نیست",

]


texts_chat = [
    "سلام",
    "های بیبی",
    "خوبی",
    "صلوم",
    "چطوری جیندا",
    "ای جان ببین چه کسی اومد",
]

texts_chat3 = [
    "کص ننت",
    "مادر جنده چرا فحش میده باید کونت بزارم",
    "کونت گزاشتن فحش میدی",
    "هی کونکش فحش نده",
    "دفعه بعدی فحش بدی ریم میشی",
]

texts_bot = [
   "کیر خر اسم من ربات نیس من فرا رباتم",
   "اسم من تایگر بگو تایگر دهنت عادت کنه",
   "نگو ربات کیونی",
]
texts_chat2 = [
    "بخوبیت عزیزم",
    "فداتشم",
    "تو خوب باشی منم خوبم",
    "نه خوب نیستم",
    "نمیدونم",
    "به تو مربوط نیست",

]



def getAds(string: str) -> bool:
    string = string.lower()
    for filter in my_filters:
        if filter in string:
            return True
        else:
            continue
    return False


def getInsults(string: str) -> bool:
    for filter in my_insults:
        if filter in string:
            return True
        else:
            continue
    return False


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Robot start time =", current_time)

async def deleteMessage(client: Client, message_ids: str):
    await sleep(5)
    await client.delete_messages(my_group, message_ids)


async def updateAdmins(client: Client) -> None:
    global group_admins
    results = await client(methods.groups.GetGroupAdminMembers(my_group))
    results = results.to_dict().get("in_chat_members")
    for result in results:
        GUID = result.get("member_guid")
        if not GUID in group_admins:
            group_admins.append(GUID)
        else:
            continue


async def get_user_name(client: Client, guid: str):
    user_info = await client.get_user_info(guid)
    return user_info.user.first_name


async def warn_user(client: Client, guid: str):
    num_warns = 0
    for warn in warning_users:
        if warn == guid:
            num_warns += 1
    name_user = await get_user_name(client, guid)
    if num_warns < warns_del:
        message_id = await client.send_message(
            my_group,
            f"👤 کاربر [{name_user}]({guid}) شما یک اخطار دریافت کردید\n\n- تعداد اخطار : {num_warns} از {warns_del} میباشد \n\n⚠️ مواظب باشید اخراج نشید",
        )
    elif num_warns >= warns_del:
        message_id = await client.send_message(
            my_group,
            f"👤 کاربر [{name_user}]({guid}) شما یک اخطار دریافت کردید\n\n- تعداد اخطار : {num_warns} از {warns_del} میباشد \n\n⚠️ شما حذف خواهید شد",
        )
        await client.ban_group_member(my_group, guid)
    await deleteMessage(client, [message_id.message_update.message_id])


async def get_guid_by_message_id(client: Client, mesage_id: str):
    messages = await client.get_messages_by_ID(my_group, [mesage_id])
    return messages.messages[0].author_object_guid


async def unwarnUser(guid: str):
    for guid_user in warning_users:
        if guid_user == guid:
            warning_users.remove(guid_user)


async def start_bot(client: Client):
    await updateAdmins(client)
    name_gap = await client.get_group_info(my_group)
    name_gap = name_gap.group.group_title
    await client.send_message(my_group, f" تایگر[{name_gap} ] با موفقیت فعال شد🌸")

async def main():
    async with Client(session="bot") as client:
        await start_bot(client)

        @client.on(handlers.MessageUpdates(models.is_group()))
        async def updates(update: Message):
            if update.object_guid == my_group:
                if (
                    not update.author_guid in group_admins
                    and "forwarded_from" in update.to_dict().get("message").keys()
                ):
                    guid = await get_guid_by_message_id(client, update.message_id)
                    await update.delete_messages()
                    warning_users.append(guid)
                    await warn_user(
                        client,
                        guid,
                    )

                if update.raw_text != None:
                    if not update.author_guid in group_admins and getAds(
                        update.raw_text
                    ):
                        guid = await get_guid_by_message_id(client, update.message_id)
                        await update.delete_messages()
                        warning_users.append(guid)
                        await warn_user(
                            client,
                            guid,
                        )

                    elif update.raw_text == "من اومدم"or update.raw_text == "عشقتون اومد":
                        await update.reply(
                            texts_chat10[random.randint(0, len(texts_chat10))]
                        )
                    elif update.raw_text == "من برم"or update.raw_text == "خدافظ" or update.raw_text == "بای":
                        await update.reply(
                            texts_chat9[random.randint(0, len(texts_chat9))]
                        )

                    elif update.raw_text == "😂"or update.raw_text == "😂😂😂" or update.raw_text == "😂😂":
                        await update.reply(
                            texts_chat8[random.randint(0, len(texts_chat8))]
                        )

                    elif update.raw_text == "چه خبر" or update.raw_text == "نخبر":
                        await update.reply(
                            texts_chat7[random.randint(0, len(texts_chat7))]
                        )
                    elif update.raw_text == "خوبم" or update.raw_text == "فداتشم":
                        await update.reply(
                            texts_chat6[random.randint(0, len(texts_chat6))]
                        )

                    elif update.raw_text == "دانستنی" or update.raw_text == "دانستنی":
                        await update.reply(
                            texts_chat5[random.randint(0, len(texts_chat5))]
                        )

                    elif update.raw_text == "تایگر" or update.raw_text == "تایگر":
                        await update.reply(
                            texts_chat4[random.randint(0, len(texts_chat4))]
                        )

                    elif update.raw_text == "کص ننت" or update.raw_text == "کص عمت":
                        await update.reply(
                            texts_chat3[random.randint(0, len(texts_chat3))]
                        )
                    elif update.raw_text == "خوبم تو جطوری" or update.raw_text == "عالم تو خوبی":
                          await update.reply(
                            texts_chat2[random.randint(0, len(texts_chat2))]
                        )

                    elif update.raw_text == "جوک" or update.raw_text == "جوک":
                        await update.reply(
                            texts_jok[random.randint(0, len(texts_jok))]
                        )

                    elif update.raw_text == "خوبی" or update.raw_text == "چطوری":
                        await update.reply(
                            texts_chat1[random.randint(0, len(texts_chat1))]
                        )

                    elif update.raw_text == "سلام" or update.raw_text == "صلوم":
                        await update.reply(
                            texts_chat[random.randint(0, len(texts_chat))]
                        )

                    elif update.raw_text == "ربات" or update.raw_text == "bot":
                        await update.reply(
                            texts_bot[random.randint(0, len(texts_bot))]
                        )

                    elif getInsults(update.raw_text):
                        message_id = await update.reply("یک پیام مستهجن حذف شد")
                        await update.delete_messages()
                        await deleteMessage(
                            client, [message_id.message_update.message_id]
                        )

                    elif (
                        update.author_guid in group_admins
                        and update.raw_text == "!open"
                    ):
                        result = await client(
                            methods.groups.SetGroupDefaultAccess(
                                my_group, ["SendMessages"]
                            )
                        )
                        message_id = await update.reply("گروه باز شد.")
                        await deleteMessage(
                            client,
                            [update.message_id, message_id.message_update.message_id],
                        )

                    elif (
                        update.author_guid in group_admins
                        and update.raw_text == "!close"
                    ):
                        result = await client(
                            methods.groups.SetGroupDefaultAccess(my_group, [])
                        )
                        message_id = await update.reply("گروه بسته شد.")
                        await deleteMessage(
                            client,
                            [update.message_id, message_id.message_update.message_id],
                        )

                    elif (
                        update.author_guid in group_admins
                        and update.raw_text == "!warn"
                        and update.reply_message_id != None
                    ):
                        guid = await get_guid_by_message_id(
                            client, update.reply_message_id
                        )
                        if not guid in group_admins:
                            warning_users.append(guid)
                            await warn_user(
                                client,
                                guid,
                            )
                            await deleteMessage(client, [update.message_id])
                        else:
                            message_id = await reply("کاربر ادمین میباشد")
                            await deleteMessage(
                                client,
                                [
                                    update.message_id,
                                    message_id.message_update.message_id,
                                ],
                            )

                    elif update.author_guid in group_admins and update.text.startswith(
                        "!unwarn @"
                    ):
                        username = update.text.split("@")[-1]
                        user_info = await client.get_object_by_username(username)
                        user_info = user_info.user.user_guid
                        if not user_info in group_admins:
                            if user_info in warning_users:
                                await unwarnUser(user_info)
                                name_user = await get_user_name(client, user_info)
                                message_id = await client.send_message(
                                    my_group,
                                    f"کاربر [{name_user}]({user_info}) اخطار های شما پاک شدند",
                                )
                            else:
                                message_id = await update.reply(
                                    "کاربر اخطاری ندارد که پاک شود"
                                )
                        else:
                            message_id = await update.reply(
                                "کاربر در گروه ادمین میباشد"
                            )
                        await deleteMessage(
                            client,
                            [update.message_id, message_id.message_update.message_id],
                        )

                    elif (
                        update.author_guid in group_admins
                        and update.raw_text == "!look-gif"
                    ):
                        global no_gifs
                        no_gifs = True
                        message_id = await update.reply("گیف قفل شد.")
                        await deleteMessage(
                            client,
                            [update.message_id, message_id.message_update.message_id],
                        )

                    elif (
                        update.author_guid in group_admins
                        and update.raw_text == "!unlook-gif"
                    ):
                        no_gifs = False
                        message_id = await update.reply("قفل گیف رفع شد.")
                        await deleteMessage(
                            client,
                            [update.message_id, message_id.message_update.message_id],
                        )

                    elif (
                        update.author_guid in group_admins
                        and update.raw_text.startswith("!silent")
                    ):
                        if update.reply_message_id != None:
                            try:
                                result = await client(
                                    methods.messages.GetMessagesByID(
                                        my_group, [update.reply_message_id]
                                    )
                                )
                                result = result.to_dict().get("messages")[0]
                                if not result.get("author_object_guid") in group_admins:
                                    global silence_list
                                    silence_list.append(
                                        result.get("author_object_guid")
                                    )
                                    message_id = await update.reply(
                                        "کاربر مورد نظر در حالت سکوت قرار گرفت."
                                    )
                                else:
                                    message_id = await update.reply(
                                        "کاربر مورد نظر در گروه ادمین است."
                                    )
                                await deleteMessage(
                                    client,
                                    [
                                        update.message_id,
                                        message_id.message_update.message_id,
                                    ],
                                )
                            except IndexError:
                                message_id = await update.reply(
                                    "ظاهرا پیامی که روی آن ریپلای کرده اید پاک شده است."
                                )
                                await deleteMessage(
                                    client,
                                    [
                                        update.message_id,
                                        message_id.message_update.message_id,
                                    ],
                                )
                        elif update.text.startswith("!silent @"):
                            username = update.text.split("@")[-1]
                            if username != "":
                                result = await client(
                                    methods.extras.GetObjectByUsername(username.lower())
                                )
                                result = result.to_dict()
                                if result.get("exist"):
                                    if result.get("type") == "User":
                                        user_guid = result.get("user").get("user_guid")
                                        if not user_guid in group_admins:
                                            silence_list.append(user_guid)
                                            message_id = await update.reply(
                                                "کاربر مورد نظر در حالت سکوت قرار گرفت."
                                            )
                                        else:
                                            message_id = await update.reply(
                                                "کاربر مورد نظر در گروه ادمین است."
                                            )
                                    else:
                                        message_id = await update.reply(
                                            "کاربر مورد نظر کاربر عادی نیست."
                                        )
                                else:
                                    message_id = await update.reply(
                                        "آیدی مورد نظر اشتباه است."
                                    )
                            else:
                                message_id = await update.reply(
                                    "آیدی مورد نظر اشتباه است."
                                )
                            await deleteMessage(
                                client,
                                [
                                    update.message_id,
                                    message_id.message_update.message_id,
                                ],
                            )
                        else:
                            message_id = await update.reply(
                                "روی یک کاربر ریپلای بزنید."
                            )
                            await deleteMessage(
                                client,
                                [
                                    update.message_id,
                                    message_id.message_update.message_id,
                                ],
                            )

                    elif (
                        update.author_guid in group_admins
                        and update.raw_text.startswith("!clean-list-silent")
                    ):
                        if silence_list == []:
                            message_id = await update.reply("لیست سکوت خالی است.")
                        else:
                            silence_list = []
                            message_id = await update.reply("لیست سکوت خالی شد.")
                        await deleteMessage(
                            client,
                            [update.message_id, message_id.message_update.message_id],
                        )

                    elif update.raw_text == "!link":
                        result = await client(methods.groups.GetGroupLink(my_group))
                        result = result.to_dict().get("join_link")
                        message_id = await update.reply(f"لینک گروه:\n{result}")
                        await deleteMessage(
                            client,
                            [update.message_id, message_id.message_update.message_id],
                        )

                    elif (
                        update.author_guid in group_admins
                        and update.text == "!update-admins"
                    ):
                        message_ids = update.message_id
                        reply = await update.reply(
                            "در حال به روزرسانی لیست ادمین ها..."
                        )
                        await updateAdmins(client)
                        await sleep(2)
                        message_id = await reply.edit(
                            "به روزرسانی لیست ادمین ها انجام شد."
                        )
                        await deleteMessage(
                            client, [message_ids, message_id.message_update.message_id]
                        )

                    elif (
                        update.author_guid in group_admins
                        and update.raw_text == "راهنما"
                    ):
                        text = f"""🖇 راهنمای تایگر

[⚙ جوک]
[⚙ دانستنی]
⚙ `!ban ` 
- حذف شخص از گپ [حتما رپلای کنید]

⚙ `!ban @id `
- حذف شخص از گپ

⚙ `!warn ` 
- اخطار به شخص [حتما رپلای کنید]

⚙ `!unwarn @id `
- حذف اخطار شخص

⚙ `!silent ` 
- حذف پیام های شخص در گپ

⚙ `!silent @id `
- حذف پیام های شخص در گپ

⚙ `!clean-list-silent`
- پاکسازی لیست سکوت

⚙ `!update-admins `
- اپدیت مدیران

⚙ `!look-gif `
- حذف گیف در گروه

⚙ `!unlook-gif `
- پاک نشدن گیف در گروه توسط ربات

⚙ `!open `
- بازکردن گروه

⚙ `!close `
- قفل گروه

───> channel : {channe_id} <───

🤖 قابلیت های خودکار

⚙ ضدلینک
- حذف لینک های ارسالی به گروه

⚙ حذف فش
- حذف فش های ارسالی به گروه

                        """
                        await update.reply(text)

                    elif update.author_guid in group_admins and update.text.startswith(
                        "!ban"
                    ):
                        if update.reply_message_id != None:
                            try:
                                result = await client(
                                    methods.messages.GetMessagesByID(
                                        my_group, [update.reply_message_id]
                                    )
                                )
                                result = result.to_dict().get("messages")[0]
                                if not result.get("author_object_guid") in group_admins:
                                    result = await client(
                                        methods.groups.BanGroupMember(
                                            my_group,
                                            result.get("author_object_guid"),
                                        )
                                    )
                                    message_id = await update.reply(
                                        "کاربر مورد نظر از گروه حذف شد."
                                    )
                                else:
                                    message_id = await update.reply(
                                        "کاربر مورد نظر در گروه ادمین است."
                                    )
                                    await deleteMessage(
                                        client,
                                        [
                                            update.message_id,
                                            message_id.message_update.message_id,
                                        ],
                                    )
                            except IndexError:
                                message_id = await update.reply(
                                    "ظاهرا پیامی که روی آن ریپلای کرده اید پاک شده است."
                                )  
                                await deleteMessage(
                                    client,
                                    [
                                        update.message_id,
                                        message_id.message_update.message_id,
                                    ],
                                )
                        elif update.text.startswith("!ban @"):
                            username = update.text.split("@")[-1]
                            if username != "":
                                result = await client(
                                    methods.extras.GetObjectByUsername(username.lower())
                                )
                                result = result.to_dict()
                                if result.get("exist"):
                                    if result.get("type") == "User":
                                        user_guid = result.get("user").get("user_guid")
                                        if not user_guid in group_admins:
                                            result = await client(
                                                methods.groups.BanGroupMember(
                                                    my_group, user_guid
                                                )
                                            )
                                            message_id = await update.reply(
                                                "کاربر مورد نظر از گروه حذف شد."
                                            )
                                        else:
                                            message_id = await update.reply(
                                                "کاربر مورد نظر در گروه ادمین است."
                                            )
                                    else:
                                        message_id = await update.reply(
                                            "کاربر مورد نظر کاربر عادی نیست."
                                        )
                                else:
                                    message_id = await update.reply(
                                        "آیدی مورد نظر اشتباه است."
                                    )
                            else:
                                message_id = await update.reply(
                                    "آیدی مورد نظر اشتباه است."
                                )
                        else:
                            message_id = await update.reply(
                                "روی یک کاربر ریپلای بزنید."
                            ) 
                        await deleteMessage(
                            client,
                            [update.message_id, message_id.message_update.message_id],
                        )

        @client.on(handlers.MessageUpdates(models.is_group()))
        async def updates(update):
            if update.object_guid == my_group:
                if update.author_guid in silence_list:
                    await update.delete_messages()
                else:
                    if no_gifs:
                        if not update.author_guid in group_admins:
                            result = await client(
                                methods.messages.GetMessagesByID(
                                    my_group, [update.message_id]
                                )
                            )
                            result = result.to_dict().get("messages")[0]
                            if (
                                result.get("type") == "FileInline"
                                and result.get("file_inline").get("type") == "Gif"
                            ):
                                await update.delete_messages() 

        await client.run_until_disconnected()
run(main())
