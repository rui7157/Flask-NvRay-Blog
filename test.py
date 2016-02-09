#coding:u8
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    values=[]
    def handle_starttag(self, tag, attrs):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
        'h1', 'h2', 'h3', 'p']
        if tag in allowed_tags:
            self.values.append("<%s>%s</%s>" %(tag,attrs,tag))
        else:
            self.values.append("<p>%s</p>" %attrs)


    #
    # def handle_endtag(self, tag):
    #     print('</%s>' % tag)
    #
    # def handle_startendtag(self, tag, attrs):
    #     print('<%s/>' % tag)

    # def handle_data(self, data):
    #     print('%s' %data)
    #
    # def handle_comment(self, data):
    #     print('<!-- -->')
    #
    # def handle_entityref(self, name):
    #     print('&%s;' % name)
    #
    # def handle_charref(self, name):
    #     print('&#%s;' % name)

parser = MyHTMLParser()
ht=u"""<p>对一个使用 Flask-Login 的应用最重要的一部分就是 <a class="reference internal" href="http://www.pythondoc.com/flask-login/index.html#flask.ext.login.LoginManager" title="flask.ext.login.LoginManager"><code>LoginManager</code></a> 类。你应该在你的代码的某处为应用创建一个，像这样:</p>
<div class="highlight-python">
<div class="highlight">
<pre>
login_manager = LoginManager()
</pre>
</div>
</div>

<p>登录管理(login manager)包含了让你的应用和 Flask-Login 协同工作的代码，比如怎样从一个 ID 加载用户，当用户需要登录的时候跳转到哪里等等。</p>

<p>一旦实际的应用对象创建后，你能够这样配置它来实现登录:</p>

<div class="highlight-python">
<div class="highlight">
<pre>
login_manager.init_app(app)
</pre>
</div>
</div>
</div>

<div class="section" id="id2">
<h2>它是如何工作</h2>

<p>你必须提供一个 <a class="reference internal" href="http://www.pythondoc.com/flask-login/index.html#flask.ext.login.LoginManager.user_loader" title="flask.ext.login.LoginManager.user_loader"><code>user_loader</code></a> 回调。这个回调用于从会话中存储的用户 ID 重新加载用户对象。它应该接受一个用户的 <a class="reference external" href="http://docs.python.org/library/functions.html#unicode" title="(in Python v2.7)"><code>unicode</code></a> ID 作为参数，并且返回相应的用户对象。比如:</p>

<div class="highlight-python">
<div class="highlight">
<pre>
@login_manager.user_loader
def load_user(userid):
    return User.get(userid)
</pre>
</div>
</div>

<p>如果 ID 无效的话，它应该返回 <a class="reference external" href="http://docs.python.org/library/constants.html#None" title="(in Python v2.7)"><code>None</code></a> (<strong>而不是抛出异常</strong>)。(在这种情况下，ID 会被手动从会话中移除且处理会继续)</p>
</div>

<h2>你的用户类</h2>

<p>你用来表示用户的类需要实现这些属性和方法:</p>

<p><code>is_authenticated</code></p>

<p>当用户通过验证时，也即提供有效证明时返回 <a class="reference external" href="http://docs.python.org/library/constants.html#True" title="(in Python v2.7)"><code>True</code></a> 。（只有通过验证的用户会满足 <a class="reference internal" href="http://www.pythondoc.com/flask-login/index.html#flask.ext.login.login_required" title="flask.ext.login.login_required"><code>login_required</code></a> 的条件。）</p>
</p>
    </div>
<div class="hr"><hr/></div>

   <!-- 多说评论框 start -->
	<div class="ds-thread" data-thread-key="4" data-title="对一个使用 Flask-Login 的应用最重要的一部分就是 LoginManager 类。你应该在你的代码的某处为应用创建一个，像这样:" data-url="/blog/4"></div>
<!-- 多说评论框 end -->
<!-- 多说公共JS代码 start (一个网页只需插入一次) -->
<script type="text/javascript">
var duoshuoQuery = {short_name:"nvray"};
	(function() {
		var ds = document.createElement('script');
		ds.type = 'text/javascript';ds.async = true;
		ds.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') + '//static.duoshuo.com/embed.js';
		ds.charset = 'UTF-8';
		(document.getElementsByTagName('head')[0]
		 || document.getElementsByTagName('body')[0]).appendChild(ds);
	})();
	</script>
<!-- 多说公共JS代码 end -->
</div>


</div>
<div class="foot">
<div class="foot-box">
    <p>© 2016 Flask | Powered by NvRay | <a href="https://github.com/rui7157" target="_blank"><i class="icon-github-alt"></i> Github</a></p>
</div>
</div>

</body>
</html><!--"""
parser.feed(ht)
print parser.values