import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("ramchowdary787@gmail.com", "Ramchowdary7")
msg = "hi!"
server.sendmail("ramchowdary787@gmail.com", "vikramgowda107@gmail.com", msg)
print("sucess")
server.quit()

