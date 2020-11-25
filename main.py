from random import randint, random
from tkinter import *
# from PIL import Image, ImageTk
# from plyer import notification
import json


def message():
    import random as r

    
    msg = [
        'Want to grow height try Tadasana',
        'Only exercise you can do after eating is Vajrasana',
        'Make fitness your favourite habit!',
        'The last three or four reps is what makes the muscle grow.\n This area of pain divides a champion from someone who \nis not a champion.',
        'If you think lifting is dangerous, try being weak.\n Being weak is dangerous',
        'Make exercise therapetuic instead of \njust phsical.',
        'Excercise is a celebration of what your body can do. \n Not a punishment for what you ate!',
        'The pain you will today while excercising,\n will be strength you feel tomorrow.',
        'You are not only working out you are preparing \nthe best version of yourself.',
        'The Pain you feel after excercising is just \nweakness leaving the body.',
        'Sweat is fat crying!'
    ]
    screen = Tk()
    screen.geometry('1330x150')
    screen.title('MESSAGE OF THE DAY!!')
    screen.configure(bg='darkgreen')
    i = r.randint(0, 10)
    msg_to_appear = Label(screen,
                          text=msg[i],
                          fg="lightgreen",
                          bg="darkgreen",
                          font='calibiri 33 bold')
    msg_to_appear.pack(fill="both")


def reg_form():

    g = Tk()
    g.geometry('1300x50')
    g.title('Instructions')
    g.configure(bg="red")
    text_of_screen = Label(g,
                           text="""Check the console of the app.""",
                           bg="red",
                           fg="yellow",
                           font='calibiri 24 bold')
    text_of_screen.pack(fill="both")

    try:
        name = input('Enter your name:')
        age = int(input('Enter your age in number(integer):'))
        gender = str(input('Enter your gender:'))
        gender = gender.lower()
        mental_or_physcial = str(input("Do you work out(Yes/No):"))
        mental_or_physcial = mental_or_physcial.lower()
        user__weight = input('Enter your weight in kg: ')
        user_weight = float(user__weight)
        user__height = input('Enter your height in cm: ')
        user__height = float(user__height)
        data = {
            'Name': name,
            'Age': age,
            'Gender': gender,
            'mental_or_physcial': mental_or_physcial,
            'weight': user__weight,
            'height': user__height
        }
        out_file = open("user_data.json", "w")
        json.dump(data, out_file, indent=6)
        out_file.close()
    except Exception as w:
        print(w)


def intro():

    g = Tk()
    g.geometry('1300x200')
    g.title('Instructions')
    g.configure(bg="red")
    text_of_screen = Label(g,
                           text="""1. Register yourself
    2. Check your report.
    3. Search for excercises. 
    4. Click any excercise you want to learn (not owned by our app)
    5. If demotivated check our messages.""",
                           bg="red",
                           fg="yellow",
                           font='calibiri 24 bold')
    text_of_screen.pack(fill="both")


def data_report():
    database_output_screen = Tk()
    database_output_screen.title("Data Report")
    database_output_screen.geometry("1300x200")

    with open('user_data.json') as json_file:
        database = json.load(json_file)
    user_age = database['Age']
    user_gender = database['Gender']
    user_name = database['Name']
    user_height = database['height']
    user_weight = database['weight']
    male_height = {
        4: '95.8',
        5: '102.2',
        6: '110.5',
        7: '125.6',
        8: '129.4',
        9: '129.8',
        10: '136.4',
        11: '140.4',
        12: '150',
        13: '157.3',
        14: '159.8',
        15: '174.6',
        16: '175.3'
    }
    female_height = {
        4: '92',
        5: '98.8',
        6: '108.8',
        7: '119.6',
        8: '123.8',
        9: '124.2',
        10: '134.5',
        11: '140.4',
        12: '145.2',
        13: '151.6',
        14: '156.4',
        15: '164.3',
        16: '172.5'
    }
    male_weight = {
        4: '16.3',
        5: '18.5',
        6: '20.8',
        7: '22.9580643 ',
        8: '25.8 ',
        9: '28.7',
        10: '32.1 ',
        11: '39.0089438',
        12: '40.7',
        13: '45.8',
        14: '51.2 ',
        15: '56.5 ',
        16: '61.1',
        17: '64.7 ',
        18: '67.3',
        19: '69.2 '
    }
    female_weight = {
        4: '15.5',
        5: '17.5',
        6: '20.0',
        7: '23.6',
        8: '26.4',
        9: '28.3',
        10: '30.6',
        11: '33.8',
        12: '36.8',
        13: '38.9',
        14: '41.2',
        15: '43.3',
        16: '46.4',
        17: '48.7',
        18: '51.9',
        19: '54'
    }
    if user_gender == "female":
        if user_age >= 20:
            title = Label(database_output_screen,
                          text=f"""  Your Height:{user_height} cm
    Average Height:{female_height[16]} cm
    Your weight:{user_weight} kg
    Average weight:{female_weight[19]} kg""",
                          bg="blue",
                          fg="yellow",
                          font="algerian 32 bold")
            title.pack(fill="both")
        else:
            title = Label(database_output_screen,
                          text=f"""  Your Height:{user_height} cm
    Average Height:{female_height[user_age]} cm
    Your weight:{user_weight} kg
    Average weight:{female_weight[user_age]} kg""",
                          bg="blue",
                          fg="yellow",
                          font="algerian 32 bold")
            title.pack(fill="both")
    else:
        if user_age < 20:
            title = Label(database_output_screen,
                          text=f"""Your Height:{user_height} cm
    Average Height:{male_height[user_age]} cm
    Your Weight:{user_weight} kg
    Average Weight: {male_weight[user_age]} kg""",
                          bg="blue",
                          fg="yellow",
                          font="algerian 32 bold")
            title.pack(fill="both")
        else:
            title = Label(database_output_screen,
                          text=f"""Your Height:{user_height} cm
    Average Height:{male_height[16]} cm
    Your Weight:{user_weight} kg
    Average Weight: {male_weight[19]} kg
    """,
                          bg="blue",
                          fg="yellow",
                          font="algerian 32 bold")
            title.pack(fill="both")


