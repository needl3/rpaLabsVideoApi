# A simple backend for video uploads using Django

## How to use

### Manual install

-   Create a virtual environment using `virtualenv`(Optional but recommended to stay away from package conflicts)
    -   `Linux`: `virtualenv <name>`
-   Activate the environment
    -   `Linux`: `. <name>/bin/activate`
-   Install required packages
    -   `pip install -r requirements.txt`
-   Create a `.env` file with following contents inside `videoApi` directory for now
    -   `APP_SECRET`: A server secret used for various cryptographic operations
-   Migrate all database schemas
    -   `python manage.py makemigrations`
    -   `python manage.py migrate`
-   Create superuser for administration purpose(Optional)
    -   `python manage.py create superuser`
-   Run development server
    -   `python manage.py runserver <PORT>`

### Use provided script if using linux

Make sure you have `python3` and `pip` installed on your system

-   Run `./install`

## Api docs

Api endpoint for the videoApp in this django project is available in `/video/api` route to seperate it from other possible apps.

All the below endpoints are relative to this root route.

### **_`/upload`_**

Type: `POST`

Description: Uploads video

Requires: `Json` body and `form` data containing file

    -   Json: `{ "title":"Video Title", "summary":"Video Summary", "type": "Video type" }`
    -   Form: `file` (Video file)

Respose:

    {
        "message": "validation error message(400)/
                received confirmation(200)/
                Server Error(500)"
    }

### **_`/listUploading`_**

Type: `GET`

Description: Lists videos being uploaded to server

Requires: Noting

Respose:

    {
        "message":"Response description",
        "videos": [
            {
                "title":"<TITLE>",
                "summary":"<VIDEO SUMMARY>",
                "type":"<VIDEO TYPE>",
                "started_at": "<UPLOAD INITIALIZED TIME>"
                }
        ]
    }

### **_`/charge`_**

Type: `GET`

Description: Returns charge for a video upload

Requires:

    {
        "type(str)": "[mkv / mp4] ie video type",
        "length(str/int)":"Video length in seconds",
        "size(int)": "Size of video file"
    }

Respose:

    Request payload +
    {
        "charge" : "<Price in $>"
            OR
        "error": "<Validation error message>"
    }

### **_`/`_**

Type: `GET`

Description: Lists videos uploaded to server

Requires: Noting

Respose:

    {
        "message":"Response description",
        "videos": [
            {
                "id": "<int>"
                "title":"<TITLE>",
                "videoSummary":"<VIDEO SUMMARY>",
                "type":"<VIDEO TYPE>",
                "data": "<UPLOADED_DATA>(Not whole binary just the name)",
                "created":"<Created timestamp>",
                "modified":"<entry modified timestamp>"
                }
        ]
    }
