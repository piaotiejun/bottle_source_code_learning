#!/usr/bin/python
#coding=utf8


from bottle import DictProperty, local_property


print('==========')
class test():
    def __init__(self, environ=None):
        self.environ = {} if environ is None else environ

    @DictProperty('environ', 'bottle.app', read_only=True)
    def app(self):
        print('in app')

    @DictProperty('environ', 'bottle.app', read_only=True)
    def run(self):
        print('in run')
        return [1, 2, 3, 4]

    def tqq(self):
        print(self.run)

        
t = test()
t.tqq()
print('==================')


class  a(object):
    def __init__(self, env):
        self.env = env
    env = local_property()

requests = 'requests'

q = a('object env')
print('env==================')
print(q.env)
q.env = 80
print(q.env)
print('env==================')

"""
dic = {
    'SERVER_SOFTWARE': 'WSGIServer/0.1 Python/2.7.6',
    'SCRIPT_NAME': '',
    'REQUEST_METHOD': 'POST',
    'HTTP_ORIGIN': 'chrome-extension://fhbjgbiflinjbdggehcddcbncdddomop',
    'SERVER_PROTOCOL': 'HTTP/1.1',
    'BOTTLE_LOCKFILE': '/tmp/bottle.ARJuJU.lock',
    'CONTENT_LENGTH': '140',
    'SHELL': '/bin/zsh',
    'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/share/gnome:/usr/local/share/:/usr/share/',
    'MANDATORY_PATH': '/usr/share/gconf/ubuntu.mandatory.path',
    'COMPIZ_CONFIG_PROFILE': 'ubuntu',
    'JOB': 'dbus',
    'TEXTDOMAIN': 'im-config',
    'XMODIFIERS': '@im=ibus',
    'SELINUX_INIT': 'YES',
    'XDG_RUNTIME_DIR': '/run/user/1000',
    'COMPIZ_BIN_PATH': '/usr/bin/',
    'route.url_args': {},
    'HTTP_CACHE_CONTROL': 'no-cache',
    'XDG_SESSION_ID': 'c2',
    'DBUS_SESSION_BUS_ADDRESS': 'unix:abstract=/tmp/dbus-zrvSfToxB8',
    'GNOME_KEYRING_PID': '1767',
    'HTTP_ACCEPT': '*/*',
    'DESKTOP_SESSION': 'ubuntu',
    'wsgi.version': (1, 0),
    'GTK_MODULES': 'overlay-scrollbar:unity-gtk-module',
    'wsgi.multiprocess': False,
    'INSTANCE': '',
    'XDG_MENU_PREFIX': 'gnome-',
    'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arj=01;31:*.taz=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lz=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.axa=00;36:*.oga=00;36:*.spx=00;36:*.xspf=00;36:',
    'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated',
    'XDG_CURRENT_DESKTOP': 'Unity',
    'PATH_INFO': '/hello',
    'bottle.app': < bottle.Bottle object at 0x7fa27eccdd90 > ,
    'QUERY_STRING': 'name=piaotiejun',
    'PS1': '%m%# ',
    'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.73 Chrome/47.0.2526.73 Safari/537.36',
    'HTTP_CONNECTION': 'keep-alive',
    'XAUTHORITY': '/home/piaotiejun/.Xauthority',
    'LANGUAGE': 'zh_CN:zh',
    'SESSION_MANAGER': 'local/piaotiejun-OptiPlex-3020:@/tmp/.ICE-unix/1922,unix/piaotiejun-OptiPlex-3020:/tmp/.ICE-unix/1922',
    'SHLVL': '1',
    'QT_QPA_PLATFORMTHEME': 'appmenu-qt5',
    'wsgi.url_scheme': 'http',
    'CLUTTER_IM_MODULE': 'xim',
    'WINDOWID': '56623115',
    'GPG_AGENT_INFO': '/run/user/1000/keyring-gGoJ2j/gpg:0:1',
    'GDMSESSION': 'ubuntu',
    'wsgi.multithread': True,
    'XDG_SEAT_PATH': '/org/freedesktop/DisplayManager/Seat0',
    '_': '/usr/bin/python',
    'GTK_IM_MODULE': 'ibus',
    'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/usr/share/upstart/xdg:/etc/xdg',
    'bottle.route': < POST '/hello' <
    function hello at 0x7fa27d489aa0 >> ,
    'COLORTERM': 'gnome-terminal',
    'wsgi.file_wrapper': < class wsgiref.util.FileWrapper at 0x7fa27d08a460 > ,
    'REMOTE_HOST': '',
    'HTTP_ACCEPT_ENCODING': 'gzip, deflate',
    'XDG_GREETER_DATA_DIR': '/var/lib/lightdm-data/piaotiejun',
    'QT4_IM_MODULE': 'xim',
    'AUTOJUMP_DATA_DIR': '/home/piaotiejun/.local/share/autojump',
    'HOME': '/home/piaotiejun',
    'DISPLAY': ':0',
    'LANG': 'zh_CN.UTF-8',
    'SESSION': 'ubuntu',
    'SERVER_PORT': '10000',
    'bottle.raw_path': '/hello',
    'VTE_VERSION': '3409',
    'HTTP_HOST': '127.0.0.1:10000',
    'bottle.request.post': < bottle.FormsDict object at 0x7fa27d424610 > ,
    'route.handle': < POST '/hello' <function hello at 0x7fa27d489aa0 >> ,
    'DEFAULTS_PATH': '/usr/share/gconf/ubuntu.default.path',
    'wsgi.run_once': False,
    'wsgi.errors': < open file '<stderr>',mode 'w' at 0x7fa27edfb1e0 > ,
    'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.8',
    'bottle.request.forms': < bottle.FormsDict object at 0x7fa27d4245d0 > ,
    'bottle.request.body': < StringIO.StringIO instance at 0x7fa27d444ab8 > ,
    'USER': 'piaotiejun',
    'BOTTLE_CHILD': 'true',
    '_cgi.FieldStorage': FieldStorage(None, None, [FieldStorage('name', None, 'qqqqq')]),
    'XDG_VTNR': '7',
    'QT_IM_MODULE': 'ibus',
    'LOGNAME': 'piaotiejun',
    'XDG_SEAT': 'seat0',
    'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
    'GNOME_KEYRING_CONTROL': '/run/user/1000/keyring-gGoJ2j',
    'TERM': 'xterm',
    'XDG_SESSION_PATH': '/org/freedesktop/DisplayManager/Session0',
    'SERVER_NAME': 'piaotiejun-OptiPlex-3020',
    'bottle.request': < LocalRequest: POST http: //127.0.0.1:10000/hello?name=piaotiejun>, 
    'SESSIONTYPE': 'gnome-session',
    'IM_CONFIG_PHASE': '1',
    'HTTP_POSTMAN_TOKEN': 'a9e33e58-088d-4bbd-3b90-0cb64a975a61',
    'SSH_AUTH_SOCK': '/run/user/1000/keyring-gGoJ2j/ssh',
    'wsgi.input': < StringIO.StringIO instance at 0x7fa27d444ab8 > ,
    'TEXTDOMAINDIR': '/usr/share/locale/',
    'UPSTART_SESSION': 'unix:abstract=/com/ubuntu/upstart-session/1000/1769',
    'GATEWAY_INTERFACE': 'CGI/1.1',
    'OLDPWD': '/home/piaotiejun/workspace/python_workspace/web',
    'REMOTE_ADDR': '127.0.0.1',
    'GDM_LANG': 'zh_CN',
    'PWD': '/home/piaotiejun/workspace/python_workspace/web/test',
    'CONTENT_TYPE': 'multipart/form-data; boundary=----WebKitFormBoundaryfh4NAS6wAFkwSzTa'
}
"""
