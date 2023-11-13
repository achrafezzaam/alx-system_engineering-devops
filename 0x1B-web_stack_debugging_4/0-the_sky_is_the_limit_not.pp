# Setting a new value to the ulimit parameter

exec {'ulimit-setup':
  # Changing the ulimit value from 15 tp 4096
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

exec {'nginx-restart':
  # Restarting the nginx service
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
