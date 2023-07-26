import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')

costs = [0.25, 0.23, 0.21, 0.19, 0.17, 0.15]

data  = {
	10000:costs[0],
	15000:costs[1],
	25000:costs[2],
	50000:costs[3],
	100000:costs[4],
	250000:costs[5],
}

def calculate():
	inp = inputtxt.get(1.0, "end-1c")
	lbl.config(text = "Provided Input: " + inp + " users")
	if inp.isnumeric():
		total_cost = 0
		number = int(inp)
		for key in data:
			if number-key >=0:
				number -= key
				total_cost += key*data[key]
			else:
				total_cost += data[key] * number
				number = 0
				print(total_cost)
				lbl2.config(text = "Total cost = $"+str(total_cost))
				break
				
	else:
		lbl.config(text = "Invalid input: "+inp + "\n enter a valid number")
		
		

# TextBox Creation
lbl0 = tk.Label(frame, text = "Enter total users:")
lbl0.pack()

inputtxt = tk.Text(frame,
				height = 5,
				width = 20)

inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,
						text = "Calculate",
						command = calculate)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()

lbl2 = tk.Label(frame, text = "")
lbl2.pack()
frame.mainloop()
