from tkinter import *
import customtkinter
import openai
import os
import pickle


root = customtkinter.CTk()
root.title("MyChatGPT BOT")
root.geometry('600x600')
root.iconbitmap('ai_lt.ico')

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def speak():
	if(chat_entry.get()):
		filename = "api_key"
		if(os.path.isfile(filename)):
			input_file=open(filename, 'rb')
			stuff = pickle.load(input_file)
				
			openai.api_key=stuff
			openai.Model.list()
			response = openai.Completion.create(
				model="text-davinci-002",
				prompt = chat_entry.get(),
				temprature = 0,
				max_tokens=60,
				top_p = 1.0,
				frequency_penalty=0.0,
				presence_penalty=0.0

				)

			my_text.insert(END, response)
			my_text.insert(END, "\n\n")
		else:
			input_file = open(filename, 'wb')
			input_file.close()
			my_text.insert(END, "\n\n YOU need an API KEY\n Get one here \n https://open.ai")

	
	
	else:
		my_text.insert(END, "\n\nHey! type something")
	root.geometry('600*750')
	api_frame.pack(pady=30)

def clear():
	my_text.delete(1.0, END)
	chat_entry.delete(0, END)
	
def key():
	
	filename = "api_key"
	if(os.path.isfile(filename)):
		input_file=open(filename, 'rb')
		stuff = pickle.load(input_file)

		api_entry.insert(END, stuff)
	else:
		input_file = open(filename, 'wb')
		input_file.close()

	root.geometry('600*750')
	api_frame.pack(pady=30)
	

def save_key():
	api_frame.pack_forget()
	root.geometry('600*600')
	filename="api_key"
	output_file = open(filename, "wb")
	pickle.dump(api_entry.get(), output_file)

	api_entry.delete(0, END)

	

text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)
my_text=Text(text_frame,
	bg="#343638",
	width=65,
	bd=1,
	fg="#d6d6d6",
	relief="flat",
	wrap=WORD,
	selectbackground="#1f538d")
my_text.grid(row=0, column=0)

text_scroll = customtkinter.CTkScrollbar(text_frame, command=my_text.yview)

text_scroll.grid(row=0,column=1,sticky="ns")

my_text.configure(yscrollcommand=text_scroll.set)

chat_entry = customtkinter.CTkEntry(master=root,
	placeholder_text="Type something to chat with Chat GPT...", 
	width=535,
	height=50,
	border_width=2)
chat_entry.pack(padx=20, pady=10)

button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)


submit_button=customtkinter.CTkButton(button_frame, text="Speak To ChatGpt", command=speak)
submit_button.grid(row=0,column=0,padx=25)


clear_button=customtkinter.CTkButton(button_frame, text="Clear Response", command=clear)
clear_button.grid(row=0,column=1,padx=35)



api_button=customtkinter.CTkButton(button_frame, text="Update API Key", command=key)
api_button.grid(row=0,column=2,padx=25)

api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=10)

api_entry = customtkinter.CTkEntry(api_frame, placeholder_text="Enter you API Key", width=350, height = 50 , border_width=1)

api_entry.grid(row=0,column=0,padx=20,pady=20)

api_save_button = customtkinter.CTkButton(api_frame, text="Save Key", command=save_key)
api_save_button.grid(row=0,column=1)
root.mainloop()

