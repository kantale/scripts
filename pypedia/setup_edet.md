## Resources
* http://83.212.99.245/mediawiki/index.php/Main_Page
* ip: 83.212.99.245
* ssh edet
* Web serving from: /var/lib/mediawiki/
* Mediawiki installatation dir: /var/lib/mediawiki/
* LocalSettings: /etc/LocalSettings.php
* PyPedia_Server location: /var/lib/mediawiki/extensions/PyPedia_server/
* Restart apache: /etc/init.d/apache2 restart

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
