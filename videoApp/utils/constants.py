VIDEO_LENGTH = 10 * 60
VIDEO_SIZE = 1 * 1024 * 1024 * 1024
ALLOWED_VIDEO_TYPES = ["mp4", "mkv"]
UPLOADING_TIMEOUT = 10  # In seconds

'''
This dictionary will contain the files that are currently being uploaded
from various sources. This is not a final implementation for this functionality
since it can overwhelm server's memory for high traffic.

I will implement it in a file/database if I was serious about the system resources

Structure of dictionary:
uploadings = [
    {
        "title":"<video_title>",
        "summary": "<video_summary>",
        "type": "<video_type>",
        "started_at":"<started_time>"
    }
]

'''
uploadings = dict()

ERRS = {
    "invalidVideoType": f"Invalid video type. Can only accept {', '.join(ALLOWED_VIDEO_TYPES)}",
    "invalidFileType": "Invalid file: Not a video file.",
    "maxSize": f"File size exceeded the limit of {round(VIDEO_SIZE/(1024*1024*1024), 3)}GB",
    "maxLength": f"Video length exceeded the limit of {round(VIDEO_LENGTH/60), 2} minutes",
    "probingError": "Probing Error",
    "invalidFields": "Invalid fields given",
    "emptyFields": "Required field are empty"
}
