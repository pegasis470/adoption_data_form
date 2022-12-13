from csv import *
from tkinter import *
from tkinter import messagebox
from datetime import datetime as dt
import pandas as pd
import datetime
import os
date=datetime.date.today()
filename=str(date)+'.csv'
path=os.path.join(os.getcwd(),'data',filename)
try:
        file=pd.read_csv(path)
except FileNotFoundError :
        open_file=open(path,'a')
        Writer=writer(open_file)
        Writer.writerow(['Date','Kind of Animal','Sex','Age','Color','Breed',"Physically Fit",'Health Acknowledgement','Ongoing Treatment','Veterinarian name','Parent/adopter name','Contact no','Contact no. 2','Email','Local Residence','Permanent residence','Adopter\'s name','Contact no','Contact no.2','Line of work','Email','Local Residence','Permanent Residence','incase of moving','pet before or currently','needs to be alone for','when not home','want a gaurd dog','Adopter’s Name','Phone no','Parent/adopter Name',' Phone no.'])
        open_file.close()

window=Tk()
window.title('ADOPTION FORM')
label1=Label(window,text='Description of the Animal',font=25)
label2=Label(window,text='Kind of Animal')
entry1=Entry(window)
label3=Label(window,text='Sex')
entry2=Entry(window)
label4=Label(window,text='Age')
label5=Label(window,text='color')
label6=Label(window,text='Breed')
lable7=Label(window,text='Physically fit')
menu=StringVar()
drop = OptionMenu(window,menu,*['yes','no'] )
label1.grid(row=0,column=1)
label2.grid(row=1,column=0)
entry1.grid(row=1,column=1)	
label3.grid(row=2,column=0)
entry2.grid(row=2,column=1)
label4.grid(row=2,column=2)
drop.grid(row=3,column=0)

Terms_window=Toplevel()
Terms_window.title('Terms and Conditions and Consent form')
Label(Terms_window,text='Terms and Conditions',font=('Arial',25)).pack()
Label(Terms_window,text='1) I shall not hold the organizers of the adoption camp responsible if the animal shows sign of illness or dies after adoption.',font=22).pack()
Label(Terms_window,text='2) I will not keep it tied or all by itself for long stretches of time.',font=22).pack()
Label(Terms_window,text='3) Whether I adopt a male or a female puppy/kitten, I will get it neutered/ spayed after it reaches the age of 7 months.',font=22).pack()
Label(Terms_window,text='4) In case the ownership of the dog needs to be changed, the CARETAKERS/ FOSTERS and Team Animals with Humanity will be notified and procedures will be followed.',font=22).pack()
Label(Terms_window,text=' I am aware that abandoning an adopted dog will attract penalty under Prevention of Cruelty to Animals Act.',font=22).pack()
Label(Terms_window,text='5) I will register the dog with the Municipal Corporation as per the rules.',font=22).pack()
Label(Terms_window,text='6) I have read the relevant sections of the Prevention of Cruelty Act, 1990 (Gol)* (Annex I), and am aware of the provisions of the Act.',font=22).pack()
Label(Terms_window,text='7) I agree that over the next six months, the organizers have the right to inspect the manner in which I am keeping the animal, without prior notice.',font=22).pack()
Label(Terms_window,text=' If there are any violations under the Prevention of Cruelty Act, 1960 (Gol), I am aware that the organizers may confiscate the animal or take action as per the law.',font=22).pack()
Label(Terms_window,text='').pack()
Label(Terms_window,text='In case the puppy/ kitten is found abandoned, in a bad condition or dead due to negligence of the owner,\nTeam Animals with Humanity can take a fine of Rs. 10,000/- and proceed with legal action on the adopter.',font=22).pack()
Label(Terms_window,text='In case, I (adopter) return the puppy/kitten, I (adopter) will be liable to pay a amount of Rs. 5000/-\nif returned within 1 week after adoption and Rs. 3000/- thereafter to Team Animals with Humanity.',font=22).pack()
Label(Terms_window,text='I enter into this contract of my own free will and understand that this is a binding contract enforceable by civil law.',font=22).pack()

#Terms_window.mainloop()
#Terms_window=Tk()
Label(Terms_window,text='CONSENT BY ADOPTER',font=("Arial", 25)).pack()
Label(Terms_window,text='1) I am adopting the puppy/kitten at my own risk and my responsibility. I have consulted other members of the family and they have agreed to adopt the pup/kitten.',font=22).pack()
Label(Terms_window,text='I have made sure that the puppy has been checked thoroughly by the Vet before adoption.',font=22).pack()
Label(Terms_window,text='2) I will ensure that the animal adopted by me is kept in clean, well-ventilated premises, properly fed and given regular exercise.',font=22).pack()
Label(Terms_window,text='3)In case the animal adopted by me falls ill, I will consult a vet. I will also ensure that the deworming and the vaccination schedule advised by the vet is followed.',font=22).pack()	
Label(Terms_window,text='4) I am fully aware that some diseases like gastro-enteritis, rabies, distemper, respiratory diseases, etc. cannot be diagnosed by a vet during the preliminary checkup.',font=22).pack()
Label(Terms_window,text='If the animal that I have adopted shows signs of some illness after a few days of adoption, then I will get it treated from a vet.',font=22).pack()
check=Checkbutton(Terms_window,text='I consent to the above terms',font=22)
check.pack()
Button(Terms_window,text='save',command=check.deselect).pack()
Terms_window.mainloop()

