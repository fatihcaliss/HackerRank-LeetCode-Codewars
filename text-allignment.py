w = int(input())   #  width
h = "H"
x = 1   #  its for top hone
for i in range(w):
    print((h * x).center(w*2))
    x += 2
#Top Pillars
for i in range(w+1):
    print((h*w).center(w*2)+(h*w).center(w*6))

#Middle Belt
for i in range((w+1)//2):
    print((h*w*5).center(w*6))    

#Bottom Pillars
for i in range(w+1):
    print((h*w).center(w*2)+(h*w).center(w*6)) 
y = w * 2 - 1
for i in range(w):
    print((h * y).center(w * 10))
    y -= 2

