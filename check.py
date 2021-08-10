#!(이곳에 파이썬이 설치된 경로를 입력해야합니다.)
#-*- coding: utf-8 -*-
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi
import cgitb
import hcskr
cgitb.enable()
data = ''

print("content-type: text/html; charset=utf-8\n\r")
form = cgi.FieldStorage();
name = form.getvalue('name');
birth = form.getvalue('birth');
region = form.getvalue('region');
school = form.getvalue('school');
password = form.getvalue('password');
level = form.getvalue('level');
data = hcskr.selfcheck(name, birth, region, school, level, password)
print(data)
