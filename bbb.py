name="john"
age=20
sex="male"
location="home"
sample="rhem"
dom="plan"
print(f"hello",{name},{age},{sex})
print(f"soma",{location},{sample},{dom})
def collect_form_data():
    # Collecting form data from user
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    message = input("Enter your message: ")

    # Display the collected data
    print("\nForm Submitted!")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")

# Run the function to simulate a form submission in terminal
collect_form_data()