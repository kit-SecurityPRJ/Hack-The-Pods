#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Million Clicker</title>
</head>
<body>
    <h2>Million Clicker</h2>
    100万回クリックしてFlagを入手しよう！！！<br><br>
    現在: %d回<br>
    %s
    <form action="/cgi-bin/clicker.py" method="GET">
        <input type="hidden" name="cnt" value="%d" /> 
        <input type="submit" value="click!" />
    </form>
</body>
</html>
"""

form = cgi.FieldStorage()
cnt = int(form.getvalue("cnt", ""))
flag = "<br>"

if 1000000 <= cnt : flag = "htp-ctf{get_requesting_did_million_clicks}<br><br>"

print('Content-type: text/html; charset=UTF-8\r\n')
print(html % (cnt, flag, cnt+1))

