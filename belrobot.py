from requests import get
from re import findall
from rubika import Bot
import time
from colorama import Fore,init
from pyfiglet import Figlet

#created By Mamad BELECTRON

print(Fore.GREEN+ "\n L o a d i n g . . . ")
time.sleep(2)
print("")

print ("__________")
time.sleep(0.7)
print ("#_________")
time.sleep(0.6)
print ("##________")
time.sleep(0.5)
print ("###_______")
time.sleep(0.4)
print ("####______")
time.sleep(0.3)
print ("#####_____")
time.sleep(0.2)
print ("######____")
time.sleep(0.1)
print ("#######___")
time.sleep(0.5)
print ("########__")
time.sleep(0.1)
print ("#########_")
time.sleep(0.5)
print ("##########")
print ("")

print(Fore.GREEN+ "\n version 2.0.0")
print("")

print(Fore.YELLOW+"\n Please subscribe to the channel to receive updates :")
print("")

print(Fore.BLUE+"\n Rubika --> @robot_000")
print("")

Sa=Figlet(font="slant")
print(Sa.renderText("BELECTRON"))
print("")

bot = Bot(input("Please Enter Your Auth :"))
target=input("Please Enter Your Guid (Group) :")

print(Fore.BLUE+"\n The Robot Was Successfully Activated !")

def hasAds(msg):
	links = list(map(lambda ID: ID.strip()[1:],findall("@[\w|_|\d]+", msg))) + list(map(lambda link:link.split("/")[-1],findall("rubika\.ir/\w+",msg)))
	joincORjoing = "joing" in msg or "joinc" in msg

	if joincORjoing: return joincORjoing
	else:
		for link in links:
			try:
				Type = bot.getInfoByUsername(link)["data"]["chat"]["abs_object"]["type"]
				if Type == "Channel":
					return True
			except KeyError: return False
			
