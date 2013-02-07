## Resources
* http://www.pypedia.com
* ip: 83.212.107.55
* <del>http://83.212.99.245/mediawiki/index.php/Main_Page</del>
* <del>ip: 83.212.99.245</del>
* ssh edet
* Web serving from: /var/lib/mediawiki/
* Mediawiki installatation dir: /var/lib/mediawiki/
* LocalSettings: /etc/LocalSettings.php
* PyPedia_Server location: /var/lib/mediawiki/extensions/PyPedia_server/
* Restart apache: /etc/init.d/apache2 restart
* Apache configuration: /etc/mediawiki/apache.conf
* Login on oceanos: https://cyclades.okeanos.grnet.gr/ui/ Username: chazapis@grnet.gr password: https://mail.google.com/mail/#inbox/139bca9d87a4f4d9
* http://83.212.107.55/pypedia/index.php/Main_Page
* Logs: tail /var/log/apache2/error.log
* Root jail machine: ssh user@snf-14105.vm.okeanos.grnet.gr
* Web server: ssh user@snf-13900.vm.okeanos.grnet.gr

## How to setup a root jail:
* https://help.ubuntu.com/community/BasicChroot
* https://help.ubuntu.com/community/DebootstrapChroot

.

    sudo apt-get update
    sudo apt-get -y install debootstrap
    sudo apt-get -y install schroot

    #sudo debootstrap --variant=buildd --arch i386 lucid /var/chroot/ http://archive.ubuntu.com/ubuntu
    sudo debootstrap --variant=buildd --arch i386 precise /var/chroot/ http://archive.ubuntu.com/ubuntu
    sudo mount -o bind /proc /var/chroot/proc
    sudo chroot /var/chroot

* How to destroy a root jail:

.

    sudo umount /var/chroot/proc
    sudo rm -rf  /var/chroot

libblas3gf  
libblas-doc  
libblas-dev  

liblapack3gf  
liblapack-doc  
liblapack-dev  

