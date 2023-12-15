from csv import *
from tkinter import *
from datetime import datetime as dt
import datetime
import random
import os
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import docx
from docx.shared import Inches,Cm,RGBColor,Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH 
#This is the Backend of the application
## global varibale contain csv file name and path 
date=datetime.date.today()
filename=str(date)+'.csv'
data_path=os.path.join(os.getcwd(),'data',filename)
## This is the camara class with all its oprations DO NOT EDIT!!
class Camara:
    def __init__(self,imageof):
        self.imageof=imageof
        self.photo=0
        self.app=0
        self.label_widget=0
    def show_photo(self):
        self.photo=Toplevel()
        label=Label(self.photo)
        opencv_image=cv2.imread(os.path.join('images','Temp_name.png'))
        opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        label.photo_image = photo_image
        label.configure(image=photo_image)
        label.pack()
        Button(self.photo,text='SAVE',command=self.Save_image).pack()
    def Take_photo(self):
        _, frame = self.vid.read()
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        cv2.imwrite(os.path.join('images','Temp_name.png'), cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR))
        self.show_photo()
    def open_camera(self): 
    
        # Capture the self.video frame by frame 
        _, frame = self.vid.read() 
      
        # Convert image from one color space to other 
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
      
        # Capture the latest frame and transform to image 
        captured_image = Image.fromarray(opencv_image) 
      
        # Convert captured image to photoimage 
        photo_image = ImageTk.PhotoImage(image=captured_image) 
      
        # Displaying photoimage in the label 
        self.label_widget.photo_image = photo_image 
      
        # Configure image in the label 
        self.label_widget.configure(image=photo_image) 
        # Repeat the same process after every 10 seconds 
        self.label_widget.after(10, self.open_camera) 
      
      
    def New_window(self):
        self.app = Toplevel()
        self.label_widget= Label(self.app)
        self.label_widget.pack()
        button2= Button(self.app,text="Take image",command=self.Take_photo)
        button2.pack()
        ## prequisites for the camera 
        self.vid = cv2.VideoCapture(0)
        width, height = 800, 600
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.open_camera()
    def end(self):
        self.app.destroy()
        self.photo.destroy()
    def Save_image(self):
        print(self.imageof)
        if self.imageof==0:
            os.rename(os.path.join('images','Temp_name.png'),os.path.join('images',f'{Breed.get()}.png'))
        elif self.imageof==1:
            os.rename(os.path.join('images','Temp_name.png'),os.path.join('images',f'{Caretaker.get()}.png'))
        elif self.imageof==2:
            os.rename(os.path.join('images','Temp_name.png'),os.path.join('images',f'{Adopter.get()}.png'))
        messagebox.showinfo("Sucess","Image captured sucessfully")
        self.vid.release()
        self.end()
