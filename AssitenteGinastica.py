from AssitentTypeEnum import AssitentTypeEnum
from Assistent import Assistent
from ssml_builder.core import Speech
import random

exercicios = [
    "Biiiiiiiiiiiiixaaaaaaaaaaaaaaaaaaa não",
    ]

speech = Speech()

for item in exercicios:
    speech.add_text(item)
    speech.pause(time="1s")



type_asistente = AssitentTypeEnum.AWS

assist = Assistent.factory(type_asistente)
mp3 = assist.synthesize_speech(speech.speak())

with open("out/{}.mp3".format(type_asistente.name), 'wb') as out:
    out.write(mp3)
