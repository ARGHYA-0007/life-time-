print('''hello student,today i will help you to make your
       full intro like a conversasion so that you can remember it.and when you are asked to tell you intro you can 
      spit you intro like a pro and escape from those fucking so called senior ''')
name=input("enter your full name:")
place=input("enter your living place, not the district:")
district=input("enter your district:")
school_name=input("enter your school name:")
affiliation_secondary=input("enter your seconday school affiliate to:")
affiliation_higher_secondary=input("enter your higher seconday school affiliate to:")
x10th_obtain_marks=int(input("enter your 10th marks"))
x10th_full_marks=int(input("enter your 10th full marks"))
x12th_obtain_marks=int(input("enter your 12th obtain marks"))
x12th_full_marks=int(input("enter your 12th full marks"))
x10th_percentage=(x10th_obtain_marks/x10th_full_marks)*100
x12th_percentage=(x12th_obtain_marks/x12th_full_marks)*100
x10th_pass_year=int(input("enter your year in which you have passed 10th"))
x12th_pass_year=int(input("enter your year in which you have passed 12th"))
competitive_examination_name=input("enter in which competitive exam you have got chance to get this college")
competitive_examination_year=int(input(f"enter in which year you give {competitive_examination_name} exam"))
obtain_marks_competitive=int(input(f"enter your rank in {competitive_examination_name}"))
college_name=input("enter your college name")
branch_name=input("enter your branch name")
hobby=input("enter what are your hobbies")
print(f'''My name is {name}. I am from {place},
       district {district}. I passed the secondary examination 
      from {school_name} affiliated to the {affiliation_secondary} with {x10th_percentage} percent that
       is {x10th_obtain_marks} out of {x10th_full_marks} marks in the year {x10th_pass_year}. I passed the
       higher secondary examination from {school_name} affiliated
       to the {affiliation_higher_secondary} with
       {x12th_percentage} percent that is {x12th_obtain_marks} out of {x12th_full_marks} marks in the year {x12th_pass_year}.
       I appeared for the {competitive_examination_name} in
       the year {competitive_examination_year} and obtained {obtain_marks_competitive} rank. Then I appeared for online
       counselling of the {competitive_examination_name} where
       I got an opportunity to study in the {branch_name} 
      department in {college_name}.
       My hobbies are {hobby}''')