def readingNotes():
    with open("exam_notes.txt","r", encoding="utf-8") as file:
        for line in file:
            print(line)

def enteringNotes():
    name = input("Student Name: ")
    surname = input("Student Surname: ")
    note1 = input("Note 1: ")
    note2 = input("Note 2: ")
    note3 = input("Note 3: ")

    with open("exam_notes.txt","a", encoding="utf-8") as file:
        file.write(name + " "+ surname+ ":"+note1+","+note2+","+note3+"\n")


def savingNotes():
    with open("exam_notes.txt","r", encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(i)

        with open("results.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)




while True:
    islem = input("1- Read Notes\n2- Enter Notes\n3- Save Notes\n4- Exit\n")

    if islem == "1":
        readingNotes()
    elif islem == "2":
        enteringNotes()
    elif islem == "3":
        savingNotes()
    else:
        break
