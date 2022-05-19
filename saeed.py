from requests import get
from re import findall
import os
import glob
from rubika.client import Bot
import requests
from rubika.tools import Tools
from rubika.encryption import encryption
from gtts import gTTS
from mutagen.mp3 import MP3
import time
import random
import urllib
import io
from pyfiglet import Figlet
from colorama import Fore,init

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

print(Fore.GREEN+ "\n version 2.1")
print("")

print(Fore.YELLOW+"\n Please subscribe to the channel to receive updates :")
print("")

print(Fore.BLUE+"\n Rubika --> @robot_000")
print("")

Sa=Figlet(font="slant")
print(Sa.renderText("ROBOT"))
print("")

bot = Bot("Bel", auth=input("Please Enter Your Auth :"))
target=input("Please Enter Your Guid (Group) :")

# Created By Mamad BeLectron

def hasAds(msg):
	links = ["http://","https://",".ir",".com",".org",".net",".me"]
	for i in links:
		if i in msg:
			return True
			
def hasInsult(msg):
	swData = [False,None]
	for i in open("dontReadMe.txt").read().split("\n"):
		if i in msg:
			swData = [True, i]
			break
		else: continue
	return swData
	
# static variable
answered, sleeped, retries = [], False, {}

alerts, blacklist = [] , []

def alert(guid,user,link=False):
	alerts.append(guid)
	coun = int(alerts.count(guid))

	haslink = ""
	if link : haslink = "گذاشتن لینک در گروه ممنوع میباشد!\n\n"

	if coun == 1:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما (1/3) اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !!!")
	elif coun == 2:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما (2/3) اخطار دریافت کرده اید ⚠️.")

	elif coun == 3:
		blacklist.append(guid)
		bot.sendMessage(target, "🚫 کاربر [ @"+user+" ] \n (3/3) اخطار دریافت کرد ، بنابراین اکنون اخراج میشود .")
		bot.banGroupMember(target, guid)


