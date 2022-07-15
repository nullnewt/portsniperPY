from tkinter import *
import psutil

program_list = [""]

port_listSTR = []
for i in range(19, 501):
    port_listSTR.append(str(i).zfill(1))

port = range(50, 500)

root = Tk()
root.title("port_meme_Maybe")


# FIX THIS-SSSS
def port_search(*args):
    result = e.get()
    get_pid()
    port_vis = p.name() + "\n Port: " + result
    if result in port_listSTR:
        label1.config(text=port_vis)
        label2.config(text=port_vis)
        label3.config(text=port_vis)
    elif result == "" or result not in port_listSTR:
        pass
        label4.config(text=port_vis)


e = Entry(root, width=10, borderwidth=5)
search = Button(root, text="Find Port", command=port_search, padx=45, pady=6)
e.bind("<Return>", port_search)


def get_pid():
    connections = psutil.net_connections()
    print("PID")
    for con in connections:
        # if e.get() in port_listSTR:
        #     print(e.get())
        #     # make me work
        #     if con.raddr != tuple():
        #         if str(con.raddr.port) == e.get():
        #             return con.pid, con.status
        # if e.get() == "":
            if con.raddr != tuple():
                if con.raddr.port in port:
                    global raddr_port
                    raddr_port = con.raddr.port
                    return con.pid ,con.status


# Labels
label1 = Label(root, text="program X\n Port: ", pady=10, padx=30)
label2 = Label(root, text="program X\n Port: ", pady=10, padx=30)
label3 = Label(root, text="program X\n Port: ", pady=10, padx=30)
label4 = Label(root, text="program X\n Port: ", pady=10, padx=30)

# Buttons
kill_port1 = Button(root, text="Kill Program" , padx=30, pady=5)
kill_port2 = Button(root, text="kill program 2", padx=30, pady=5)
kill_port3 = Button(root, text="kill program 3", padx=30, pady=5)
kill_port4 = Button(root, text="kill program 4", padx=30, pady=5)

label1.grid(column=0, row=1)
label2.grid(column=0, row=3)
label3.grid(column=0, row=5)
label4.grid(column=0, row=7)

kill_port1.grid(column=1, row=1)
kill_port2.grid(column=1, row=3)
kill_port3.grid(column=1, row=5)
kill_port4.grid(column=1, row=7)

search.grid(column=1, row=0)
e.grid(column=0, row=0)

x = 1
while x < 5:
    if len(list(port)) > 1:
        pid = get_pid()
        if pid == -1:
            pass
        else:
            p = psutil.Process(pid[0])
            if p.name() not in program_list:
                x += 1
                label_txt = p.name() + "\n" + "Port: " + str( raddr_port )
                label_inc = "label" + str(x)
                configobj = eval(label_inc)
                configobj.config(text=label_txt)
                program_list.insert(0,p.name())
                # print( program_list )
                print(x)
            if p.name() in program_list:
                pass

root.mainloop()


