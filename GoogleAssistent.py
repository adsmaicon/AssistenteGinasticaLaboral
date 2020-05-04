from google.cloud import texttospeech


class GoogleAssistent:

    def synthesize_speech(self, ssml_text):
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.types.SynthesisInput(ssml=ssml_text)

        voice = texttospeech.types.VoiceSelectionParams(
            language_code='pt-BR',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        response = client.synthesize_speech(synthesis_input, voice, audio_config)

        return response.audio_content