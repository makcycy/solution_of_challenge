
def setEnv(path):
    import os

    credential_path = path
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path