import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(title, text, to_email):
    # 세션생성, 로그인
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('barahana123', 'ywtmexgpvvjziqld')

    # 제목, 본문 작성
    msg = MIMEMultipart()
    msg['Subject'] = title
    msg.attach(MIMEText(text, 'plain'))

    # 파일첨부 (파일 미첨부시 생략가능)
    # attachment = open('파일명', 'rb')
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= " + filename)
    # msg.attach(part)

    # 메일 전송
    s.sendmail("barahana123@gmail.com", to_email, msg.as_string())
    s.quit()