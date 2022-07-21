from django.forms import ValidationError
from . import constants
import time


def cleanUploadings():
    '''
        Will clean uploading listings after expiration
        Schedule this function with cron or any other process managers
    '''
    for k in constants.uploadings.keys():
        if time.time() - constants.uploadings.get(k).get("started_at") > constants.UPLOADING_TIMEOUT:
            del constants.uploadings[k]


def addUploadings(queryDict, videoId):
    print(f"Adding {queryDict.get('title')} in uploading list")
    try:
        constants.uploadings[str(videoId)] = {
            "title": queryDict.get("title"),
            "summary": queryDict.get("summary"),
            "started_at": time.time()
        }
    except:
        raise ValidationError(constants.ERRS.get('invalidField'))


def removeUploadings(videoId):
    del constants.uploadings[videoId]