## declear a global var to access this class
## class to test and create csv file
class BackEnd:
    def __init__(self):
        date=datetime.date.today()
        filename=str(date)+'.csv'
        self.data_path=os.path.join(os.getcwd(),'data',filename)
        self.file_path=os.path.join(os.getcwd(),'Forms',f'{Adopter.get()}.docx')
        self.Test_file()                
    def Test_file(self):
        try:
            file=open(data_path)
            file.close()
        except FileNotFoundError :
            try:
                open_file=open(data_path,'w')
                Writer=writer(open_file)
                Writer.writerow(['counselor name','Date','Time','Tag number','Sex','Age','Color','Breed','Physical Fitness','Vaccination','Sterlisation','Caretaker/Foster name','caretaker Contact no','caretaker whatsapp','Email','social ID','Local Residence','Permanent residence','Adopter\'s name','adopter Contact no','adopter whatsapp','Email','Social ID','Local Residence','Permanent Residence','What are your plans for your pet if you shift to another town/place?','What are your plans for your pet if you shift to another town/place?','Amount of time your pet may have to be alone in a day?','Who will take care of your pet if you go out of town temporarily?'])
                open_file.close()
            except FileNotFoundError:
                os.mkdir(os.path.join(os.getcwd(),'data'))
                Test_file()
    def Check_duplicate(self):
        path=os.path.join(os.getcwd(),'Forms')
        file_name =f"{Adopter.get()}.docx"
        try:
            files=os.listdir(path)
        except FileNotFoundError:
            os.mkdir(path)
            files=os.listdir(path)
        if file_name in files:
            messagebox.showerror("ERROR","Two files with same name found")
            return False
        else:
            return True


    def Write_form(self):
        image_animal=os.path.join('images',f'{Breed.get()}.png')
        caretaker_image=os.path.join('images',f'{Caretaker.get()}.png')
        adopter_image=os.path.join('images',f'{Adopter.get()}.png')
        doc = docx.Document()
        sections = doc.sections
        for section in sections:
            section.top_margin = Cm(0.5)
            section.bottom_margin = Cm(0.5)
            section.left_margin = Cm(1)
            section.right_margin = Cm(1)
        doc.add_paragraph("Serial NO - __________________")
        doc.add_picture('logo.jpg', width=Inches(5), height=Inches(1.5))
        img=doc.paragraphs[-1]
        img.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        h1=doc.add_heading("ADOPTION AND CONSENT FORM",0)
        h1.style.font.color.rgb = RGBColor(0,0,0)
        h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_paragraph(f"Councler Name: {Councler.get()}					Date: {datetime.date.today()} ")
        dic=doc.add_heading("DESCRIPTION OF ANIMAL",1)
        dic.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        dic.style.font.color.rgb = RGBColor(0,0,0)
        animal=doc.add_table(rows=1,cols=2) 
        animal.cell(0,0).add_paragraph(f"Colour: {Color.get()}        \nGender: {Gender.get()}    Age: 12\nBreed: {Breed.get()}\nPhysically Fitness Status: {Health.get()}\nVaccination Status: {Vaccination.get()}\nSterilisation Status: {Sterilisation.get()}")
        animal.cell(0,1).add_paragraph().add_run().add_picture(image_animal,width=Inches(2),height=Inches(1.75))
        details=doc.add_heading("DETAILS OF CARETAKER                   DETAILS OF ADOPTER",1)
        details.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        details.style.font.color.rgb = RGBColor(0,0,0)
        caretaker=doc.add_table(rows=2,cols=2)
        if SameVar.get():
            formated_text=f"Name of Caretaker: {Caretaker.get()}\nContact No.: {CaretakerContact.get()}\nWhatsapp No.: {CaretakerWhatsapp.get()}\nEmail I'd: {Email.get()}\nLocal Residence: {LocalAdd.get()}\nPermanent Residence: {LocalAdd.get()}\nInstagram/Facebook ID: {ID.get()}\nSigneture:_______________"
        else:
            formated_text=f"Name of Caretaker: {Caretaker.get()}\nContact No.: {CaretakerContact.get()}\nWhatsapp No.: {CaretakerWhatsapp.get()}\nEmail I'd: {Email.get()}\nLocal Residence: {LocalAdd.get()}\nPermanent Residence: {PermanentAdd.get()}\nInstagram/Facebook ID: {ID.get()}\nSigneture:_______________"  
        caretaker.cell(0,0).add_paragraph(formated_text)
        if SameVar1.get():
            formated_text=f"Name of Adopter: {Adopter.get()}\nContact No.: {AdopterContact.get()}\nWhatsapp No.: {AdopterWhatsapp.get()}\nEmail Id: {Email1.get()}\nLocal Residence: {AdopterLocalAdd.get()}\nPermanent Residence: {AdopterLocalAdd.get()}\nInstagram/Facebook ID: {Adoptor_ID.get()}\nSigneture:_______________" 
        else:
           formated_text=f"Name of Adopter: {Adopter.get()}\nContact No.: {AdopterContact.get()}\nWhatsapp No.: {AdopterWhatsapp.get()}\nEmail Id: {Email1.get()}\nLocal Residence: {AdopterLocalAdd.get()}\nPermanent Residence: {AdopterPermanentAdd.get()}\nInstagram/Facebook ID: {Adoptor_ID.get()}\nSigneture:_______________" 
        caretaker.cell(0,1).add_paragraph(formated_text)
        caretaker.cell(1,0).add_paragraph().add_run().add_picture(caretaker_image,width=Inches(2),height=Inches(2))
        img=caretaker.cell(1,1).add_paragraph()
        img.add_run().add_picture(adopter_image,width=Inches(2),height=Inches(2))
        img.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_heading("General information from Adopter",1)
        para=doc.add_paragraph(f"What are your plans for your pet if you shift to another town/place?\n {Plans.get('1.0','end-1c')}")
        para.add_run(f"\nHave you had a pet before or have one right now?\n{Owned.get()}")
        para.add_run(f"\nAmount of time your pet may have to be alone in a day?\n{Alone.get()}")
        para.add_run(f"\nWho will take care of your pet if you go out of town temporarily?\n{NotHome.get()}")
        con=doc.add_heading("Consent By Adopter",1)
        con.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        con.style.font.color.rgb = RGBColor(0,0,0)
        doc.add_paragraph('With the unanimous consent of all my family members, I am willingly adopting the pet, assuming full responsibility and acknowledging that I will always regard my pet as an integral part of our family, ensuring that it is never treated merely as an object.',style='List Bullet')
        doc.add_paragraph("I commit to maintaining a clean and well-ventilated environment for the adopted pet, providing proper nourishment, and ensuring regular exercise. I will refrain from keeping the animal tethered or chained with an unreasonably short or heavy restraint for an extended duration.",style='List Bullet')
        doc.add_paragraph("I acknowledge that certain diseases may not be detectable during the initial checkup of the adopted pet, and the Animals With Humanity Team will not be held responsible for such conditions. Therefore, it is recommended to conduct a comprehensive post-adoption health examination.",style='List Bullet')
        doc.add_paragraph("If the pet I adopt becomes unwell, I will promptly seek advice from a veterinarian and notify the Animals With Humanity Team. Additionally, I will take responsibility for adhering to the deworming, vaccination, and sterilization schedule for the well-being of the pet.",style='List Bullet')
        doc.add_paragraph("Should the responsibility of pet parenting need to be transferred, I will provide advance notice to both the caretaker and Team Animals With Humanity. I understand that the adoption process will need to be repeated for the new caretakers, and a fine of Rs. 5,000/- will be duly acknowledged and paid.",style='List Bullet')
        doc.add_paragraph("I acknowledge that the Animals With Humanity Team possesses the authority to conduct unannounced inspections of the conditions in which I'm taking care for the adopted pet. In the event of any violations, the Animals With Humanity Team is empowered to take legal action as per applicable law.",style='List Bullet')
        doc.add_paragraph("I ______________ acknowledge that abandoning or subjecting my pet to mistreatment may lead to legal consequences under the Prevention of Cruelty to Animals Act of 1960. In case my pet is found in any such situation, Team Animals With Humanity will take a fine upto Rs. 10,000/- depending on the situation and proceed with legal action.",style='List Bullet')
        doc.add_paragraph("I enter into this contract of my own free will and understand that this is a binding contract enforceable by civil law.",style='List Bullet')
        doc.save(self.file_path)
    def Append_data(self):
        data=[Councler.get(),dt.now().strftime("%d.%m.%y %I:%m %p"),'Tag.get()',Gender.get(),Age.get(),Color.get(),Breed.get(),Health.get(),Vaccination.get(),Sterilisation.get(),Caretaker.get(),CaretakerContact.get(),CaretakerWhatsapp.get(),Email.get(),LocalAdd.get(),PermanentAdd.get(),Adopter.get(),AdopterContact.get(),AdopterWhatsapp.get(),Email1.get(),Adoptor_ID.get(),AdopterLocalAdd.get(),PermanentAdd.get(),Plans.get("1.0","end-1c"),Owned.get(),Alone.get(),NotHome.get()]
        try:
                file=open(self.data_path,'a') 
        except PermissionError:
                messagebox.showerror('ERROR',"The data base file is locked as it may be in use by another application please close that instance and try agian ")
                return None
        Writer=writer(file)
        Writer.writerow(data)
        file.close()
        messagebox.showinfo("success","data saved") 
    def clear(self):
        Councler.delete(0,END)
        Gender.delete(0,END)
        Age.delete(0,END)
        Color.delete(0,END)
        Breed.delete(0,END)
        #Tag.delete(0,END)
        Health.delete(0,END)
        Vaccination.delete(0,END)
        Sterilisation.delete(0,END)
        Caretaker.delete(0,END)
        CaretakerContact.delete(0,END)
        CaretakerWhatsapp.delete(0,END)
        Email.delete(0,END)
        ID.delete(0,END)
        LocalAdd.delete(0,END)
        PermanentAdd.delete(0,END)
        Adopter.delete(0,END)
        AdopterContact.delete(0,END)
        AdopterWhatsapp.delete(0,END)
        Adoptor_ID.delete(0,END)
        Email1.delete(0,END)
        AdopterLocalAdd.delete(0,END)
        PermanentAdd.delete(0,END)
        Plans.delete("1.0","end")
        Owned.delete(0,END)
        Alone.delete(0,END)
        NotHome.delete(0,END)
        
