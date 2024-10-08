# დაწერე ფუნქცია, რომელიც იღებს x და y პარამეტრებს და აბრუნებს მათ სხვაობას. მაგალითად, გამოიყენე არგუმენტები 10 და 5. (გამოიტანა: 5)

def difference(x, y):
    return x - y

result = difference(10, 5)
print(result) 


# შექმენი ფუნქცია, რომელიც იღებს word1 და word2 პარამეტრებს და აბრუნებს მათ ერთად შერწყმულს. მაგალითად, გამოიყენე არგუმენტები "გამარჯობა" და "მეგობარო". (გამოიტანა: "გამარჯობა მეგობარო")

def concatenate(word1, word2):
    return word1 + " " + word2

result = concatenate("გამარჯობა", "მეგობარო")
print(result)

# დაწერე ფუნქცია, რომელიც იღებს length და width პარამეტრებს და ითვლის მართკუთხედის ფართობს. მაგალითად, გამოიყენე არგუმენტები 4 და 6. (გამოიტანა: 24)

def rectangle_area(length, width):
    return length * width

result = rectangle_area(4, 6)
print(result)


# შექმენი ფუნქცია, რომელიც იღებს name პარამეტრს და აბრუნებს "გამარჯობა, [name]" შეტყობინებას. მაგალითად, გამოიყენე არგუმენტი "ანა". (გამოიტანა: "გამარჯობა, ანა")
def greet(name):
    return f"გამარჯობა, {name}"

result = greet("ანა")
print(result)
