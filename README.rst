Title1
======

Checks xx raise an alert if some is found.

`VERSION  <burp_reports/VERSION>`__

Install
=======

Linux::

    sudo pip3 install curlnagios --upgrade

Also is possible to use::

    sudo python3 -m pip install curlnagios --upgrade

On windows with python3.5::

    pip install curlnagios --upgrade

For proxies add::

    --proxy='http://user:passw@server:port'

Usage
=====

Use the command line::

    curlnagios --help

Example usage
=============

Example use::

    > examplecommand -u domain\user -p pass -s http://spurl:9876

Example using proxy, and authentication with ntlm for the website:

    > curlnagios --url='http://xx/dd' --extra_args='--proxy http://user:pass@host:8080 --user user:pass --ntlm'

TODO
====

* Use hash passwords
* Add Unit tests?
