SERVER = "smtp.office365.com"
FROM = "Senders Email here"
PASSWORD = "Senders password here"
TO = ["Receivers email here"] # must be a list

SUBJECT = "Hello!"
threshold_value     = 87
max_cpu_usage       = 89
min_cpu_usage       = 16
predicted_cpu_value = 98
date1 = 1
date2 = 2
date3 = 3
date4 = 4
body = """\
<html>
  <head>
    <meta charset="utf-8">
    <title>EXERCISE TITLE</title>
  </head>
  <body>
    <p>Hi Team,</p>
    <p>Please find below the prediction analysis on the CIMICGROUP-APP1 server</p>
    <p>Based on history and predicted data, we come to below conclusion : </p>

    <table border="1">
      <thead>
        <th>Description</th>
        <th>Value</th>
        <th>Timestamp</th>
      </thead>
      <!--  tr is a Table Row -->
      <tr>
        <!-- These are table cells -->
        <td>Threshold value</td>
        <td>%(threshold_value)f</td>
        <td>%(date1)s</td>
      </tr>
      <tr>
        <td>Max CPU usage in last 30 days</td>
        <td>%(Max_CPU)f</td>
        <td>%(date2)s</td>
      </tr>
      <tr>
        <td>Min CPU usage in last 30 days</td>
        <td>%(Min_CPU)f</td>
        <td>%(date3)s</td>
      </tr>
      <tr>
        <td>Expected highest CPU</td>
        <td>%(Pred_CPU)f</td>
        <td>%(date4)s</td>
      </tr>

    </table>

    <br>

      <a href="https://grafana.linuxlabz.net/d/-cja90iZz/cimic-account?orgId=1&fullscreen&panelId=2&from=1554586836085&to=1557437420408">
        Please click here to go see full graph</a>

     <p>Please check and take the necessary precautionary steps</p>
     <p>Regards, <br>
        CIS-ML Team</p>
  </body>
</html>

""" %  {"threshold_value": threshold_value, "Max_CPU": max_cpu_usage, "Min_CPU" : min_cpu_usage, "Pred_CPU" : predicted_cpu_value , "date1" : date1, "date2" : date2, "date3" : date3, "date4" : date4}


# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

msgText = MIMEText(body,'html')
msg.attach(msgText)
import smtplib
try:
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    server.login(FROM, PASSWORD)
    text = msg.as_string()
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddr, text)
    print("Successfully sent email")
    server.quit()
except smtplib.SMTPException as e:
    print("Error: unable to send email")
    print "Error code : ",e
print("Email Alert Sent To : ", TO)
