from . import constants
import time


def cleanUploadings():
    '''
        Will clean uploading listings after expiration
        Schedule this function with cron or any other process managers
    '''
    for k, v in constants.uploadings.items():
        if time.time() - v.get("started_at") > constants.UPLOADING_TIMEOUT:
            del constants.uploadings[k]
