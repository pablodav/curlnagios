Title1
======

Checks an url raise an alert if some problem is found.
Uses curl with all its power, so you can extend your check with all curl options.

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

    > curlnagios --help
      usage: curlnagios [-h] [-u [URL]] [-e [EXTRA_ARGS]]

        optional arguments:
        -h, --help            show this help message and exit
        -u [URL], --url [URL]
                                url to check 
        -e [EXTRA_ARGS], --extra_args [EXTRA_ARGS]
                                extra args to add to curl, see `curl manpage <https://curl.haxx.se/docs/manpage.html>`_.


Example usage
=============

Example use with proxy::

    > curlnagios --url='http://xx/dd' --extra_args='--proxy http://user:pass@host:8080'

Example using proxy, and authentication with ntlm for the website:

    > curlnagios --url='http://xx/dd' --extra_args='--proxy http://user:pass@host:8080 --user user:pass --ntlm'

All the extra_args are options directly comming from curl manpage, you can use almost any 
with exception of -s, -o, -w as these are
implicit added on the curl command line argument to format the output for this plugin.

Example usage with AzureAD oauth2
=================================

When creating authentication with AzureAD oauth2, you need to create a client Application and Azure AD only applications:

https://apps.dev.microsoft.com/#/appList

Then use:

    > curlnagios --url 'https://{yoururltotest}/api/path' --client_id 'unique-client-id' --scope 'https://{tenant}/unique-id-here-for-the-app/.default' --client_secret 'theclientoken' --grant_type 'client_credentials' --auth_url 'https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token' --oauth2

Change {tenant} with your identifier and the unique id for client and for application.
Add your client secret

This comes from documentation using token: https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow#request-an-access-token

Nagios config
=============

Example command::

    define command{
        command_name  check_http_curl
        command_line  /usr/local/bin/curlnagios --url='$ARG1$' --extra_args='$ARG2$'
    }

    define command{
        command_name  check_http_curl_azuread
        command_line  /usr/local/bin/curlnagios --url='$ARG1$' --client_id '$ARG2$' --scope '$ARG3$' --client_secret '$ARG4$' --auth_url 'https://login.microsoftonline.com/$ARG5$/oauth2/v2.0/token' --oauth2 --extra_args='$ARG6$'
    }

Example service::

    define service {
            host_name                       SERVERX
            service_description             service_name
            check_command                   check_http_curl!http://url/path!--proxy http://user:name@host:8080 --user user:name --ntlm
            use				                generic-service
            notes                           some useful notes
    }

Example service bypassing reverse proxy and dns and proxy server::

    define service {
            host_name                       SERVERY
            service_description             fqdn.backend1
            check_command                   check_http_curl!http://192.168.10.10:80!--noproxy "192.168.10.10" -H "Host: fqdn.site.name"
            use				                generic-service
            notes                           Monitoring backend1 de of site fqdn.site.name
    }

     ## In this way you can connect to some backend and pass with -H the host header to get and also ensure no proxy used to connect to url.

Example using azuread oauth2::

    define service {
            host_name                       SERVERY
            service_description             fqdn.backend1
            check_command                   check_http_curl_azuread!http://fqdn.site.name/api/xx!client-unique-id!https://{tenant}/unique-id-here-for-the-app/.default!client-secret-unique!tenant!some extra args if desired
            use				                generic-service
            notes                           Monitoring backend1 de of site fqdn.site.name
    }

You can use ansible role that already has the installation and command: https://github.com/CoffeeITWorks/ansible_nagios4_server_plugins

TODO
====

* Use hash passwords
* Add Unit tests?
