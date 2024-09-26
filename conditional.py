#conditional statement will check the condition
# to check the condition we use if else

# # wap to check user eligible for voting
# userage=int(input("enter your age-"))
# # note the default input func return type is string
# # for vote user is must be greater then 18.
# if userage>18:
#   print("you are eligible for voting ")
# else:
#   print("you are not elible for voting")






# usergender=input("enter your gender -")
# if usergender=="male":
#   print("you are not eligible for sitting inthe first compartment ")
# elif usergender=="female":
#    print("you are  eligible for sitting in first compartment ")
# else:
#   print("you are eligible for setting in any campartment ")





# wap if gender is female and greater then 18-govt job apply
# else male is greter then 18 then u will apply for the private job
userage=int(input("enter your age-"))
usergender=input("enter your gender-")
if userage >18:
 if usergender=="female":
  print("you can apply for the govt.job ")
 elif usergender=="male":
   print("you  can apply for private job ")
 else:
   print("there is no openinng")
else :
   print("you are not elible for the job")


