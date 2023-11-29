# install flask 2.1.0

exec { 'flask':
  command => '/usr/bin/apt-get -y install puppet-lint -v 2.1.0',
}
