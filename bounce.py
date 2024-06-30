from vpython import *

'''
會用到的參數
'''
g=9.8
size = 0.25
theta=pi/4
c_drag = 0.9




'''
背景以及顏色與高度的設定
還有球以及向量
'''

scene = canvas(width=600,height=600,center=vec(0,5,0),align='left',background=vec(0.5,0.5,0))
floor = box(length=30, height=0.5, width=10, color=color.blue)
ball = sphere(radius = size, color=color.red, make_trail = True)

vtgraph=graph(width=600,align='left')
funct1=gcurve(graph=vtgraph,color=color.purple,width=4)


ball.pos = vec( -15,size, 0)               
ball.v = vec(20*cos(theta),20*sin(theta), 0)
a1=arrow(color=color.green,shaftwidth=0.1)




            
'''
迴圈內容
(1)只要彈跳3次
(2)計算最高高度
(3)路徑長分段討論(小段畢式)
'''
dt = 0.001
t=0
s=0                                                 #總路徑長從0開始加
boundtimes=0                                        #從彈跳次數為0開始加起
larges_height=0                                     #先從最高高度為0當起始
while boundtimes<3:                   
    rate(1000)
    

    ball.pos += ball.v*dt                           #等同於 ball.pos=ball.pos+ball.v*dt
    ball.v += vec(0,-g,0)*dt-c_drag*ball.v*dt
    t+=dt
    funct1.plot(pos=(t,ball.v.mag))

    a1.pos=ball.pos                                 #箭頭位置隨著球移動
    a1.axis=ball.v*1                                #向量與速度的比例
    s=s+(((ball.v.x)**2+(ball.v.y)**2)**(1/2))*dt   #總路徑長


    if ball.pos.y <= size and ball.v.y < 0:         #碰到地板
        ball.v.y = - ball.v.y                       #完全彈性碰撞(速度加負號)
        boundtimes +=1
    if ball.pos.y > larges_height: 
        larges_height=ball.pos.y

        

displacement=mag(ball.pos-vec( -15,size, 0))        #位移


            
'''
圖片顯示資訊
'''

msg1 =text(text = 'total_distance='+str(s), pos = vec(-10, 8, 0))
msg2 =text(text = 'larges_height='+str(larges_height), pos = vec(-10, 10, 0))
msg3 =text(text ='displacement='+ str(displacement), pos = vec(-10, 12, 0))

print('displacement=',displacement)
print('larges_height=' ,larges_height)
print('total_distance=' ,s)




