# coding:utf-8
from __future__ import unicode_literals

import os
from email.header import make_header

from django.core.mail import send_mail, EmailMultiAlternatives

from drug import settings
from drug.settings import EMAIL_FROM


def email_send(email, code, send_type="register"):

    if send_type == "register":
        email_title = "邮箱注册验证码"
        email_body = "注册高通量药物筛选平台邮箱验证码为 %s" % code

        send_status = send_mail(subject=email_title, message=email_body,
                                from_email=EMAIL_FROM,
                                recipient_list=[email])
        return send_status
    elif send_type == "forget":
        email_title = "邮箱找回验证码"
        email_body = "重置高通量药物筛选平台邮箱验证码为 %s" % code

        send_status = send_mail(subject=email_title, message=email_body,
                                from_email=EMAIL_FROM, recipient_list=[email])
        return send_status


def email_status(email,file_path,name,work_name):
    email_title = '虚拟筛选服务器'
    email_body = '%s，'%name+'您的任务%s已经完成。'%work_name
    from_email = settings.DEFAULT_FROM_EMAIL
    msg = EmailMultiAlternatives(email_title, email_body, from_email, [email])
    try:
        text = open(file_path, 'rb').read()
        file_name = os.path.basename(file_path)
        b = make_header([(file_name, 'utf-8')]).encode('utf-8')
        msg.attach(b, text)
        msg.send()
    except IOError:
        email_body = '%s，' % name + '您的任务%s已经完成，无有效结果。' % work_name
        msg = EmailMultiAlternatives(email_title, email_body, from_email, [email])
        msg.send()
    # send_status = send_mail(subject=email_title, message=email_body, from_email=EMAIL_FROM, recipient_list=[email], fail_silently=False)
    # return send_status
