# Use Puppet to automate the task of creating a custom HTTP header response

# Execute 'apt-get update' before installing Nginx
exec { 'update':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
  ensure => 'present',
}

# Add custom HTTP header to Nginx configuration
file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

# Restart Nginx service after updating configuration
exec { 'run':
  command => '/usr/sbin/service nginx restart',
}

