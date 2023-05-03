#Copy and run this code in your compiler to enjoy my game.
#Guessing the number Game
#You will definitely enjoy it
import random
n=[1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33,
34,
35,
36,
37,
38,
39,
40,
41,
42,
43,
44,
45,
46,
47,
48,
49,
50,
51,
52,
53,
54,
55,
56,
57,
58,
59,
60,
61,
62,
63,
64,
65,
66,
67,
68,
69,
70,
71,
72,
73,
74,
75,
76,
77,
78,
79,
80,
81,
82,
83,
84,
85,
86,
87,
88,
89,
90,
91,
92,
93,
94,
95,
96,
97,
98,
99,
100]
num=random.choice(n)
print("Welcome to the Game")
print("You have to guess the correct number between 1 to 100")
level=input("Choose level Easy or Hard")
if(level=="easy"):
  print("You have 10 attempts")
  t=10;
  while(t):
    guess=int(input("Guess number"))
    if(guess==num):
      print("Congratulations! You Win")
    elif(guess>num):
      print("TO high")
    elif(guess<num):
      print("To low")
      t=t-1

if(level=="hard"):
  print("You have 5 attempts")
  t2=5;
  while(t2):
    guess=int(input("Guess number"))
    if(guess==num):
      print("Congratulations! You Win")
    elif(guess>num):
      print("TO high")
    elif(guess<num):
      print("To low")
      t2=t2-1
  



