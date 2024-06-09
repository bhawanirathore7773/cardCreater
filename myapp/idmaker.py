from PIL import ImageFont,ImageDraw,Image
import barcode
from barcode.writer import ImageWriter
import os



class IdMaker:
    def font(size,type):
        return ImageFont.truetype(f"myapp/static/template/{type}.ttf",size=size)

    def barNum(type):
        with open("myapp/static/template/bCode/bNumber.txt",'r') as f:
            data=f.read()
        bar_number=f'V000{data}'
        if type==1:
            with open("myapp/static/template/bCode/bNumber.txt",'w') as f:
                new_data=int(data)+1
                f.write(str(new_data))  
        return bar_number
       
        
    def barCodeGenerate():
        barcode_format=barcode.get_barcode_class('code128')
        bar_number=IdMaker.barNum(type=1)
        writer =ImageWriter()
        bCode_generated=barcode_format(bar_number,writer)
        bCode_generated.save(f"myapp/static/template/bCode/{bar_number}",{"module_width":0.35, "module_height":10, "quiet_zone": 3})
        pil_image=Image.open(f"myapp/static/template/bCode/{bar_number}.png")
        crop_image=pil_image.crop((33,9,410,132))
        crop_image=crop_image.resize((897,259))
        return crop_image
        
    def balaji_id_card(idcard):
        boldFont=IdMaker.font(90,"Bold")
        boldFont1=IdMaker.font(77,"Bold")
        liteFont=IdMaker.font(90,"lightFont")
        bar_number=IdMaker.barNum(type=0)   
        barcode_image=IdMaker.barCodeGenerate()
        
        template=Image.open("myapp/static/template/balaji/balaji_template.png")
        template.paste(barcode_image,(42,1280,939,1539))
        os.remove(f"myapp/static/template/bCode/{bar_number}.png")
        draw = ImageDraw.Draw(template)
        photo = Image.open(idcard.image).resize((547, 707), Image.LANCZOS)
        template.paste(photo, (37, 552, 584, 1259))
        draw.text((1090, 530), (idcard.name).upper(), font=boldFont, fill=(237, 28, 36))
        draw.text((278, 1530), bar_number, font=liteFont, fill='black')
        draw.text((1090, 650), f'MR. {(idcard.father_name).upper()}', font=boldFont1, fill='black')
        draw.text((1090, 763), (idcard.course).upper(), font=boldFont1, fill='black')
        draw.text((1090, 875), (idcard.dob).upper(), font=boldFont1, fill='black')
        draw.text((1090, 987), f'{idcard.mobile}', font=boldFont1, fill='black')
        draw.text((1090, 1102), (idcard.address).upper(), font=boldFont1, fill='black')
        draw.text((1090, 1200), (idcard.state).upper(), font=boldFont1, fill='black')
        return template