def call_backend():
    back=BackEnd()
    back.Write_form()
    back.Append_data()
    back.clear()
# This is the front end of the application
##function to show the hindi version of T&C
def translate():
    new=Toplevel()
    new.iconphoto(False,icon)
    new.title("नियम शर्तें और सहमति प्रपत्र")
    Label(new,text="एडॉप्टर द्वारा सहमति",font=("Arial",20,"bold")).pack()
    Label(new,text="1) मैं पिल्ला/बिल्ली के बच्चे को अपने जोखिम और अपनी जिम्मेदारी पर गोद ले रहा हूं। मैंने परिवार के अन्य सदस्यों से परामर्श किया है और वे पिल्ला/बिल्ली के बच्चे को गोद लेने के लिए सहमत हो गए हैं।",font=("Arial",15,"bold")).pack()
    Label(new,text='मैं यह सुनिश्चित करूंगा कि गोद लिए गए पालतू जानवर को गोद लेने के बाद पशु चिकित्सक द्वारा पूरी तरह से जांच की जाए।',font=("Arial",15,"bold")).pack()
    Label(new,text='2) मैं यह सुनिश्चित करूंगा कि मेरे द्वारा गोद लिए गए पशु को स्वच्छ, हवादार परिसर में रखा जाए, ठीक से खिलाया जाए और नियमित व्यायाम किया जाए।',font=("Arial",15,"bold")).pack()
    Label(new,text='3) यदि मेरे द्वारा गोद लिया गया जानवर बीमार हो जाता है, तो मैं पशु चिकित्सक से परामर्श लूंगा। मैं यह भी सुनिश्चित करूंगा कि पशु चिकित्सक द्वारा बताए गए कृमिनाशक और टीकाकरण कार्यक्रम का पालन किया जाए।',font=("Arial",15,"bold")).pack()
    Label(new,text='4) मुझे इस बात की पूरी जानकारी है कि प्रारंभिक जांच के दौरान कुछ बीमारियों जैसे गैस्ट्रो-एंटराइटिस, रेबीज, डिस्टेंपर, सांस की बीमारियों आदि का निदान पशु चिकित्सक द्वारा नहीं किया जा सकता है।',font=("Arial",15,"bold")).pack()
    Label(new,text='जिस जानवर को मैंने गोद लिया है, अगर गोद लेने के कुछ दिनों के बाद उसमें किसी बीमारी के लक्षण दिखाई देते हैं, तो मैं पशु चिकित्सक से पालतू जानवर का इलाज करवाऊंगा।',font=("Arial",15,"bold")).pack()
    Label(new,text='नियम और शर्तें',font=("Arial",20,"bold")).pack()
    Label(new,text='1) मैं पालतू जानवर को हर समय कठोर परिस्थितियों में बंधा या बाहर नहीं रखूंगा या लंबे समय तक अकेला नहीं रखूंगा।',font=("Arial",15,"bold")).pack()
    Label(new,text='2) चाहे मैं नर या मादा पिल्ले/बिल्ली के बच्चे को गोद लूं, पालतू जानवरों के अच्छे स्वास्थ्य को सुनिश्चित करने के लिए मैं इसे न्यूट्रेड/स्पाय करवाऊंगा।',font=("Arial",15,"bold")).pack()
    Label(new,text='3) यदि कुत्ते के स्वामित्व को बदलने की आवश्यकता है, तो मैं केयरटेकर/पालक और टीम A.w.h को सूचित करूंगा और प्रक्रियाओं का पालन किया जाएगा।',font=("Arial",15,"bold")).pack()
    Label(new,text='4) मुझे पता है कि गोद लिए कुत्ते को छोड़ने पर पशु क्रूरता निवारण अधिनियम, 1960 के तहत जुर्माना लगेगा। टीम एनिमल्स विथ ह्यूमैनिटी ऐसा करने पर दत्तक कुत्ते के खिलाफ कानूनी कार्रवाई की मांग कर सकती है।',font=("Arial",15,"bold")).pack()
    Label(new,text='5) मैं अपनी इच्छा से गोद लिए गए पालतू पशु का नियमानुसार नगर निगम में पंजीकरण कराऊंगा।',font=("Arial",15,"bold")).pack()
    Label(new,text='6) मुझे पता है कि उचित परामर्श और परामर्श के साथ पालतू जानवर को गोद लेने की लागत शून्य रुपये (रु. 0/-) है।',font=("Arial",15,"bold")).pack()
    Label(new,text='7) मैं मानता हूं कि गोद लिए गए पालतू जानवर की जीवन भर की अवधि में, टीम एनिमल्स विद ह्यूमैनिटी और केयरटेकर/पालक को यह निरीक्षण करने का अधिकार है कि मैं जानवर को घर पर कैसे ',font=("Arial",15,"bold")).pack()
    Label(new,text='रख रहा हूं, साथ ही मैं अपने पालतू जानवर को अन्य जगहों पर डिजिटल रूप से ले जा रहा हूं। या बिना किसी पूर्व सूचना के भौतिक मुलाकातों द्वारा।',font=("Arial",15,"bold")).pack()
    Label(new,text='मैं टीम एनिमल्स विद ह्यूमैनिटी को गोद लिए गए पालतू जानवरों के बारे में नियमित अपडेट दूंगा। यदि क्रूरता निवारण अधिनियम, 1960 के तहत कोई उल्लंघन होता है, तो मुझे पता है कि टीम एनिमल्स विथ ह्यूमैनिटी जानवर को जब्त कर',font=("Arial",15,"bold")).pack()
    Label(new,text='सकती है या कानून के अनुसार कार्रवाई कर सकती है।',font=("Arial",15,"bold")).pack()
    Label(new,text='यदि पिल्ला/बिल्ली का बच्चा/पालतू पशु मालिक की लापरवाही के कारण लावारिस, अस्वस्थ, बुरी स्थिति में या मृत पाया जाता है, तो टीम एनिमल्स ',font=("Arial",15,"bold")).pack()
    Label(new,text='विथ ह्यूमैनिटी रुपये का जुर्माना ले सकती है। 10,000/- और दत्तक ग्रहण करने वाले पर कानूनी कार्रवाई के लिए आगे बढ़ें।',font=("Arial",15,"bold")).pack()
    Label(new,text="शर्तों पर हस्ताक्षर करने के बाद, यदि मैं (दत्तक) अपनाए गए पालतू जानवर को लौटाता हूं, तो मैं (दत्तक)  5000/- रुपये तक की राशि का भुगतान करने के लिए उत्तरदायी होगा लौटाने पर।",font=("Arial",15,"bold")).pack()
    Label(new,text=" मैं (दत्तक) गोद लिए गए पालतू जानवर को केवल टीम AWH को मानवता के साथ लौटाऊंगा और इसे नहीं छोड़ूंगा।",font=("Arial",15,"bold")).pack()
    Button(new,text="ठीक",command=new.destroy).pack()


