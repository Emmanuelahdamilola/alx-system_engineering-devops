include stdlib
# Puppet script to configure SSH settings

# Ensure that 'PasswordAuthentication' is set to 'no' in the SSH config.
file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

# Ensure that 'IdentityFile' is set to '~/.ssh/school' in the SSH config.
file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school', # Set IdentityFile to '~/.ssh/school'.
}

