class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self,recipient,message):
        return f"Email sent to {recipient} with message: '{message}'"

class SMSNotification(Notification):
    def send(self,recipient,message):
        return f"SMS sent to {recipient} with message: '{message}'"


recipient_email=input("Enter email recipient:\t")
email_message=input("Enter email message:\t")
email=EmailNotification()
print(email.send(recipient_email,email_message))

recipient_sms=input("\nEnter SMS recipient:\t")
sms_message=input("Enter SMS message:\t")
sms=SMSNotification()
print(sms.send(recipient_sms,sms_message))