## primary
window=Tk()
icon=PhotoImage(file=os.path.join(os.getcwd(),'icon.png'))
window.iconphoto(False,icon)
window.title('ADOPTION FORM')
#window.geometry('2')
window.protocol("WM_DELETE_WINDOW", window.destroy)
Label(window,text="Counselor name",font=("Nimbus Sans Narrow",15)).grid(sticky="E",row=0,column=0)
Councler=Entry(window)
Councler.grid(sticky="W",row=0,column=1)
Label(window,text="Description of the Animal:",font=("Arial",15,"bold","underline")).grid(sticky="W",row=1,column=1)
#sex.grid(sticky="W",row=2,column=1)
#Label(window,text="Tag Number",font=("Nimbus Sans Narrow",15)).grid(sticky="E",row=3,column=0)
#Tag=Entry(window)
#Tag.grid(sticky="W",row=3,column=1)
Label(window,text='Gender',font=("Nimbus Sans Narrow",15)).grid(sticky="E",row=2,column=0)
Gender=Entry(window)
Gender.grid(sticky="W",row=2,column=1)
Label(window,text='Age',font=("Nimbus Sans Narrow",15)).grid(sticky="E",row=2,column=2)
Age=Entry(window)
Age.grid(sticky="W",row=2,column=3)
Label(window,text='Colour',font=("Arial",15)).grid(sticky="E",row=3,column=0)
Color=Entry(window)
Color.grid(sticky="W",row=3,column=1)
Label(window,text='Breed',font=("Arial",15)).grid(sticky="E",row=3,column=2)
Breed=Entry(window)
#Lable(window,text='Tag Number',font=("Arial",15)).grid(sticky="E",row=3,column=2)
Breed.grid(sticky="W",row=3,column=3)
Label(window,text='Physically Fitness Status',font=("Arial",15)).grid(sticky="E",row=4,column=0)
Health=Entry(window)
Health.grid(sticky="W",row=4,column=1)
Label(window,text="Vaccination status",font=("Nimbus Sans Narrow",15)).grid(sticky="E",row=4,column=2)
Vaccination=Entry(window)
Vaccination.grid(sticky="E",row=4,column=3)
Label(window,text="Sterilisation Status",font=("Nimbus Sans Narrow",15)).grid(sticky="E",row=5,column=0)
Sterilisation=Entry(window)
Sterilisation.grid(sticky="W",row=5,column=1)
Button(window,text="Photo Of Animal",command=Camara(0).New_window).grid(row=5,column=2)
Label(window,text="Specifics of the Caretaker/Foster",font=("Arial",15,"bold","underline")).grid(sticky="W",row=6,column=1)
Label(window,text='Caretaker/Foster’s name',font=("Arial",15)).grid(sticky="E",row=7,column=0)
Caretaker=Entry(window)
Caretaker.grid(sticky="W",row=7,column=1)
Label(window,text='Contact no',font=("Arial",15)).grid(sticky="E",row=8,column=0)
CaretakerContact=Entry(window)
CaretakerContact.grid(sticky="W",row=8,column=1)
Label(window,text='Contact no/Whatsapp',font=("Arial",15)).grid(sticky="E",row=8,column=2)
CaretakerWhatsapp=Entry(window)
CaretakerWhatsapp.grid(sticky="E",row=8,column=3)
Label(window,text='Email',font=("Arial",15)).grid(sticky="E",row=9,column=0)
Email=Entry(window)
Email.grid(sticky="W",row=9,column=1)
Label(window,text='Instagram/Facebook ID',font=("Arial",15)).grid(sticky="E",row=9,column=2)
ID=Entry(window)
ID.grid(sticky="W",row=9,column=3)
Label(window,text='Local Residence',font=("Arial",15)).grid(sticky="E",row=10,column=0)
LocalAdd=Entry(window)
LocalAdd.grid(sticky="W",row=10,column=1)
Button(window,text="Photo of Caretaker",command=Camara(1).New_window).grid(row=10,column=2)
SameVar = IntVar()
Same1=Checkbutton(window,text="same as local",font=("Arial",15),variable=SameVar,onvalue=True,offvalue=False)
### handle this in backend call SameVar.get() at time of submitting ##
Same1.grid(sticky="W",row=11,column=2)
Label(window,text='Permanent Residence',font=("Arial",15)).grid(sticky="E",row=11,column=0)
PermanentAdd=Entry(window)
PermanentAdd.grid(sticky="W",row=11,column=1)
Label(window,text="Specifics of the Adopter",font=("Arial",15,"bold","underline")).grid(sticky="W",row=13,column=1)
Label(window,text="Adopter's Name",font=("Arial",15)).grid(sticky="E",row=14,column=0)
Adopter=Entry(window)
Adopter.grid(sticky="W",row=14,column=1)
Label(window,text='Contact No',font=("Arial",15)).grid(sticky="E",row=15,column=0)
AdopterContact=Entry(window)
AdopterContact.grid(sticky="W",row=15,column=1)
Label(window,text='Contact No/Whatsapp',font=("Arial",15)).grid(sticky="E",row=15,column=2)
AdopterWhatsapp=Entry(window)
AdopterWhatsapp.grid(sticky="W",row=15,column=3)
Label(window,text='Instagram/Facebook ID',font=("Arial",15)).grid(sticky="E",row=16,column=0)
Adoptor_ID=Entry(window)
Adoptor_ID.grid(sticky="W",row=16,column=1)
Button(window,text="Photo of Adopter",command=Camara(2).New_window).grid(row=16,column=2)
Label(window,text='Email',font=("Arial",15)).grid(sticky="E",row=17,column=0)
Email1=Entry(window)
Email1.grid(sticky="W",row=17,column=1)
Label(window,text='Local Address',font=("Arial",15)).grid(sticky="E",row=18,column=0)
AdopterLocalAdd=Entry(window)
AdopterLocalAdd.grid(sticky="W",row=18,column=1)
SameVar1 = IntVar()
Same2=Checkbutton(window,text="same as local",font=("Arial",15),variable=SameVar1,onvalue=True,offvalue=False)
### handle this in backend call SameVar.get() at time of submitting ##
Same2.grid(sticky="W",row=19,column=2)
Label(window,text='Permanent Residence',font=("Arial",15)).grid(sticky="E",row=19,column=0)
AdopterPermanentAdd=Entry(window)
AdopterPermanentAdd.grid(sticky="W",row=19,column=1)
Label(window,text='What are your plans for your pet if you shift to another town/place?',font=("Arial",15)).grid(sticky="e",row=20,column=0,columnspan=2)
Plans=Text(window,height=3,width=45)
Plans.grid(sticky="W",row=20,column=2,columnspan=2)
Label(window,text='Have you had a pet before or have one right now?',font=("Arial",15)).grid(sticky="E",row=21,column=0)
Owned=Entry(window)
Owned.grid(sticky="W",row=21,column=1)
Label(window,text='Amount of time your pet may have to be alone in a day?',font=("Arial",15)).grid(sticky="E",row=22,column=0)
Alone=Entry(window)
Alone.grid(sticky="W",row=22,column=1)
Label(window,text='Who will take care of your pet if you go out of town temporarily?',font=("Arial",15)).grid(sticky="W",row=23,column=0)
NotHome=Entry(window)
NotHome.grid(sticky="W",row=23,column=1)
button=Button(window,text="save,print and clear",command=call_backend)
button.grid(row=24,column=1)
backend=BackEnd()
backend.Test_file()

