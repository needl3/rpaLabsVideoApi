import json

from django.forms import ValidationError
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from . import models
from .utils import charges


# Ignoring csrf validation for testing purposes only
# Send proper headers in production
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        try:
            newVideoEntry = models.Video(data=request.FILES['data'])

            # Run validators
            newVideoEntry.full_clean()

            # If no ValidationError is raised, save to db
            newVideoEntry.save()
            return JsonResponse({
                'message': 'Video received'
            })
        except ValidationError as ve:
            return JsonResponse({
                'message': str(ve)
            }, status=400)
        except Exception as e:
            msg = {
                'message': 'Internal Server Error'
            }

            if settings.DEBUG == True:
                msg['Error'] = str(e)

            return JsonResponse(msg, status=500)

    return JsonResponse({
        'message': 'You cannot just GET here.',
    }, status=400)


def listUploading(request):
    return JsonResponse({
        'message': 'This endpoint will return the list of videos being uploaded.'
    })


# Remove this exemption in production
@csrf_exempt
def charge(request):
    if request.method == "GET":
        videoData = json.loads(request.body)

        #
        # Calculate charges and add 'charge' field to response object
        # If there's validation error, return that error in response
        #
        try:
            videoData['charge'] = charges.calculateCharge(videoData)
        except ValidationError as ve:
            videoData['error'] = str(ve)

        return JsonResponse(videoData, status=400 if videoData.get('error') else 200)
    return JsonResponse({
        'message': 'GET in this endpoint with proper data will give you info on video charges'
    })


#
# A test endpoint to check list of UPLOADED videos
#
def listUploaded(request):
    return JsonResponse({
        'message': 'List of uploaded videos',
        'videos': list(models.Video.objects.values())
    }, status=400)
