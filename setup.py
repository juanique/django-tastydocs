from setuptools import setup, find_packages

setup(
    name="tastydocs",
    version="0.1",
    packages = find_packages(),
    package_data={
        'tastydocs' : [
            'templates/tastydocs/*.html',
            'static/css/tastydocs/*.css',
            'static/css/tastydocs/lib/*.css',
            'static/css/tastydocs/SyntaxHighlighter/*.css',
            'static/img/bootstrap/*.png',
            'static/js/tastydocs/*.coffee',
            'static/js/tastydocs/lib/*.js',
            'static/js/tastydocs/lib/SyntaxHighlighter/*.js'
        ]
    },
    long_description="Automagic web documentation for tastypie REST APIs."
)

