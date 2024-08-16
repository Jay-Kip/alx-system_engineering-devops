# A Puppet script to replace a line in a file on a server
file_line { 'replace-phpp-with-php':
  path        => '/var/www/html/wp-settings.php',
  line        => 'phpp',
  match       => '^phpp$',
  substitute  => 'php',
  multiple    => true,
  replace     => true,
  replace_all => true,
  backup      => '.bak',
  show_diff   => true,
  notify      => Exec['restart-apache'],
}

exec { 'restart-apache':
  command     => '/usr/sbin/systemctl restart apache2',
  path        => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  refreshonly => true,
}
