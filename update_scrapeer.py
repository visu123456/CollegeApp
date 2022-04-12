from turtle import up
import requests

from bs4 import BeautifulSoup




def give_data():
    updates_str = ""
    u = "https://www.gtu.ac.in/Circular.aspx"

    r = requests.get(u)
    pg_soup = BeautifulSoup(r.content,"html.parser")

    all_updates = pg_soup.find_all('ul',class_="timeline")

    for tb in all_updates:
        for updt in tb.find_all('div',class_="rows")[:12]:
            updates_str += str(updt)
    

    fl = open("Templates/gtu_data.html","w",encoding='utf-8')
    fl.write('''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notice</title>
    <style>
    .rows {
	float:left;
	width:100%;
    display:table;
	border:#e7e7e7 solid 1px;
	border-left:#e7e7e7 solid 5px;
	-webkit-box-sizing:border-box;
	-moz-box-sizing:border-box;
	box-sizing:border-box;
}

.desc-sec {
	width:100%;
	display:table-row;
}
 .desc-sec .date {
	width:65px;
	
	padding:10px 20px 10px 20px;
	display:table-cell;
	vertical-align:top;
border-right: 1.75px #CCC dotted;

}
 .desc-sec .date .date-in {
	background:#000;
	display:block;
	height:30px;
	width:100px;
	text-align:center;
	color:#FFF;
	border-radius:3px;
	font-family: 'Source Sans Pro', sans-serif;
}
a{
    text-decoration: none;
    color: #337ab7;
    background-color: transparent;
}
.desc-sec .date .date-in span {
	width:100%;
	display:block;
	text-align:center;
	font-size:12px;
}
.Content{
    font-size:12px;
}
.desc-sec .date .date-in span:first-child {
	font-size:12px;
	font-weight:bold;
	padding:5px 0px 10px 0px;
}
    </style>
</head>
<body>''')
    fl.write(updates_str)
    fl.write("\n")
    fl.write("</body>")
    fl.write('</html>')
    return updates_str



if __name__ == "_main_":
    give_data()