## Resources
* http://83.212.99.245/mediawiki/index.php/Main_Page
* ip: 83.212.99.245
* ssh edet
* Web serving from: /var/lib/mediawiki/
* Mediawiki installatation dir: /var/lib/mediawiki/
* LocalSettings: /etc/LocalSettings.php
* PyPedia_Server location: /var/lib/mediawiki/extensions/PyPedia_server/
* Restart apache: /etc/init.d/apache2 restart
* Apache configuration: /etc/mediawiki/apache.conf
* Login on oceanos: https://cyclades.okeanos.grnet.gr/ui/ Username: chazapis@grnet.gr password: https://mail.google.com/mail/#inbox/139bca9d87a4f4d9

## How to setup a root jail:
debootstrap --variant=buildd --arch i386 lucid /var/chroot/ http://archive.ubuntu.com/ubuntu  
mount -o bind /proc /var/chroot/proc

https://help.ubuntu.com/community/BasicChroot

chroot /var/chroot

libblas3gf  
libblas-doc  
libblas-dev  

liblapack3gf  
liblapack-doc  
liblapack-dev  

INSIDE THE ROOT JAIL:

apt-get update  
apt-get install python  
apt-get install python-dev  
apt-get install gfortran  
apt-get install libc6-dev-amd64  

mkdir tools  

* Building LAPACK
curl http://www.netlib.org/lapack/lapack-3.1.1.tgz > /root/tools/lapack-3.1.1.tgz  
cd /root/tools; tar zxvf lapack-3.1.1.tgz  
cp /root/tools/lapack-3.1.1/INSTALL/make.inc.gfortran /root/tools/lapack-3.1.1/make.inc  

* Edit make.inc  
OPTS = -O2 -fPIC  
NOOPT = -O0 -fPIC  

cd /root/tools/lapack-3.1.1/SRC; make  

* BUILD  

curl https://dl.dropbox.com/u/5548517/atlas3.10.0.tar.bz2 > /root/tools/atlas3.10.0.tar.bz2  
cd /root/tools/; bunzip2 atlas3.10.0.tar.bz2 ; tar xvf atlas3.10.0.tar  
mkdir /root/tools/ATLAS/ATLAS_LINUX  
cd /root/tools/ATLAS/ATLAS_LINUX; ../configure -Fa alg -fPIC --with-netlib-lapack-tarfile=/root/tools/lapack-3.1.1/lapack_LINUX.a  

* Download numpy  
python setup.py install  


* Old verions..:  
apt-get install python-numpy  

apt-get install curl  

curl http://python-distribute.org/distribute_setup.py | python  
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python  

pip install nose  

## Backup script from gandi

    rm -f /home/kantale/backup/pypedia.xml.gz
    rm -f /home/kantale/backup/pypedia_test.xml.gz
    rm -f /home/kantale/backup/mywiki.xml.gz
    rm -f /home/kantale/backup/pypedia.tgz
    rm -f /home/kantale/backup/mywiki.tgz
    rm -f /home/kantale/backup/pypedia.tar
    rm -f /home/kantale/backup/mywiki.tar
    rm -f /home/kantale/backup/pypedia.sql.gz
    rm -f /home/kantale/backup/mywiki.sql.gz

    #Backing up pypedia maintenance --> pypedia.xml.gz
    php /var/www/pypedia/maintenance/dumpBackup.php --full | gzip > /home/kantale/backup/pypedia.xml.gz

    #Backing up pypedia_test maintenance --> pypedia_test.xml.gz
    php /var/www/pypedia/pyp_test/maintenance/dumpBackup.php --full | gzip > /home/kantale/backup/pypedia_test.xml.gz

    #Backing up mywiki maintenance --> mywiki.xml.gz
    php /var/www/kantale/maintenance/dumpBackup.php --full | gzip > /home/kantale/backup/mywiki.xml.gz

    #Taring complete pypedia directory --> pypedia.tgz
    tar zcvf /home/kantale/backup/pypedia.tgz /var/www/pypedia

    #Taring complete mywiki directory --> mywiki.tgz
    tar zcvf /home/kantale/backup/mywiki.tgz /var/www/kantale/

    #mysqldump pypedia --> pypedia.sql.gz
    mysqldump -u root -p<PASSWORD> pypedia -c | gzip > /home/kantale/backup/pypedia.sql.gz

    #mysqldump mywiki --> mywiki.sql.gz
    mysqldump -u root -p<PASSWORD> kantale -c | gzip > /home/kantale/backup/mywiki.sql.gz

    #Taring pypedia
    tar cvf /home/kantale/backup/pypedia.tar /home/kantale/backup/pypedia.xml.gz /home/kantale/backup/pypedia_test.xml.gz /home/kantale/backup/pypedia.tgz /home/kantale/backup/pypedia.sql.gz

    #Taring mywiki
    tar cvf /home/kantale/backup/mywiki.tar /home/kantale/backup/mywiki.xml.gz /home/kantale/backup/mywiki.tgz /home/kantale/backup/mywiki.sql.gz

    echo "Backup files: "
    echo "/home/kantale/backup/pypedia.tar" 
    echo "/home/kantale/backup/mywiki.tar"

