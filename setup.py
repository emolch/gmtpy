from distutils.core import setup

setup( 
    name    = 'gmtpy',
    version = '0.1',
    description = 'Thin GMT interface plus autoscaling plus layout management.',
    py_modules = ['gmtpy'],
    scripts = [ 'gmtpy-epstopdf' ],
    author = 'Sebastian Heimann',
    author_email = 'sebastian.heimann@zmaw.de',
    url = 'http://emolch.github.com/gmtpy/',

)