while True:
	# time.sleep(15)
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]

		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue

		for msg in messages:
			try:
				if msg["type"]=="Text" and not msg.get("message_id") in answered:
					if not sleeped:
						if hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins :
							guid = msg.get("author_object_guid")
							user = bot.getUserInfo(guid)["data"]["user"]["username"]
							bot.deleteMessages(target, [msg.get("message_id")])
							alert(guid,user,True)

						elif msg.get("text") == "!stop" or msg.get("text") == "/stop" and msg.get("author_object_guid") in admins :
							try:
								sleeped = True
								bot.sendMessage(target, "✅ ربات اکنون خاموش است", message_id=msg.get("message_id"))
							except:
								print("err off bot")
								
						elif msg.get("text") == "!restart" or msg.get("text") == "/restart" and msg.get("author_object_guid") in admins :
							try:
								sleeped = True
								bot.sendMessage(target, "در حال راه اندازی مجدد . . .", message_id=msg.get("message_id"))
								sleeped = False
								bot.sendMessage(target, "ربا‌ت با موفقیت مجددا راه اندازی شد !", message_id=msg.get("message_id"))
							except:
								print("err Restart bot")
								
						elif msg.get("text").startswith("حذف") and msg.get("author_object_guid") in admins :
							try:
								number = int(msg.get("text").split(" ")[1])
								answered.reverse()
								bot.deleteMessages(target, answered[0:number])

								bot.sendMessage(target, "✅ "+ str(number) +" پیام اخیر با موفقیت حذف شد", message_id=msg.get("message_id"))
								answered.reverse()

							except IndexError:
								bot.deleteMessages(target, [msg.get("reply_to_message_id")])
								bot.sendMessage(target, "✅ پیام با موفقیت حذف شد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text").startswith("/ban") and msg.get("author_object_guid") in admins :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									bot.banGroupMember(target, guid)
									# bot.sendMessage(target, "کاربر  {user} به دلیل رعایت نکردن قوانین\nازگروه اخراج شد✅", message_id=msg.get("message_id"))
								else :
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))
									
							except IndexError:
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								# bot.sendMessage(target, "✅ کاربر با موفقیت از گروه اخراج شد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))

						elif msg.get("text").startswith("افزودن") or msg.get("text").startswith("/add") :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]
								if guid in blacklist:
									if msg.get("author_object_guid") in admins:
										alerts.remove(guid)
										alerts.remove(guid)
										alerts.remove(guid)
										blacklist.remove(guid)

										bot.invite(target, [guid])
									else:
										bot.sendMessage(target, "❌ کاربر محدود میباشد", message_id=msg.get("message_id"))
								else:
									bot.invite(target, [guid])
									# bot.sendMessage(target, "✅ کاربر اکنون عضو گروه است", message_id=msg.get("message_id"))

							except IndexError:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
							
							except:
								bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))
								
						elif msg.get("text") == "/panel":
							try:
								rules = open("help.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								
						elif msg.get("text") == "ادمین":
							try:
								rules = open("admen.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								
						elif msg.get("text").startswith("آپدیت ادمین") and msg.get("author_object_guid") in admins:
							try:
								rules = open("admen.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت ادمین")))
								bot.sendMessage(target, "✅  ادمین ها آپدیت شد", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
						elif msg.get("text") == "!Iran":
							try:
								rules = open("safar.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								
						elif msg.get("text") == "لینک":
							try:
								rules = open("leink.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								
						elif msg.get("text").startswith("آپدیت لینک") and msg.get("author_object_guid") in admins:
							try:
								rules = open("leink.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت لینک")))
								bot.sendMessage(target, "✅  لینک گروه آپدیت شد ", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
						
						elif msg.get("text") == "منو":
							try:
								rules = open("mno.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								
						elif msg.get("text") == "!ins":
							try:
								rules = open("Insta.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								
						elif msg.get("text") == "!boo":
							try:
								rules = open("boo.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								
						elif msg.get("text") == "/panel":
							try:
								rules = open("balad.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								
						elif msg.get("text") == "!anlaen":
							try:
								rules = open("anlaen.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								
						elif msg.get("text") == "/bot":
							try:
								rules = open("bot.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								
						elif msg.get("text") == "درباره گروه":
							try:
								rules = open("help.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err dastorat")
								
						elif msg.get("text").startswith("آپدیت درباره") and msg.get("author_object_guid") in admins:
							try:
								rules = open("rules.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت درباره")))
								bot.sendMessage(target, "درباره گروه آپدیت شد", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
						elif msg["text"].startswith("!number") or msg["text"].startswith("بشمار"):
							try:
								response = get(f"http://api.codebazan.ir/adad/?text={msg['text'].split()[1]}").json()
								bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
								bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])
							
						elif msg.get("text").startswith("/time"):
							try:
								response = get("https://api.codebazan.ir/time-date/?td=all").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err answer time")
								
						elif msg.get("text") == "ساعت":
							try:
								bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))
							except:
								print("err time answer")
						
						elif msg.get("text") == "/date":
							try:
								bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))
							except:
								print("err date")
								
						elif msg.get("text") == "/del" and msg.get("author_object_guid") in admins :
							try:
								bot.deleteMessages(target, [msg.get("reply_to_message_id")])
								bot.sendMessage(target, "پیام مورد نظر پاک شد...", message_id=msg.get("message_id"))
							except:
								print("err pak")
								
						elif msg.get("text").startswith("/cal") or msg.get("text").startswith("حساب"):
							msd = msg.get("text")
							if plus == True:
								try:
									call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
									if call[1] == "+":
										try:
											am = float(call[0]) + float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
											plus = False
										except:
											print("err answer +")
										
									elif call[1] == "-":
										try:
											am = float(call[0]) - float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
										except:
											print("err answer -")
										
									elif call[1] == "*":
										try:
											am = float(call[0]) * float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
										except:
											print("err answer *")
										
									elif call[1] == "/":
										try:
											am = float(call[0]) / float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
										except:
											print("err answer /")
											
								except IndexError:
									bot.sendMessage(target, "متاسفانه دستور شما اشتباه میباشد!" ,message_id=msg.get("message_id"))
									plus= True
						
						elif hasInsult(msg.get("text"))[0] and not msg.get("author_object_guid") in admins :
							try:
								print("yek ahmagh fohsh dad")
								bot.deleteMessages(target, [str(msg.get("message_id"))])
								print("fohsh pak shod")
							except:
								print("err del fohsh Bug")
								
						elif msg.get("text").startswith("سلام") or msg.get("text").startswith("سلم") or msg.get("text").startswith("صلام") or msg.get("text").startswith("صلم") or msg.get("text").startswith("سیلام") or msg.get("text").startswith("صیلام"):
							try:
								bot.sendMessage(target,'چطوری' ,message_id=msg.get("message_id"))
							except:
								print("err hello")

						elif msg.get("text").startswith("ربات") or msg.get("text").startswith("بات") or msg.get("text").startswith("بلکترون") or msg.get("text").startswith("روبات") or msg.get("text").startswith("belectron") or msg.get("text").startswith("Belectron"):
							try:
								bot.sendMessage(target,'جانم' ,message_id=msg.get("message_id"))
							except:
								print("err robot")

						elif msg.get("text").startswith("خوبی") or msg.get("text").startswith("text"):
							try:
					  			bot.sendMessage(target, "بخوبیت دلبر", message_id=msg.get("message_id"))
							except:
								print("err luagh")
								
						elif msg.get("text") == "🤣🤣🤣":
							try:
								bot.sendMessage(target, "جون تو فقط بخند🤤", message_id=msg.get("message_id"))

                                                          
                                                     elif msg.get("text").startswith("مدیر"):
						bot.sendMessage(target, "مدییر خوابه !", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("چه خبر"):
						bot.sendMessage(target, "سلامتیت عشقم", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("هعب"):
						bot.sendMessage(target, "هیس چسناله نکن", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("کیر"):
						bot.sendMessage(target, "فحاشی نکن وگرنه همین الان سیکتو از گپ میزنم", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("قرم"):
						bot.sendMessage(target, "بتخمم که قهری", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("قهرم"):
						bot.sendMessage(target, "نه بیا بقلم عشقم قر نکنننننن", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("ممد"):
						bot.sendMessage(target, "پدر منو چیکار داری؟", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("محمد"):
						bot.sendMessage(target, "پدرته سجده بزن جلوش", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("علی"):
						bot.sendMessage(target, "عه علیههههههههههههه", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("میرم"):
						bot.sendMessage(target, "برو به چپم که میری", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("اها"):
						bot.sendMessage(target, "اره", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("هایاه"):
						bot.sendMessage(target, "داری کون میدی عشقم؟", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("هعی"):
						bot.sendMessage(target, "هعی دا هعیییییییی", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("کوس"):
						bot.sendMessage(target, "میتانم کوسیتان را بیقولم ؟", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("خبی"):
						bot.sendMessage(target, "عین آدم چت کن خبی چیه؟", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("من"):
						bot.sendMessage(target, "عن", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("دلام"):
						bot.sendMessage(target, "دلام عجقم قوبی؟", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("لواط"):
						bot.sendMessage(target, "لواط مایه حیات", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("قوبی"):
						bot.sendMessage(target, "نه حالم کیریه همشم تقصیر توعههه", message_id=msg["message_id"])
					
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
						
					elif msg.get("text") == "تو":
						bot.sendMessage(target, "سرت تو گوه", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "هی":
						bot.sendMessage(target, "ناله نکن اینجا هیئت نیست", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("خارت گاییدست"):
						bot.sendMessage(target, "اره مثل ننه تو", message_id=msg["message_id"])
						
					elif msg.get("text") == "کیرمی":
						bot.sendMessage(target, "کیر بخور باو تو کیرت کجا بود؟", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "ندارم":
						bot.sendMessage(target, "بکیرم ک نداری😂", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("تایم"):
						bot.sendMessage(target, "به فدات", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("آموزش ساخت ربات"):
						bot.sendMessage(target, "سید اگه میخوای توعم ربات داشته باشی بیا داخل چنل زیر و ربات خودتو بساز :\nhttps://rubika.ir/@robot_000", message_id=msg["message_id"])
						
					elif msg.get("text") == "کونده":
						bot.sendMessage(target,
				  "کونده هفت جدت", message_id=msg.get("message_id"))
									
					elif msg.get("text").startswith("باشه"):
						bot.sendMessage(target, "وا کن تا جاشه ", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("خدایی رباتی"):
						bot.sendMessage(target, "نه احمق زاده فرا انسانم با دستای جقیم میخام برات بساکم", message_id=msg["message_id"])
						
					elif msg.get("text") == "کیرم بخور":
						bot.sendMessage(target, "به دودولت میگی کیر؟", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "کیرمو بخور":
						bot.sendMessage(target, "من فقط کسمادرتو میخورم", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "کس":
						bot.sendMessage(target, "ای جان کس شق کردم سید", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "🙁":
						bot.sendMessage(target, "خارکسه بغض نکن بیا لواط کنیم حالت خوب میشه", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "بکیرم":
						bot.sendMessage(target, "ننت به زیرم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بی حیاس":
						bot.sendMessage(target, "به خواهرت رفتم😐", message_id=msg.get("message_id"))	
						
					elif msg.get("text") == "خواهر ندارم":
						bot.sendMessage(target, "بکیرم ک نداری", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "چخبر":
						bot.sendMessage(target, "سلامتیت عشقمممم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بگو ممد":
						bot.sendMessage(target, "ممد", message_id=msg.get("message_id"))		
								
					elif msg.get("text") == "کیر میخوری":
						bot.sendMessage(target, "نه بده خواهرت بخوره جون بگیره😂", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "کسننت":
						bot.sendMessage(target, "کیر آقام دست ننت", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "ربات":
						bot.sendMessage(target, "ربات پدر لپرته من یک فرا انسان هستم", message_id=msg.get("message_id"))
					elif msg.get("text") == "زشته":
						bot.sendMessage(tar.
						get, "زشت پدرته", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "🤣🤣🤣":
						bot.sendMessage(target, "کیر توش باشه بخندی", message_id=msg.get("message_id"))
					elif msg.get("text") == "Fuck":
						bot.sendMessage(target, "تو کست", message_id=msg.get("message_id"))	
						
					elif msg.get("text") == "سلان":
						bot.sendMessage(target, "سلان و کیرخر ", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "تایپرها چه کسانی هستند":
						bot.sendMessage(target, "تایپر ها انسان هایی عقب مانده هستند که با چس مست کردن ادعای بزرگی میکنن ولی در واقعیت جز جیش کردن کار دیگری بلد نیستند این فراد در واقعیت بسیار تو سری خور هستند و به همین دلیل برای خالی کردن عقده هایشان به روبیک پناه می اورند باشد که نسلشان منقرض شود\n@belectron_bot", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ریده":
						bot.sendMessage(target, "اره سید عنم گرفته بود ریدم در خونتون😂😂😂", message_id=msg.get("message_id"))
							
                                                                                  

							except:
								print("err poker answer")

						elif msg.get("text") == "/bomber":
							try:
								bot.sendMessage(target, "💣 Bomber PaneL \n📍 این دستور توسط سازنده ربات برای کاربرانی که از نسخه رایگان ربات استفاده میکنند متوقف شده است . برای خرید این دستور لطفا به پیوی زیر مراجعه کنید.\n #Admin --> @robot7770", message_id=msg.get("message_id"))
							except:
								print("err poker answer")
		
						elif msg.get("text") == "سنجاق" and msg.get("author_object_guid") in admins :
							try:
								bot.pin(target, msg["reply_to_message_id"])
								bot.sendMessage(target, "پیام مورد نظر با موفقیت سنجاق شد!", message_id=msg.get("message_id"))

							except:
								print("err pin")
								
						elif msg.get("text") == "برداشتن سنجاق" and msg.get("author_object_guid") in admins :
							try:
								bot.unpin(target, msg["reply_to_message_id"])
								bot.sendMessage(target, "پیام مورد نظر از سنجاق برداشته شد!", message_id=msg.get("message_id"))
							except:
								print("err unpin")
								
						elif msg.get("text").startswith("/tran"):
							try:
								responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
								al = [responser["result"]]
								bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
								bot.sendMessage(target, "نتیجه رو برات ارسال کردم", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "دستور رو درست وارد کن دیگه", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("!font"):
							try:
								response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
								bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
								bot.sendMessage(target, "نتیجه رو برات ارسال کردم", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "دستور رو درست وارد کن دیگه", message_id=msg["message_id"])
						
						elif msg.get("text").startswith("جوک") or msg.get("text").startswith("/jok") or msg.get("text").startswith("!jok"):
							try:
								response = get("https://api.codebazan.ir/jok/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("ذکر") or msg.get("text").startswith("/zekr") or msg.get("text").startswith("!zekr"):
							try:
								response = get("http://api.codebazan.ir/zekr/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "ببخشید، خطایی پیش اومد!", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("حدیث") or msg.get("text").startswith("/hadis") or msg.get("text").startswith("!hadis"):
							try:
								response = get("http://api.codebazan.ir/hadis/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "ببخشید، خطایی تو ارسال پیش اومد!", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("بیو") or msg.get("text").startswith("/bio") or msg.get("text").startswith("!bio"):
							try:
								response = get("https://api.codebazan.ir/bio/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "ببخشید، خطایی تو ارسال پیش اومد!", message_id=msg["message_id"])
								
						elif msg["text"].startswith("/weather"):
							try:
								response = get(f"https://api.codebazan.ir/weather/?city={msg['text'].split()[1]}").json()
								bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
								bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("دیالوگ"):
							try:
								response = get("http://api.codebazan.ir/dialog/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "متاسفانه تو ارسال مشکلی پیش اومد!", message_id=msg["message_id"])
							
						elif msg.get("text").startswith("دانستنی"):
							try:
								response = get("http://api.codebazan.ir/danestani/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("پ ن پ") or msg.get("text").startswith("/pa-na-pa") or msg.get("text").startswith("په نه په"):
							try:
								response = get("http://api.codebazan.ir/jok/pa-na-pa/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "شرمنده نتونستم بفرستم!", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("الکی مثلا") or msg.get("text").startswith("/alaki-masalan"):
							try:
								response = get("http://api.codebazan.ir/jok/alaki-masalan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "نشد بفرستم:(", message_id=msg["message_id"])
								
						elif msg.get("text").startswith("داستان") or msg.get("text").startswith("/dastan"):
							try:
								response = get("http://api.codebazan.ir/dastan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "مشکلی پیش اومد!", message_id=msg["message_id"])
							
						elif msg.get("text").startswith("/ping"):
							try:
								responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
								bot.sendMessage(target, responser,message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "دستور رو درست وارد کن دیگه", message_id=msg["message_id"])
								
						elif "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
							try:
								print("Yek ahmagh forwared Zad")
								bot.deleteMessages(target, [str(msg.get("message_id"))])
								print("tabligh forearedi pak shod")
							except:
								print("err delete forwared")
						
						elif msg.get("text") == "قوانین":
							try:
								rules = open("rules.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err ghanon")
								
						elif msg.get("text") == "/gj1":
							try:
								rules = open("grat1.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err ghanon")
								
						elif msg.get("text") == "/gj2":
							try:
								rules = open("grat2.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err ghanon")
								
						elif msg.get("text") == "/smf":
							try:
								rules = open("smf.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err ghanon")
								
						elif msg.get("text") == "/games":
							try:
								rules = open("byb.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err ghanon")
							
						elif msg.get("text") == "حالت آرام" and msg.get("author_object_guid") in admins:
							try:
								number = 10
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))
								
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
						elif msg.get("text") == "!speak" or msg.get("text") == "/speak" or msg.get("text") == "Speak" or msg.get("text") == "بگو":
							try:
								if msg.get('reply_to_message_id') != None:
									msg_reply_info = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if msg_reply_info['text'] != None:
										text = msg_reply_info['text']
										speech = gTTS(text)
										changed_voice = io.BytesIO()
										speech.write_to_fp(changed_voice)
										b2 = changed_voice.getvalue()
										changed_voice.seek(0)
										audio = MP3(changed_voice)
										dur = audio.info.length
										dur = dur * 1000
										f = open('sound.ogg','wb')
										f.write(b2)
										f.close()
										bot.sendVoice(target , 'sound.ogg', dur,message_id=msg["message_id"])
										os.remove('sound.ogg')
										print('sended voice')
								else:
									bot.sendMessage(target, 'پیام شما متن یا کپشن ندارد',message_id=msg["message_id"])
							except:
								print('server gtts bug')
							
						elif msg.get("text") == "برداشتن حالت آرام" and msg.get("author_object_guid") in admins:
							try:
								number = 0
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("اخطار") and msg.get("author_object_guid") in admins:
							try:
								user = msg.get("text").split(" ")[1][1:]
								guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									alert(guid,user)
									
								else :
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))
									
							except IndexError:
								guid = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								user = bot.getUserInfo(guid)["data"]["user"]["username"]
								if not guid in admins:
									alert(guid,user)
								else:
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))



						elif msg.get("text") == "/lock" and msg.get("author_object_guid") in admins :
							try:
								bot.setMembersAccess(target, ["AddMember"])
								bot.sendMessage(target, "🔒 گروه قفل شد", message_id=msg.get("message_id"))
							except:
								print("err lock GP")

						elif msg.get("text") == "بازکردن گروه" or msg.get("text") == "/unlock" and msg.get("author_object_guid") in admins :
							try:
								bot.setMembersAccess(target, ["SendMessages","AddMember"])
								bot.sendMessage(target, "🔓 گروه اکنون باز است", message_id=msg.get("message_id"))
							except:
								print("err unlock GP")

					else:
						if msg.get("text") == "!start" or msg.get("text") == "/start" and msg.get("author_object_guid") in admins :
							try:
								sleeped = False
								bot.sendMessage(target, "ربا‌ت با موفقیت روشن شد!", message_id=msg.get("message_id"))
							except:
								print("err on bot")
								
				elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
					name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
					data = msg['event_data']
					if data["type"]=="RemoveGroupMembers":
						try:
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							bot.sendMessage(target, f"دیدی کپص پدرت گزاشتم {user}", message_id=msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
						except:
							print("err rm member answer")
					
					elif data["type"]=="AddedGroupMembers":
						try:
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							bot.sendMessage(target, f"Hey {user} 🍒 !\nWelcome to {name} 🏖\n\n📑 To get information about robot commands, send a /panel command !\n🔗 ChanneL; rubika.ir/robot_000", message_id=msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
						except:
							print("err add member answer")
					
					elif data["type"]=="LeaveGroup":
						try:
							user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
							bot.sendMessage(target, f"لف دادن کون نیس که هر دفعه میدی {user}", message_id=msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
						except:
							print("err Leave member Answer")
							
					elif data["type"]=="JoinedGroupByLink":
						try:
							user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
							bot.sendMessage(target, f"Hey {user} 🍒 !\nWelcome to {name} 🏖\n\n📑 To get information about robot commands, send a /panel command !\n🔗 ChanneL; rubika.ir/robot_000", message_id=msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
						except:
							print("err Joined member Answer")
							
				else:
					if "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("message_id")])
						guid = msg.get("author_object_guid")
						user = bot.getUserInfo(guid)["data"]["user"]["username"]
						bot.deleteMessages(target, [msg.get("message_id")])
						alert(guid,user,True)
					
					continue
			except:
				continue

			answered.append(msg.get("message_id"))
			print("[" + msg.get("message_id")+ "] >>> " + msg.get("text") + "\n")

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
