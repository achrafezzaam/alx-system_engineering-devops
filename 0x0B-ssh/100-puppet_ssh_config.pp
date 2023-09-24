# Setting the config file to use the ~/.ssh/school
# private key and reject password authentications
include stdlib

file_line { 'file _identity':
  ensure  => present,
  path    => 'etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^IdentityFile',
  replace => true,
}

file_line { 'authentication':
  ensure  => present,
  path    => 'etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
  replace => true,
}