import webbrowser as wb


def excercise_page():
    def digestion_page():
        def Vajrasana():
            wb.open('https://www.youtube.com/watch?v=tFIrxireDAo')

        def Pawan_Mukt_Aasana():
            wb.open('https://www.youtube.com/watch?v=N6vK1LbF-58')

        def Balasana():
            wb.open('https://www.youtube.com/watch?v=2MJGg-dUKh0')

        def MarjaryasanaBitilasana():
            wb.open('https://www.youtube.com/watch?v=kqnua4rHVVA')

        def Trikonasana():
            wb.open('https://www.youtube.com/watch?v=S6gB0QHbWFE')

        def Paschimottasana():
            wb.open('https://www.youtube.com/watch?v=298tj3pcPF8')

        def Ardha_Matsyendrasana():
            wb.open('https://www.youtube.com/watch?v=z0XHmCRIdyE')

        cr = Tk()
        cr.geometry('1000x600')
        cr.configure(bg="orange")
        cr.title('Digestion')
        vajrasana_frame = Frame(cr, bg="blue")
        vajrasana_btn = Button(cr,
                               text="Vajrasana",
                               cursor="hand2",
                               height=1,
                               bg="dark blue",
                               fg="yellow",
                               font="calibiri 24 bold italic",
                               command=Vajrasana)
        vajrasana_btn.pack(fill="both", expand=True)
        vajrasana_frame.pack(fill="both", pady=10)
        Pawan_Mukt_Aasana_frame = Frame(cr, bg="blue")
        Pawan_Mukt_Aasana_btn = Button(cr,
                                       text="Pawan Mukt Aasana",
                                       cursor="hand2",
                                       height=1,
                                       bg="dark blue",
                                       fg="yellow",
                                       font="calibiri 24 bold italic",
                                       command=Pawan_Mukt_Aasana)
        Pawan_Mukt_Aasana_btn.pack(fill="both", expand=True)
        Pawan_Mukt_Aasana_frame.pack(fill="both", pady=10)
        Marjaryasana_Bitilasana_frame = Frame(cr, bg="blue")
        Marjaryasana_Bitilasana_btn = Button(cr,
                                             text="Marjaryasana Bitilasana",
                                             cursor="hand2",
                                             height=1,
                                             bg="dark blue",
                                             fg="yellow",
                                             font="calibiri 24 bold italic",
                                             command=MarjaryasanaBitilasana)
        Marjaryasana_Bitilasana_btn.pack(fill="both", expand=True)
        Marjaryasana_Bitilasana_frame.pack(fill="both", pady=10)
        Balasana_frame = Frame(cr, bg="blue")
        Balasana_btn = Button(cr,
                              text="Balasana",
                              cursor="hand2",
                              height=1,
                              bg="dark blue",
                              fg="yellow",
                              font="calibiri 24 bold italic",
                              command=Balasana)
        Balasana_btn.pack(fill="both", expand=True)
        Balasana_frame.pack(fill="both", pady=10)
        Trikonasana_frame = Frame(cr, bg="blue")
        Trikonasana_btn = Button(cr,
                                 text="Trikonasana",
                                 cursor="hand2",
                                 height=1,
                                 bg="dark blue",
                                 fg="yellow",
                                 font="calibiri 24 bold italic",
                                 command=Trikonasana)
        Trikonasana_btn.pack(fill="both", expand=True)
        Trikonasana_frame.pack(fill="both", pady=10)
        Paschimottasana_frame = Frame(cr, bg="blue")
        Paschimottasana_btn = Button(cr,
                                     text="Paschimottasana",
                                     cursor="hand2",
                                     height=1,
                                     bg="dark blue",
                                     fg="yellow",
                                     font="calibiri 24 bold italic",
                                     command=Paschimottasana)
        Paschimottasana_btn.pack(fill="both", expand=True)
        Paschimottasana_frame.pack(fill="both", pady=10)
        Ardha_Matsyendrasana_frame = Frame(cr, bg="blue")
        Ardha_Matsyendrasana_btn = Button(
            cr,
            text="Ardha Matsyendrasana / Right Vakrasana",
            cursor="hand2",
            height=1,
            bg="dark blue",
            fg="yellow",
            font="calibiri 24 bold italic",
            command=Ardha_Matsyendrasana)
        Ardha_Matsyendrasana_btn.pack(fill="both", expand=True)
        Ardha_Matsyendrasana_frame.pack(fill="both", pady=10)

    def heightgrowth_page():
        def Tadasana():
            wb.open("https://www.youtube.com/watch?v=2HTvZp5rPrg")

        def Pelvic_Shift():
            wb.open("https://www.youtube.com/watch?v=_kEPfhQpjg8")

        def Hanging():
            wb.open('https://youtu.be/8bppcsg07Rc')

        def SingleLeg():
            wb.open("https://www.youtube.com/watch?v=6v0dZ03bcd4")

        def puppypose():
            wb.open("https://www.youtube.com/watch?v=mytWLo8fHbw")

        def Side_Stretch():
            wb.open("https://www.youtube.com/watch?v=dqdgOhpYmXw")

        def cobra():
            wb.open("https://www.youtube.com/watch?v=JDcdhTuycOI")

        r = Tk()
        r.geometry('1000x600')
        r.configure(bg="orange")
        r.title('Height Growth')
        Tadasana_frame = Frame(r, bg="blue")
        Tadasana_btn = Button(r,
                              text="Tadasana",
                              cursor="hand2",
                              height=1,
                              bg="dark blue",
                              fg="yellow",
                              font="calibiri 24 bold italic",
                              command=Tadasana)
        Tadasana_btn.pack(fill="both", expand=True)
        Tadasana_frame.pack(fill="both", pady=10)
        Pelvic_Shift_frame = Frame(r, bg="blue")
        Pelvic_Shift_btn = Button(r,
                                  text="Pelvic Shift",
                                  cursor="hand2",
                                  height=1,
                                  bg="dark blue",
                                  fg="yellow",
                                  font="calibiri 24 bold italic",
                                  command=Pelvic_Shift)
        Pelvic_Shift_btn.pack(fill="both", expand=True)
        Pelvic_Shift_frame.pack(fill="both", pady=10)
        Hanging_frame = Frame(r, bg="blue")
        Hanging_btn = Button(r,
                             text="Monkey Bar",
                             cursor="hand2",
                             height=1,
                             bg="dark blue",
                             fg="yellow",
                             font="calibiri 24 bold italic",
                             command=Hanging)
        Hanging_btn.pack(fill="both", expand=True)
        Hanging_frame.pack(fill="both", pady=10)
        Single_Leg_Hopping_frame = Frame(r, bg="blue")
        Single_Leg_Hopping_btn = Button(r,
                                        text="Single Leg Hopping",
                                        cursor="hand2",
                                        height=1,
                                        bg="dark blue",
                                        fg="yellow",
                                        font="calibiri 24 bold italic",
                                        command=SingleLeg)
        Single_Leg_Hopping_btn.pack(fill="both", expand=True)
        Single_Leg_Hopping_frame.pack(fill="both", pady=10)
        Puppy_Pose_frame = Frame(r, bg="blue")
        Puppy_Pose_btn = Button(r,
                                text="Puppy Pose",
                                cursor="hand2",
                                height=1,
                                bg="dark blue",
                                fg="yellow",
                                font="calibiri 24 bold italic",
                                command=puppypose)
        Puppy_Pose_btn.pack(fill="both", expand=True)
        Puppy_Pose_frame.pack(fill="both", pady=10)
        Side_Stretch_frame = Frame(r, bg="blue")
        Side_Stretch_btn = Button(r,
                                  text="Side Stretch",
                                  cursor="hand2",
                                  height=1,
                                  bg="dark blue",
                                  fg="yellow",
                                  font="calibiri 24 bold italic",
                                  command=Side_Stretch)
        Side_Stretch_btn.pack(fill="both", expand=True)
        Side_Stretch_frame.pack(fill="both", pady=10)
        Cobra_Stretch_frame = Frame(r, bg="blue")
        Cobra_Stretch_btn = Button(r,
                                   text="Side Stretch",
                                   cursor="hand2",
                                   height=1,
                                   bg="dark blue",
                                   fg="yellow",
                                   font="calibiri 24 bold italic",
                                   command=cobra)
        Cobra_Stretch_btn.pack(fill="both", expand=True)
        Cobra_Stretch_frame.pack(fill="both", pady=10)

    def weightgrowth_page():
        ar = Tk()
        ar.geometry('1000x600')
        ar.configure(bg="orange")
        ar.title("Weight Gain")

        def Supta_Badhakonasana():
            wb.open("https://www.youtube.com/watch?v=VNx6l5RmJhQ")

        def Vajrasana():
            wb.open("https://www.youtube.com/watch?v=tFIrxireDAo")

        def Matsyasana():
            wb.open("https://www.youtube.com/watch?v=vhFdcezAyL8")

        def Bhujangasana():
            wb.open('https://www.youtube.com/watch?v=99RR2vRvgi8')

        def Sarvangasana():
            wb.open("https://www.youtube.com/watch?v=SfAoPVt64LE")

        def Virabhadrasana():
            wb.open("https://www.youtube.com/watch?v=X-oPQ9eO360")

        Supta_Badhakonasana_frame = Frame(ar, bg="blue")
        Supta_Badhakonasana_btn = Button(ar,
                                         text="Supta Badhakonasana",
                                         cursor="hand2",
                                         height=1,
                                         bg="dark blue",
                                         fg="yellow",
                                         font="calibiri 24 bold italic",
                                         command=Supta_Badhakonasana)
        Supta_Badhakonasana_btn.pack(fill="both", expand=True)
        Supta_Badhakonasana_frame.pack(fill="both", pady=10)
        Vajrasana_frame = Frame(ar, bg="blue")
        Vajrasana_btn = Button(ar,
                               text="Vajrasana",
                               cursor="hand2",
                               height=1,
                               bg="dark blue",
                               fg="yellow",
                               font="calibiri 24 bold italic",
                               command=Vajrasana)
        Vajrasana_btn.pack(fill="both", expand=True)
        Vajrasana_frame.pack(fill="both", pady=10)
        Matsyasana_frame = Frame(ar, bg="blue")
        Matsyasana_btn = Button(ar,
                                text="Matsyasana",
                                cursor="hand2",
                                height=1,
                                bg="dark blue",
                                fg="yellow",
                                font="calibiri 24 bold italic",
                                command=Matsyasana)
        Matsyasana_btn.pack(fill="both", expand=True)
        Matsyasana_frame.pack(fill="both", pady=10)
        Bhujangasana_frame = Frame(ar, bg="blue")
        Bhujangasana_btn = Button(ar,
                                  text="Bhujangasana",
                                  cursor="hand2",
                                  height=1,
                                  bg="dark blue",
                                  fg="yellow",
                                  font="calibiri 24 bold italic",
                                  command=Bhujangasana)
        Bhujangasana_btn.pack(fill="both", expand=True)
        Bhujangasana_frame.pack(fill="both", pady=10)
        Sarvangasana_frame = Frame(ar, bg="blue")
        Sarvangasana_btn = Button(
            ar,
            text="Sarvangasana",
            cursor="hand2",
            height=1,
            bg="dark blue",
            fg="yellow",
            font="calibiri 24 bold italic",
        )
        Sarvangasana_btn.pack(fill="both", expand=True)
        Sarvangasana_frame.pack(fill="both", pady=10)
        Shavasana_frame = Frame(ar, bg="blue")
        Shavasana_btn = Button(ar,
                               text="Shavasana",
                               cursor="hand2",
                               height=1,
                               bg="dark blue",
                               fg="yellow",
                               font="calibiri 24 bold italic",
                               command=Sarvangasana)
        Shavasana_btn.pack(fill="both", expand=True)
        Shavasana_frame.pack(fill="both", pady=10)
        Virabhadrasana_frame = Frame(ar, bg="blue")
        Virabhadrasana_btn = Button(ar,
                                    text="Virabhadrasana",
                                    cursor="hand2",
                                    height=1,
                                    bg="dark blue",
                                    fg="yellow",
                                    font="calibiri 24 bold italic",
                                    command=Virabhadrasana)
        Virabhadrasana_btn.pack(fill="both", expand=True)
        Virabhadrasana_frame.pack(fill="both", pady=10)

    def weightdecrease_page():
        xr = Tk()
        xr.geometry('1000x600')
        xr.configure(bg="orange")
        xr.title('Weight Loss')

        def Walking():
            wb.open('https://www.youtube.com/watch?v=-fD2TSL2s7I')

        def Baagho():
            wb.open("https://www.youtube.com/watch?v=fQ7ewHFw_I8")

        def Cycle():
            wb.open("https://www.youtube.com/watch?v=x4WHeVf5DN4")

        def Swim():
            wb.open("https://www.youtube.com/watch?v=pFN2n7CRqhw")

        def Chaturangadandasana():
            wb.open("https://www.youtube.com/watch?v=1usSRvFYS6I")

        def Virabhadrasana():
            wb.open("https://www.youtube.com/watch?v=X-oPQ9eO360")

        def AdhoMukhaSvanasana():
            wb.open("https://www.youtube.com/watch?v=ETSIv8WetjI")

        Walking_frame = Frame(xr, bg="blue")
        Walking_btn = Button(xr,
                             text="Walking",
                             cursor="hand2",
                             height=1,
                             bg="dark blue",
                             fg="yellow",
                             font="calibiri 24 bold italic",
                             command=Walking)
        Walking_btn.pack(fill="both", expand=True)
        Walking_frame.pack(fill="both", pady=10)
        Jogging_frame = Frame(xr, bg="blue")
        Jogging_btn = Button(xr,
                             text="Jogging",
                             cursor="hand2",
                             height=1,
                             bg="dark blue",
                             fg="yellow",
                             font="calibiri 24 bold italic",
                             command=Baagho)
        Jogging_btn.pack(fill="both", expand=True)
        Jogging_frame.pack(fill="both", pady=10)
        Cylcing_frame = Frame(xr, bg="blue")
        Cylcing_btn = Button(xr,
                             text="Cylcing",
                             cursor="hand2",
                             height=1,
                             bg="dark blue",
                             fg="yellow",
                             font="calibiri 24 bold italic",
                             command=Cycle)
        Cylcing_btn.pack(fill="both", expand=True)
        Cylcing_frame.pack(fill="both", pady=10)
        Swimming_frame = Frame(xr, bg="blue")
        Swimming_btn = Button(xr,
                              text="Swimming",
                              cursor="hand2",
                              height=1,
                              bg="dark blue",
                              fg="yellow",
                              font="calibiri 24 bold italic",
                              command=Swim)
        Swimming_btn.pack(fill="both", expand=True)
        Swimming_frame.pack(fill="both", pady=10)
        Chaturangadandasana_frame = Frame(xr, bg="blue")
        Chaturangadandasana_btn = Button(xr,
                                         text="Chaturangadandasana",
                                         cursor="hand2",
                                         height=1,
                                         bg="dark blue",
                                         fg="yellow",
                                         font="calibiri 24 bold italic",
                                         command=Chaturangadandasana)
        Chaturangadandasana_btn.pack(fill="both", expand=True)
        Chaturangadandasana_frame.pack(fill="both", pady=10)
        Virabhadrasana_frame = Frame(xr, bg="blue")
        Virabhadrasana_btn = Button(xr,
                                    text="Virabhadrasana",
                                    cursor="hand2",
                                    height=1,
                                    bg="dark blue",
                                    fg="yellow",
                                    font="calibiri 24 bold italic",
                                    command=Virabhadrasana)
        Virabhadrasana_btn.pack(fill="both", expand=True)
        Virabhadrasana_frame.pack(fill="both", pady=10)
        Adho_Mukha_Svanasana_frame = Frame(xr, bg="blue")
        Adho_Mukha_Svanasana_btn = Button(xr,
                                          text="Adho Mukha Svanasana",
                                          cursor="hand2",
                                          height=1,
                                          bg="dark blue",
                                          fg="yellow",
                                          font="calibiri 24 bold italic",
                                          command=AdhoMukhaSvanasana)
        Adho_Mukha_Svanasana_btn.pack(fill="both", expand=True)
        Adho_Mukha_Svanasana_frame.pack(fill="both", pady=10)

    def bodybuilding_page():
        mr = Tk()
        mr.geometry('1000x600')
        mr.configure(bg="orange")
        mr.title("Body Building")

        def BarbellBellPress():
            wb.open("https://www.youtube.com/watch?v=TQZKiSFh8js")

        def Squats():
            wb.open("https://www.youtube.com/watch?v=U3HlEF_E9fo")

        def Dumbles():
            wb.open("https://www.youtube.com/watch?v=ykJmrZ5v0Oo")

        def Reps():
            wb.open("https://youtu.be/wFElbNOzzrA")

        def Deadlift():
            wb.open("https://www.youtube.com/watch?v=ytGaGIn3SjE")

        def Barbell():
            wb.open("https://www.youtube.com/watch?v=kBWAon7ItDw")

        def Military():
            wb.open("https://www.youtube.com/watch?v=waeCyaAQRn8")

        Barbell_Bench_Press_frame = Frame(mr, bg="blue")
        Barbell_Bench_Press_btn = Button(mr,
                                         text="Barbell Bench Press",
                                         cursor="hand2",
                                         height=1,
                                         bg="dark blue",
                                         fg="yellow",
                                         font="calibiri 24 bold italic",
                                         command=BarbellBellPress)
        Barbell_Bench_Press_btn.pack(fill="both", expand=True)
        Barbell_Bench_Press_frame.pack(fill="both", pady=10)
        Squat_frame = Frame(mr, bg="blue")
        Squat_btn = Button(mr,
                           text="Squat",
                           cursor="hand2",
                           height=1,
                           bg="dark blue",
                           fg="yellow",
                           font="calibiri 24 bold italic",
                           command=Squats)
        Squat_btn.pack(fill="both", expand=True)
        Squat_frame.pack(fill="both", pady=10)
        Dumbles_frame = Frame(mr, bg="blue")
        Dumbles_btn = Button(mr,
                             text="Dumbles",
                             cursor="hand2",
                             height=1,
                             bg="dark blue",
                             fg="yellow",
                             font="calibiri 24 bold italic",
                             command=Dumbles)
        Dumbles_btn.pack(fill="both", expand=True)
        Dumbles_frame.pack(fill="both", pady=10)
        Reps_frame = Frame(mr, bg="blue")
        Reps_btn = Button(mr,
                          text="Reps",
                          cursor="hand2",
                          height=1,
                          bg="dark blue",
                          fg="yellow",
                          font="calibiri 24 bold italic",
                          command=Reps)
        Reps_btn.pack(fill="both", expand=True)
        Reps_frame.pack(fill="both", pady=10)
        Deadlift_frame = Frame(mr, bg="blue")
        Deadlift_btn = Button(mr,
                              text="Deadlift",
                              cursor="hand2",
                              height=1,
                              bg="dark blue",
                              fg="yellow",
                              font="calibiri 24 bold italic",
                              command=Deadlift)
        Deadlift_btn.pack(fill="both", expand=True)
        Deadlift_frame.pack(fill="both", pady=10)
        Barbell_Row_frame = Frame(mr, bg="blue")
        Barbell_Row_btn = Button(mr,
                                 text="Barbell Row",
                                 cursor="hand2",
                                 height=1,
                                 bg="dark blue",
                                 fg="yellow",
                                 font="calibiri 24 bold italic",
                                 command=Barbell)
        Barbell_Row_btn.pack(fill="both", expand=True)
        Barbell_Row_frame.pack(fill="both", pady=10)
        Barbell_Military_Press_frame = Frame(mr, bg="blue")
        Barbell_Military_Press_btn = Button(mr,
                                            text="Barbell Military Press",
                                            cursor="hand2",
                                            height=1,
                                            bg="dark blue",
                                            fg="yellow",
                                            font="calibiri 24 bold italic",
                                            command=Military)
        Barbell_Military_Press_btn.pack(fill="both", expand=True)
        Barbell_Military_Press_frame.pack(fill="both", pady=10)

    def bodypain_page():
        dr = Tk()
        dr.geometry('1000x600')
        dr.configure(bg="orange")
        dr.title('Body Pain')

        def Uttanasana():
            wb.open("https://www.youtube.com/watch?v=g7Uhp5tphAs")

        def VK():
            wb.open("https://www.youtube.com/watch?v=a4thkiW2uPA")

        def Matsyasana():
            wb.open("https://www.youtube.com/watch?v=vhFdcezAyL8")

        def Snake():
            wb.open('https://www.youtube.com/watch?v=99RR2vRvgi8')

        def Badha():
            wb.open("https://www.youtube.com/watch?v=E3611YwA51E")

        def Dhanur():
            wb.open("https://www.youtube.com/watch?v=wgH2PdPnZGM")

        def Vira():
            wb.open("https://www.youtube.com/watch?v=KlYkyAUHrO8")

        Uttanasana_frame = Frame(dr, bg="blue")
        Uttanasana_btn = Button(dr,
                                text="Uttanasana",
                                cursor="hand2",
                                height=1,
                                bg="dark blue",
                                fg="yellow",
                                font="calibiri 24 bold italic",
                                command=Uttanasana)
        Uttanasana_btn.pack(fill="both", expand=True)
        Uttanasana_frame.pack(fill="both", pady=10)
        ViparitaKarani_frame = Frame(dr, bg="blue")
        ViparitaKarani_btn = Button(dr,
                                    text="ViparitaKarani",
                                    cursor="hand2",
                                    height=1,
                                    bg="dark blue",
                                    fg="yellow",
                                    font="calibiri 24 bold italic",
                                    command=VK)
        ViparitaKarani_btn.pack(fill="both", expand=True)
        ViparitaKarani_frame.pack(fill="both", pady=10)
        Matsyasana_frame = Frame(dr, bg="blue")
        Matsyasana_btn = Button(dr,
                                text="Matsyasana",
                                cursor="hand2",
                                height=1,
                                bg="dark blue",
                                fg="yellow",
                                font="calibiri 24 bold italic",
                                command=Matsyasana)
        Matsyasana_btn.pack(fill="both", expand=True)
        Matsyasana_frame.pack(fill="both", pady=10)
        Bhujangasana_frame = Frame(dr, bg="blue")
        Bhujangasana_btn = Button(dr,
                                  text="Bhujangasana",
                                  cursor="hand2",
                                  height=1,
                                  bg="dark blue",
                                  fg="yellow",
                                  font="calibiri 24 bold italic",
                                  command=Snake)
        Bhujangasana_btn.pack(fill="both", expand=True)
        Bhujangasana_frame.pack(fill="both", pady=10)
        Baddha_Konasana_frame = Frame(dr, bg="blue")
        Baddha_Konasana_btn = Button(dr,
                                     text="Baddha Konasana",
                                     cursor="hand2",
                                     height=1,
                                     bg="dark blue",
                                     fg="yellow",
                                     font="calibiri 24 bold italic",
                                     command=Badha)
        Baddha_Konasana_btn.pack(fill="both", expand=True)
        Baddha_Konasana_frame.pack(fill="both", pady=10)
        Dhanurasana_frame = Frame(dr, bg="blue")
        Dhanurasana_btn = Button(dr,
                                 text="Dhanurasana",
                                 cursor="hand2",
                                 height=1,
                                 bg="dark blue",
                                 fg="yellow",
                                 font="calibiri 24 bold italic",
                                 command=Dhanur)
        Dhanurasana_btn.pack(fill="both", expand=True)
        Dhanurasana_frame.pack(fill="both", pady=10)
        Virasana_frame = Frame(dr, bg="blue")
        Virasana_btn = Button(dr,
                              text="Virasana",
                              cursor="hand2",
                              height=1,
                              bg="dark blue",
                              fg="yellow",
                              font="calibiri 24 bold italic",
                              command=Vira)
        Virasana_btn.pack(fill="both", expand=True)
        Virasana_frame.pack(fill="both", pady=10)

    def goodsleep_page():
        tr = Tk()
        tr.geometry('1000x600')
        tr.configure(bg="orange")
        tr.title("Sleep")

        def wideknee():
            wb.open("https://youtu.be/eqVMAPM00DM")

        def cpp():
            wb.open("https://youtu.be/0KzyEgkq7zw")

        def rba():
            wb.open("https://youtu.be/vksA9pqOpVI")

        def legupwall():
            wb.open("https://youtu.be/_OQEIiZLY-0")

        def corpse():
            wb.open("https://youtu.be/eSeRjoolN2A")

        Wide_Knee_Child_Pose_frame = Frame(tr, bg="blue")
        Wide_Knee_Child_Pose_btn = Button(tr,
                                          text="Wide-Knee Child's Pose",
                                          cursor="hand2",
                                          height=1,
                                          bg="dark blue",
                                          fg="yellow",
                                          font="calibiri 24 bold italic",
                                          command=wideknee)
        Wide_Knee_Child_Pose_btn.pack(fill="both", expand=True)
        Wide_Knee_Child_Pose_frame.pack(fill="both", pady=10)
        Standing_Forward_Bend_frame = Frame(tr, bg="blue")
        Standing_Forward_Bend_btn = Button(tr,
                                           text="Wide-Knee Child's Pose",
                                           cursor="hand2",
                                           height=1,
                                           bg="dark blue",
                                           fg="yellow",
                                           font="calibiri 24 bold italic",
                                           command=cpp)
        Standing_Forward_Bend_btn.pack(fill="both", expand=True)
        Standing_Forward_Bend_frame.pack(fill="both", pady=10)
        RecliningBoundAngle_frame = Frame(tr, bg="blue")
        RecliningBoundAngle_btn = Button(tr,
                                         text="Reclining Bound Angle",
                                         cursor="hand2",
                                         height=1,
                                         bg="dark blue",
                                         fg="yellow",
                                         font="calibiri 24 bold italic",
                                         command=rba)
        RecliningBoundAngle_btn.pack(fill="both", expand=True)
        RecliningBoundAngle_frame.pack(fill="both", pady=10)
        LegsUpTheWallPose_frame = Frame(tr, bg="blue")
        LegsUpTheWallPose_btn = Button(
            tr,
            text="Legs Up The Wall Pose",
            cursor="hand2",
            height=1,
            bg="dark blue",
            fg="yellow",
            font="calibiri 24 bold italic",
        )
        LegsUpTheWallPose_btn.pack(fill="both", expand=True)
        LegsUpTheWallPose_frame.pack(fill="both", pady=10)
        CorpsePose_frame = Frame(tr, bg="blue")
        CorpsePose_btn = Button(tr,
                                text="Corpse Pose",
                                cursor="hand2",
                                height=1,
                                bg="dark blue",
                                fg="yellow",
                                font="calibiri 24 bold italic",
                                command=legupwall)
        CorpsePose_btn.pack(fill="both", expand=True)
        CorpsePose_frame.pack(fill="both", pady=10)
        LegsonaChairPose_frame = Frame(tr, bg="blue")
        LegsonaChairPose_btn = Button(tr,
                                      text="Legs on a Chair Pose",
                                      cursor="hand2",
                                      height=1,
                                      bg="dark blue",
                                      fg="yellow",
                                      font="calibiri 24 bold italic",
                                      command=corpse)
        LegsonaChairPose_btn.pack(fill="both", expand=True)
        LegsonaChairPose_frame.pack(fill="both", pady=10)

    def overall_page():
        br = Tk()
        br.geometry('1000x600')
        br.configure(bg="orange")
        br.title("Overall Fitness")

        def boat():
            wb.open("https://youtu.be/8KsyQvwi85Q")

        def dolphinplank():
            wb.open("https://youtu.be/fbxtdLxYQfM")

        def dolphin():
            wb.open('https://youtu.be/6w4ZoSuBDCg')

        def e():
            wb.open("https://youtu.be/0lfzG9jH6cM")

        def nn():
            wb.open("https://youtu.be/zSknyN77t2k")

        def lotus():
            wb.open("https://youtu.be/0kxczNm1xF4")

        def plank():
            wb.open("https://youtu.be/6qg3r4zZE_k")

        BoatPose_frame = Frame(br, bg="blue")
        BoatPose_btn = Button(br,
                              text="Boat Pose",
                              cursor="hand2",
                              height=1,
                              bg="dark blue",
                              fg="yellow",
                              font="calibiri 24 bold italic",
                              command=boat)
        BoatPose_btn.pack(fill="both", expand=True)
        BoatPose_frame.pack(fill="both", pady=10)
        DolphinPlankPose_frame = Frame(br, bg="blue")
        DolphinPlankPose_btn = Button(br,
                                      text="Dolphin Plank Pose",
                                      cursor="hand2",
                                      height=1,
                                      bg="dark blue",
                                      fg="yellow",
                                      font="calibiri 24 bold italic",
                                      command=dolphinplank)
        DolphinPlankPose_btn.pack(fill="both", expand=True)
        DolphinPlankPose_frame.pack(fill="both", pady=10)
        DolphinPose_frame = Frame(br, bg="blue")
        DolphinPose_btn = Button(br,
                                 text="Dolphin Pose",
                                 cursor="hand2",
                                 height=1,
                                 bg="dark blue",
                                 fg="yellow",
                                 font="calibiri 24 bold italic",
                                 command=dolphin)
        DolphinPose_btn.pack(fill="both", expand=True)
        DolphinPose_frame.pack(fill="both", pady=10)
        Extended_Side_Angle_Pose_frame = Frame(br, bg="blue")
        Extended_Side_Angle_Pose_btn = Button(br,
                                              text="Extended Side Angle Pose",
                                              cursor="hand2",
                                              height=1,
                                              bg="dark blue",
                                              fg="yellow",
                                              font="calibiri 24 bold italic",
                                              command=e)
        Extended_Side_Angle_Pose_btn.pack(fill="both", expand=True)
        Extended_Side_Angle_Pose_frame.pack(fill="both", pady=10)
        FourLimbedStaffPose_frame = Frame(br, bg="blue")
        FourLimbedStaffPose_btn = Button(br,
                                         text="Four-Limbed Staff Pose",
                                         cursor="hand2",
                                         height=1,
                                         bg="dark blue",
                                         fg="yellow",
                                         font="calibiri 24 bold italic",
                                         command=nn)
        FourLimbedStaffPose_btn.pack(fill="both", expand=True)
        FourLimbedStaffPose_frame.pack(fill="both", pady=10)
        LocustPose_frame = Frame(br, bg="blue")
        LocustPose_btn = Button(br,
                                text="Locust Pose",
                                cursor="hand2",
                                height=1,
                                bg="dark blue",
                                fg="yellow",
                                font="calibiri 24 bold italic",
                                command=lotus)
        LocustPose_btn.pack(fill="both", expand=True)
        LocustPose_frame.pack(fill="both", pady=10)
        PlanktPose_frame = Frame(br, bg="blue")
        PlankPose_btn = Button(br,
                               text="Plank Pose",
                               cursor="hand2",
                               height=1,
                               bg="dark blue",
                               fg="yellow",
                               font="calibiri 24 bold italic",
                               command=plank)
        PlankPose_btn.pack(fill="both", expand=True)
        PlanktPose_frame.pack(fill="both", pady=10)

    page = Tk()
    page.title("Excercises")
    page.geometry("1000x700")
    page.configure(bg="lightblue")
    digestion_frame = Frame(page, bg="blue")
    digestion_btn = Button(digestion_frame,
                           text="Digestion",
                           cursor="hand2",
                           height=1,
                           bg="dark blue",
                           fg="yellow",
                           font="calibiri 24 bold italic",
                           command=digestion_page)
    digestion_btn.pack(fill="both", expand=True)
    digestion_frame.pack(fill="both", pady=10)
    height_growth_frame = Frame(page, bg="blue")
    height_growth_btn = Button(height_growth_frame,
                               text="Height Growth",
                               cursor="hand2",
                               height=1,
                               bg="dark blue",
                               fg="yellow",
                               font="calibiri 24 bold italic",
                               command=heightgrowth_page)
    height_growth_btn.pack(fill="both", expand=True)
    height_growth_frame.pack(fill="both", pady=10)
    weight_growth_frame = Frame(page, bg="blue")
    weight_growth_btn = Button(weight_growth_frame,
                               text="Weight Gain",
                               cursor="hand2",
                               height=1,
                               bg="dark blue",
                               fg="yellow",
                               font="calibiri 24 bold italic",
                               command=weightgrowth_page)
    weight_growth_btn.pack(fill="both", expand=True)
    weight_growth_frame.pack(fill="both", pady=10)
    weight_decrease_frame = Frame(page, bg="blue")
    weight_decrease_btn = Button(weight_decrease_frame,
                                 text="Weight Loss",
                                 cursor="hand2",
                                 height=1,
                                 bg="dark blue",
                                 fg="yellow",
                                 font="calibiri 24 bold italic",
                                 command=weightdecrease_page)
    weight_decrease_btn.pack(fill="both", expand=True)
    weight_decrease_frame.pack(fill="both", pady=10)
    bodybuilding_frame = Frame(page, bg="blue")
    bodybuilding_btn = Button(bodybuilding_frame,
                              text="Body Building",
                              cursor="hand2",
                              height=1,
                              bg="dark blue",
                              fg="yellow",
                              font="calibiri 24 bold italic",
                              command=bodybuilding_page)
    bodybuilding_btn.pack(fill="both", expand=True)
    bodybuilding_frame.pack(fill="both", pady=10)
    bodypain_frame = Frame(page, bg="blue")
    bodypain_btn = Button(bodypain_frame,
                          text="Body Pain",
                          cursor="hand2",
                          height=1,
                          bg="dark blue",
                          fg="yellow",
                          font="calibiri 24 bold italic",
                          command=bodypain_page)
    bodypain_btn.pack(fill="both", expand=True)
    bodypain_frame.pack(fill="both", pady=10)
    goodsleep_frame = Frame(page, bg="blue")
    goodsleep_btn = Button(goodsleep_frame,
                           text="Sleep",
                           cursor="hand2",
                           height=1,
                           bg="dark blue",
                           fg="yellow",
                           font="calibiri 24 bold italic",
                           command=goodsleep_page)
    goodsleep_btn.pack(fill="both", expand=True)
    goodsleep_frame.pack(fill="both", pady=10)
    overall_frame = Frame(page, bg="blue")
    overall_btn = Button(overall_frame,
                         text="Overall Fitness",
                         cursor="hand2",
                         height=1,
                         bg="dark blue",
                         fg="yellow",
                         font="calibiri 24 bold italic",
                         command=overall_page)
    overall_btn.pack(fill="both", expand=True)
    overall_frame.pack(fill="both", pady=10)


