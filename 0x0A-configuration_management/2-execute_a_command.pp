# Kill the process killnow
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
