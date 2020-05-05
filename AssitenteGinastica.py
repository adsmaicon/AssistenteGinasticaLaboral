from AssitentTypeEnum import AssitentTypeEnum
from Assistent import Assistent
from ssml_builder.core import Speech
import random

exercicios = [
    "Alongar os braços para frente 15 segundos",
    "Alongar o braço direito atrás do pescoço 15 segundos",
    "Alongar o braço esquerdo atrás do pescoço 15 segundos",
    "Mexer o pescoço para baixo e para cima 15 segundos",
    "Girando as mãos 15 segundos",
    "Alongando os dedos 15 segundos",    
    "Alongando as pernas 15 segundos",
    "Flexionando as perna direita 15 segundos",
    "Flexionando as perna esquerda 15 segundos",    
    "Joelho direito na frente 15 segundos",
    "Joelho esquerdo na frente 15 segundos",    
    "Flexionar o Joelho direito 15 segundos",
    "Flexionar o Joelho esquerdo 15 segundos"]

half_1 = [1,2,3,4,5,6,7]
half_2 = [8,9,10,11,12,13,14,15]

mylist = [
    "Nada pode parar quem sabe onde quer chegar.",
    "Tudo o que um sonho precisa para ser realizado é alguém que acredite que ele possa ser realizado.",
    "O sacrifício é o intervalo entre seu objetivo e a glória.",
    "Transforme a motivação em hábito.",
    "A dor é temporária. A glória é eterna.",
    "O que não te desafia não te faz mudar.",
    "Para ter sucesso é preciso primeiro acreditar que podemos.",
    "A excelência não é um ato, mas um hábito.",
    "O preço da perfeição é a prática constante.",
    "Acreditar é essencial, mas ter a atitude é o que faz a diferença.",
    "Uma conquista por dia.",
    "Mentalize coisas boas e elas acontecerão.",
    "Se a vida não ficar mais fácil, trate de ficar mais forte.",
    "Um passo de cada vez. Mas sempre para frente.",
    "Quem não desiste não pode ser vencido.",
    "Mantenha o corpo forte e a cabeça erguida.",
]

speech = Speech()

for item in exercicios:
    speech.add_text(item)
    speech.pause(time="2s")
    for n in half_1:
        speech.add_text(str(n))
        speech.pause(time="1s")

    speech.add_text(random.choice(mylist))
    speech.pause(time="1s")

    for n in half_2:
        speech.add_text(str(n))
        speech.pause(time="1s")

type_asistente = AssitentTypeEnum.AWS

assist = Assistent.factory(type_asistente)
mp3 = assist.synthesize_speech(speech.speak())

with open("out/{}.mp3".format(type_asistente.name), 'wb') as out:
    out.write(mp3)
