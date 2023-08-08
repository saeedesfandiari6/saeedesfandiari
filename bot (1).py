from rubpy import Message, Client, handlers, models, methods
from asyncio import run, sleep
import random
my_group = ""
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


]

texts_chat1 = [
      "خوبم تو خوبی"و
         "مرسی "و
     "به تو مربوط نیست",

]


texts_chat = [
    "سلام",
    "های بیبی",
    "خوبی",
    "صلوم",
    "چطوری جیندا",
    "ای جان ببینچه کسی اومد",
]


texts_bot = [
    "بنال",
    "چیه بدبخت",
    "باز اومد",
    "هعی",
    "هن",
    "بگیر بخواب",
    "بله",
    "بلههه",
    "جانم",
    "جونم",
    "بگو",
    "خستم کردی",
    "بسه دیگه"
    "سلام",
    "خوبی",
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
    await client.send_message(my_group, f"ربات [ {name_gap} ] با موفقیت فعال شد 🌸")


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

                    elif update.raw_text == "جوک" or update.raw_text == "bot":
                        await update.reply(
                            texts_jok[random.randint(0, len(texts_jok))]
                        )

                    elif update.raw_text == "چطوری" or update.raw_text == "bot":
                        await update.reply(
                            texts_chat1[random.randint(0, len(texts_chat1))]
                        )

                    elif update.raw_text == "سلام" or update.raw_text == "bot":
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
                        and update.raw_text == "!info"
                    ):
                        text = f"""🖇 رهنمای ربات


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
