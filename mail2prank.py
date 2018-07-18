import smtplib as a
while(True):
    l=['samuraijack9006@gmail.com','Sanathrao4@gmail.com','rvgofmys@gmail.com','hcthejeshgowda1297@gmail.com','naveennvn1998@gmail.com','mail2tejashr@gmail.com','madan10km@gmail.com','syedjawad469@gmail.com','bhuvanesh2804@gmail.com','anushreek659@gmail.com','keraofmys@gmail.com']
    for i in l:
        
        s=a.SMTP('smtp.gmail.com',587)

        u="spamersden555@gmail.com"
        s.starttls()
        s.login(u,"spamersden@555")
        msg="u've been spamed,can not wish u good morning"
   
        s.sendmail(u,i,msg)
        s.quit()
        if i==l[-1]:
            i=l[0]
