# # from turtle import *
# # import colorsys

# # speed(0)
# # bgcolor("black")
# # h = 0
# # for i in range(144):
# #     for j in range(19):
# #         c = colorsys.hsv_to_rgb(h, 1, 1)
# #         color(c)
# #         h += 8.0 / 255 
# #         rt(90)
# #         circle(150 - j * 1.1, 360)
# #         lt(90)
# #         circle(150 - j * 1.1, 360)
# #         rt(180)
# #     circle (40,24)     
# #     done()



# from turtle import *
# import colorsys
# speed(0)
# bgcolor("black")
# pensize(2)
# h = 0

# for i in range(100):
#     c = colorsys.hsv_to_rgb(h, 1, 1)
#     h += 0.01
#     color(c)
#     circle(150)
#     right(10)

# done()


 # Program to print multiplication table using range()

# # Taking user input
# num = int(input("Enter a number to print its multiplication table: "))

# print(f"\nMultiplication Table of {num}\n")

# # Using range() to print 1 to 10 multiples
# for i in range(1, 11):
#     result = num * i
#     print(f"{num} x {i} = {result}")
