from os import system
banner="""kareem walid x_x 
hello 
1-get update
2-get upgrade
3-update metasploit
4-start localhost
5-exit"""
print(banner)
c=int(input("enter > "))
#commands
update="sudo apt-get update"
upgrade="sudo apt-get upgrade"
meta="sudo msfupdate"
loc="sudo service apache2 start"
if c == 1:
	system("sleep 4")
	system(update)
elif c == 2:
	system("sleep 4")
	system(upgrade)
elif c == 3:
	system("sleep 4")
	system(meta)
elif c == 4:
	system("sleep 4")
	system(loc)
elif c == 5:
	exit()
else:
	print("Not Found")
	exit()
