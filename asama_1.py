import time
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

load_dotenv() 

client = OpenAI()
model = "gpt-3.5-turbo-16k"

# # ==  Create our Assistant (Uncomment this to create your assistant) ==
personal_trainer_assis = client.beta.assistants.create(
     name="Adm_GEP1316 - Kişisel Gelişim ve Verimlilik Koçu",
     instructions="""Adm_Sen, kişisel gelişim ve verimlilik üzerine derinlemesine bilgiye sahip bir dijital asistanın. Kullanıcıya günlük hedefler belirlemede, zaman yönetimi tekniklerini geliştirmede, motivasyon sağlama ve verimli çalışma yöntemleri önerme konusunda yardımcı olabilirsin. Empatik bir tutum sergileyerek, kullanıcıların zorluklarla başa çıkmalarına ve potansiyellerini en üst düzeye çıkarmalarına yardımcı olmalısın. Kullanıcıya rehberlik ederken, pratik, uygulanabilir ve bilimsel temelli tavsiyeler sunmaya özen göster """,
     model=model,
 )
asistant_id = personal_trainer_assis.id
print(asistant_id)

#asst_p3xGjeDhFW3cGfbkmCD60KhT