import tkinter.font
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tensorflow as tf
from tkinter import filedialog
import cv2

model2 = tf.keras.models.load_model(r'malaria/malaria.h5')
model3 = tf.keras.models.load_model(r'Covid_Pnemonia/Covid1.h5')
model4 = tf.keras.models.load_model(r'brain_tumor/tumrmodel.h5')
model5 = tf.keras.models.load_model(r'Cancer/cancer1.h5')
model6 = tf.keras.models.load_model(r'Chest xray Abnormality/xray_cxr.h5')
model7 = tf.keras.models.load_model(r'brain_tumor_classification/brain_tumor_classification.h5')
model8 = tf.keras.models.load_model(r'Eye Dibaties/retinonew.h5')
model9 = tf.keras.models.load_model(r'bactarial_vs_covid/bactvirus.h5')

root = Tk()
root.geometry("1024x750")
root.title("Medical App")
root.iconbitmap(r"common/icon.ico")
notebook = ttk.Notebook(root)
root.maxsize(1024, 750)
root.minsize(1024, 750)

# Main
frame1 = Frame(notebook, width=1020, height=745)
frame1.grid(row=0, column=0)
notebook.add(frame1, text="  Main  ")

# Malaria part
frame2 = Frame(notebook, width=1020, height=745)
frame2.grid(row=1, column=0)
notebook.add(frame2, text="  Malaria  ")
notebook.grid(row=0, column=0)

# Covid / Pnemonia
frame3 = Frame(notebook, width=1020, height=745)
frame3.grid(row=1, column=0)
notebook.add(frame3, text="  Covid-19/Pneumonia  ")
notebook.grid(row=0, column=0)

# Brain Tumor
frame4 = Frame(notebook, width=1020, height=745)
frame4.grid(row=1, column=0)
notebook.add(frame4, text="  Brain Tumor  ")
notebook.grid(row=0, column=0)

# Cancer
frame5 = Frame(notebook, width=1020, height=745)
frame5.grid(row=1, column=0)
notebook.add(frame5, text="  Malignant/Benign  ")
notebook.grid(row=0, column=0)

# Abnormal Chest X-ray
frame6 = Frame(notebook, width=1020, height=745)
frame6.grid(row=1, column=0)
notebook.add(frame6, text="  Abnormal Chest X-ray  ")
notebook.grid(row=0, column=0)

# Brain Tumor Classification
frame7 = Frame(notebook, width=1020, height=745)
frame7.grid(row=1, column=0)
notebook.add(frame7, text="  Brain Tumor Classification  ")
notebook.grid(row=0, column=0)

# Eye Diabetic
frame8 = Frame(notebook, width=1020, height=745)
frame8.grid(row=1, column=0)
notebook.add(frame8, text="  Diabetic Retinopathy  ")
notebook.grid(row=0, column=0)

# Bacterial vs Virus
frame9 = Frame(notebook, width=1020, height=745)
frame9.grid(row=1, column=0)
notebook.add(frame9, text="   Pnemonia Bacterial/Viral   ")
notebook.grid(row=0, column=0)

# Main
img1_load = ImageTk.PhotoImage(Image.open(r"common/icon.PNG").resize((100, 100)), Image.ANTIALIAS)
img1 = Label(frame1, image=img1_load, width=150, height=150)
img1.place(x=100, y=30)

label1_1 = Label(frame1, text="MEDSCAN", font=tkinter.font.Font(family="Helvetica", size=100, weight="bold"), fg="blue")
label1_1.place(x=230, y=30)

label1_2 = Label(frame1,
                 text="Diagnose your  MRI, CITY SCAN with us!  we  use  modern machine learning algorithms to predict out the best possible disease. output from   model  is  not  100%   true,  it  all  depends  on  the  accuracy of model, data   on which   model is   train   on,  quality   of training data,   quality of input image, type of disease and other factors.",
                 font=tkinter.font.Font(family="Helvetica", size=20, weight="bold"), fg="black", wraplength=900,
                 justify=LEFT)
label1_2.place(x=50, y=200)


# Cancer
# Functions
def callback5(path):
    img5 = ImageTk.PhotoImage(Image.open(filename5_1).resize((250, 200), Image.ANTIALIAS))
    img5_5label.configure(image=img5)
    img5_5label.image = img5


def getfile5():
    global filename5_1
    try:
        filename5_1 = filedialog.askopenfilename(initialdir="C:/", title="Select A File", filetypes=(
            ("jpg file", "*.jpg"), ("png files", "*.png"), ("jpeg file", "*.jpeg")))
        callback5(filename5_1)
    except:
        filename5_1 = r"common/NAN.jpg"
        callback5(filename5_1)
    callback5_1()
    root.bind("<Return>", callback5)


def callback5_1():
    filename3 = filename5_1[::-1]
    filename4 = ""
    filename5 = "/"
    filename4 = filename3.find(filename5)
    filename4 = filename3[0:filename4]
    filename4 = filename4[::-1]
    label5_predict.config(text=filename4)


def prediction5label1():
    label5_11.config(text=prediction5label)
    label5_12.config(text=str(prediction5Accuracy) + "%")


def predict5(img):
    global prediction5
    global prediction5label
    global prediction5Accuracy
    image_array2 = cv2.imread(img)
    new_array2 = cv2.resize(image_array2, (200, 200))
    new_array2 = new_array2.reshape(-1, 200, 200, 3)
    new_array2 = [new_array2 / 255.0]
    prediction5 = model5.predict(new_array2)
    prediction5 = prediction5[0]
    benign = prediction5[0]
    malignant = prediction5[1]
    if malignant >= benign:
        prediction5label = "Malignant"
        prediction5Accuracy = malignant * 100
    else:
        prediction5label = "Benign"
        prediction5Accuracy = benign * 100
    prediction5Accuracy = round(prediction5Accuracy, 2)
    prediction5label1()
    root.bind("<Return>", prediction5label1)


# left Porition
width3 = 110
height3 = 110

img5_1i = ImageTk.PhotoImage(Image.open(r"Cancer/mal (1).jpg").resize((110, 110)), Image.ANTIALIAS)
img5_1 = Label(frame5, image=img5_1i, width=width3, height=height3)
img5_2i = ImageTk.PhotoImage(Image.open(r"Cancer/be.jpg").resize((110, 110)), Image.ANTIALIAS)
img5_2 = Label(frame5, image=img5_2i, width=width3, height=height3)
img5_3i = ImageTk.PhotoImage(Image.open(r"Cancer/mal (2).jpg").resize((110, 110)), Image.ANTIALIAS)
img5_3 = Label(frame5, image=img5_3i, width=width3, height=height3)

