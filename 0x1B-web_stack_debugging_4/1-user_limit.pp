# Setting a new value to the soft and hard limit of the holberton

exec {'soft-limit':
  # Changing the soft limit value
  command => 'sed -i "/^holberton soft/s/4/400/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}


exec {'hard-limit':
  # Changing the hard limit value
  command => 'sed -i "/^holberton hard/s/5/500/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
