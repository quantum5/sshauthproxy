# `sshauthproxy` [![PyPI](https://img.shields.io/pypi/v/sshauthproxy.svg)](https://pypi.org/project/sshauthproxy/) [![PyPI - Format](https://img.shields.io/pypi/format/sshauthproxy.svg)](https://pypi.org/project/sshauthproxy/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sshauthproxy.svg)](https://pypi.org/project/sshauthproxy/)

`sshauthproxy` is a simple `tornado`-based daemon that exports your SSH keys
from an `AuthorizedKeysCommand` via a simple HTTP-based API.

## Why?

I am rather fond of `sss_ssh_authorizedkeys` and managing SSH keys in LDAP.
However, I would like to be able to pull SSH keys from an LDAP directory on
servers that I do not want to be added to the directory. Now, I can run
`sshauthproxy` on a server in the directory, and pull the keys from any server
I want.

While the default `AuthorizedKeysCommand` is `sss_ssh_authorizedkeys`, I am
sure there are other `AuthorizedKeysCommand` that would be useful when proxied.

## Installation

```
# On the machine publishing the keys (server):
pip install sshauthproxy

# Run the server:
sshauthproxy [--address=<the IP to listen on>] [--port=<port to listen on>]
# To proxy something other than sss_ssh_authorizedkeys, specify --command=<your command>.
# By default, the server binds to 0.0.0.0:8888 and [::]:8888.

# On the machine using the keys (client):
sudo curl https://raw.githubusercontent.com/quantum5/sshauthproxy/master/sshauth-client -o/usr/local/bin/sshauth-client
echo https://sshauth.example.com | sudo tee /etc/sshauth-server

# Now add the following lines to /etc/ssh/sshd_config on the client:
AuthorizedKeysCommand /usr/local/bin/sshauth-client
AuthorizedKeysCommandUser nobody
```

## API

The API is very simple:

* `GET /`: shows usage information.
* `GET /<username>`: shows the SSH keys for the given username, if available.
  Otherwise, it returns 404 with a blank response body.
