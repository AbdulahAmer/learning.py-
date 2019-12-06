'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Abdulah Amer 
Uploaded: December 6th 2019 

Learning how to model physical situations using vpython
Starting with a  one dimensional ball drop, complete with GUI 
and an ability to make relevant graphs. 

Hit startand then change parameters, hit reset again, then hit start once more.
Keep going on often as youd like and see how terminal velocity works. 

Any questions let me know! 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


from vpython import *
scene.width=400
scene.center=vector(0,5,0)
scene.height=400

ball=sphere(pos=vector(0,10,0), radius=.5, color=color.red, make_trail=False, trail_type="points", retain=100)
ground=box(pos=vector(0,0,0), size=vector(10,.1,10), color=color.blue)


g=-9.8
y=10
V=0
dt=.01
drag=0
t=0

V_vs_t=graph(width=300, height=200, title='<b> Velcoity vs Time </b>',
xtitle='<i> time </i>', ytitle='<i> Velocity <i>')
VDots = gdots(color=color.green)

a_vs_t=graph(width=300, height=200, title='<b> Acceleration versus Time </b> ',
xtitle='<i> Time </i>', ytitle='<i> Acceleration <i>')
aDots=gdots(color=color.red)


def makegraphs():
    global V_vs_t, VDots, a_vs_t, aDots

    V_vs_t=graph(width=400, height=200, title='<b> Velcoity vs Time </b>',
    xtitle='<i> time </i>', ytitle='<i> Velocity <i>')
    VDots = gdots(color=color.green)


    a_vs_t=graph(width=300, height=200, title='<b> Acceleration versus Time </b> ',
    xtitle='<i> Time </i>', ytitle='<i> Acceleration <i>')
    aDots=gdots(color=color.red)

    return V_vs_t, VDots, a_vs_t, aDots

def deletegraphs():
    V_vs_t.delete()
    a_vs_t.delete()

makegraphs()

def airdrop():
    global y,V,drag,t,output
    while ball.pos.y-ball.radius>0:
        rate(100)
        a=g+(drag*V**2)
        y+=V*dt
        V+=a*dt
        ball.pos=vector(0,y,0)
        t+=dt
        

        VDots.plot(t,V)
        aDots.plot(t,a)

    string='finished in: '+ str(t)+ ' seconds '+'final velcoity of: '+ str(V)+ ' m/s'

    output=wtext(text='\n' + string)

    return output

#great we see that we can not pass arguments to functions that are bound to buttons

#lets try this with sliders now to change values for practice

def adjustDrag():
    dragSliderReadout.text=dragSlider.value

dragSlider=slider(max=5, min=0, step=.1, value=0, bind=adjustDrag)
scene.append_to_caption('Drag: ')
dragSliderReadout=wtext(text='0')

def adjustHeight():
    heightSliderReadout.text=heightSlider.value

heightSlider=slider(min=0, max=100, step=1, value=y, bind=adjustHeight)
scene.append_to_caption('Height: ')
heightSliderReadout=wtext(text=y)


def reset():
    global y,V,drag,t
    y=heightSlider.value
    V=0
    t=0
    drag=dragSlider.value
    ball.pos=vector(0,y,0)
    scene.center=vector(0,ball.pos.y/2, 0)
    deletegraphs()
    makegraphs()

rbutton=button(bind=reset, text='reset')
abutton=button(bind=airdrop, text='start')
