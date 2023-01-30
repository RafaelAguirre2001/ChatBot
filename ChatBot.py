import json
import tkinter as tk

def search_response(question, data):
    for q in data:
        if q["question"].lower() == question.lower():
            return q["answer"]
    return "Lo siento, no tengo una respuesta para esa pregunta."

class ChatBotGUI:
    def __init__(self, master, data):
        self.master = master
        self.data = data

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.question_label = tk.Label(self.frame, text="Pregunta:")
        self.question_label.pack()

        self.question_entry = tk.Entry(self.frame)
        self.question_entry.pack()

        self.ask_button = tk.Button(self.frame, text="Preguntar", command=self.ask)
        self.ask_button.pack()

        self.answer_label = tk.Label(self.frame, text="Respuesta:")
        self.answer_label.pack()

        self.answer_text = tk.Text(self.frame, height=10, width=50)
        self.answer_text.pack()

    def ask(self):
        question = self.question_entry.get()
        answer = search_response(question, self.data)
        self.answer_text.delete("1.0", tk.END)
        self.answer_text.insert(tk.END, answer)

if __name__ == "__main__":
    with open("preguntas.json", "r") as file:
        data = json.load(file)

    root = tk.Tk()
    app = ChatBotGUI(root, data)
    root.mainloop()
