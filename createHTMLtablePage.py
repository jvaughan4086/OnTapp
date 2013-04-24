#! /bin/env python
import sys,string,os,tempfile
import sqlite3
import csv, subprocess

filename = sys.argv[1]
beforeTag=filename[:-4]


dataTag="%s.db" % (beforeTag)
htmlTag="%s.html" % (beforeTag)

htmlTable = open(htmlTag, "w")

htmlTable.write("<!DOCTYPE html>\n")
htmlTable.write("<html lang='en'>\n")
htmlTable.write("<head>\n")
htmlTable.write("  <title>Whats onTap</title>\n")
htmlTable.write("<style type='text/css'>\n")
htmlTable.write(".datagrid table { border-collapse: collapse; text-align: left; width: 100%; } \n")
htmlTable.write(".datagrid {font: normal 12px/150% Arial, Helvetica, sans-serif; background: #fff; overflow: hidden; border: 1px solid #A65B1A; -webkit-border-radius: 3px; -moz-border-radius: 3px; border-radius: 3px; }\n")
htmlTable.write(".datagrid table td, .datagrid table th { padding: 3px 10px; }\n")
htmlTable.write(".datagrid table thead th {background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #AD7F00), color-stop(1, #7F4614) );background:-moz-linear-gradient( center top, #AD7F00 5%, #7F4614 100% );filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#AD7F00', endColorstr='#7F4614');background-color:#AD7F00; color:#FFFFFF; font-size: 17px; font-weight: bold; border-left: 2px solid #6B3B11; } \n")
htmlTable.write(".datagrid table thead th:first-child { border: none; }\n")
htmlTable.write(".datagrid table tbody td { color: #7F4614; border-left: 2px solid #6B3B11;font-size: 15px;border-bottom: 2px solid #6B3B11;font-weight: normal; }\n")
htmlTable.write(".datagrid table tbody .alt td { background: #F0E5CC; color: #7F4614; }\n")
htmlTable.write(".datagrid table tbody td:first-child { border-left: none; }\n")
htmlTable.write(".datagrid table tbody tr:last-child td { border-bottom: none; }\n")
htmlTable.write("h2 {\n")
htmlTable.write("  font:normal 1.2em/1.3em arial;\n")
htmlTable.write("	color:#B84300;\n")
htmlTable.write("	margin:0;\n")


htmlTable.write("	padding:0;\n")
htmlTable.write("}\n")
htmlTable.write("p {\n")
htmlTable.write("	font:normal 1em/1.2em arial;\n")
htmlTable.write("	color:#333;\n")
htmlTable.write("	margin:0 0 .2em 0;\n")
htmlTable.write("	padding:0;\n")
htmlTable.write("}\n")
htmlTable.write("ul {\n")
htmlTable.write("	list-style:none;\n")
htmlTable.write("	margin:0;\n")
htmlTable.write("	padding:0;\n")
htmlTable.write("}\n")

htmlTable.write("</style>\n")


htmlTable.write("<script type='text/javascript'>\n")

htmlTable.write("</script>\n")
htmlTable.write("</head>\n")
htmlTable.write("<body background='beer-foam.jpg'>\n")

htmlTable.write("<center>\n")
htmlTable.write("<h1>\n")
htmlTable.write("<font COLOR='#F7F8E0' size='15'>Whats On Tap</font>\n")
htmlTable.write("</p>\n")
htmlTable.write("</h1>\n")
htmlTable.write("</center>\n")

htmlTable.write("<center>\n")
htmlTable.write("<h2>\n")
htmlTable.write("<div class='datagrid'><table>\n")

con = sqlite3.connect(dataTag)
with con:
  cur = con.cursor()
  header1="Beer Name"
  header2="CATEGORY"
  header3="DESCRIPTION"
  header4="ABV"
  header5="BREWED"
  header6="Price-Small"
  header7="Price-Large"
  header8="Price-Growler"
  
  headerPrint= "<thead><tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr></thead>\n" % (header1, header2, header3, header4, header5, header6, header7, header8) 
  htmlTable.write(headerPrint)
  htmlTable.write("	<tbody>\n")
  cur.execute("SELECT * FROM OnTapp")
  
  rows = cur.fetchall()
  for row in rows:
    curExec="<tr class='alt'><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    htmlTable.write(curExec)

  htmlTable.write("	<tbody>\n")
  


htmlTable.write("</tbody>\n")
htmlTable.write("</table></div>\n")
htmlTable.write("</p>\n")
htmlTable.write("</h2>\n")
htmlTable.write("</center>\n")
htmlTable.write("</ul>\n")
htmlTable.write("</body>\n")
htmlTable.write("</html>\n")
