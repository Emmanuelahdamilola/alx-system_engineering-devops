# manifest that kills a process named killmenow.

exec { 'pkill':
  command     => 'pkill -f killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
  onlyif      => 'pgrep -f killmenow',
}

