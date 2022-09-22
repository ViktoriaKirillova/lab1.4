mail = input("Введите свою электронную почту:\n")

n = mail.find("@") + 1

print(mail[n:])