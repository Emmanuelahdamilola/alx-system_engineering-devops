# Puppet manifest for configuring custom HTTP header in Nginx

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
      listen 80 default_server;
      error_page 404 /404.html;
      location = /404.html {
        root /var/www/html;
        internal;
      }
      listen [::]:80 default_server;

      root /etc/nginx/html;
      index index.html index.htm index.nginx-debian.html;

      server_name _;
      rewrite ^/redirect_me https://www.google.com/ permanent;
      error_page 404 /404.html;
      location = /404.html {
        root /etc/nginx/html;
        internal;
      }
      rewrite ^/redirect_me https://www.google.com permanent;

      # Puppet configuration for custom HTTP header
      add_header X-Served-By $hostname;

    }
  ",
  notify  => Service['nginx'],
}

# Enable the default site by creating a symbolic link
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  notify  => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

