VIDEO_LENGTH = 10 * 60
VIDEO_SIZE = 1 * 1024 * 1024 * 1024
ALLOWED_VIDEO_TYPES = ["mp4", "mkv"]

ERRS = {
    "invalidVideoType": f"Invalid video type. Can only accept {', '.join(ALLOWED_VIDEO_TYPES)}",
    "invalidFileType": "Invalid file: Not a video file.",
    "maxSize": f"File size exceeded the limit of {round(VIDEO_SIZE/(1024*1024*1024), 3)}GB",
    "maxLength": f"Video length exceeded the limit of {round(VIDEO_LENGTH/60), 2} minutes",
    "probingError": "Probing Error",
    "invalidFields": "Invalid fields given"
}
