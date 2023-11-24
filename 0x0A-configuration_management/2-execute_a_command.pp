# Kills a process 'killmenow'
exec { 'kill_process':
  command => 'pkill killmenow',
  path    => '/usr/bin',
  onlyif  => 'pgrep killmenow',
}
