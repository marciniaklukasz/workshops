import turtle
boki = int(turtle.numinput('Pytanie', 'Podaj liczbe bokow'))
t = turtle.Turtle()
turtle.c
kat = 360/boki

for i in range (1,boki+1):
    t.color('blue')
    t.width(5)
    t.left(kat)
    t.forward(50/(boki*.05))

turtle.mainloop()