#!/bin/bash
openssl  dgst -md5 -hmac $1 $2 > .authenticate
echo $1 >> .authenticate

