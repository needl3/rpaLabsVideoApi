import json
from sys import excepthook
from turtle import up

from django.forms import ValidationError
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from . import models
from .utils import charges, constants, utils

# Ignoring csrf validation for testing purposes only
# Send proper headers in production


@csrf_exempt
def upload(request):
    if request.method == "POST":
        try:
            newVideoEntry = models.Video(data=request.FILES["data"])
            # Now since the file is received completely, validation
            # won't take much since the file is under 1GB
            # So remove the video from the list of uploadings
            utils.removeUploadings(request.POST.get("videoId"))

            # Run validators
            # Didn't used forms, because idk, this was fast at the moment
            # using form is better here
            newVideoEntry.full_clean()

            # If no ValidationError is raised, save to db
            newVideoEntry.save()
            return JsonResponse({
                "message": "Video saved"
            })
        except ValidationError as ve:
            return JsonResponse({
                "message": str(ve)
            }, status=400)
        except Exception as e:
            # In case user cancels large uploads, server error will be raised
            # Clean corresponding request entry from uploadingDict
            utils.cleanUploadings()
            msg = {
                "message": "Internal Server Error"
            }

            if settings.DEBUG == True:
                msg["Error"] = str(e)

            return JsonResponse(msg, status=500)

    if request.method == "GET":
        # First add an entry to denote a video is being uploaded
        uploading_id = list(
            constants.uploadings)[-1]+1 if bool(constants.uploadings) else 0
        try:
            utils.addUploadings(json.loads(request.body), uploading_id)
            return JsonResponse({
                "videoId": uploading_id
            })
        except ValidationError as ve:
            return JsonResponse({
                "message": str(ve)
            }, code=400)

    return JsonResponse({
        "message": "You cannot just GET here.",
    }, status=400)


def listUploading(request):
    if request.method == "GET":
        return JsonResponse({
            "message": "List of videos being uploaded on the server",
            "videos": constants.uploadings
        })
    return JsonResponse({
        "message": "This endpoint will return the list of videos being uploaded."
    })


# Remove this exemption in production
@ csrf_exempt
def charge(request):
    if request.method == "GET":

        #
        # Calculate charges and add "charge" field to response object
        # If there's validation error, return that error in response
        #
        try:
            videoData = dict()
            try:
                videoData = json.loads(request.body)
            except json.decoder.JSONDecodeError:
                raise ValidationError(constants.ERRS.get("emptyFields"))
            videoData["charge"] = charges.calculateCharge(videoData)
        except ValidationError as ve:
            videoData["error"] = str(ve)

        return JsonResponse(videoData, status=400 if videoData.get("error") else 200)
    return JsonResponse({
        "message": "GET in this endpoint with proper data will give you info on video charges"
    })


#
# A test endpoint to check list of UPLOADED videos
#
def listUploaded(request):
    return JsonResponse({
        "message": "List of uploaded videos",
        "videos": list(models.Video.objects.values())
    }, status=400)
