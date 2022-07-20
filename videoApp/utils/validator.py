# Can't just check the extension these days, people are smart like me ** Cries in the corner **
# Have to check the contents to be more secure
# So used ffmpeg and magic
import ffmpeg
import magic

import os
from django.core.exceptions import ValidationError

from . import constants
from .constants import ERRS


def validateVideo(data):
    # Temporary Directory to write intermediate data
    # Before updating in database
    # Because you didn't specify to modify video data
    # I just made this simple validator
    # I have to create validator per attribute if I was to create endpoint to
    # Update existing video data or maybe use form validations
    tmpdir = "tmp/"
    if not os.path.exists(tmpdir):
        os.mkdir(tmpdir)

    tmpfile = tmpdir+data.name
    if data.size > constants.VIDEO_SIZE:
        raise ValidationError(ERRS.get('maxSize'))

    #
    #   Do not use this read method in production
    #   Have to write to temporary location, validate then update in database
    #   To avoid copying data in memory and kill my babe
    #
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
