from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader
# from .forms import Question
# from utils.handle_upload_file import handle_uploaded_file
from . import apps
import cv2

import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile, UploadedFile

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
    
    
def upload(req):
    if req.method == 'POST':
        if 'file' in req.FILES:
            file = req.FILES['file']
            filename = file._name
            
            image = UploadedFile.read(file)
            print image
            # apps.ImageTrans.getGrayscale(file)
            image2 = cv2.imread(image,0)
            print image2
            
            fp = open('%s/%s' % ('image/data', filename) , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            return HttpResponse('File Uploaded')
    return HttpResponse('Failed to Upload File')
  
