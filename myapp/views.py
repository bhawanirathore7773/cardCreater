from django.shortcuts import render
from django.http import FileResponse
from .models import Template, Balaji_IdCard
from .idmaker import IdMaker
from django.templatetags.static import static
import uuid

def idcard_home(request):
    return render(request, 'myapp/index.html')

def createCard(request, cardName):
    content={'cardName':cardName}
    if request.method == "POST":
        name = request.POST.get('name')
        father_name = request.POST.get('fatherName')
        course = request.POST.get('course')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        state = request.POST.get('state')
        mobile = request.POST.get('mobile')
        image = request.FILES.get('image')
        user_data = Balaji_IdCard(name=name,father_name=father_name, course=course, dob=dob, address=address, state=state, mobile=mobile, image=image)
        user_data.save()
        
        template=IdMaker.balaji_id_card(user_data)
        unique_id = str(uuid.uuid4())
        template_path = f"media/templates/{unique_id}.png"
        template.save(template_path, 'PNG')
        template_path_other=f"templates/{unique_id}.png"
        template_data = Template(template=template_path_other, unique_id=unique_id)
        template_data.save()
        
        return render(request, "myapp/idcard_download.html",{"unique_id":unique_id, "cardName":cardName})
    return render(request, "myapp/idcard.html",content)


def idcard_download(request, unique_id):
    file = open('media/templates/{}.png'.format(unique_id), 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename=idcard.png'
    return response


def home_page(request):
    return render(request, 'myapp/index.html')




