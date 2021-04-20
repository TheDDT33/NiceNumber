# Nice Number

from tkinter import *

GUI = Tk()
GUI.geometry('550x450')


F1 = Frame(GUI)
F1.pack()

FONT1 = (None,20)

L = Label(F1, text='หมายเลขของคุณคือ', font=FONT1)
L.pack()

v_yournumber = StringVar()
L0 = Label(F1, textvariable=v_yournumber, font=FONT1, fg='BLUE')
L0.pack()

L1 = Label(F1, text='ผลรวมของคุณคือ', font=FONT1)
L1.pack()

v_total = StringVar()
L2 = Label(F1, textvariable=v_total, font=FONT1, fg='BLUE')
L2.pack()

L3 = Label(F1, text='ผลลัพธ์ที่ได้คือ', font=FONT1)
L3.pack()

v_meaning = StringVar()
L4 = Label(F1, textvariable=v_meaning, font=FONT1, fg='BLUE')
L4.pack(ipadx=15,ipady=15)

L5 = Label(F1, text='กรุณาใส่หมายเลขโทรศัพท์', font=FONT1)
L5.pack()

v_number1 = StringVar()
E1 = Entry(F1, textvariable=v_number1, font=FONT1, justify='center')
E1.pack()


def TotalNum(event=None):
    total = 0
    number = v_number1.get()
    v_yournumber.set(number)
    for i in number:
        total += int(i)
        v_number1.set('')

    def NiceTranslate(number):
        meaning = ''
        if number in (9, 14, 15, 19, 23, 24, 32, 36, 40, 41, 42, 44, 45, 46, 50, 51, 54, 55, 56, 59, 63, 64, 65):
            meaning = 'ให้คุณระดับดีมาก'

        elif number in (69, 79):
            meaning = 'โอกาสประสบผลสำเร็จสูง\n อุปสรรคน้อย\n เจริญรุ่งเรือง ร่ำรวย\n รวดเร็ว และมีความสุข'

        elif number in (10, 13, 16, 18, 20, 22, 25, 26, 28, 31, 35, 38, 39, 47, 49, 52, 53, 57, 58, 60, 61):
            meaning = 'ให้คุณระดับดีปานกลาง'

        elif number in (62, 66, 68, 74, 75):
            meaning = 'เหนื่อย มีอุปสรรค แต่ยังมีโอกาสประสบผลสำเร็จ หากมีความพยายาม'

        elif number in (11, 12, 17, 21, 27, 29, 30, 33, 34, 37, 43, 48, 67, 70, 71, 72, 73, 76, 77, 78, 80):
            meaning = 'เหนื่อยมาก อุปสรรคมาก\n เจอปัญหารุมเร้า การงาน\n การเงิน ความรัก\n เกิดอุบัติเหตุชีวิตไม่จบไม่สิ้น'
        
        return meaning

    v_meaning.set(NiceTranslate(total))

    return v_total.set(total)

GUI.bind('<Return>',TotalNum)

B1 = Button(F1, text='START', command=TotalNum, font=FONT1)
B1.pack()

GUI.mainloop()