from pyscript import document

class Classmate:
    def __init__(self, name, section, favsubject):
        self.name = name
        self.section = section
        self.favsubject = favsubject

    def introduce(self):
        return f"Hello! I am {self.name} from {self.section}. My favorite subject is {self.favsubject}."

# Proper list name
classmate_list = [
    Classmate("Kaitlin", "Emerald", "I.C.T"),
    Classmate("Sophia", "Emerald", "C.A.T"),
    Classmate("Margaux", "Emerald", "Music & Arts"),
    Classmate("Alwit", "Emerald", "Math"),
    Classmate("Rochel", "Emerald", "English"),
    Classmate("Padme", "Emerald", "Arts"),
    Classmate("Matt Sky", "Emerald", "Science"),
    Classmate("Samuel", "Emerald", "Physical Education"),
]

# HTML elements
name_input = document.getElementById("name")
section_input = document.getElementById("section")
favsubject_input = document.getElementById("favsubject")
output = document.getElementById("output")
message = document.getElementById("message")

# function to display list
def render_list(event=None):
    output.innerHTML = ""

    if not classmate_list:
        output.innerHTML = '<p class="text-muted">No classmates added yet.</p>'
        return

    for student in classmate_list:
        output.innerHTML += f'<p class="mb-2">{student.introduce()}</p>'

# Add classmate
def addClassmate(event=None):
    name = name_input.value.strip()
    section = section_input.value.strip()
    subject = favsubject_input.value.strip()

    # to make sure all fields are filled in
    if not name or not section or not subject:
        message.innerHTML = 'Please fill in all fields.'
        return

    classmate_list.append(Classmate(name, section, subject))

    name_input.value = ""
    section_input.value = ""
    favsubject_input.value = ""

    message.innerHTML = 'A new classmate is added! Click "Show List" again :)'

# Show list
def showList(event=None):
    render_list()