### New instance configuration in edet
* Ubuntu Server system1.01 GB Ubuntu 12.04.1 LTS. Kernel 3.2.0
* 2 CPUs, 2048MB RAM, 10 GB Disk space
* PyPedia2
* password: https://mail.google.com/mail/#inbox/13c4313f13dc0d1b
* ip: 83.212.107.55
* Connect: ssh user@snf-13900.vm.okeanos.grnet.gr
* Try to install here: /var/www/pypedia

* Apache configuration file: /etc/apache2/sites-available/default

.

    <VirtualHost *:80>
        ServerAdmin admin@www.pypedia.com
	    ServerName www.pypedia.com:80
	    DocumentRoot /var/www/pypedia
	    <Directory />
		    Options FollowSymLinks
		    AllowOverride None
	    </Directory>
	    <Directory /var/www/pypedia>
		    Options Indexes FollowSymLinks MultiViews
		    AllowOverride None
		    Order allow,deny
		    allow from all
	    </Directory>

	    ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
	    <Directory "/usr/lib/cgi-bin">
		    AllowOverride None
		    Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
		    Order allow,deny
		    Allow from all
	    </Directory>

	    ErrorLog ${APACHE_LOG_DIR}/pypedia/error.log

	    # Possible values include: debug, info, notice, warn, error, crit,
	    # alert, emerg.
	    LogLevel warn

	    CustomLog ${APACHE_LOG_DIR}/pypedia/access.log combined

        Alias /doc/ "/usr/share/doc/"
        <Directory "/usr/share/doc/">
            Options Indexes MultiViews FollowSymLinks
            AllowOverride None
            Order deny,allow
            Deny from all
            Allow from 127.0.0.0/255.0.0.0 ::1/128
        </Directory>

    </VirtualHost>



### Create image:

    sudo apt-get update
    sudo apt-get install apache2
    sudo apt-get install php5
    sudo apt-get install git
    sudo apt-get install mysql-server mysql-client 
    sudo apt-get install php5-mysql
    sudo apt-get install zip
    sudo apt-get install automake
    sudo apt-get install php-pear
    sudo apt-get install make
    sudo apt-get install libpcre3-dev
    sudo apt-get install imagemagick
    sudo apt-get install highlight
    sudo apt-get install php5-curl
    sudo apt-get install libicu-dev
    sudo apt-get install g++

    sudo pecl install apc
    #     edit file: /etc/php5/apache2/php.ini ADD: extension=apc.so
    sudo python -c "a = open('/etc/php5/apache2/php.ini', 'a'); a.write('extension=apc.so\n'); a.close()"
    
    mkdir -p $HOME/tools
    cd $HOME/tools; git clone git://git.libssh2.org/libssh2.git
    cd $HOME/tools/libssh2; ./buildconf; ./configure ; make; make install
    cd $HOME
    
    sudo pecl install ssh2 channel://pecl.php.net/ssh2-0.12
    #edit file: /etc/php5/apache2/php.ini ADD: extension=ssh2.so
    sudo python -c "a = open('/etc/php5/apache2/php.ini', 'a'); a.write('extension=ssh2.so\n'); a.close()"
  
    sudo pecl install intl
    sudo python -c "a = open('/etc/php5/apache2/php.ini', 'a'); a.write('extension=intl.so\n'); a.close()"
  
    #Restart apache
    sudo /etc/init.d/apache2 restart
    
    #Get data from gandi:
    scp kantale@www.pypedia.com:backup/pypedia.tar $HOME/from_gandi/pypedia.tar
    scp kantale@www.pypedia.com:backup/mywiki.tar $HOME/from_gandi/mywiki.tar

    #Get mediawiki
    cd /var/www
    sudo wget http://download.wikimedia.org/mediawiki/1.20/mediawiki-1.20.2.tar.gz
    sudo tar zxvf mediawiki-1.20.2.tar.gz
    sudo rm mediawiki-1.20.2.tar.gz
    sudo mv mediawiki-1.20.2/ pypedia/
    
    #Point to: 
    #http://83.212.107.55/pypedia/mw-config/index.php
    #and install mediawiki
