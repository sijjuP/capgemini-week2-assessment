
class Logger:
    def log(self,message,warning=None,error=None):
        if(warning==None and error==None):
            return f"info: {message}"
        elif(error==None):
            return f"Warning has occured: {warning}"
        else:
            return f"error occured: {error}"
        
log_obj=Logger()
print(log_obj.log("hello","warn","err"))
print(log_obj.log("hello","warn"))
print(log_obj.log("hello"))