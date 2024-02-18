import json

path = "D:\Mark\Desktop\Logika_Python\notes\data\notes.json"

class NotesDao():


    def createNote(self, title):
        note = {
            "title": title,
            "text": "",
            "tags": []
        }

    def getNotes(self):
        pass

    def updateNoteText(self, title, newText):

        pass

    def deleteNote(self, deleteTitle):
        
       pass


    def addTag(self, title, tag):
        pass

    def deleteTag(self):
        pass

    def saveFile(self, notes):
        pass