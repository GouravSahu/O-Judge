import filecmp

f1=open("C:/Users/HP/Desktop/Algo_project/media/2/my-out.txt","r")
f2=open("C:/Users/HP/Desktop/Algo_project/media/2/out.txt","r")

lines1=f1.readlines()
lines2=f2.readlines()


if(lines1==lines2):
    print(True)
else:
    print(False)


# Create your tests here