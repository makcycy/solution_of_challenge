
def setEnv():
    import os

    credential_path = 'credentials/speech-analysis-312306-6aedd9ae798f.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path