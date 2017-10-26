from django.contrib import admin
from django.shortcuts import get_object_or_404
from multiupload.admin import MultiUploadAdmin

# Register your models here.
from .models import Photo, Gallery, Image


class PhotoAdmin(admin.ModelAdmin):
    model = Photo
    fields = ('image',)


class ImageInlineAdmin(admin.TabularInline):
    model = Image


class GalleryMultiuploadMixing(object):

    def process_uploaded_file(self, uploaded, gallery, request):
        if gallery:
            image = gallery.images.create(file=uploaded)
        else:
            image = Image.objects.create(file=uploaded, gallery=None)
        return {
            'url': image.file.url,
            'thumbnail_url': image.file.url,
            'id': image.id,
            'name': image.filename
}

class GalleryAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    inlines = [ImageInlineAdmin,]
    multiupload_form = True
    multiupload_list = False

    def delete_file(self, pk, request):
        '''
        Delete an image.
        '''
        obj = get_object_or_404(Image, pk=pk)
        return obj.delete()


class ImageAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    multiupload_form = False
multiupload_list = True

admin.site.register(Photo, PhotoAdmin)

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