window = Tk()
window.title("Stay Fit App")
window.geometry("1300x760")
window.configure(bg="lightgrey")

title = Label(
    window,
    text=
    "---------------------------------------Welcome to Stay Fit app----------------------------",
    bg="blue",
    fg="yellow",
    font="algerian 32 bold")
title.pack(fill="both")

reg_frame = Frame(window, bg="blue")
registering = Button(reg_frame,
                     text="Register yourself to our app 📝",
                     cursor="hand2",
                     height=2,
                     bg="dark blue",
                     fg="yellow",
                     font="calibiri 24 bold italic",
                     command=reg_form)
registering.pack(fill="both", expand=True)
reg_frame.pack(fill="both", pady=10)
button_frame = Frame(window, bg="red")
diet = Button(button_frame,
              text="Report based on your data 📋",
              height=2,
              cursor="hand2",
              bg="red",
              fg="yellow",
              font="calibiri 24 bold italic",
              command=data_report)
diet.pack(fill="both")
button_frame.pack(pady=10, fill="both")

msg_frame = Frame(window, bg="hotpink")
msg_btn = Button(msg_frame,
                 text="Motivational Messages! ✉",
                 height=2,
                 cursor="hand2",
                 bg="hotpink",
                 fg="purple",
                 font="calibiri 24 bold italic",
                 command=message)
msg_btn.pack(fill="both")
msg_frame.pack(fill="both", pady=10)

msg_frame = Frame(window, bg="hotpink")
msg_btn = Button(msg_frame,
                 text="Exercises 💪🏻",
                 height=2,
                 cursor="hand2",
                 bg="lightblue",
                 fg="blue",
                 font="calibiri 24 bold italic",
                 command=excercise_page)
msg_btn.pack(fill="both")
msg_frame.pack(fill="both", pady=10)

btn_frame = Frame(window, bg="dark green")
setting_btn = Button(btn_frame,
                     text="Instructions",
                     height=2,
                     cursor="hand2",
                     bg="dark green",
                     fg="yellow",
                     font="calibiri 24 bold italic",
                     command=intro)
setting_btn.pack(fill="both")
btn_frame.pack(fill="both")
button_frame.pack(pady=30, fill="both")

while True:
    try:
        from plyer import noticification
        noticification.notify(
            title="STAY FIT APP",
            message=
            "Welcome to stay fit app. Please read instructions if any confusion on how to use the app. We don't own any of the tutorials the respective youtube channels own them.",
            timeout=12)
        window.mainloop()
    except:
        window.mainloop()
