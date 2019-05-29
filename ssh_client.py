from pexpect import pxssh
def reboot(ip, usuario, password):
    s = pxssh.pxssh()
    if not s.login (ip, usuario, password):
        print ("SSH session failed on login.")
        print (str(s))
    else:
        print ("SSH session login successful")
        s.sendline ('uptime')
        s.prompt()         # match the prompt
        print (s.before)     # print everything before the prompt.
        #We can also execute multiple command like this:
        print(s.sendline ('pwd'))
        s.logout()
        
        