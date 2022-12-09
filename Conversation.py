from chatterbot import ChatBot, filters
from chatterbot.trainers import ListTrainer
from time import sleep



chatbot = ChatBot(
    'CaririTalk',
    filters=[filters.get_recent_repeated_responses],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
    )

trainer = ListTrainer(chatbot)


trainer.train([
    "Olá",
    "Olá! Em que posso ajudar?",
    "Minha internet não tá pegando",
    "Analisando... Já verificou se o equipamento está conectado à tomada?",
    "Sim",
    "Bom, em caso de perda total de conexão, redirecionaremos você ao suporte técnico.",
    
])

trainer.train([
    "Oi",
    "Olá! Em que posso ajudar?",
    "Minha internet tá falhando",
    "Analisando... Já verificou se o equipamento está conectado à tomada?",
    "Ss",
    "Bom, em caso de perda total de conexão, redirecionaremos você ao suporte técnico.",
    
])

trainer.train([
    "Opa",
    "Olá! Em que posso ajudar?",
    "A internet tá devagar",
    "Analisando... Já verificou se o equipamento está conectado à tomada?",
    "Verifiquei",
    "Bom, em caso de perda total de conexão, redirecionaremos você ao suporte técnico.",
    
])

trainer.train([
    "Aôba",
    "Olá! Em que posso ajudar?",
    "A internet aqui tá pouca",
    "Analisando... Já verificou se o equipamento está conectado à tomada?",
    "Já",
    "Bom, em caso de perda total de conexão, redirecionaremos você ao suporte técnico.",
    
])

trainer.train([
    "Ahoy",
    "Olá! Em que posso ajudar?",
    "A internet tá fraca",
    "Analisando... Já verificou se o equipamento está conectado à tomada?",
    "Tá conectado",
    "Bom, em caso de perda total de conexão, redirecionaremos você ao suporte técnico.",
    
])

trainer.train([
    "Eae",
    "Olá! Em que posso ajudar?",
    "Minha internet tá fraca",
    "Analisando... Já verificou se o equipamento está conectado à tomada?",
    "Tá botado aqui",
    "Bom, em caso de perda total de conexão, redirecionaremos você ao suporte técnico.",
    
])

while True:
    try:
        resposta = input("Você: ")
        bot_input = chatbot.get_response(resposta)
        verificacao = str(bot_input)
        if verificacao == "Bom, em caso de perda total de conexão, redirecionaremos você ao suporte técnico.":
            print("CaririTalk: Bom, em caso de perda total de conexão, redirecionaremos você ao suporte técnico.")
            sleep(1)
            print("CaririTalk: A empresa X agradece seu contato!")
            break
        print(f"CaririTalk: {bot_input}")

    except(KeyboardInterrupt, EOFError, SystemExit):
        break