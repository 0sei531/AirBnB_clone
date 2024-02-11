#!/usr/bin/python3
"""
W3C validator for Holberton School

For HTML and CSS files.

Based on 2 APIs:

- https://validator.w3.org/nu/
- http://jigsaw.w3.org/css-validator/validator


Usage:

Simple file:

    ```
./w3c_validator.py index.html
```

Multiple files:


```
./w3c_validator.py index.html header.html styles/common.css
```

All errors are printed in `STDERR`

Return:
Exit status is the # of errors, 0 on Success

References

https://developer.mozilla.org/en-US/

"""
import sys
import requests
import argparse

def __print_stdout(msg):
    """Print message in STDOUT"""
    sys.stdout.write(msg)

def __print_stderr(msg):
    """Print message in STDERR"""
    sys.stderr.write(msg)

def __analyse_html(file_path):
    """Start analysis of HTML file"""
    h = {'Content-Type': "text/html; charset=utf-8"}
    d = open(file_path, "rb").read()
    u = "https://validator.w3.org/nu/?out=json"
    r = requests.post(u, headers=h, data=d)
    res = []
    messages = r.json().get('messages', [])
    for m in messages:
        res.append("[{}:{}] {}".format(file_path, m['lastLine'], m['message']))
    return res

def __analyse_css(file_path):
    """Start analysis of CSS file"""
    d = {'output': "json"}
    f = {'file': (file_path, open(file_path, 'rb'), 'text/css')}
    u = "http://jigsaw.w3.org/css-validator/validator"
    r = requests.post(u, data=d, files=f)
    res = []
    errors = r.json().get('cssvalidation', {}).get('errors', [])
    for e in errors:
        res.append("[{}:{}] {}".format(file_path, e['line'], e['message']))
    return res

def __analyse(file_path):
    """Start analysis of a file and print the result"""
    nb_errors = 0
    try:
        result = None
        if file_path.endswith('.css'):
            result = __analyse_css(file_path)
        else:
            result = __analyse_html(file_path)

        if len(result) > 0:
            for msg in result:
                __print_stderr("{}\n".format(msg))
                nb_errors += 1
        else:
            __print_stdout("{}: OK\n".format(file_path))

    except Exception as e:
        __print_stderr("[{}] {}\n".format(e.__class__.__name__, e))
        nb_errors += 1

    return nb_errors

def __files_loop(files):
    """Loop that analyses for each file from input arguments"""
    nb_errors = 0
    for file_path in files:
        nb_errors += __analyse(file_path)
    return nb_errors

def parse_arguments():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description="W3C validator for Holberton School")
    parser.add_argument("files", nargs="+", help="HTML and CSS files to validate")
    return parser.parse_args()

if __name__ == "__main__":
    """Main"""
    args = parse_arguments()
    sys.exit(__files_loop(args.files))