answered = [Bot.getGroupAdmins]
retries = {}
sleeped = False
delmess = ["دولی","کصکش","کون","کص","کیر" ,"خر","کستی","دول","گو","کس","کسکش","کوبص","کون","کص","کصخل","ننه جنده","کونی","کیری","کیرم"]
plus= True

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue
		
		open("id.db","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if msg.get("text") == "/bot" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "📍 The robot is active ", message_id=msg.get("message_id"))
                    #elif msg.get("text") == "@" :
                 #       bot.deleteMessages(target)
					elif msg.get("text").startswith("/add") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "➕ User added to group", message_id=msg.get("message_id"))

					elif msg.get("text") == "/panel":
						bot.sendMessage(target, "❮ List of robot commands ❯ :\n✅ /start : فعالسازی ربات\n❎ /stop : غیر فعالسازی ربات\n🤖 /bot : وضعیت ربات\n⏳ /time : ساعت\n📆 /date : تاریخ\n♻️ /del : حذف یک پیام\n🔒 /lock : قفل گروه\n🔓 /unlock : باز کردن قفل گروه\n⛔️ /ban : حذف کاربر\n📨 /send : ارسال پیام ناشناس\n🎶 /add : افزودن کاربر به گروه\n🗃 /panel : لیست دستورات ربات\n🔖 /user : اطلاعات کاربر\n📟 /cal : ماشین حساب\n📝 /font : ارسال فونت\n🌐 /ping : گرفتن پینگ سایت\n🔤 /tran : مترجم انگلیسی\n💣 /bomber : اسپم پیامک\n ─┅━━━━━━━┅─ \n🔮 سرگرمی ها :\n✢ با ارسال کلمه جوک ربات برای شما یک جوک ارسال میکند .\n✢ با ارسال کلمه دانستنی ربات برای شما یک دانستنی ارسال میکند .\n ✢ با ارسال کلمه فال ربات برای شما یک فال ارسال میکند .\n✢ با ارسال کلمه داستان ربات برای شما یک داستان ارسال میکند ‌.\n✢ با ارسال کلمه هواشناسی ... ربات آب و هوای اون منطقه رو ارسال میکند .\n✢ با ارسال کلمه اخبار ربات اخبار دقیق همون روز رو ارسال میکند .\n✢ با ارسال کلمه بیوگرافی ربات یک بیوگرافی به طور تصادفی ارسال میکند .\n✢ با ارسال کلمه ذکر ربات ذکر روز رو ارسال میکند.\n✢ با ارسال کلمه حدیث ربات یک حدیث ارسال میکند.\n─┅━━━━━━━┅─ \n🔸ChanneL : rubika.ir/belectron_bot")
				
					elif msg.get("text").startswith("/cal"):
						msd = msg.get("text")
						if plus == True:
							try:
								call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
								if call[1] == "+":
									am = float(call[0]) + float(call[2])
									bot.sendMessage(target, "حاصل -->\n"+"".join(str(am)), message_id=msg.get("message_id"))
									plus = False
							
								elif call[1] == "-":
									am = float(call[0]) - float(call[2])
									bot.sendMessage(target, "حاصل -->\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "*":
									am = float(call[0]) * float(call[2])
									bot.sendMessage(target, "حاصل -->\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "/":
									am = float(call[0]) / float(call[2])
									bot.sendMessage(target, "حاصل -->\n"+"".join(str(am)), message_id=msg.get("message_id"))
							except IndexError:
								bot.sendMessage(target, "⊖ دستور صحیح نمیباشد !\n  \n✠ به این فرم دستور را تایپ کنید :\nمثال ⇜ 1 * 2" ,message_id=msg.get("message_id"))
						plus= True
					elif msg.get("text").startswith("/send") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "Massage was sended !", message_id=msg.get("message_id"))
						 		
					elif msg.get("text").startswith("@"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("rubika.ir"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("+98"):
						bot.sendMessage(target, "پنل بمبر برای شما فعال نمیباشد لطفا اشتراک خریداری کنید تا بتوانید از این دستور استفاده کنید !", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("مدیر"):
						bot.sendMessage(target, "مدییر خوابه !", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("چه خبر"):
						bot.sendMessage(target, "سلامتیت عشقم", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("هعب"):
						bot.sendMessage(target, "هیس چسناله نکن", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("کیر"):
						bot.sendMessage(target, "فحاشی نکن وگرنه همین الان سیکتو از گپ میزنم", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("قهرم"):
						bot.sendMessage(target, "نه بیا بقلم عشقم قر نکنننننن", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("علی"):
						bot.sendMessage(target, "عه علیههههههههههههه", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("اها"):
						bot.sendMessage(target, "اره", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("هایاه"):
						bot.sendMessage(target, "داری کون میدی عشقم؟", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("هعی"):
						bot.sendMessage(target, "هعی دا هعیییییییی", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("خبی"):
						bot.sendMessage(target, "عین آدم چت کن خبی چیه؟", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("دلام"):
						bot.sendMessage(target, "دلام عجقم قوبی؟", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("لواط"):
						bot.sendMessage(target, "لواط مایه حیات", message_id=msg["message_id"])
					
					
					elif msg.get("text").startswith("چرا"):
						bot.sendMessage(target, "چون زیرا", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("https"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
											
					elif msg.get("text").startswith("ربات زن داری"):
						bot.sendMessage(target, " اره خوبشم دارم کل روبیک برام میماله", message_id=msg["message_id"])       
						
					elif msg.get("text").startswith("ممد کیه"):
						bot.sendMessage(target, "تو فکر کن زن ایلیه ولی به کسی نگیا", message_id=msg["message_id"])
								
					elif msg.get("text").startswith("شعر بخون"):
						bot.sendMessage(target, "سلام ای ناله ی بارون سلام ای کس های گریون سلام کیرمو کردم توش هنوزم ابم نیومد سلام ای کاندوم خوبم سلام ای همدم خپبم سلام شب های تاخیری هنوزم دوسشون دارم", message_id=msg["message_id"])
						
					elif msg.get("text") == "بات":
						bot.sendMessage(target, "جونم عشقممم" or "بله" or "بنال", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "کیرمی":
						bot.sendMessage(target, "کیر بخور باو تو کیرت کجا بود؟", message_id=msg.get("message_id"))
							
					
					elif msg.get("text") == "کیرم بخور":
						bot.sendMessage(target, "به دودولت میگی کیر؟", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "چخبر":
						bot.sendMessage(target, "سلامتیت عشقمممم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بگو ممد":
						bot.sendMessage(target, "ممد", message_id=msg.get("message_id"))		
								
					elif msg.get("text") == "ربات":
						bot.sendMessage(target, "ربات پدر لپرته من یک فرا انسان هستم", message_id=msg.get("message_id"))

					elif msg.get("text") == "تایپرها چه کسانی هستند":
						bot.sendMessage(target, "تایپر ها انسان هایی عقب مانده هستند که با چس مست کردن ادعای بزرگی میکنن ولی در واقعیت جز جیش کردن کار دیگری بلد نیستند این فراد در واقعیت بسیار تو سری خور هستند و به همین دلیل برای خالی کردن عقده هایشان به روبیک پناه می اورند باشد که نسلشان منقرض شود\n@belectron_bot", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "بیا سکسچت":
						bot.sendMessage(target, "اوففففف لخت کن دارم میام", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "مایل به کار های گناه":
						bot.sendMessage(target, "بستگی داره چی باشه لواط و پایم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "صاحب روبات":
						bot.sendMessage(target, "@Sjjsjsjsp", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "کانال":
						bot.sendMessage(target, "🤖 کانال ما :\nhttp://rubika.ir/@robot_000", message_id=msg.get("message_id"))
											
					elif msg.get("text") == "تپچی":
						bot.sendMessage(target, "چقد صدام میزنی حاجی", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "/bomber":
						bot.sendMessage(target, "کاربر گرامی لطفا اقدام به خرید اشتراک بکنید سپس میتوانید از این دستور استفاده کنید.\nchannel : @robot_000", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "خوبی عزیزم":
						bot.sendMessage(target, "اوفف به من گفتی عزیزم؟🤤💜", message_id=msg.get("message_id"))
										
					elif msg.get("text") == "خوبی":
						bot.sendMessage(target, "ن حالم خرابه هعی", message_id=msg.get("message_id"))
											
					if  msg.get("text").startswith('/user @'):
						try:
							user_info = bot.getInfoByUsername( msg.get("text")[7:])
							if user_info['data']['exist'] == True:
								if user_info['data']['type'] == 'User':
									bot.sendMessage(target, 'Name User:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nBio User:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
									print('sended response')
								else:
									bot.sendMessage(target, "خطا !\nاین یوزرنیم مربوط به یک کانال میباشد." ,  msg.get('message_id'))
									print('sended response')
							else:
								bot.sendMessage(target, "کاربری وجود ندارد ❌" ,  msg.get('message_id'))
								print('sended response')
						except:
							print('server bug6')
							bot.sendMessage(target, "خطا در اجرای دستور مجددا سعی کنید ❌" ,message_id=msg.get("message_id"))
							

					elif msg.get("text") == "/stop" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "the robot is offline !", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("/ping"):
						
						try:
							responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
							bot.sendMessage(target, responser,message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن جقی!", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("ترجمه فارسی"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن جقی!", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("ترجمه انگلیسی"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=fa&to=en&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن جقی!", message_id=msg["message_id"])
			     	   
					elif msg.get("text").startswith("ترجمه عربی"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=fa&to=ar&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن جقی!", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("واژه"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/vajehyab/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن جقی!", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("/font"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن جقی!", message_id=msg["message_id"])
									
					elif msg.get("text").startswith("ذکر"):
						
						try:
							response = get("https://api.codebazan.ir/zekr/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن باو", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("حدیث"):
						
						try:
							response = get("https://api.codebazan.ir/hadis").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "اشتباه وارد کردی دستورو عشقم", message_id=msg["message_id"])
					elif msg.get("text").startswith("اوقات شرعی"):
						
						try:
							response = get("https://api.codebazan.ir/owghat/?city=تهران").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "اشتباه وارد کردی دستورو عشقم", message_id=msg["message_id"])
														
					elif msg["text"].startswith("هواشناسی"):
						response = get(f"https://api.codebazan.ir/weather/?city={msg['text'].split()[1]}").json()
						#print("\n".join(list(response["result"].values())))
						try:
							bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
							bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
						except:
								bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])
										
					elif msg.get("text").startswith("قیمت خودرو"):
						
						try:
							response = get("http://api.codebazan.ir/car-price/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "احمق دستور رو درست وارد کن!!!", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("جوک"):
						
						try:
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "احمق دستور رو درست وارد کن!!!", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("ساعت"):
						
						try:
							response = get("http://api.codebazan.ir/time-date/?td=all").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "احمق دستور رو درست وارد کن!!!", message_id=msg["message_id"])
									
					elif msg.get("text").startswith("دانستنی"):
						
						try:
							response = get("https://api.codebazan.ir/danestani/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن باو", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("فال"):
						
						try:
							response = get("https://api.codebazan.ir/fal").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن باو", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("بیوگرافی"):
						
						try:
							response = get("https://api.codebazan.ir/bio/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن باو", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("داستان"):
						
						try:
							response = get("https://api.codebazan.ir/dastan/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "خنگ زاده دستور رو درست وارد کن", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("اخبار"):
						
						try:
							response = get("https://api.codebazan.ir/khabar/?kind=iran").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "اشتباه وارد کردی دستورو عشقم", message_id=msg["message_id"])
													
					elif msg.get("text") == "/time":
						bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))

					elif msg.get("text") == "/date":
						bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))

					elif msg.get("text") == "/del" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "پیام پاک شد ✅", message_id=msg.get("message_id"))
						
					#				elif msg.get("text").split(" ")[0] in  delmess:
	#				bot.deleteMessages(target, [msg.get("message_id")])
	#				bot.sendMessage(target, "یک پیام مستهجن پاک شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "/lock" and msg.get("author_object_guid") in admins :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "گپ قفل شد ✅", message_id=msg.get("message_id"))						
					elif msg.get("text") == "/unlock" and msg.get("author_object_guid") in admins :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "گپ باز شد ✅", message_id=msg.get("message_id"))
							
					elif msg.get("text").startswith("/ban") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, f" ✅ کاربر حذف شد", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, f" کاربر حذف نشد❌", message_id=msg.get("message_id"))
								
						except IndexError:
							a = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
							if a in admins:
								bot.sendMessage(target, f" کاربر حذف نشد ❌ ", message_id=msg.get("message_id"))
							else:
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								bot.sendMessage(target, f" کاربر حذف شد ✅", message_id=msg.get("message_id"))

				else:
					if msg.get("text") == "/start" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "the robot is online !", message_id=msg.get("message_id"))
			
			elif msg.get("text") == "/pin" and msg.get("author_object_guid") in admins :
				bot.pin(target, msg["reply_to_message_id"])
				
			elif msg.get("text") == "/unpin" and msg.get("author_object_guid") in admins :
				bot.unpin(target, msg["reply_to_message_id"])
				bot.sendMessage(target, "The message was successfully removed from the pin !", message_id=msg.get("message_id"))
			
			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"لینک میدی حالا سیک کن {user}", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"Hey {user} 💜\nWelcome to {name} 🛸\n channel : @robot_000 🗿", message_id=msg["message_id"])
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"چه بهتر", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"Hey {user} 💜\nWelcome to {name} 🛸\nChannel : @robot_000 🗿", message_id=msg["message_id"])

			answered.append(msg.get("message_id"))

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue	
