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
    "Você saberia dizer se a queda de conexão afeta a região em que você mora?",
    "Não sei",
    "Bom, em caso de perda total de conexão, redirecionaremos você ao suporte técnico.",
    
])

trainer.train([
    "Bom dia",
    "Olá! Em que posso ajudar?",
    "Internet aqui tá é pôde",
    "Analisando... Já verificou se o equipamento está conectado à tomada?",
    "Sss",
    "Você saberia dizer se a queda de conexão afeta a região em que você mora?",
    "N",
    "Bom, em caso de perda total de conexão, redirecionaremos você ao suporte técnico.",
    
])

trainer.train([
    "Boa tarde",
    "Olá! Em que posso ajudar?",
    "Internet tá pegando não",
    "Analisando... Já verificou se o equipamento está conectado à tomada?",
    "Tá ligado",
    "Você saberia dizer se a queda de conexão afeta a região em que você mora?",
    "Nn",
    "Bom, em caso de perda total de conexão, redirecionaremos você ao suporte técnico.",
    
])

trainer.train([
    "Oi",
    "Olá! Em que posso ajudar?",
    "Minha internet tá falhando",
    "Analisando... Já verificou se o equipamento está conectado à tomada?",
    "Ss",
    "Você saberia dizer se a queda de conexão afeta a região em que você mora?",
    "Caiu",
    "Já que o problema é regional, mandaremos um de nossos técnicos para resolver a situação e manteremos você informado!",
    
])

trainer.train([
    "Opa",
    "Olá! Em que posso ajudar?",
    "A internet tá devagar",
    "Analisando... Já verificou se o equipamento está conectado à tomada?",
    "Verifiquei",
    "Você saberia dizer se a queda de conexão afeta a região em que você mora?",
    "Sim",
    "Já que o problema é regional, mandaremos um de nossos técnicos para resolver a situação e manteremos você informado!",
    
])

trainer.train([
    "Aôba",
    "Olá! Em que posso ajudar?",
    "A internet aqui tá pouca",
    "Analisando... Já verificou se o equipamento está conectado à tomada?",
    "Já",
    "Você saberia dizer se a queda de conexão afeta a região em que você mora?",
    "Afeta",
    "Já que o problema é regional, mandaremos um de nossos técnicos para resolver a situação e manteremos você informado!",
    
])

trainer.train([
    "Ahoy",
    "Olá! Em que posso ajudar?",
    "A internet tá fraca",
    "Analisando... Já verificou se o equipamento está conectado à tomada?",
    "Tá conectado",
    "Você saberia dizer se a queda de conexão afeta a região em que você mora?",
    "Pdpa",
    "Já que o problema é regional, mandaremos um de nossos técnicos para resolver a situação e manteremos você informado!",
    
])

trainer.train([
    "Eae",
    "Olá! Em que posso ajudar?",
    "Minha internet tá fraca",
    "Analisando... Já verificou se o equipamento está conectado à tomada?",
    "Tá botado aqui",
    "Você saberia dizer se a queda de conexão afeta a região em que você mora?",
    "Caiu foi tudo aqui",
    "Já que o problema é regional, mandaremos um de nossos técnicos para resolver a situação e manteremos você informado!",
    
])

while True:
    try:
        resposta = input("Você: ")
        bot_input = chatbot.get_response(resposta)
        verificacao = str(bot_input)
        print(f"CaririTalk: {bot_input}")
        if verificacao == "Bom, em caso de perda total de conexão, redirecionaremos você ao suporte técnico." or verificacao == "Já que o problema é regional, mandaremos um de nossos técnicos para resolver a situação e manteremos você informado!":
            sleep(1)
            print("CaririTalk: A empresa [Nome da Empresa] agradece seu contato!")
            break
        
    except(KeyboardInterrupt, EOFError, SystemExit):
        break