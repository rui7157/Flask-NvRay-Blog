import sae
#新浪sinaapp，sae链接文件
from myapp import app
application = sae.create_wsgi_app(app)