## INSIDE THE ROOT JAIL:


    apt-get update  
    apt-get -y install python  
    apt-get -y install python-dev  
    apt-get -y install git
    apt-get -y install gfortran  
    apt-get -y install libc6-dev-amd64
    apt-get -y install curl
    apt-get -y install python.numpy
    apt-get -y install libblas3gf libblas-doc libblas-dev
    apt-get -y install liblapack3gf liblapack-doc liblapack-dev
    apt-get -y install libfreetype6 libfreetype6-dev
    apt-get -y install libpng-dev libjpeg8-dev

    echo 'none /dev/shm tmpfs rw,nosuid,nodev,noexec 0 0' >> /etc/fstab
    mount -a

    mkdir /root/tools

    cd /root/tools; git git clone https://github.com/haypo/pysandbox.git
    cd /root/tools/pysandbox; python setup.py build
    cd /root/tools/pysandbox; python setup.py install
    
    cd /root/tools; curl https://dl.dropbox.com/u/5548517/scipy-0.11.0.tar.gz > scipy-0.11.0.tar.gz
    cd /root/tools; tar zxvf scipy-0.11.0.tar.gz
    cd /root/tools/scipy-0.11.0; python setup.py build
    cd /root/tools/scipy-0.11.0; python setup.py install

    curl http://python-distribute.org/distribute_setup.py | python  
    curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python  
    pip install nose 
    
    cd /root/tools; curl  http://sympy.googlecode.com/files/sympy-0.7.1.tar.gz > sympy-0.7.1.tar.gz
    cd /root/tools; tar zxvf sympy-0.7.1.tar.gz
    cd /root/tools/sympy-0.7.1; python setup.py build
    cd /root/tools/sympy-0.7.1; python setup.py install
    
    #Install matplotlib
    pip install matplotlib
    sed -i 's/^backend[ \t]*:.*$/backend : Agg/g' `python -c 'import matplotlib; print matplotlib.matplotlib_fname()'`

    #Install mpmath
    apt-get -y install libmpc-dev
    apt-get -y install libmpfr-dev
    apt-get -y install libgmp3-dev
    cd /root/tools; curl http://www.multiprecision.org/mpc/download/mpc-1.0.1.tar.gz > mpc-1.0.1.tar.gz
    cd /root/tools; tar zxvf mpc-1.0.1.tar.gz
    cd /root/tools/mpc-1.0.1; ./configure; make; make install
    pip install gmpy2
    cd /root/tools; curl http://mpmath.googlecode.com/files/mpmath-all-0.17.tar.gz > mpmath-all-0.17.tar.gz
    cd /root/tools; tar zxvf mpmath-all-0.17.tar.gz 
    cd /root/tools/mpmath-all-0.17; python setup.py build; python setup.py install
    
    #Fix Bug: https://bugs.archlinux.org/task/30020
    chmod ag+r /usr/local/lib/python2.7/dist-packages/python_dateutil-2.1-py2.7.egg/EGG-INFO/*

    #Install biopython
    cd /root/tools; curl http://biopython.org/DIST/biopython-1.60.tar.gz > biopython-1.60.tar.gz
    cd /root/tools; tar zxvf biopython-1.60.tar.gz
    cd /root/tools/biopython-1.60/; python setup.py build
    cd /root/tools/biopython-1.60/; python setup.py install
    
    #Install basemap
    cd /root/tools; wget http://download.osgeo.org/geos/geos-3.3.7.tar.bz2
    cd /root/tools; bzip2 -d geos-3.3.7.tar.bz2
    cd /root/toos; tar xvf geos-3.3.7.tar
    cd /root/tools/geos-3.3.7; ./configure; make; make install
    cd /root/tools; wget "http://downloads.sourceforge.net/project/matplotlib/matplotlib-toolkits/basemap-1.0.6/basemap-1.0.6.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fmatplotlib%2Ffiles%2Fmatplotlib-toolkits%2Fbasemap-1.0.6%2F&ts=1359637493&use_mirror=superb-dca3" -O basemap-1.0.6.tar.gz
    cd /root/tools; tar zxvf basemap-1.0.6.tar.gz
    cd /root/tools/basemap-1.0.6; pyton setup.py build
    cd /root/tools/basemap-1.0.6; pyton setup.py install
    
    #install  sckikit-learn
    pip install -U scikit-learn
    
    #Install networkx
    cd /root/tools; wget http://pypi.python.org/packages/source/n/networkx/networkx-1.7.tar.gz#md5=1a73da9d571a206aa40f6ef69254f7b4
    cd /root/tools; tar zxvf networkx-1.7.tar.gz
    cd /root/tools/networkx-1.7; python setup.py build
    cd /root/tools/networkx-1.7; python setup.py install
    
    useradd puser
    passwd puser
    
    mkdir /home/puser
    cd /home/puser; curl https://raw.github.com/kantale/PyPedia_server/master/utils/pyp_sandbox2.py > pyp_sandbox2.py
    
    touch /home/puser/nohup.out
    chmod 622 /home/puser/nohup.out
    
    su - puser
    
    #As a puser
    #cd /home/puser; nohup python pyp_sandbox2.py &
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
    sudo apt-get -y install apache2
    sudo apt-get -y install php5
    sudo apt-get -y install git
    sudo apt-get -y install mysql-server mysql-client 
    sudo apt-get -y install php5-mysql
    sudo apt-get -y install zip
    sudo apt-get -y install automake
    sudo apt-get -y install php-pear
    sudo apt-get -y install make
    sudo apt-get -y install libpcre3-dev
    sudo apt-get -y install imagemagick
    sudo apt-get -y install highlight
    sudo apt-get -y install php5-curl
    sudo apt-get -y install libicu-dev
    sudo apt-get -y install g++
    sudo apt-get -y install ocaml
    sudo apt-get -y install texlive-latex-base
    sudo apt-get -y install texlive-full #Probably this can be avoided

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
    #and install mediawiki. Admin's account: admin
    
    #Install Math extension
    cd /var/www/pypedia/extensions; sudo git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Math.git
    cd /var/www/pypedia/extensions/Math/math; sudo make
    #Add to LocalSettings.php: 
    # require_once("$IP/extensions/Math/Math.php");
    # $wgTexvc = "$wgScriptPath/extensions/Math/math/texvc";
    cd /var/www/pypedia/maintenance; sudo php update.php
    sudo mkdir /var/www/pypedia/images/math
    sudo chown www-data /var/www/pypedia/images/math
    sudo chgrp www-data /var/www/pypedia/images/math
    
    #Load backup data to wiki
    mkdir $HOME/restore
    cp $HOME/from_gandi/pypedia.tar /$HOME/restore/pypedia.tar
    cd $HOME/restore/; tar xvf pypedia.tar 
    cd $HOME/restore/home/kantale/backup; gunzip pypedia.xml.gz

    #If problems with importDump:
    sudo python -c "a = open('/var/www/pypedia/LocalSettings.php').read(); a = a.replace('$wgMainCacheType = CACHE_ACCEL;', '$wgMainCacheType = CACHE_ANYTHING;'); b = open('/var/www/pypedia/LocalSettings.php', 'w').write(a)"
    
    cd /var/www/pypedia/maintenance; sudo php importDump.php  /home/user/restore/home/kantale/backup/pypedia.xml
    cd /var/www/pypedia/maintenance; sudo php rebuildrecentchanges.php 
    
    cd $HOME/restore/home/kantale/backup; tar zxvf pypedia.tgz
    sudo php importImages.php $HOME/restore/home/kantale/backup/var/www/pypedia/images/

    #Copy secret key value from old wiki. 
    $Copy $wgSecretKey from $HOME/restore/home/kantale/backup/var/www/pypedia/LocalSettings.php /var/www/LocalSettings.php
    
    #Insert user information
    #scp kantale@www.pypedia.com:/home/kantale/backup/pypedia_user.sql ./pypedia_user.sql
    #mysql -u root -p<PASSWORD>
    #use pypedia
    #drop table pypuser;
    #source /home/user/restore/home/kantale/backup/pypedia_user.sql
    
    #Insert blocked ips
    #From source: mysqldump -u root -p<PASSWORD> pypedia pypipblocks -c > /home/kantale/backup/pypedia_ipblocks.sql
    #From target: scp kantale@www.pypedia.com:/home/kantale/backup/pypedia_ipblocks.sql $HOME/restore/home/kantale/backup/pypedia_ipblocks.sql
    #REMOVE THE PART WHERE IT DROPS AND CREATES THE TABLE. KEEP ONLY THE INSERT STATEMENT and create the file /home/user/restore/home/kantale/backup/pypedia_ipblocks_donotdrop.sql
    #mysql -u root -p<PASSWORD>
    #use pypedia
    #source /home/user/restore/home/kantale/backup/pypedia_ipblocks_donotdrop.sql

    #Install pypedia..
    cd /var/www/pypedia/extensions; sudo git clone https://github.com/kantale/PyPedia_server.git
    
    #Install MyVariables extension
    cd /var/www/pypedia/extensios/PyPedia_server; sudo git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/MyVariables.git
    #Add extra settings to LocalSettings.php
    
    #This is problematic for some versions of mediawiki..
    #Add to index.php: after $mediaWiki = new MediaWiki();
    pypedia_REST_API($wgRequest);
    
    #This might not work (it is better to edit explicitly and add the particular code)
    cp /var/www/pypedia/skins/Vector.php /var/www/pypedia/skins/Vector.php.backup
    cp /var/www/pypedia/extensions/PyPedia_server/Vector.php /var/www/pypedia/skins/Vector.php
    
    #Edit line 2738 of includes/OutputPage.php before:
    #if ( $wgResourceLoaderExperimentalAsyncLoading ) {
    #Add the following: (substitute www.pypedia.com with your's installation domain name)

    $scripts .= '
    <!-- PYPEDIA JS SCRIPTS -->
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.0/jquery.min.js"></script>
    <script src="http://www.pypedia.com/extensions/PyPedia_server/pypedia.js"></script>
    <script src="http://www.pypedia.com/extensions/PyPedia_server/import_gist.js"></script>
    <!-- END OF PYPEDIA JS SCRIPTS -->
    ';
    
    #From: https://github.com/kantale/PyPedia_server/blob/master/INSTALL STEP 5: Create file with passwords
    
    #Fix /etc/apache2/sites-available/default
    #Set: $wgScriptPath       = ""; in LocalSettings.php
    
    #Add to LocalSettings.php regarding copyright:
    $wgRightsPage = "PyPedia:License"; # Set to the title of a wiki page that describes your license/copyright
    $wgRightsUrl = "http://opensource.org/licenses/bsd-license.php";
    $wgRightsText = "Simplified BSD License";
    $wgRightsIcon = "{$wgStylePath}/common/images/License_icon-bsd-88x31.png";
    
    #Add spam control tools
    require_once( "$IP/extensions/ConfirmEdit/ConfirmEdit.php" );
    require_once( "$IP/extensions/ConfirmEdit/QuestyCaptcha.php");
    $wgCaptchaClass = 'QuestyCaptcha';
    $wgCaptchaQuestions[] = array( 'question' => "What is this wiki's name?", 'answer' => "$wgSitename" );

    #Allow for first letter of articles to be lowercase
    $wgCapitalLinks = false;

    cd /var/www/pypedia/skins/common/images; sudo wget http://upload.wikimedia.org/wikipedia/commons/4/42/License_icon-bsd-88x31.png

### Initial Main_Page content:

    ==Introduction==
    PyPedia is a collaborative programming web environment. Each article in this wiki is a function or class or any other piece of [http://www.python.org/ Python] code. No need to import anything. Just call the function or instantiate the class that belongs to any other article. 

    '''Simple as this:'''
    {{#input:type=textarea|name=whatever|rows=8|cols=20|id=main_form}}
    {{#form:id=parameters_form}} 
    {{#input:type=ajax|value=Run|id=eobm}}
    {{#formend:}}

    [[Pascal_triangle]] and [[Hanoi_towers]] are articles in this wiki! Check out all [[:Category:Validated|validated methods]].

    ==Documentation==
    *First time in PyPedia? please read this [http://www.slideshare.net/kantale/pypedia presentation] or download it: [http://dl.dropbox.com/u/5548517/PyPedia.pptx powerpoint], [http://dl.dropbox.com/u/5548517/PyPedia.pdf pdf]
    *Are you more of a visual type? Watch this [http://www.youtube.com/watch?v=25jMEivICD8 video]. It is only 2 minutes..
    *For more read: [[PyPedia:Documentation|Documentation]].
    *To execute locally the code hosted here, install the PyPedia python library:
    <pre>
    git clone git://github.com/kantale/pypedia.git
    </pre>
    Then you can download and run the code:
    <pre>
    >>> import pypedia
    >>> from pypedia import Hello_world
    >>> Hello_world()
    Hello world!
    >>>
    </pre>
    * Request an article: [[PyPedia:Wanted algorithms|Wanted algorithms]], request a feature: [[PyPedia_talk:Feature_requests|Feature requests discussion]]
    * Sign in our mailing list: http://groups.google.com/group/pypedia
    * Follow on twitter : [https://twitter.com/#!/pypedia @PyPedia]
    * A blog about developing PyPedia: http://pypedia.blogspot.nl/

### Extra settings for LocalSettings.php

    $wgUseAjax = true;
    require_once( "{$IP}/extensions/PyPedia_server/pypedia.php");
    #Before wgLogo (No particular reason)
    $wgLogo = "$wgScriptPath/extensions/PyPedia_server/pypedia.png";

    #Hooks for PyPedia
    $wgHooks['EditPage::attemptSave'][] = 'pypediaEditPageAttemptSave';
    $wgHooks['EditFormPreloadText'][] = array('pypediaPrefill');
    $wgHooks['EditFilter'][] = 'pypediaEditFilter';
    $wgHooks['DoEditSectionLink'][] = 'pypediaDoEditSectionLink';
    $wgHooks['EditPage::showEditForm:initial'][] = 'pypediaEditForm';

    #The group that can edit the code
    $wgGroupPermissions['codeeditor'] = $wgGroupPermissions['user'];

    #The administrators.
    $wgGroupPermissions['pypediaadmin'] = $wgGroupPermissions['user'];

    # Do not have to, but it is a good idea, for Anonymous not to be able to create pages
    $wgGroupPermissions['*']['createpage'] = false;


