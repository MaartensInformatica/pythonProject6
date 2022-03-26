import mysql.connector as conn
import tkinter
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.db = Database()

        self.main_window = tkinter.Tk()
        song_var = tkinter.StringVar(value=[])
        self.listbox = tkinter.Listbox(self.main_window,
                                       listvariable=song_var,
                                       height=20,
                                       selectmode='extended')
        self.listbox.pack(expand=True, fill=tkinter.Y)
        self.fill_listbox(self.db.get_songs())
        tkinter.mainloop()

    def fill_listbox(self, songs):
        for i in range(len(songs)):
            self.listbox.insert(i, songs[i])



class Database:
    def __init__(self):
        self.connection = conn.connect(
            host="145.74.104.145",
            user="onnzj",
            password="Aa674667!",
            database="blok3")

    def get_songs(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT name, m.title "
                       "FROM muzieknummers m "
                       "JOIN album a on a.id = m.album_id "
                       "JOIN artiest a2 on a.artiest_id = a2.id")
        result = cursor.fetchall()

        return result





if __name__ == '__main__':

    gui = GUI()


