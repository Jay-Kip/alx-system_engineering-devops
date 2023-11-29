# install flask 2.1.0

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.0.2',
  path    => '/usr/bin',
  creates => '/usr/local/lib/python3.11/dist-packages/flask',
}
