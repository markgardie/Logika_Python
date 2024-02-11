import json

path = "D:\Mark\Desktop\Logika_Python\notes\data\notes.json"

class NotesDao():


    def createNote(self, title):
        note = {
            "title": title,
            "text": "",
            "tags": []
        }

        notes = self.getNotes()
        notes.append(note)

        self.saveFile(notes)

    def getNotes(self):
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def updateNoteText(self, title, newText):

        notes = self.getNotes()

        for note in notes:
            if note["title"] == title:
                note["text"] = newText

        self.saveFile(notes)
        

    def deleteNote(self, deleteTitle):
        
        notes = self.getNotes()

        for note in notes:
            if note["title"] == deleteTitle:
                notes.remove(note)

        self.saveFile(notes)


    def addTag(self, title, tag):
        notes = self.getNotes()

        for note in notes:
            if note["title"] == title:
                note["tags"].append(tag)

    def deleteTag(self):
        pass

    def saveFile(self, notes):
        with open(path, "w", encoding="utf-8") as file:
            json.dump(notes, file)