label5 = Label(frame5, text="INPUT EXAMPLE", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
img5_1label = Label(frame5, text="Example 1", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img5_2label = Label(frame5, text="Example 2", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img5_3label = Label(frame5, text="Example 3", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))

img5_1tag = Label(frame5, text="Malignant", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img5_2tag = Label(frame5, text="Benign", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img5_3tag = Label(frame5, text="Malignant", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))

label5.place(x=175, y=10)
img5_1label.place(x=40, y=50)
img5_2label.place(x=220, y=50)
img5_3label.place(x=400, y=50)
img5_1.place(x=20, y=75)
img5_2.place(x=200, y=75)
img5_3.place(x=380, y=75)
img5_1tag.place(x=50, y=190)
img5_2tag.place(x=235, y=190)
img5_3tag.place(x=410, y=190)

# About
label5_61 = Label(frame5, text="About Malignant and Benign",
                  font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label5_61.place(x=135, y=220)
label5_6 = Label(frame5, wraplength=500, justify=LEFT, text="""Malignant
Our bodies constantly produce new cells to replace old ones. Sometimes, DNA gets damaged in the process, so new cells develop abnormally. Instead of dying off, they continue to multiply faster than the immune system can handle, forming a tumor.
Cancer cells can break away from tumors and travel through the bloodstream or lymphatic system to other parts of the body.

Benign
Benign tumors aren’t cancerous. They won’t invade surrounding tissue or spread elsewhere.
Even so, they can cause serious problems when they grow near vital organs, press on a nerve, or restrict blood flow. Benign tumors usually respond well to treatment.
""")
label5_6.place(x=5, y=250)

# treatment
label5_91 = Label(frame5, text="Treatment", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label5_9 = Label(frame5, wraplength=500, justify=LEFT, text="""Malignant
Treatment for cancerous tumors depends on many factors, such as where the primary tumor is located and whether it’s spread. A pathology report can reveal specific information about the tumor to help guide treatment, which may include:
surgery
radiation therapy
chemotherapy
targeted therapy
immunotherapy, also known as biological therapy

Benign
In many cases, benign tumors need no treatment. Doctors may simply use "watchful waiting" to make sure they cause no problems. But treatment may be needed if symptoms are a problem. Surgery is a common type of treatment for benign tumors. The goal is to remove the tumor without damaging surrounding tissues. Other types of treatment may include medication or radiation.
""")
label5_9.place(x=5, y=461)
label5_91.place(x=185, y=435)

# Right Portion
label5_10 = Label(frame5, text="MALIGNANT/BENIGN PREDICTION",
                  font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label5_10.place(x=600, y=10)

Button5_1 = Button(frame5, text="Upload Image", command=getfile5,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button5_1.place(x=580, y=270)
Button5_1 = Button(frame5, text="Upload Image", command=getfile5,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button5_1.place(x=580, y=270)

label5_13 = Label(frame5, text="File name:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label5_13.place(x=580, y=350)

label5_14 = Label(frame5, text="Prediction:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label5_14.place(x=580, y=390)

label5_13 = Label(frame5, text="Accuracy:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label5_13.place(x=580, y=430)

filename5 = r"common/NAN.jpg"
img5_5i = ImageTk.PhotoImage(Image.open(filename5).resize((250, 200), Image.ANTIALIAS))
img5_5label = Label(frame5, image=img5_5i, height=200, width=250, relief="solid")
img5_5label.place(x=635, y=50)

# model
try:
    Button5_2 = Button(frame5, text="Predict", command=lambda: predict5(filename5_1),
                       font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                       relief="solid", activebackground="white")
    Button5_2.place(x=800, y=270)

except:
    print("error")

try:
    label5_predict = Label(frame5, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label5_11 = Label(frame5, text=prediction5label, font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label5_12 = Label(frame5, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
except:
    label5_11 = Label(frame5, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label5_12 = Label(frame5, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label5_predict = Label(frame5, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label5_predict.place(x=690, y=350)
label5_11.place(x=690, y=390)
label5_12.place(x=690, y=430)

# border
border5_2 = Label(frame5, text="", bg="black", bd=1, height=745)
border5_2.place(x=510, y=0)

img5_4 = ImageTk.PhotoImage(Image.open(r"malaria/normal1.png").resize((20, 1)), Image.ANTIALIAS)
border5_1 = Label(frame5, image=img5_4, bg="black", bd=1, width=510, height=1)
border5_1.place(x=0, y=210)


# Brain Tumor Function
def callback4(path4):
    img4 = ImageTk.PhotoImage(Image.open(filename4_1).resize((250, 200), Image.ANTIALIAS))
    img4_5label.configure(image=img4)
    img4_5label.image = img4


def getfile4():
    global filename4_1
    try:
        filename4_1 = filedialog.askopenfilename(initialdir="C:/", title="Select A File", filetypes=(
            ("jpg file", "*.jpg"), ("png files", "*.png"), ("jpeg file", "*.jpeg")))
        callback4(filename4_1)
    except:
        filename4_1 = r"common/NAN.jpg"
        callback4(filename4_1)
    callback4_1()
    root.bind("<Return>", callback4)


def callback4_1():
    filename3 = filename4_1[::-1]
    filename4 = ""
    filename5 = "/"
    filename4 = filename3.find(filename5)
    filename4 = filename3[0:filename4]
    filename4 = filename4[::-1]
    label4_predict.config(text=filename4)


def prediction4label1():
    label4_11.config(text=prediction4label)
    label4_12.config(text=str(prediction4Accuracy) + "%")


def predict4(img):
    global prediction4
    global prediction4label
    global prediction4Accuracy
    image_array2 = cv2.imread(img)
    image_array2 = cv2.cvtColor(image_array2, cv2.COLOR_BGR2RGB)
    new_array2 = cv2.resize(image_array2, (224, 224))
    new_array2 = new_array2.reshape(-1, 224, 224, 3)
    new_array2 = [new_array2 / 255]
    prediction4 = model4.predict(new_array2)
    prediction4 = prediction4[0]
    no_Tumor = prediction4[0]
    Tumor = prediction4[1]
    if no_Tumor > Tumor:
        prediction4label = "Normal"
        prediction4Accuracy = no_Tumor * 100
    else:
        prediction4label = "Tumor"
        prediction4Accuracy = Tumor * 100
    prediction4Accuracy = round(prediction4Accuracy, 2)
    prediction4label1()
    root.bind("<Return>", prediction4label1)


# function end

# left

width3 = 110
height3 = 110

img4_1i = ImageTk.PhotoImage(Image.open(r"brain_tumor/Y251.JPG").resize((110, 110)), Image.ANTIALIAS)
img4_1 = Label(frame4, image=img4_1i, width=width3, height=height3)
img4_2i = ImageTk.PhotoImage(Image.open(r"brain_tumor/18 no.jpg").resize((110, 110)), Image.ANTIALIAS)
img4_2 = Label(frame4, image=img4_2i, width=width3, height=height3)
img4_3i = ImageTk.PhotoImage(Image.open(r"brain_tumor/Y258.JPG").resize((110, 110)), Image.ANTIALIAS)
img4_3 = Label(frame4, image=img4_3i, width=width3, height=height3)

label4 = Label(frame4, text="INPUT EXAMPLE", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
img4_1label = Label(frame4, text="Example 1", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img4_2label = Label(frame4, text="Example 2", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img4_3label = Label(frame4, text="Example 3", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))

img4_1tag = Label(frame4, text="Tumor", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img4_2tag = Label(frame4, text="Normal", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img4_3tag = Label(frame4, text="Tumor", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))

label4.place(x=175, y=10)
img4_1label.place(x=40, y=50)
img4_2label.place(x=220, y=50)
img4_3label.place(x=400, y=50)
img4_1.place(x=20, y=75)
img4_2.place(x=200, y=75)
img4_3.place(x=380, y=75)
img4_1tag.place(x=55, y=190)
img4_2tag.place(x=235, y=190)
img4_3tag.place(x=415, y=190)

# About
label4_61 = Label(frame4, text="About Brain Tumor", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label4_61.place(x=150, y=220)
label4_6 = Label(frame4, wraplength=500, justify=LEFT,
                 text="""A cancerous or non-cancerous mass or growth of abnormal cells in the brain.Tumours can start in the brain, or cancer elsewhere in the body can spread to the brain.Symptoms include new or increasingly strong headaches, blurred vision, loss of balance, confusion and seizures. In some cases, there may be no symptoms.""")
label4_6.place(x=5, y=250)

# symptoms
label4_71 = Label(frame4, text="Symptoms", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))

label4_7 = Label(frame4, wraplength=500, justify=LEFT, text="""Headache: can be acute or persistent
Muscular: difficulty walking, instability, muscle weakness, problems with coordination, weakness of one side of the body, or weakness of the arms and legs
Whole body: dizziness, fatigue, or vertigo
Gastrointestinal: nausea or vomiting
Sensory: pins and needles or reduced sensation of touch
Cognitive: inability to speak or understand language or mental confusion
Also common: blurred vision, difficulty speaking, personality change, seizures, or sleepiness
""")
label4_7.place(x=6, y=360)
label4_71.place(x=185, y=330)

# treatment
label4_91 = Label(frame4, text="Treatment", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label4_9 = Label(frame4, wraplength=500, justify=LEFT, text="""Treatment depends on stage
Treatments include surgery, radiation and chemotherapy.
Medications: Chemotherapy
Surgery: Craniotomy
Medical procedure: Tomotherapy and Radiation therapy""")
label4_9.place(x=5, y=526)
label4_91.place(x=185, y=500)
# right
label4_10 = Label(frame4, text="BRAIN TUMOR PREDICTION",
                  font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label4_10.place(x=650, y=10)

Button4_1 = Button(frame4, text="Upload Image", command=getfile4,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button4_1.place(x=580, y=270)
Button4_1 = Button(frame4, text="Upload Image", command=getfile4,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button4_1.place(x=580, y=270)

label4_13 = Label(frame4, text="File name:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label4_13.place(x=580, y=350)

label4_14 = Label(frame4, text="Prediction:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label4_14.place(x=580, y=390)

label4_13 = Label(frame4, text="Accuracy:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label4_13.place(x=580, y=430)

filename4 = r"common/NAN.jpg"
img4_5i = ImageTk.PhotoImage(Image.open(filename4).resize((250, 200), Image.ANTIALIAS))
img4_5label = Label(frame4, image=img4_5i, height=200, width=250, relief="solid")
img4_5label.place(x=635, y=50)

# model
try:
    Button4_2 = Button(frame4, text="Predict", command=lambda: predict4(filename4_1),
                       font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                       relief="solid", activebackground="white")
    Button4_2.place(x=800, y=270)

except:
    print("error")

try:
    label4_predict = Label(frame4, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label4_11 = Label(frame4, text=prediction4label, font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label4_12 = Label(frame4, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
except:
    label4_11 = Label(frame4, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label4_12 = Label(frame4, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label4_predict = Label(frame4, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label4_predict.place(x=690, y=350)
label4_11.place(x=690, y=390)
label4_12.place(x=690, y=430)

# border
border4_2 = Label(frame4, text="", bg="black", bd=1, height=745)
border4_2.place(x=510, y=0)

img4_4 = ImageTk.PhotoImage(Image.open(r"malaria/normal1.png").resize((20, 1)), Image.ANTIALIAS)
border4_1 = Label(frame4, image=img4_4, bg="black", bd=1, width=510, height=1)
border4_1.place(x=0, y=210)


# Covid-19/Pneumonia function place
def callback3(path3):
    img3 = ImageTk.PhotoImage(Image.open(filename3_1).resize((250, 200), Image.ANTIALIAS))
    img3_5label.configure(image=img3)
    img3_5label.image = img3


def getfile3():
    global filename3_1
    try:
        filename3_1 = filedialog.askopenfilename(initialdir="C:/", title="Select A File", filetypes=(
            ("jpg file", "*.jpg"), ("png files", "*.png"), ("jpeg file", "*.jpeg")))
        callback3(filename3_1)
    except:
        filename3_1 = r"common/NAN.jpg"
        callback3(filename3_1)
    callback3_1()
    root.bind("<Return>", callback3)


def callback3_1():
    filename3 = filename3_1[::-1]
    filename4 = ""
    filename5 = "/"
    filename4 = filename3.find(filename5)
    filename4 = filename3[0:filename4]
    filename4 = filename4[::-1]
    label3_predict.config(text=filename4)


def prediction3label1():
    label3_11.config(text=prediction3label)
    label3_12.config(text=str(prediction3Accuracy) + "%")


def predict3(img):
    global prediction3
    global prediction3label
    global prediction3Accuracy
    image_array2 = cv2.imread(img)
    new_array2 = cv2.resize(image_array2, (164, 164))
    new_array2 = new_array2.reshape(-1, 164, 164, 3)
    new_array2 = [new_array2 / 255.0]
    prediction3 = model3.predict(new_array2)
    prediction3 = prediction3[0]
    Covid = prediction3[0]
    Normal = prediction3[1]
    Pnemonia = prediction3[2]
    if Covid > Normal and Covid > Pnemonia:
        prediction3label = "Covid 19"
        prediction3Accuracy = Covid * 100
    elif Pnemonia > Normal and Pnemonia > Covid:
        prediction3label = "Pnemonia"
        prediction3Accuracy = Pnemonia * 100
    else:
        prediction3label = "Normal"
        prediction3Accuracy = Normal * 100
    prediction3Accuracy = round(prediction3Accuracy, 2)
    prediction3label1()
    root.bind("<Return>", prediction3label1)


# function end

# left

width3 = 110
height3 = 110

img3_1i = ImageTk.PhotoImage(Image.open(r"Covid_Pnemonia/COVID19(3).jpg").resize((110, 110)), Image.ANTIALIAS)
img3_1 = Label(frame3, image=img3_1i, width=width3, height=height3)
img3_2i = ImageTk.PhotoImage(Image.open(r"Covid_Pnemonia/NORMAL(0).jpg").resize((110, 110)), Image.ANTIALIAS)
img3_2 = Label(frame3, image=img3_2i, width=width3, height=height3)
img3_3i = ImageTk.PhotoImage(Image.open(r"Covid_Pnemonia/PNEUMONIA(0).jpg").resize((110, 110)), Image.ANTIALIAS)
img3_3 = Label(frame3, image=img3_3i, width=width3, height=height3)

label3 = Label(frame3, text="INPUT EXAMPLE", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
img3_1label = Label(frame3, text="Example 1", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img3_2label = Label(frame3, text="Example 2", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img3_3label = Label(frame3, text="Example 3", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))

img3_1tag = Label(frame3, text="Covid 19", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img3_2tag = Label(frame3, text="Normal", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img3_3tag = Label(frame3, text="Pneumonia", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))

label3.place(x=175, y=10)
img3_1label.place(x=40, y=50)
img3_2label.place(x=220, y=50)
img3_3label.place(x=400, y=50)
img3_1.place(x=20, y=75)
img3_2.place(x=200, y=75)
img3_3.place(x=380, y=75)
img3_1tag.place(x=55, y=190)
img3_2tag.place(x=235, y=190)
img3_3tag.place(x=400, y=190)

# About
label3_61 = Label(frame3, text="About Covid 19 and Pneumonia",
                  font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label3_61.place(x=100, y=220)
label3_6 = Label(frame3, wraplength=500, justify=LEFT, text="""Covid 19
Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.

Pneumonia
Infection that inflames air sacs in one or both lungs, which may fill with fluid.
With pneumonia, the air sacs may fill with fluid or pus. The infection can be life-threatening to anyone, but particularly to infants, children and people over 65.
Symptoms include a cough with phlegm or pus, fever, chills and difficulty breathing.
""")
label3_6.place(x=5, y=250)

# symptoms
label3_71 = Label(frame3, text="Symptoms", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))

label3_7 = Label(frame3, wraplength=500, justify=LEFT, text="""Covid 19
Most common symptoms are fever,dry cough and tiredness. Less common are aches and pains, sore throat, diarrhoea, conjunctivitis, headache,loss of taste or smell.

Pneumonia
Pain types: can be sharp in the chest
Whole body: fever, chills, dehydration, fatigue, loss of appetite, malaise, clammy skin, or sweating
Respiratory: fast breathing, shallow breathing, shortness of breath, or wheezing
""")
label3_7.place(x=6, y=418)
label3_71.place(x=185, y=392)

# treatment
label3_91 = Label(frame3, text="Treatment", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label3_9 = Label(frame3, wraplength=500, justify=LEFT, text="""Covid 19
Treatment for patients with mild/asymptomatic disease in home isolation
Patients must be in communication with a treating physician and promptly report in case of any worsening.
Continue the medications for other co-morbid illness after consulting the treating physician.

Pneumonia
Antibiotics can treat many forms of pneumonia. Some forms of pneumonia can be prevented by vaccines.""")
label3_9.place(x=5, y=580)
label3_91.place(x=185, y=559)
# right
label3_10 = Label(frame3, text="COVID 19/PNEUMONIA PREDICTION",
                  font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label3_10.place(x=600, y=10)

Button3_1 = Button(frame3, text="Upload Image", command=getfile3,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button3_1.place(x=580, y=270)
Button3_1 = Button(frame3, text="Upload Image", command=getfile3,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button3_1.place(x=580, y=270)

label3_13 = Label(frame3, text="File name:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label3_13.place(x=580, y=350)

label3_14 = Label(frame3, text="Prediction:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label3_14.place(x=580, y=390)

label3_13 = Label(frame3, text="Accuracy:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label3_13.place(x=580, y=430)

filename3 = r"common/NAN.jpg"
img3_5i = ImageTk.PhotoImage(Image.open(filename3).resize((250, 200), Image.ANTIALIAS))
img3_5label = Label(frame3, image=img3_5i, height=200, width=250, relief="solid")
img3_5label.place(x=635, y=50)

# model
try:
    Button3_2 = Button(frame3, text="Predict", command=lambda: predict3(filename3_1),
                       font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                       relief="solid", activebackground="white")
    Button3_2.place(x=800, y=270)

except:
    print("error")

try:
    label3_predict = Label(frame3, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label3_11 = Label(frame3, text=prediction3label, font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label3_12 = Label(frame3, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
except:
    label3_11 = Label(frame3, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label3_12 = Label(frame3, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label3_predict = Label(frame3, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label3_predict.place(x=690, y=350)
label3_11.place(x=690, y=390)
label3_12.place(x=690, y=430)

# border
border3_2 = Label(frame3, text="", bg="black", bd=1, height=745)
border3_2.place(x=510, y=0)

img3_4 = ImageTk.PhotoImage(Image.open(r"malaria/normal1.png").resize((20, 1)), Image.ANTIALIAS)
border3_1 = Label(frame3, image=img3_4, bg="black", bd=1, width=510, height=1)
border3_1.place(x=0, y=210)


# Malaria function place
def callback2(path2):
    img2 = ImageTk.PhotoImage(Image.open(filename2).resize((250, 200), Image.ANTIALIAS))
    img2_5label.configure(image=img2)
    img2_5label.image = img2


def getfile2():
    global filename2
    try:
        filename2 = filedialog.askopenfilename(initialdir="C:/", title="Select A File", filetypes=(
            ("jpg file", "*.jpg"), ("png files", "*.png"), ("jpeg file", "*.jpeg")))
        callback2(filename2)
    except:
        filename2 = r"common/NAN.jpg"
        callback2(filename2)
    callback2_1()
    root.bind("<Return>", callback2)


def callback2_1():
    filename3 = filename2[::-1]
    filename4 = ""
    filename5 = "/"
    filename4 = filename3.find(filename5)
    filename4 = filename3[0:filename4]
    filename4 = filename4[::-1]
    label2_predict.config(text=filename4)


def prediction2label1():
    label2_11.config(text=prediction2label)
    label2_12.config(text=str(prediction2Accuracy) + "%")


def predict2(img):
    global prediction2
    global prediction2label
    global prediction2Accuracy
    image_array2 = cv2.imread(img)
    image_array2 = cv2.cvtColor(image_array2, cv2.COLOR_BGR2RGB)
    new_array2 = cv2.resize(image_array2, (128, 128))
    new_array2 = new_array2.reshape(-1, 128, 128, 3)
    new_array2 = [new_array2]
    prediction2 = model2.predict(new_array2)
    prediction2 = prediction2[0]
    infected2 = prediction2[0]
    non_infected2 = prediction2[1]
    if infected2 > non_infected2:
        prediction2label = "INFECTED"
        prediction2Accuracy = infected2 * 100
    else:
        prediction2label = "Not Infected"
        prediction2Accuracy = non_infected2 * 100
    prediction2Accuracy = round(prediction2Accuracy, 2)
    prediction2label1()
    root.bind("<Return>", prediction2label1)


# function end


# left

width2 = 110
height2 = 110

img2_1i = ImageTk.PhotoImage(Image.open(r"malaria/normal1.png").resize((110, 110)), Image.ANTIALIAS)
img2_1 = Label(frame2, image=img2_1i, width=width2, height=height2)
img2_2i = ImageTk.PhotoImage(Image.open(r"malaria/infected.png").resize((110, 110)), Image.ANTIALIAS)
img2_2 = Label(frame2, image=img2_2i, width=width2, height=height2)
img2_3i = ImageTk.PhotoImage(Image.open(r"malaria/normal2.png").resize((110, 110)), Image.ANTIALIAS)
img2_3 = Label(frame2, image=img2_3i, width=width2, height=height2)

label2 = Label(frame2, text="INPUT EXAMPLE", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
img2_1label = Label(frame2, text="Example 1", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img2_2label = Label(frame2, text="Example 2", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img2_3label = Label(frame2, text="Example 3", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))

img2_1tag = Label(frame2, text="Normal", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img2_2tag = Label(frame2, text="Infected", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img2_3tag = Label(frame2, text="Normal", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))

label2.place(x=175, y=10)
img2_1label.place(x=40, y=50)
img2_2label.place(x=220, y=50)
img2_3label.place(x=400, y=50)
img2_1.place(x=20, y=75)
img2_2.place(x=200, y=75)
img2_3.place(x=380, y=75)
img2_1tag.place(x=55, y=190)
img2_2tag.place(x=235, y=190)
img2_3tag.place(x=415, y=190)

# About
label2_61 = Label(frame2, text="About Malaria", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label2_61.place(x=175, y=220)
label2_6 = Label(frame2, wraplength=500, justify=LEFT,
                 text="""A  disease caused  by a  plasmodium  parasite, transmitted bythe bite of infected mosquitoes. The severity of malaria varies based on the species of plasmodium. Symptoms are chills, fever and sweating, usually occurring a few weeks after being bitten.People travelling to areas where malaria is  common  typically  take protective  drugs before,  during and  after their  trip. Treatment includes antimalarial drugs.The above example show the picture of blood, using this type of pic, this model is going to predict Malaria.""")
label2_6.place(x=5, y=250)

# symptoms
label2_71 = Label(frame2, text="Symptoms", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label2_71.place(x=185, y=370)
label2_7 = Label(frame2, wraplength=500, justify=LEFT,
                 text="""Symptoms are chills, fever and sweating, usually occurring a few weeks after being bitten.""")
label2_7.place(x=5, y=400)
label2_8 = Label(frame2, wraplength=500, justify=LEFT, text="""Pain areas: in the abdomen or muscles
Whole body: chills, fatigue, fever, night sweats, shivering, or sweating
Gastrointestinal: diarrhoea, nausea, or vomiting
Also common: fast heart rate, headache, mental confusion, or pallor""")
label2_8.place(x=5, y=420)

# treatment
label2_91 = Label(frame2, text="Treatment", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label2_91.place(x=185, y=510)
label2_9 = Label(frame2, wraplength=500, justify=LEFT, text="Treatment consists of anti-parasitics")
label2_9.place(x=5, y=540)
label2_92 = Label(frame2, wraplength=500, justify=LEFT,
                  text="People travelling to areas where malaria is common typically take protective drugs before, during and after their trip. Treatment includes antimalarial drugs.")
label2_92.place(x=5, y=560)
label2_93 = Label(frame2, wraplength=500, justify=LEFT, text="""MEDICATION
Antiparasitic: Kills parasites.
AntibioticsStops: the growth of or kills bacteria.
""")
label2_93.place(x=5, y=600)

# right
label2_10 = Label(frame2, text="MALARIA PREDICTION", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label2_10.place(x=650, y=10)

Button2_1 = Button(frame2, text="Upload Image", command=getfile2,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button2_1.place(x=580, y=270)
Button2_1 = Button(frame2, text="Upload Image", command=getfile2,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button2_1.place(x=580, y=270)

label2_13 = Label(frame2, text="File name:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label2_13.place(x=580, y=350)

label2_14 = Label(frame2, text="Prediction:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label2_14.place(x=580, y=390)

label2_13 = Label(frame2, text="Accuracy:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label2_13.place(x=580, y=430)

filename2 = r"common/NAN.jpg"
img2_5i = ImageTk.PhotoImage(Image.open(filename2).resize((250, 200), Image.ANTIALIAS))
img2_5label = Label(frame2, image=img2_5i, height=200, width=250, relief="solid")
img2_5label.place(x=635, y=50)

# model
try:
    Button2_2 = Button(frame2, text="Predict", command=lambda: predict2(filename2),
                       font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                       relief="solid", activebackground="white")
    Button2_2.place(x=800, y=270)

except:
    print("error")

try:
    label2_predict = Label(frame2, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label2_11 = Label(frame2, text=prediction2label, font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label2_12 = Label(frame2, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
except:
    label2_11 = Label(frame2, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label2_12 = Label(frame2, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label2_predict = Label(frame2, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label2_predict.place(x=690, y=350)
label2_11.place(x=690, y=390)
label2_12.place(x=690, y=430)

# border
border2 = Label(frame2, text="", bg="black", bd=1, height=745)
border2.place(x=510, y=0)

img2_4 = ImageTk.PhotoImage(Image.open(r"malaria/normal1.png").resize((20, 1)), Image.ANTIALIAS)
border3 = Label(frame2, image=img2_4, bg="black", bd=1, width=510, height=1)
border3.place(x=0, y=210)


# Abnormal Chest X-ray
def callback6(path6):
    img6 = ImageTk.PhotoImage(Image.open(filename6_1).resize((250, 200), Image.ANTIALIAS))
    img6_5label.configure(image=img6)
    img6_5label.image = img6


def getfile6():
    global filename6_1
    try:
        filename6_1 = filedialog.askopenfilename(initialdir="C:/", title="Select A File", filetypes=(
            ("jpg file", "*.jpg"), ("png files", "*.png"), ("jpeg file", "*.jpeg")))
        callback6(filename6_1)
    except:
        filename6_1 = r"common/NAN.jpg"
        callback6(filename6_1)
    callback6_1()
    root.bind("<Return>", callback6)


def callback6_1():
    filename3 = filename6_1[::-1]
    filename4 = ""
    filename5 = "/"
    filename4 = filename3.find(filename5)
    filename4 = filename3[0:filename4]
    filename4 = filename4[::-1]
    label6_predict.config(text=filename4)


def prediction6label1():
    label6_11.config(text=prediction6label)
    label6_12.config(text=str(prediction6Accuracy) + "%")


def predict6(img):
    global prediction6
    global prediction6label
    global prediction6Accuracy
    image_array2 = cv2.imread(img)
    image_array2 = cv2.cvtColor(image_array2, cv2.COLOR_BGR2RGB)
    new_array2 = cv2.resize(image_array2, (256, 256))
    new_array2 = new_array2.reshape(-1, 256, 256, 3)
    prediction6 = model6.predict(new_array2)
    prediction6 = prediction6[0]
    abnormal = 1 - prediction6[0]
    normal6 = prediction6[0]
    if abnormal >= normal6:
        prediction6label = "Abnormal"
        prediction6Accuracy = abnormal * 100
    else:
        prediction6label = "Normal"
        prediction6Accuracy = normal6 * 100
    prediction6Accuracy = round(prediction6Accuracy, 2)
    prediction6label1()
    root.bind("<Return>", prediction6label1)


# function end

# left

width3 = 110
height3 = 110

img6_7i = ImageTk.PhotoImage(Image.open(r"Chest xray Abnormality/normal23.jpg").resize((110, 110)), Image.ANTIALIAS)
img6_1i = ImageTk.PhotoImage(Image.open(r"Chest xray Abnormality/Abnormal8.jpg").resize((110, 110)), Image.ANTIALIAS)
img6_1 = Label(frame6, image=img6_1i, width=width3, height=height3)
img6_2i = ImageTk.PhotoImage(Image.open(r"Chest xray Abnormality/normal14.jpg").resize((110, 110)), Image.ANTIALIAS)
img6_2 = Label(frame6, image=img6_2i, width=width3, height=height3)
img6_3i = ImageTk.PhotoImage(Image.open(r"Chest xray Abnormality/Abnormal9.jpg").resize((110, 110)), Image.ANTIALIAS)
img6_3 = Label(frame6, image=img6_3i, width=width3, height=height3)
img6_4i = ImageTk.PhotoImage(Image.open(r"Chest xray Abnormality/Abnormal19.jpg").resize((110, 110)), Image.ANTIALIAS)
img6_4 = Label(frame6, image=img6_4i, width=width3, height=height3)
img6_5i = ImageTk.PhotoImage(Image.open(r"Chest xray Abnormality/normal23.jpg").resize((110, 110)), Image.ANTIALIAS)
img6_5 = Label(frame6, image=img6_7i, width=width3, height=height3)
img6_6i = ImageTk.PhotoImage(Image.open(r"Chest xray Abnormality/Abnormal21.jpg").resize((110, 110)), Image.ANTIALIAS)
img6_6 = Label(frame6, image=img6_6i, width=width3, height=height3)

label6 = Label(frame6, text="INPUT EXAMPLE", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
img6_1label = Label(frame6, text="Example 1", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img6_2label = Label(frame6, text="Example 2", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img6_3label = Label(frame6, text="Example 3", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img6_4label = Label(frame6, text="Example 4", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img6_5label = Label(frame6, text="Example 5", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img6_6label = Label(frame6, text="Example 6", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))

img6_1tag = Label(frame6, text="Abnormal", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img6_2tag = Label(frame6, text="Normal", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img6_3tag = Label(frame6, text="Abnormal", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img6_4tag = Label(frame6, text="Abnormal", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img6_5tag = Label(frame6, text="Normal", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img6_6tag = Label(frame6, text="Abnormal", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))

label6.place(x=175, y=10)
img6_1label.place(x=40, y=50)
img6_2label.place(x=220, y=50)
img6_3label.place(x=400, y=50)
img6_1.place(x=20, y=75)
img6_2.place(x=200, y=75)
img6_3.place(x=380, y=75)
img6_1tag.place(x=50, y=190)
img6_2tag.place(x=235, y=190)
img6_3tag.place(x=410, y=190)

img6_4label.place(x=40, y=230)
img6_5label.place(x=220, y=230)
img6_6label.place(x=400, y=230)
img6_4.place(x=20, y=255)
img6_5.place(x=200, y=255)
img6_6.place(x=380, y=255)
img6_4tag.place(x=50, y=370)
img6_5tag.place(x=235, y=370)
img6_6tag.place(x=410, y=370)

# About
label6_61 = Label(frame6, text="About Chest X-ray Abnormality",
                  font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label6_61.place(x=100, y=400)
label6_6 = Label(frame6, wraplength=470, justify=LEFT, text="""If the X-ray images  show abnormalities, this means  that there is something unusual on the image of the chest. This is usually indicative of a problem, and could be immediately obvious,  such as a  broken or  fractured  rib, or  could simply  be a shadow  that needs further investigation.

An abnormal X-ray can also indicate the presence of the following abnormal conditions:
Pneumonia.
Excess fluid around the lung.
Bronchitis.
Asthma.
Cysts.
Heart failure.
Fluid around the heart.
Enlarged heart.
""")
label6_6.place(x=5, y=430)

# right
label6_10 = Label(frame6, text="CHEST X-RAY ABNORMALITY",
                  font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label6_10.place(x=620, y=10)

Button6_1 = Button(frame6, text="Upload Image", command=getfile6,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button6_1.place(x=580, y=270)
Button6_1 = Button(frame6, text="Upload Image", command=getfile6,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button6_1.place(x=580, y=270)

label6_13 = Label(frame6, text="File name:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label6_13.place(x=580, y=350)

label6_14 = Label(frame6, text="Prediction:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label6_14.place(x=580, y=390)

label6_13 = Label(frame6, text="Accuracy:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label6_13.place(x=580, y=430)

filename6 = r"common/NAN.jpg"
img6_5i = ImageTk.PhotoImage(Image.open(filename6).resize((250, 200), Image.ANTIALIAS))
img6_5label = Label(frame6, image=img6_5i, height=200, width=250, relief="solid")
img6_5label.place(x=635, y=50)

# model
try:
    Button6_2 = Button(frame6, text="Predict", command=lambda: predict6(filename6_1),
                       font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                       relief="solid", activebackground="white")
    Button6_2.place(x=800, y=270)

except:
    print("error")

try:
    label6_predict = Label(frame6, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label6_11 = Label(frame6, text=prediction6label, font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label6_12 = Label(frame6, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
except:
    label6_11 = Label(frame6, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label6_12 = Label(frame6, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label6_predict = Label(frame6, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label6_predict.place(x=690, y=350)
label6_11.place(x=690, y=390)
label6_12.place(x=690, y=430)

# border
border6_2 = Label(frame6, text="", bg="black", bd=1, height=745)
border6_2.place(x=510, y=0)

img6_4 = ImageTk.PhotoImage(Image.open(r"malaria/normal1.png").resize((20, 1)), Image.ANTIALIAS)
border6_1 = Label(frame6, image=img6_4, bg="black", bd=1, width=510, height=1)
border6_1.place(x=0, y=390)


# Brain Tumor Classification
def callback7(path7):
    img7 = ImageTk.PhotoImage(Image.open(filename7_1).resize((250, 200), Image.ANTIALIAS))
    img7_5label.configure(image=img7)
    img7_5label.image = img7


def getfile7():
    global filename7_1
    try:
        filename7_1 = filedialog.askopenfilename(initialdir="C:/", title="Select A File", filetypes=(
            ("jpg file", "*.jpg"), ("png files", "*.png"), ("jpeg file", "*.jpeg")))
        callback7(filename7_1)
    except:
        filename7_1 = r"common/NAN.jpg"
        callback7(filename7_1)
    callback7_1()
    root.bind("<Return>", callback7)


def callback7_1():
    filename3 = filename7_1[::-1]
    filename4 = ""
    filename5 = "/"
    filename4 = filename3.find(filename5)
    filename4 = filename3[0:filename4]
    filename4 = filename4[::-1]
    label7_predict.config(text=filename4)


def prediction7label1():
    label7_11.config(text=prediction7label)
    label7_12.config(text=str(prediction7Accuracy) + "%")


def predict7(img):
    global prediction7
    global prediction7label
    global prediction7Accuracy
    image_array2 = cv2.imread(img)
    new_array2 = cv2.resize(image_array2, (150, 150))
    new_array2 = new_array2.reshape(-1, 150, 150, 3)
    prediction7 = model7.predict(new_array2 / 255.0)
    prediction7 = prediction7[0]
    glioma_tumor = prediction7[0]
    no_tumor = prediction7[1]
    meningioma_tumor = prediction7[2]
    pituitary_tumor = prediction7[3]

    if (glioma_tumor > no_tumor) and (glioma_tumor > meningioma_tumor) and (glioma_tumor > pituitary_tumor):
        prediction7label = "Glioma Tumor"
        prediction7Accuracy = glioma_tumor * 100
    elif (no_tumor > glioma_tumor) and (no_tumor > meningioma_tumor) and (no_tumor > pituitary_tumor):
        prediction7label = "No Tumor"
        prediction7Accuracy = no_tumor * 100
    elif (meningioma_tumor > glioma_tumor) and (meningioma_tumor > no_tumor) and (meningioma_tumor > pituitary_tumor):
        prediction7label = "Meningioma Tumor"
        prediction7Accuracy = meningioma_tumor * 100
    else:
        prediction7label = "Pituitary Tumor"
        prediction7Accuracy = pituitary_tumor * 100
    prediction7Accuracy = round(prediction7Accuracy, 2)
    prediction7label1()
    root.bind("<Return>", prediction7label1)


# function end

# left

width3 = 110
height3 = 110

img7_8i = ImageTk.PhotoImage(Image.open(r"brain_tumor_classification/normal.jpg").resize((110, 110)), Image.ANTIALIAS)
img7_1i = ImageTk.PhotoImage(Image.open(r"brain_tumor_classification/glioma.jpg").resize((110, 110)), Image.ANTIALIAS)
img7_1 = Label(frame7, image=img7_1i, width=width3, height=height3)
img7_2i = ImageTk.PhotoImage(Image.open(r"brain_tumor_classification/no tumor2.jpg").resize((110, 110)),
                             Image.ANTIALIAS)
img7_2 = Label(frame7, image=img7_2i, width=width3, height=height3)
img7_3i = ImageTk.PhotoImage(Image.open(r"brain_tumor_classification/pituitary.jpg").resize((110, 110)),
                             Image.ANTIALIAS)
img7_3 = Label(frame7, image=img7_3i, width=width3, height=height3)
img7_4i = ImageTk.PhotoImage(Image.open(r"brain_tumor_classification/meningioma.jpg").resize((110, 110)),
                             Image.ANTIALIAS)
img7_4 = Label(frame7, image=img7_4i, width=width3, height=height3)
img7_5i = ImageTk.PhotoImage(Image.open(r"brain_tumor_classification/normal.jpg").resize((110, 110)), Image.ANTIALIAS)
img7_5 = Label(frame7, image=img7_8i, width=width3, height=height3)
img7_6i = ImageTk.PhotoImage(Image.open(r"brain_tumor_classification/glioma (2).jpg").resize((110, 110)),
                             Image.ANTIALIAS)
img7_6 = Label(frame7, image=img7_6i, width=width3, height=height3)

label7 = Label(frame7, text="INPUT EXAMPLE", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
img7_1label = Label(frame7, text="Example 1", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img7_2label = Label(frame7, text="Example 2", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img7_3label = Label(frame7, text="Example 3", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img7_4label = Label(frame7, text="Example 4", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img7_5label = Label(frame7, text="Example 5", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img7_6label = Label(frame7, text="Example 6", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))

img7_1tag = Label(frame7, text="Glioma", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img7_2tag = Label(frame7, text="Normal", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img7_3tag = Label(frame7, text="Pituitary", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img7_4tag = Label(frame7, text="Meningioma", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img7_5tag = Label(frame7, text="Normal", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img7_6tag = Label(frame7, text="Glioma", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))

label7.place(x=175, y=10)
img7_1label.place(x=40, y=50)
img7_2label.place(x=220, y=50)
img7_3label.place(x=400, y=50)
img7_1.place(x=20, y=75)
img7_2.place(x=200, y=75)
img7_3.place(x=380, y=75)
img7_1tag.place(x=50, y=190)
img7_2tag.place(x=235, y=190)
img7_3tag.place(x=410, y=190)

img7_4label.place(x=40, y=220)
img7_5label.place(x=220, y=220)
img7_6label.place(x=400, y=220)
img7_4.place(x=20, y=245)
img7_5.place(x=200, y=245)
img7_6.place(x=380, y=245)
img7_4tag.place(x=50, y=360)
img7_5tag.place(x=235, y=360)
img7_6tag.place(x=410, y=360)

# About
label7_61 = Label(frame7, text="About Brain Tumor", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label7_61.place(x=150, y=380)
label7_6 = Label(frame7, wraplength=500, justify=LEFT,
                 text="""A cancerous or non-cancerous mass or growth of abnormal cells in the brain.Tumours can start in the brain, or cancer elsewhere in the body can spread to the brain.Symptoms include new or increasingly strong headaches, blurred vision, loss of balance, confusion and seizures. In some cases, there may be no symptoms.""")
label7_6.place(x=5, y=410)

# symptoms
label7_71 = Label(frame7, text="Symptoms", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))

label7_7 = Label(frame7, wraplength=500, justify=LEFT, text="""Headache: can be acute or persistent
Muscular: difficulty walking, instability, muscle weakness, problems with coordination, weakness of one side of the body, or weakness of the arms and legs
Whole body: dizziness, fatigue, or vertigo
Gastrointestinal: nausea or vomiting
Sensory: pins and needles or reduced sensation of touch
Cognitive: inability to speak or understand language or mental confusion
Also common: blurred vision, difficulty speaking, personality change, seizures, or sleepiness
""")
label7_7.place(x=6, y=500)
label7_71.place(x=185, y=473)

# treatment
label7_91 = Label(frame7, text="Treatment", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label7_9 = Label(frame7, wraplength=500, justify=LEFT, text="""Treatment depends on stage
Treatments include surgery, radiation and chemotherapy.
Medications: Chemotherapy
Surgery: Craniotomy
Medical procedure: Tomotherapy and Radiation therapy""")
label7_9.place(x=5, y=646)
label7_91.place(x=185, y=620)

# right
label7_10 = Label(frame7, text="BRAIN TUMOR CLASSIFICATION",
                  font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label7_10.place(x=600, y=10)

Button7_1 = Button(frame7, text="Upload Image", command=getfile7,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button7_1.place(x=580, y=270)
Button7_1 = Button(frame7, text="Upload Image", command=getfile7,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button7_1.place(x=580, y=270)

label7_13 = Label(frame7, text="File name:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label7_13.place(x=580, y=350)

label7_14 = Label(frame7, text="Prediction:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label7_14.place(x=580, y=390)

label7_13 = Label(frame7, text="Accuracy:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label7_13.place(x=580, y=430)

filename7 = r"common/NAN.jpg"
img7_5i = ImageTk.PhotoImage(Image.open(filename7).resize((250, 200), Image.ANTIALIAS))
img7_5label = Label(frame7, image=img7_5i, height=200, width=250, relief="solid")
img7_5label.place(x=635, y=50)

# model
try:
    Button7_2 = Button(frame7, text="Predict", command=lambda: predict7(filename7_1),
                       font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                       relief="solid", activebackground="white")
    Button7_2.place(x=800, y=270)

except:
    print("error")

try:
    label7_predict = Label(frame7, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label7_11 = Label(frame7, text=prediction7label, font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label7_12 = Label(frame7, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
except:
    label7_11 = Label(frame7, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label7_12 = Label(frame7, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label7_predict = Label(frame7, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label7_predict.place(x=690, y=350)
label7_11.place(x=690, y=390)
label7_12.place(x=690, y=430)

# border
border7_2 = Label(frame7, text="", bg="black", bd=1, height=745)
border7_2.place(x=510, y=0)

img7_4 = ImageTk.PhotoImage(Image.open(r"malaria/normal1.png").resize((20, 1)), Image.ANTIALIAS)
border7_1 = Label(frame7, image=img7_4, bg="black", bd=1, width=510, height=1)
border7_1.place(x=0, y=380)


# Eye Diabetic
def callback8(path8):
    img8 = ImageTk.PhotoImage(Image.open(filename8_1).resize((250, 200), Image.ANTIALIAS))
    img8_5label.configure(image=img8)
    img8_5label.image = img8


def getfile8():
    global filename8_1
    try:
        filename8_1 = filedialog.askopenfilename(initialdir="C:/", title="Select A File", filetypes=(
        ("jpg file", "*.jpg"), ("png files", "*.png"), ("jpeg file", "*.jpeg")))
        callback8(filename8_1)
    except:
        filename8_1 = r"common/NAN.jpg"
        callback8(filename8_1)
    callback8_1()
    root.bind("<Return>", callback8)


def callback8_1():
    filename3 = filename8_1[::-1]
    filename4 = ""
    filename5 = "/"
    filename4 = filename3.find(filename5)
    filename4 = filename3[0:filename4]
    filename4 = filename4[::-1]
    label8_predict.config(text=filename4)


def prediction8label1():
    label8_11.config(text=prediction8label)
    label8_12.config(text=str(prediction8Accuracy) + "%")


def predict8(img):
    global prediction8
    global prediction8label
    global prediction8Accuracy
    image_array2 = cv2.imread(img)
    image_array2 = cv2.cvtColor(image_array2, cv2.COLOR_BGR2RGB)
    new_array2 = cv2.resize(image_array2, (224, 224))
    new_array2 = new_array2.reshape(-1, 224, 224, 3)
    prediction8 = model8.predict(new_array2 / 255.0)
    prediction8 = prediction8[0]
    No_DR = prediction8[0]
    Mild_DR = prediction8[1]
    Modarate_DR = prediction8[2]
    Server_DR = prediction8[3]
    Prolife_DR = prediction8[4]

    if (No_DR > Mild_DR) and (No_DR > Mild_DR) and (No_DR > Modarate_DR) and (No_DR > Server_DR) and (
            No_DR > Prolife_DR):
        prediction8label = "No Diabetic Retinopathy"
        prediction8Accuracy = No_DR * 100
    elif (Mild_DR > No_DR) and (Mild_DR > Modarate_DR) and (Mild_DR > Server_DR) and (Mild_DR > Prolife_DR):
        prediction8label = "Mild Diabetic Retinopathy"
        prediction8Accuracy = Mild_DR * 100
    elif (Modarate_DR > No_DR) and (Modarate_DR > Mild_DR) and (Modarate_DR > Server_DR) and (Modarate_DR > Prolife_DR):
        prediction8label = "Moderate Diabetic Retinopathy"
        prediction8Accuracy = Modarate_DR * 100
    elif (Server_DR > No_DR) and (Server_DR > Mild_DR) and (Server_DR > Modarate_DR) and (Server_DR > Prolife_DR):
        prediction8label = "Severe Diabetic Retinopathy"
        prediction8Accuracy = Server_DR * 100
    else:
        prediction8label = "Proliferative Diabetic Retinopathy"
        prediction8Accuracy = Prolife_DR * 100
    prediction8Accuracy = round(prediction8Accuracy, 2)
    prediction8label1()
    root.bind("<Return>", prediction8label1)


# function end

# left

width3 = 110
height3 = 110

img8_7i = ImageTk.PhotoImage(Image.open(r"Eye Dibaties/0i.png").resize((110, 110)), Image.ANTIALIAS)
img8_1i = ImageTk.PhotoImage(Image.open(r"Eye Dibaties/1.png").resize((110, 110)), Image.ANTIALIAS)
img8_1 = Label(frame8, image=img8_1i, width=width3, height=height3)
img8_2i = ImageTk.PhotoImage(Image.open(r"Eye Dibaties/0.png").resize((110, 110)), Image.ANTIALIAS)
img8_2 = Label(frame8, image=img8_2i, width=width3, height=height3)
img8_3i = ImageTk.PhotoImage(Image.open(r"Eye Dibaties/2.png").resize((110, 110)), Image.ANTIALIAS)
img8_3 = Label(frame8, image=img8_3i, width=width3, height=height3)
img8_4i = ImageTk.PhotoImage(Image.open(r"Eye Dibaties/3.png").resize((110, 110)), Image.ANTIALIAS)
img8_4 = Label(frame8, image=img8_4i, width=width3, height=height3)
img8_5i = ImageTk.PhotoImage(Image.open(r"Eye Dibaties/0i.png").resize((110, 110)), Image.ANTIALIAS)
img8_5 = Label(frame8, image=img8_7i, width=width3, height=height3)
img8_6i = ImageTk.PhotoImage(Image.open(r"Eye Dibaties/4.png").resize((110, 110)), Image.ANTIALIAS)
img8_6 = Label(frame8, image=img8_6i, width=width3, height=height3)

label8 = Label(frame8, text="INPUT EXAMPLE", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
img8_1label = Label(frame8, text="Example 1", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img8_2label = Label(frame8, text="Example 2", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img8_3label = Label(frame8, text="Example 3", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img8_4label = Label(frame8, text="Example 4", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img8_5label = Label(frame8, text="Example 5", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img8_6label = Label(frame8, text="Example 6", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))

img8_1tag = Label(frame8, text="Mild DR", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img8_2tag = Label(frame8, text="No DR", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img8_3tag = Label(frame8, text="Moderate DR", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img8_4tag = Label(frame8, text="Severe DR", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img8_5tag = Label(frame8, text="No DR", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img8_6tag = Label(frame8, text="Proliferative DR", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))

label8.place(x=175, y=10)
img8_1label.place(x=40, y=50)
img8_2label.place(x=220, y=50)
img8_3label.place(x=400, y=50)
img8_1.place(x=20, y=75)
img8_2.place(x=200, y=75)
img8_3.place(x=380, y=75)
img8_1tag.place(x=50, y=190)
img8_2tag.place(x=235, y=190)
img8_3tag.place(x=400, y=190)

img8_4label.place(x=40, y=220)
img8_5label.place(x=220, y=220)
img8_6label.place(x=400, y=220)
img8_4.place(x=20, y=245)
img8_5.place(x=200, y=245)
img8_6.place(x=380, y=245)
img8_4tag.place(x=50, y=360)
img8_5tag.place(x=235, y=360)
img8_6tag.place(x=400, y=360)

# About
label8_61 = Label(frame8, text="About Retinopathy Detection",
                  font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label8_61.place(x=150, y=380)
label8_6 = Label(frame8, wraplength=500, justify=LEFT,
                 text="""People with diabetes can have an eye disease called diabetic retinopathy. This is when high blood sugar levels cause damage to blood vessels in the retina. These blood vessels can swell and leak. Or they can close, stopping blood from passing through. Sometimes abnormal new blood vessels grow on the retina. All of these changes can steal your vision.""")
label8_6.place(x=5, y=410)

# symptoms
label8_71 = Label(frame8, text="Symptoms", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))

label8_7 = Label(frame8, wraplength=500, justify=LEFT, text="""People may experience:
Visual: vision disorder, blurred vision, distorted vision, impaired colour vision, seeing spots, or vision loss
Also common: new and abnormal blood vessels

""")
label8_7.place(x=6, y=500)
label8_71.place(x=185, y=473)

# treatment
label8_91 = Label(frame8, text="Treatment", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label8_9 = Label(frame8, wraplength=500, justify=LEFT, text="""Treatment consists of diet modifications and insulin
Mild cases may be treated with careful diabetes management. Advanced cases may require laser treatment or surgery.
Self-care
Blood glucose management and Diabetic diet
Surgery
Vitrectomy, Laser coagulation and Laser surgery
Medications
VEGFR inhibitor and Steroid""")
label8_9.place(x=5, y=590)
label8_91.place(x=185, y=564)

# right
label8_10 = Label(frame8, text="DIABETIC RETINOPATHY",
                  font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label8_10.place(x=620, y=10)

Button8_1 = Button(frame8, text="Upload Image", command=getfile8,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button8_1.place(x=580, y=270)
Button8_1 = Button(frame8, text="Upload Image", command=getfile8,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button8_1.place(x=580, y=270)

label8_13 = Label(frame8, text="File name:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label8_13.place(x=580, y=350)

label8_14 = Label(frame8, text="Prediction:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label8_14.place(x=580, y=390)

label8_13 = Label(frame8, text="Accuracy:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label8_13.place(x=580, y=430)

filename8 = r"common/NAN.jpg"
img8_5i = ImageTk.PhotoImage(Image.open(filename8).resize((250, 200), Image.ANTIALIAS))
img8_5label = Label(frame8, image=img8_5i, height=200, width=250, relief="solid")
img8_5label.place(x=635, y=50)

# model
try:
    Button8_2 = Button(frame8, text="Predict", command=lambda: predict8(filename8_1),
                       font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                       relief="solid", activebackground="white")
    Button8_2.place(x=800, y=270)

except:
    print("error")

try:
    label8_predict = Label(frame8, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label8_11 = Label(frame8, text=prediction8label, font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label8_12 = Label(frame8, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
except:
    label8_11 = Label(frame8, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label8_12 = Label(frame8, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label8_predict = Label(frame8, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label8_predict.place(x=690, y=350)
label8_11.place(x=690, y=390)
label8_12.place(x=690, y=430)

# border
border8_2 = Label(frame8, text="", bg="black", bd=1, height=745)
border8_2.place(x=510, y=0)

img8_4 = ImageTk.PhotoImage(Image.open(r"malaria/normal1.png").resize((20, 1)), Image.ANTIALIAS)
border8_1 = Label(frame8, image=img8_4, bg="black", bd=1, width=510, height=1)
border8_1.place(x=0, y=380)


# Bacterial vs Virus
def callback9(path9):
    img9 = ImageTk.PhotoImage(Image.open(filename9_1).resize((250, 200), Image.ANTIALIAS))
    img9_5label.configure(image=img9)
    img9_5label.image = img9


def getfile9():
    global filename9_1
    try:
        filename9_1 = filedialog.askopenfilename(initialdir="C:/", title="Select A File", filetypes=(
            ("jpg file", "*.jpg"), ("png files", "*.png"), ("jpeg file", "*.jpeg")))
        callback9(filename9_1)
    except:
        filename9_1 = r"common/NAN.jpg"
        callback9(filename9_1)
    callback9_1()
    root.bind("<Return>", callback9)


def callback9_1():
    filename3 = filename9_1[::-1]
    filename4 = ""
    filename5 = "/"
    filename4 = filename3.find(filename5)
    filename4 = filename3[0:filename4]
    filename4 = filename4[::-1]
    label9_predict.config(text=filename4)


def prediction9label1():
    label9_11.config(text=prediction9label)
    label9_12.config(text=str(prediction9Accuracy) + "%")


def predict9(img):
    global prediction9
    global prediction9label
    global prediction9Accuracy
    image_array2 = cv2.imread(img)
    image_array2 = cv2.resize(image_array2, (200, 200))
    new_array2 = cv2.cvtColor(image_array2, cv2.COLOR_BGR2RGB)
    new_array2 = new_array2.reshape(-1, 200, 200, 3)
    new_array2 = [new_array2 / 255.0]
    prediction9 = model9.predict(new_array2)
    prediction9 = prediction9[0]
    Normal = prediction9[0]
    bacterial = prediction9[1]
    viral = prediction9[2]
    if Normal > bacterial and Normal > viral:
        prediction9label = "Normal"
        prediction9Accuracy = Normal * 100
    elif bacterial > Normal and bacterial > viral:
        prediction9label = "Bacterial Pnemonia"
        prediction9Accuracy = bacterial * 100
    else:
        prediction9label = "Viral Pnemonia"
        prediction9Accuracy = viral * 100
    prediction9Accuracy = round(prediction9Accuracy, 2)
    prediction9label1()
    root.bind("<Return>", prediction9label1)


# function end

# left

width3 = 110
height3 = 110

img9_1i = ImageTk.PhotoImage(Image.open(r"bactarial_vs_covid/person104_bacteria_492.jpeg").resize((110, 110)),
                             Image.ANTIALIAS)
img9_1 = Label(frame9, image=img9_1i, width=width3, height=height3)
img9_2i = ImageTk.PhotoImage(Image.open(r"bactarial_vs_covid/IM-0017-0001.jpeg").resize((110, 110)), Image.ANTIALIAS)
img9_2 = Label(frame9, image=img9_2i, width=width3, height=height3)
img9_3i = ImageTk.PhotoImage(Image.open(r"bactarial_vs_covid/person1_virus_13.jpeg").resize((110, 110)),
                             Image.ANTIALIAS)
img9_3 = Label(frame9, image=img9_3i, width=width3, height=height3)

label9 = Label(frame9, text="INPUT EXAMPLE", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
img9_1label = Label(frame9, text="Example 1", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img9_2label = Label(frame9, text="Example 2", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))
img9_3label = Label(frame9, text="Example 3", font=tkinter.font.Font(family="Helvetica", size=12, weight="normal"))

img9_1tag = Label(frame9, text="Bacterial", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img9_2tag = Label(frame9, text="Normal", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))
img9_3tag = Label(frame9, text="Viral", font=tkinter.font.Font(family="Helvetica", size=9, weight="normal"))

label9.place(x=175, y=10)
img9_1label.place(x=40, y=50)
img9_2label.place(x=220, y=50)
img9_3label.place(x=400, y=50)
img9_1.place(x=20, y=75)
img9_2.place(x=200, y=75)
img9_3.place(x=380, y=75)
img9_1tag.place(x=55, y=190)
img9_2tag.place(x=235, y=190)
img9_3tag.place(x=420, y=190)

# About
label9_61 = Label(frame9, text="About Pneumonia",
                  font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label9_61.place(x=160, y=220)
label9_6 = Label(frame9, wraplength=500, justify=LEFT, text="""Infection that inflames air sacs in one or both lungs, which may fill with fluid.
With pneumonia, the air sacs may fill with fluid or pus. The infection can be life-threatening to anyone, but particularly to infants, children and people over 65.
Symptoms include a cough with phlegm or pus, fever, chills and difficulty breathing.
Antibiotics can treat many forms of pneumonia. Some forms of pneumonia can be prevented by vaccines.
""")
label9_6.place(x=5, y=250)

# symptoms
label9_71 = Label(frame9, text="Symptoms", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))

label9_7 = Label(frame9, wraplength=500, justify=LEFT, text="""Pain types: can be sharp in the chest
Whole body: fever, chills, dehydration, fatigue, loss of appetite, malaise, clammy skin, or sweating
Respiratory: fast breathing, shallow breathing, shortness of breath, or wheezing
Also common: coughing or fast heart rate
""")
label9_7.place(x=6, y=418)
label9_71.place(x=185, y=392)

# treatment
label9_91 = Label(frame9, text="Treatment", font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label9_9 = Label(frame9, wraplength=500, justify=LEFT, text="""Treatment consists of antibiotics
Antibiotics can treat many forms of pneumonia. Some forms of pneumonia can be prevented by vaccines.

Medications
Antibiotics and Penicillin

Supportive care
Oxygen therapy, Oral rehydration therapy and IV fluids""")
label9_9.place(x=5, y=580)
label9_91.place(x=185, y=559)
# right
label9_10 = Label(frame9, text="PNEUMONIA BACTERIAL/VIRAL",
                  font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"))
label9_10.place(x=600, y=10)

Button9_1 = Button(frame9, text="Upload Image", command=getfile9,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button9_1.place(x=580, y=270)
Button9_1 = Button(frame9, text="Upload Image", command=getfile9,
                   font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                   relief="solid", activebackground="white")
Button9_1.place(x=580, y=270)

label9_13 = Label(frame9, text="File name:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label9_13.place(x=580, y=350)

label9_14 = Label(frame9, text="Prediction:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label9_14.place(x=580, y=390)

label9_13 = Label(frame9, text="Accuracy:", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label9_13.place(x=580, y=430)

filename9 = r"common/NAN.jpg"
img9_5i = ImageTk.PhotoImage(Image.open(filename9).resize((250, 200), Image.ANTIALIAS))
img9_5label = Label(frame9, image=img9_5i, height=200, width=250, relief="solid")
img9_5label.place(x=635, y=50)

# model
try:
    Button9_2 = Button(frame9, text="Predict", command=lambda: predict9(filename9_1),
                       font=tkinter.font.Font(family="Helvetica", size=15, weight="bold"), width=13, height=1,
                       relief="solid", activebackground="white")
    Button9_2.place(x=800, y=270)

except:
    print("error")

try:
    label9_predict = Label(frame9, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label9_11 = Label(frame9, text=prediction9label, font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label9_12 = Label(frame9, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
except:
    label9_11 = Label(frame9, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label9_12 = Label(frame9, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
    label9_predict = Label(frame9, text="NaN", font=tkinter.font.Font(family="Helvetica", size=14, weight="bold"))
label9_predict.place(x=690, y=350)
label9_11.place(x=690, y=390)
label9_12.place(x=690, y=430)

# border
border9_2 = Label(frame9, text="", bg="black", bd=1, height=745)
border9_2.place(x=510, y=0)

img9_4 = ImageTk.PhotoImage(Image.open(r"malaria/normal1.png").resize((20, 1)), Image.ANTIALIAS)
border9_1 = Label(frame9, image=img9_4, bg="black", bd=1, width=510, height=1)
border9_1.place(x=0, y=210)

# For loading GPU setting
temp = cv2.imread(r"common/NAN.jpg")
temp = cv2.resize(temp, (200, 200))
temp = temp.reshape(-1, 200, 200, 3)
temp = [temp / 255.0]
model5.predict(temp)

root.mainloop()
