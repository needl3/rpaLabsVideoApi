from fileinput import filelineno
from . import constants
from django.core.exceptions import ValidationError


def calculateSizeCharge(fileSize):
    try:
        if int(fileSize) <= 500 * 1024:
            return 5
        elif int(fileSize) > 500*1024:
            return 12.5
        else:
            raise ValidationError(constants.ERRS.get('invalidFields'))
    except:
        raise ValidationError(constants.ERRS.get('invalidFields'))


def calculateLengthCharge(videoLength):
    try:
        if int(videoLength) < 6 * 60 + 18:
            return 12.5
        elif int(videoLength) > 6 * 60 + 18:
            return 20
        else:
            raise ValidationError(constants.ERRS.get('invalidFields'))
    except:
        raise ValidationError(constants.ERRS.get('invalidFields'))


def checkValidity(data):
    # Handle a case where there might not be indended data ie. size, type, length
    # That will raise TypeError
    if int(data.get('size')) > 1 * 1024 * 1024:
        raise ValidationError(constants.ERRS.get('maxSize'))
    elif data.get('type') not in constants.ALLOWED_VIDEO_TYPES:
        raise ValidationError(constants.ERRS.get('invalidVideoType'))
    elif int(data.get('length')) > 10 * 60:
        raise ValidationError(constants.ERRS.get('maxLength'))
    return True


def calculateCharge(data):
    charge = 0
    if checkValidity(data):
        charge += calculateSizeCharge(data.get('size'))
        charge += calculateLengthCharge(data.get('length'))
    return charge
