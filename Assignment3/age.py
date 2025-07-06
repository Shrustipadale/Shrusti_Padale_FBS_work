#Write a program to check if person is eligible to marry or not (male age >=21 andfemale age>=18)

male_age=int(input("Enter male age: "))
female_age=int(input("Enter female age: "))

if(male_age >=21 and female_age >=18):
    print("The person is eligible to marry")

else:
    print("The person is not eligible to marry")
