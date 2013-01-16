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

    sudo pecl install apc

    edit file: /etc/php5/apache2/php.ini ADD: extension=apc.so
    sudo vim /etc/php5/apache2/php.ini
    
    mkdir tools
    cd tools; git clone git://git.libssh2.org/libssh2.git
    cd libssh2; ./buildconf; ./configure ; make; make install
    
    
