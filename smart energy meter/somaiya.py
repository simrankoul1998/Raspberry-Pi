import MySQLdb
import smtplib
from smtplib import SMTP
import io
from email.mime.image import MIMEImage
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="rootco",  # your password
                     db="bill")        # name of the data base
# you must create a Cursor object. It will let
#  you execute all the queries you need
sender = 'ayushsuri97@gmail.com'
cur = db.cursor()
numbers=[1,2,3]
for i in numbers:
    rs=cur.execute("SELECT NAME FROM cutomer where ID=' %d ' " % i)
    row=cur.fetchone()
    rt=cur.execute("SELECT MONTH FROM cutomer where ID=' %d ' " % i)
    row1=cur.fetchone()
    ru=cur.execute("SELECT UINT FROM cutomer where ID=' %d ' " % i)
    row2=cur.fetchone()
    rv=cur.execute("SELECT COST FROM cutomer where ID=' %d ' " % i)
    row3=cur.fetchone()
    rw=cur.execute("SELECT EMAILID FROM cutomer where ID=' %d ' " % i)
    row4=cur.fetchone()
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "BILL"
    msg['From'] = sender
    msg['To'] = [row4]
    s="Dear Customer"+str(row)+"your Electricity consumption for"+str(row1)+"month is"+str(row2)+"units hence your bill is Rs/-"+str(row3)+"."
    s1="""\
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Electricity Bill Payment</title>
    
    <style>
    .invoice-box{
        max-width:800px;
        margin:auto;
        padding:30px;
        border:1px solid #eee;
        box-shadow:0 0 10px rgba(0, 0, 0, .15);
        font-size:16px;
        line-height:24px;
        font-family:'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
        color:#555;
    }
    
    .invoice-box table{
        width:100%;
        line-height:inherit;
        text-align:left;
    }
    
    .invoice-box table td{
        padding:5px;
        vertical-align:top;
    }
    
    .invoice-box table tr td:nth-child(2){
        text-align:right;
    }
    
    .invoice-box table tr.top table td{
        padding-bottom:20px;
    }
    
    .invoice-box table tr.top table td.title{
        font-size:45px;
        line-height:45px;
        color:#333;
    }
    
    .invoice-box table tr.information table td{
        padding-bottom:40px;
    }
    
    .invoice-box table tr.heading td{
        background:#eee;
        border-bottom:1px solid #ddd;
        font-weight:bold;
    }
    
    .invoice-box table tr.details td{
        padding-bottom:20px;
    }
    
    .invoice-box table tr.item td{
        border-bottom:1px solid #eee;
    }
    
    .invoice-box table tr.item.last td{
        border-bottom:none;
    }
    
    .invoice-box table tr.total td:nth-child(2){
        border-top:2px solid #eee;
        font-weight:bold;
    }
    
    @media only screen and (max-width: 600px) {
        .invoice-box table tr.top table td{
            width:100%;
            display:block;
            text-align:center;
        }
        
        .invoice-box table tr.information table td{
            width:100%;
            display:block;
            text-align:center;
        }
    }
    </style>
</head>

<body>
    <div class="invoice-box">
        <table cellpadding="0" cellspacing="0">
            <tr class="top">
                <td colspan="2">
                    <table>
                        <tr>
                            <td class="title">
                                <img src="file:///home/ubuntupr/Desktop/Electricity Bill Payment_files/1.jpg" style="width:100%; max-width:300px;">
                            </td>
                            
                            <td>
                                Invoice #: 2<br>
                                Created:"""+str(row1)+""" <br>
                                Due: January 28, 2019
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            
            <tr class="information">
                <td colspan="2">
                    <table>
                        <tr>
                            <td>
                               Cusomer ID: """+ str(i) +"""
                               <br>Customer Name:"""+str(row) +"""
                               <br>Email Address:"""+str(row4) + """
                            </td>
                            
                            <td>
                                Phone Number: 9820341293
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            
            <tr class="heading">
                <td>
                   Energy Calculator
                </td>
                
                <td>
                </td>
            </tr>
            
            <tr class="details">
                <td>
                    Meter Readings(in Units)
                </td>
                """+str(row2)+"""
                <td>
                
                </td>
            </tr>
            
            <tr class="heading">
                <td>
                    Electricity Consumption Bill
                </td>
                
                <td>
                    Cost
                </td>
            </tr>
            
            <tr class="item">
                <td>
                    Total Units Consumed
                </td>
                
                <td>"""+str(row2)+"""
                </td>
            </tr>
            
            <tr class="item">
                <td>
                    Cost per unit
                </td>
                
                <td>
                    Rs.15
                </td>
            </tr>
            
            <tr class="item last">
                <td>
                    Total
                </td>
                
                <td>
                    Rs.15000
                </td>
            </tr>
            
            <tr class="total">
                <td>Total incl.taxes</td>
                
                <td>
			Rs.15050
                </td>
            </tr>
        </table>
    </div>
</body>
</html>
"""
    part1=MIMEText(s,'html')
    part2 = MIMEText(s1, 'html')
    msg.attach(part1)
    msg.attach(part2)
    sender = 'ayusayushsuri97@gmail.com'
    receivers = [row4]
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('ayushsuri97@gmail.com', 'ransh1512')
    smtpObj.sendmail(sender, receivers, str(part1)+str(part2))
print "Successfully sent email"
db.close()
