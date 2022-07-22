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

## How to upload and test the api

-   Start the server
-   Go to `http://localhost:<PORT>/video/`
-   Upload a large file, or test with small by relaying through a longer network route by maybe using `portmap.io` or `ngrok` or your `private server`
-   Test endpoint to list currently uploading file by `GET` ting at `/video/api/listUploading`

## Api docs

Api endpoint for the videoApp in this django project is available in `/video/api` route to seperate it from other possible apps.

All the below endpoints are relative to this root route.

### **_`/upload`_**

Type: `POST`

Description: Uploads video with logic specified in `upload.html`'s script section inside `templates` directory.

Requires: first `GET` with json body with `{title:<>, summary:<>}` then second `POST` request is a `form submit` with video `data` + received `videoId` from previous `GET`
Response:

    {
        "message": "validation error message(400)/
                received confirmation(200)/
                Server Error(500)"
    }

### **_`/listUploading`_**

Type: `GET`

Description: Lists videos being uploaded to server

Requires: Nothing

Response:

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
        "size(int)": "Size of video file in KB"
    }

Response:

    Request payload +
    {
        "charge" : "<Price in $>"
            OR
        "error": "<Validation error message>"
    }

### **_`/`_**

Type: `GET`

Description: Lists videos uploaded to server

Requires: Nothing

Response:

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

## Known shortcomings

Because the instructions didn't require me to implement and I was short on time

    -    Cannot modify video data once uploaded, even from admin panel because I'm relying on temporary file on system's `/tmp` directory to validate upload request
    -    Cannot delete video except from admin panel

## Made for Python internship's technical round at RPA Labs
