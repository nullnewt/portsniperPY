from tkinter import *
import psutil
import time

program_list = [""]

port_listSTR = []
for i in range(19, 501):
    port_listSTR.append(str(i).zfill(1))

port = range(50, 5000)

root = Tk()
root.title("Port Proj")


def port_search(*args):
    # get_pid()
    port_vis = p.name() + "\n Port: " + e.get()
    if e.get() in port_listSTR:
        label1.config(text=port_vis)
        label2.config(text=port_vis)
        label3.config(text=port_vis)
        label4.config(text=port_vis)
    elif e.get() == "" or e.get() not in port_listSTR:
        pass


e = Entry(root, width=10, borderwidth=5)
search = Button(root, text="Find Port", command=port_search, padx=45, pady=6)
e.bind("<Return>", port_search)


def get_pid():
    connections = psutil.net_connections()
    for con in connections:
            if con.raddr != tuple():
                if con.raddr.port in port:
                    return con.pid, con.status, con.raddr.port
            #
            # if e.get() in port_listSTR:
            #     if con.raddr != tuple():
            #         if str(con.raddr.port) == e.get():
            #             return con.pid, con.status


# Labels
label1 = Label(root, text="program X\n Port: ", pady=10, padx=30)
label2 = Label(root, text="program X\n Port: ", pady=10, padx=30)
label3 = Label(root, text="program X\n Port: ", pady=10, padx=30)
label4 = Label(root, text="program X\n Port: ", pady=10, padx=30)

label1.grid(column=0, row=1)
label2.grid(column=0, row=3)
label3.grid(column=0, row=5)
label4.grid(column=0, row=7)

search.grid(column=1, row=0)
e.grid(column=0, row=0)

# Buttons - Add kill button
kill_port1 = Button(root, text="Kill Program", padx=30, pady=5)
kill_port2 = Button(root, text="kill program", padx=30, pady=5)
kill_port3 = Button(root, text="kill program", padx=30, pady=5)
kill_port4 = Button(root, text="kill program", padx=30, pady=5)

kill_port1.grid(column=1, row=1)
kill_port2.grid(column=1, row=3)
kill_port3.grid(column=1, row=5)
kill_port4.grid(column=1, row=7)

x = 0
if __name__ == '__main__':
    start = time.time()
    while x < 4:
            pid = get_pid()
            p = psutil.Process(pid[0])
            # Checking if program is in list
            # If not in list, put in list and append labels.
            if p.name() not in program_list:
                x += 1
                label_txt = p.name() + "\n" + f"{pid[1]}" + "\nPort: " + str(pid[2])
                # Appending to label so all labels are named correctly with different programs
                label_inc = "label" + str(x)
                configobj = eval(label_inc)
                configobj.config(text=label_txt)
                # Adding name of program to list as to not insert same program twice.
                program_list.insert(0, p.name())
            # If program in list, pass
            if p.name() in program_list:
                pass

#
# def kill_me():
#     p = psutil.Process(pid[0])
#     p.terminate()




root.mainloop()

end = time.time()
print("time taken")
print(end - start)
