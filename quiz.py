import json, random, tkinter
from tkinter import *
from tkinter import messagebox

def click(x,y,index):
    global question_index, score

    if ans_btn_list[x][y]["text"] == question_list[question_index]["answer"]:
        
        score +=10
        
        score_lbl.config(
            text="SCORE {}".format(score)
        )

        ans_btn_list[x][y].config(
            bg="green"
        )
        messagebox.showinfo("FEEDBACK", "CORRECT")
        question_index = (question_index + 1) % len(question_list)
        next_question(question_index)
    else:
        messagebox.showinfo("FEEDBACK", "WRONG")

def next_question(question_index):
    for i in range(len(question_list)):
        random.shuffle(question_list[i]["choices"])

    for i in range(len(ans_btn_list)):
        for j in range(len(ans_btn_list[0])):
            ans_btn_list[i][j].config(
                bg="#f0f0f0"
            )

    question_label.config(text=question_list[question_index]["question_name"])
    item = 0
    for i in range(len(ans_btn_list)):
        for j in range(len(ans_btn_list[0])):
            ans_btn_list[i][j].config(
                text=question_list[question_index]["choices"][item]
            )
            item +=1
    
def reset():
    global score, question_index
    score, question_index = 0,0
    score_lbl.config(text="SCORE {}".format(score))
    random.shuffle(question_list)
    next_question(question_index)
    
def init_game():
    

    random.shuffle(question_list)
    for i in range(len(question_list)):
        random.shuffle(question_list[i]["choices"])
    question_label = Label(
    window,
    text=question_list[0]["question_name"],
    font=("futura-bold", 14),
    bg="yellow",
    padx=10,
    pady=10,
    wraplength=450
    )
    question_label.pack(padx=10, pady=10)

    item = 0
    question_index = 0 % len(question_list)
    for i in range(len(ans_btn_list)):
        for j in range(len(ans_btn_list[0])):
            ans_btn_list[i][j] = Button(
                window,
                padx=10,
                pady=10,
                font=("futura-bold", 14),
                width=50,
                wraplength=450,
                justify=CENTER,
                text=question_list[question_index]["choices"][item],
                command=lambda x=i, y=j, index=question_index:click(x,y,index)
            )
            item +=1
            ans_btn_list[i][j].pack()

window = Tk()
window.geometry(f"500x500")
window.title("Quiz game")
window.resizable(False, False)

with open("question.json") as f:
    question_file = json.load(f)
    
question_list = [
    question_file["questions"][i] for i in range(len(question_file["questions"]))
]

random.shuffle(question_list)
for i in range(len(question_list)):
    random.shuffle(question_list[i]["choices"])
    

top_frame = Frame(
    window
)
top_frame.pack(side=TOP, padx=10, pady=10)
    
score = 0       
score_lbl = Label(
    top_frame,
    font=14,
    text="SCORE 0",
    padx=10,
    pady=10,
    width=10
)
score_lbl.pack(side=LEFT)

reset = Button(
    top_frame,
    font=14,
    padx=10,
    pady=10,
    text="Reset",
    command=reset
)
reset.pack(side=RIGHT)

question_label = Label(
    window,
    text=question_list[0]["question_name"],
    font=("futura-bold", 14),
    bg="yellow",
    padx=10,
    pady=10,
    wraplength=450
)
question_label.pack(padx=10, pady=10)



ans_btn_list = [
    [0,0],
    [0,0]
]
item = 0
question_index = 0 % len(question_list)
for i in range(len(ans_btn_list)):
    for j in range(len(ans_btn_list[0])):
        ans_btn_list[i][j] = Button(
            window,
            padx=10,
            pady=10,
            font=("futura-bold", 14),
            width=50,
            wraplength=450,
            justify=CENTER,
            text=question_list[question_index]["choices"][item],
            command=lambda x=i, y=j, index=question_index:click(x,y,index)
        )
        item +=1
        ans_btn_list[i][j].pack()

window.mainloop()
