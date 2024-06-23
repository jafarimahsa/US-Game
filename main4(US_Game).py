import turtle , pandas

#print(data)
screen = turtle.Screen()
screen.title('U.S .States Game')
screen.setup(height=500 , width=740)
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
states_to_learn = list()
gussed_states = list()

while len(gussed_states) < 50 :
    answer_state = screen.textinput(title=f'{len(gussed_states)}/50 states correct' , prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        for state in all_states:
            if state not in gussed_states:
                states_to_learn.append(state)
        print(states_to_learn)
        break
    elif answer_state in all_states:
        gussed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x) , int(state_data.y))
        #t.write(state_data.state)
        t.write(answer_state) # or : t.write(state_data.data.item())
        
new_data = pandas.DataFrame(states_to_learn)
print(new_data)
new_data.to_csv('states_to_learn.csv')
#screen.exitonclick()  #turtle.mainloop()