##T&C window
Terms_window=Toplevel()
Terms_window.iconphoto(False,icon)
Terms_window.title('Terms and Conditions and Consent form')
Label(Terms_window,text='CONSENT BY ADOPTER',font=("Arial", 25,"bold")).pack()
Label(Terms_window,text='1) I am adopting the puppy/kitten at my own risk and my responsibility. I have consulted other members of the family and they have agreed to adopt the pup/kitten.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='I will make sure that the adopted pet gets checked thoroughly by the Vet after adoption.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='2) I will ensure that the animal adopted by me is kept in clean, well-ventilated premises, properly fed and given regular exercise.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='3)In case the animal adopted by me falls ill, I will consult a vet. I will also ensure that the deworming and the vaccination schedule advised by the vet is followed.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='4) I am fully aware that some diseases like gastro-enteritis, rabies, distemper, respiratory diseases, etc. cannot be diagnosed by a vet during the preliminary checkup.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='If the animal that I have adopted shows signs of some illness after a few days of adoption, then I will get the pet treated from a vet.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='Terms and Conditions',font=('Arial',25,"bold")).pack()
#Label(Terms_window,text='1) I shall not hold the organizers of the adoption camp responsible if the animal shows sign of illness or dies after adoption.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='1) 1 will not keep the pet tied or outside in harsh conditions all the time or all by itself for long stretches of time.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='2) Whether I adopt a male or a female puppy/kitten, I will get it neutered/ spayed to ensure good health of the pet.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='3) In case the ownership of the dog needs to be changed, I will inform the CARETAKERS/FOSTERS and Team Animals with Humanity and the procedures will be followed.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='4) I am aware that Abandoning an adopted dog will attract penalty under Prevention of Cruelty to Animals Act, 1960. Team Animals With Humanity can seek legal actions against the Adopter if done so.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='5) I will register the pet I adopted at my will with the Municipal Corporation as per the rules. ',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='6) I\'m aware that the pet adoption is at Zero Rupees (Rs. 0/-) cost with proper counseling & consultation.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='7) I agree that over the lifetime period of the Adopted Pet, Team Animals With Humanity and the Caretaker/Foster have the right to inspect the manner in which I am keeping the animal at home',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='along with other places I take my pet to, digitally or by physical meet ups WITHOUT PRIOR NOTICE',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='I will give Team Animals With Humanity regular updates of the Adopted Pet. If there are any violations under the Prevention of Cruelty Act, 1960,',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='I am aware that Team Animals With Humanity may confiscate the animal or take action as per the law.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='In case the puppy/kitten/pet is found abandoned, in a unhealthy, bad condition or dead due to negligence of the owner,',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='Team Animals with Humanity can take a fine of Rs. 10,000/- and proceed with legal action on the Adopter',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='After signing to the terms, in case, I (adopter) return the Adopted Pet, I (adopter) will be liable to pay an amount up to Rs. 5000/- if returned. ',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='I (adopter) will return the Adopted Pet ONLY to Team Animals with Humanity and won\'t abandon it.',font=("Arial",15,"bold")).pack()
Label(Terms_window,text='I enter into this contract of my own free will and understand that this is a binding contract enforceable by civil law.',font=("Arial",15,"bold")).pack()
check=Checkbutton(Terms_window,text='I consent to the above terms',font=("Arial",15,"bold"))
check.pack()
Button(Terms_window,text='translate to hindi',command=translate).pack()
Terms_window.mainloop()

if __name__=='__main__':
    ##preform backend prequisites here## 
    window.mainloop()

