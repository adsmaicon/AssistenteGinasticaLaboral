import boto3


class AwsAssistent():    

    def synthesize_speech(self, ssml_text):
        polly_client = boto3.Session(
            region_name='us-west-2').client('polly')

        response = polly_client.synthesize_speech(
            VoiceId="Giorgio",
            OutputFormat='mp3', 
            LanguageCode='pt-BR',
            TextType='ssml',
            Text = ssml_text)

        return response['AudioStream'].read()