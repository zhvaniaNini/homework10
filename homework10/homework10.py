# -*- coding: utf-8 -*-
import numpy as np

names = np.random.choice(['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ', 'კლარა', 'სიმონ', 'ანზორ', 'სოფია', 'სოსო', 'ნელი', 'ბონდო', 'ედუარდ', 'სონია', 'არჩილ', 'მარიამ', 'სოფია', 'ემა', 'იზოლდა', 'ომარ', 'ტატიანა', 'ვიქტორ', 'კარინე', 'გუგული', 'კახა', 'როზა', 'რუსუდან', 'სიმონ', 'ნელი', 'ბადრი', 'მადონა', 'ირინე', 'მინდია', 'ნათია', 'გულნარა', 'კახა', 'ელზა', 'როინ', 'ნაირა', 'ლიანა', 'ნინელი', 'მაყვალა', 'რეზო', 'ჟუჟუნა', 'ზინა', 'გოჩა', 'მურმან'], 100)
surnames = np.random.choice(['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია', 'კევლიშვილი', 'ბუჩუკური', 'ტყებუჩავა', 'მიქაბერიძე', 'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა', 'ნაკაშიძე', 'ღურწკაია', 'გვაზავა', 'გვასალია', 'ზარანდია', 'სხირტლაძე', 'ბერაძე', 'ხვიჩია', 'ბასილაშვილი', 'კაკაბაძე', 'მერებაშვილი', 'ნოზაძე', 'ხარაბაძე', 'მუსაევა', 'მამულაშვილი', 'ელიზბარაშვილი', 'მამულაშვილი', 'ჯოჯუა', 'გულუა', 'ხალვაში', 'ხარატიშვილი', 'დუმბაძე', 'ბერიანიძე', 'ჯოხაძე', 'სამხარაძე', 'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე', 'ინასარიძე', 'ბერაძე', 'შენგელია', 'ქობალია', 'მიქავა', 'რევაზიშვილი'], 100)
students = np.array([f"{name} {surname}" for name, surname in zip(names, surnames)])
subjects = np.array(['მათემატიკა', 'ქართული', 'ინლისური', 'ისტორია', 'გეოგრაფია'])
scores = np.random.randint(0, 101, size=(len(students), len(subjects)))

average_scores = np.mean(scores, axis=1)
highest_score_index = np.argmax(average_scores)
student_with_highest_score = students[highest_score_index]
highest_average_score = average_scores[highest_score_index]
print(f"ყველაზე მაღალი საშუალო ქულის მქონე სტუდენტია: {student_with_highest_score}, საშუალო ქულით: {highest_average_score:.2f}")
print()

math_scores = scores[:, 0]
lowest_math_score = np.min(math_scores)
lowest_math_score_index = np.argmin(math_scores)
student_with_lowest_math_score = students[lowest_math_score_index]
print(f"ყველაზე დაბალი ქულა მათემატიკაში აქვს: {student_with_lowest_math_score}, ქულით: {lowest_math_score} ")
print()

english_scores = scores[:, 2]
average_english_score = np.mean(english_scores)
students_above_average_english = np.where(english_scores > average_english_score)[0]
students_names_above_average_english = students[students_above_average_english]
students_scores_above_average_english = english_scores[students_above_average_english]
print("სტუდენტები, რომლებსაც ინგლისურში საშუალოზე მაღალი ქულა აქვთ:")
print(f"საშუალო ქულა ინგლისურში: {average_english_score}")
for name, score in zip(students_names_above_average_english, students_scores_above_average_english):
    print(f"{name}: {score}")






