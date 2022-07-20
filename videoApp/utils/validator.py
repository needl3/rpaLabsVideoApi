# Can't just check the extension these days, people are smart like me ** Cries in the corner **
# Have to check the contents to be more secure
# So used ffmpeg and magic
import ffmpeg
import magic
import os

from django.core.exceptions import ValidationError
from django.conf import settings

from . import constants
from .constants import ERRS


def validateVideo(data):
    #
    # Temporary Directory to write intermediate data
    # Before updating in database
    # Because you didn't specify to modify video data
    # I just made this simple validator
    # I have to create validator per attribute or fill in the blanks
    # if I was to create endpoint to update existing video data or maybe use form validations
    # Also I can use counts in tmp directory for
    # Counting videos being uploaded
    #
    tmpfile = settings.FILE_UPLOAD_TEMP_DIR+data.name
    if data.size > constants.VIDEO_SIZE:
        raise ValidationError(ERRS.get('maxSize'))

    with open(tmpfile, 'wb+') as f:
        for chunk in data.chunks():
            f.write(chunk)

    t, ext = magic.from_file(tmpfile, mime=True).split("/")

    if t != "video":
        raise ValidationError(ERRS.get('invalidFileType'))
    if ext not in constants.ALLOWED_VIDEO_TYPES:
        raise ValidationError(ERRS.get('invalidVideoType'))
    try:
        metadata = ffmpeg.probe(tmpfile, select_streams="v")['streams'][0]
    except TypeError:
        raise ValidationError(ERRS.get(
            'probingError')+ERRS.get('invalidFileType'))

    if float(metadata['duration']) > float(constants.VIDEO_LENGTH):
        raise ValidationError(ERRS.get('maxLength'))

    # Because this file passed all validation
    # We can safely delete the temporary file `#SaveSpace`
    os.remove(tmpfile)
