##How to hide a password in a Python script with keyring
##
##keyring is an easy-to-use package that works by allowing you to store a password in your operating system’s credential store. It’s great in that it can work across multiple different operating systems. To get started, just use pip to install:
##
##	
##pip install keyring  ##Tried not required already installed.
##
##Next, let’s import keyring.
##
##	
##import keyring
##
##Once we’ve imported keyring, we can store a username / password combination using the set_password method. This method has three parameters. First, it takes a “servicename”. This is the name we choose for whatever service our username / password is associated with e.g. email, database, etc. In our example, we’ll just call it “test”. Next, the second and third parameters are the username and password, respectively.
##
##	
##keyring.set_password("test", "secret_username", "secret_password_U3ATest")
##
##To retrieve the password, we just need to use the get_password method with the “servicename” value and username.
##
##	
##print("password stored was "+ keyring.get_password("test", "secret_username"))
##The above worked but I needed to enter the keyring password
