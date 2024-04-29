#  მომხმარებელს შეეკითხეთ სწავლობს თუარა გოაში, თუ სწავლობს შეეკითხეთ
#  რომელ ჯგუფშია, თუ პასუხი იქნება ჯგუფი13 შეეკითეთ რომ არის თუ არა გაბრ
# იელი მისი მენტორი, თუ პასუხი იქნება კი უთხარით რომ თქვენც აქ სწავლობთ
# და ნამდვილად გაბრიელია ორივეს მენტორი, თუ პასუხი არიქნება გაბრიელი ყველა
# სხვა შემთხვევაში დაუბეჭდეთ რომ ის ტყუის და არარის სინამდვილეში ჯგუფ13-ში 

study = input("do you study in GOA?: ")
if study == "yes":
    group = input("in wich group do you study?: ")
    if group == "13":
        mentor = input("is Gabriel your mentor?: ")
        print("you really study in GOA congratulations!!!")
        
    else:
        print("you do not study in GOA")