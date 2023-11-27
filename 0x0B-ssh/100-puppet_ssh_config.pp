#!/usr/bin/env bash
# manifest to configure ssh client

file  {  '/etc/ssh/ssh_config':
  ensure  =>  file,
  content =>  "
	# SSH client config
	host*
	IdentityFile school
	PasswordAuthentication no
	",
}
