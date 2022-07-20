from django.db import models
from .utils import validator


class Video(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, default="Video Title")
    videoSummary = models.TextField(default="Video Summary")

    type = models.CharField(max_length=100, default="mp4")

    # Actual binary data is stored as FileField in static/uploads
    # Since I'm using Sqlite here
    # We can hit some cdns to handle media files for serious projects
    # Or some other database that supports raw binary data storage natively
    # Like the MongoDB with GridFsStorage
    data = models.FileField(
        upload_to="uploads/", max_length=250, validators=[validator.validateVideo])

    # Timestamps
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
