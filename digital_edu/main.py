import pandas as pd

df = pd.read_csv(r"digital_edu\train.csv")

df.drop(["id", "bdate", "has_photo"], axis=1, inplace=True)

def fill_form(form):
    if form == "Full-time":
        return 1
    return 0

df["education_form"] = df["education_form"].apply(fill_form, axis=1)


print(df.value_counts(df["education_status"])) # передивитись скільки, які є рівні освіти

def fill_status(status):
    # для кожного рівня освіти визначити цифру
    # Alumnus - означає випускник
    # Student - діючий студент (ще не випустився)
    # Undergraduate Applicant - вступник на рівень бакалавра
    # Рівні освіти: спеціаліст, бакалавр, магістр, кандидат наук, доктор наук
    if status == "Alumnus (Specialist)":
        return 0
    if status == "Student (Bachelor's)":
        return 1
    if status == "Alumnus (Master's)":
        return 2
    return 3

df["education_status"] = df["education_status"].apply(fill_status, axis=1)

