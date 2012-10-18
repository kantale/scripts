#Get Minimach
#wget http://www.sph.umich.edu/csg/cfuchsb/minimac-beta-2012.8.15.tgz

#tar xvf minimac-beta-2012.8.15.tgz

import os
import re
import sys
import urllib2

#pipeline = 'minimac'
#pipeline = 'beagle'
pipeline = 'compare_grid'

#environment = 'gpfs'
#environment = 'macbookair'
environment = 'vm'

#queue = 'gcc'
queue = 'test-long'

#scheduler = 'PBS' # For gpfs
scheduler = 'GRID' # For Grid

#Import workflow to molgenis?
import_to_molgenis = True

def fetch_page(url):
	print "Fetching: " + url
	try:
		fp = urllib2.urlopen(url)
		ret = fp.read()
		fp.close()
	except urllib2.HTTPError:
		print '   FAIL import'
		ret = ''

	return ret

def fetch_page_l(url):
	return lambda : fetch_page(url)

project_name = 'myProject'
parameters_name = 'parameters'

# molgenis_dir = '/target/gpfs2/gcc/home/fvandijk/impute2/working_standalone/molgenis_compute-a476811/'
if environment == 'gpfs':
	molgenis_dir = '/target/gpfs2/gcc/home/akanterakis/tools/molgenis_compute-aabb8f3/'
elif environment == 'macbookair':
	molgenis_dir = '/Users/alexandroskanterakis/GitHub/molgenis_apps/bin/molgenis_compute-aabb8f3'
	molgenis_apps_dir = '/Users/alexandroskanterakis/GitHub/molgenis_apps'
elif environment == 'vm':
	molgenis_dir = None
	molgenis_apps_dir = '/srv/molgenis/compute/molgenis_apps' 
	import_to_molgenies = True
else:
	raise Exception('Unknown value for environment variable: ' + str(environment))

molgenis_script = 'molgenis_compute.sh'

#Script specific parameters
run_id = 'run_01'

if pipeline == 'minimac':
	scripts_dir = '/target/gpfs2/gcc/home/akanterakis/runs/Mach_5_Sep_2012/mach_minimach'
	workflow_name = 'workflowMachMinimac'
	worksheet = fetch_page('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/mach_minimach/worksheet_example.csv')
	workflow = fetch_page('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/mach_minimach/workflowMachMinimac.csv')
	parameters = fetch_page('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/mach_minimach/parameters.csv')
elif pipeline == 'beagle':
	scripts_dir = '/target/gpfs2/gcc/home/akanterakis/runs/Beagle_19_Sep_2012/beagle/'
	workflow_name = 'workflowBeagle'
	worksheet = fetch_page('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/beagle/worksheet_example.csv')
	workflow = fetch_page('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/beagle/workflowBeagle.csv')
	parameters = fetch_page('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/mach_minimach/parameters.csv')
elif pipeline == 'compare_grid':
	if environment == 'gpfs':
		scripts_dir = '/target/gpfs2/gcc/home/akanterakis/runs/Grid_test/grid_compare'
	elif environment == 'macbookair':
		scripts_dir = '/Users/alexandroskanterakis/runs/grid_compare'
	elif environment == 'vm':
		scripts_dir = '/srv/molgenis/alex/runs/compare_grid'
	else:
		raise Exception('Unknown value for environment variable: ' + str(environment))

	workflow_name = 'workflowComparison'
	worksheet = fetch_page('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/worksheet_example.csv')
	workflow = fetch_page('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/workflowComparison.csv')
	parameters = fetch_page('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/parameters.csv')
else:
	raise Exception("Error")

protocols_dir = os.path.join(scripts_dir, 'protocols')

#Substitue clusterQueue, scheduler
parameters = re.sub(r'clusterQueue,[\w\-]*,', r'clusterQueue,' + queue + ',', parameters)
parameters = re.sub(r'scheduler,[\w\-]*,', r'scheduler,' + scheduler + ',', parameters)

protocol_convertPedMapToTriTyper = {
	"name" : "convertPedMapToTriTyper",
	"content" : fetch_page_l('https://raw.github.com/freerkvandijk/molgenis_apps/master/modules/compute/protocols/imputation/impute2/protocols/convertPedMapToTriTyper.ftl') 
}

protocol_preparePedMapForImpute2 = {
	"name" : "preparePedMapForImpute2",
	"content" : fetch_page_l('https://raw.github.com/freerkvandijk/molgenis_apps/master/modules/compute/protocols/imputation/impute2/protocols/preparePedMapForImpute2.ftl') 
}

#Compare study with reference with ImputationTool
protocol_prepareStudy = {
	"name" : "prepareStudy",
	"content" : fetch_page_l('https://raw.github.com/freerkvandijk/molgenis_apps/master/modules/compute/protocols/imputation/impute2/protocols/prepareStudy.ftl') 
}

#Compare study with reference with ImputationTool by using batches. Suitable for beagle
protocol_prepareStudyWithBatches = {
	"name" : 'prepareStudyWithBatches',
	"content" : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/beagle/prepareStudyWithBatches.ftl') 
}

#Create batches with ImputationTool
protocol_createBatches = {
	"name" : "createBatches",
	"content" : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/beagle/createBatches.ftl')
}

protocol_phase_study_with_mach = {
	"name" : "phase_study_with_mach",
	"content" : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/mach_minimach/phase_study_with_mach.ftl')
}

protocol_impute_with_minimac = {
	"name" : "impute_with_minimac",
	"content" : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/mach_minimach/impute_with_minimach.ftl')
}

#Post process minimac results and compute Beagle's allelic R2
protocol_minimacPostProcessing = {
	"name" : "postProcessing",
	"content" : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/mach_minimach/postProcessing.ftl')
}

#Convert from ped and map generated from ImputationTool to beagle format
protocol_convertPreparedStudyToBeagle = {
	"name" : 'convertPreparedStudyToBeagle',
	"content" : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/beagle/convertPreparedStudyToBeagle.ftl')
}

protocol_imputeWithBeagle = {
	"name" : 'imputeWithBeagle',
	"content" : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/beagle/imputeWithBeagle.ftl')
}

protocol_concatImputationResults = {
	"name" : 'concatImputationResults',
	"content" : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/concatImputationResults.ftl')
}

if pipeline == 'minimac':
	protocols = [
		protocol_prepareStudy, 
		protocol_preparePedMapForImpute2, 
		protocol_convertPedMapToTriTyper, 
		protocol_phase_study_with_mach, 
		protocol_impute_with_minimac,
		protocol_minimacPostProcessing
	]
elif pipeline == 'beagle':
	protocols = [
#		protocol_prepareStudy,
		protocol_prepareStudyWithBatches,
		protocol_createBatches, 
		protocol_preparePedMapForImpute2, 
		protocol_convertPedMapToTriTyper, 
		protocol_convertPreparedStudyToBeagle,
		protocol_imputeWithBeagle,
	]
elif pipeline == 'compare_grid':
	protocols = [
		protocol_concatImputationResults,
	]
else:
	raise Exception("Error")

#####################################################################
########## NO NEED TO EDIT FROM THAT POINT ##########################
#####################################################################

worksheet_fn = os.path.join(scripts_dir, project_name + '.csv')
parameters_fn = os.path.join(scripts_dir, parameters_name + '.csv')
workflow_fn = os.path.join(scripts_dir, workflow_name + '.csv')

#TODO! Make ftl files in scripts_dir

def remove_empty_lines(text):
	return str.join('\n', [x for x in text.split('\n') if len(x) > 0])

def make_scripts():

	#Check scripts directory
	if not os.path.exists(scripts_dir):
		os.mkdir(scripts_dir)

	if not os.path.exists(protocols_dir):
		os.mkdir(protocols_dir)

	#Save worksheet
	worksheet_nl = remove_empty_lines(worksheet)
	open(worksheet_fn, 'w').write(worksheet_nl + '\n')

	#Remove empty lines of parameters
	parameters_nl = remove_empty_lines(parameters)

	#Save parameters
	open(parameters_fn, 'w').write(parameters_nl + '\n')

	#Remove empty lines of workflow
	workflow_nl = remove_empty_lines(workflow)

	#Save workflow
	open(workflow_fn, 'w').write(workflow_nl + '\n')

	#Save protocols
	for protocol in protocols:
		protocol_fn = os.path.join(protocols_dir, protocol['name'] + '.ftl')
		open(protocol_fn, 'w').write(protocol['content']() + '\n')

	#Necessary files
	open(os.path.join(protocols_dir, 'Header.ftl'), 'w').write(fetch_page('https://raw.github.com/freerkvandijk/molgenis_apps/master/modules/compute/protocols/imputation/impute2/protocols/Header.ftl'))
	open(os.path.join(protocols_dir, 'Footer.ftl'), 'w').write(fetch_page('https://raw.github.com/freerkvandijk/molgenis_apps/master/modules/compute/protocols/imputation/impute2/protocols/Footer.ftl'))
	open(os.path.join(protocols_dir, 'CustomSubmit.sh.ftl'), 'w')
	open(os.path.join(protocols_dir, 'Macros.ftl'), 'w').write(fetch_page('https://raw.github.com/freerkvandijk/molgenis_apps/master/modules/compute/protocols/imputation/impute2/protocols/Macros.ftl'))
	open(os.path.join(protocols_dir, 'Helpers.ftl'), 'w').write(fetch_page('https://raw.github.com/freerkvandijk/molgenis_apps/master/modules/compute/protocols/imputation/impute2/protocols/Helpers.ftl'))


def clean_compute():
	command = "echo 'DROP DATABASE IF EXISTS compute; CREATE DATABASE compute;' | mysql -u molgenis -pmolgenis"
	print "Running: " + command
	os.system(command)

def compile_molgenis():
	command = "cd %s; ant -f build_compute.xml clean-generate-compile" % (molgenis_apps_dir)	
	print "Running: " + command
	os.system(command)

	#After compile. Change persistence.xml.
	#build/classes/META-INF/persistence.xml
	# sed -i 's/validate/update/g' build/classes/META-INF/persistence.xml

def start_molgenis(port = 8080):
	if environment == 'vm':
		command = "kill `ps aux | grep ant-launcher | grep -v grep | cut -d ' ' -f 3`"
	else:
		command = "kill -9 `lsof -i :%i -t`" % (port)
	print "Running: " + command
	os.system(command)

	command = "cd %s; nohup ant -f build_compute.xml runOn -Dport=%i & " % (molgenis_apps_dir, port)
	print "Running: " + command
	os.system(command)

	command = "sleep 4"
	print "Waiting for molgenis to start up.."
	os.system(command)
	print "ok"

def import_workflow():
	command = """cd %s; java -cp molgenis_apps/build/classes:molgenis/bin:\
molgenis/lib/ant-1.8.1.jar:molgenis/lib/ant-apache-log4j.jar:molgenis/lib/aopalliance-1.0.jar:molgenis/lib/apache-poi-3.8.2:\
molgenis/lib/arq.jar:molgenis/lib/asm-3.3.jar:molgenis/lib/axiom-api-1.2.7.jar:molgenis/lib/axiom-impl-1.2.7.jar:\
molgenis/lib/bcprov-jdk15-1.43.jar:molgenis/lib/commons-codec-1.3.jar:molgenis/lib/commons-collections-3.2.1.jar:\
molgenis/lib/commons-dbcp-1.2.1.jar:molgenis/lib/commons-fileupload-1.1.jar:molgenis/lib/commons-io-2.4.jar:\
molgenis/lib/commons-lang-2.5.jar:molgenis/lib/commons-lang3-3.1.jar:molgenis/lib/commons-logging-1.1.1.jar:molgenis/lib/commons-pool-1.5.2.jar:\
molgenis/lib/concurrent.jar:molgenis/lib/cxf-bundle-minimal-2.5.2.jar:molgenis/lib/d2rq-0.7.jar:molgenis/lib/d2r-server-0.7.jar:\
molgenis/lib/dom4j-1.6.1.jar:molgenis/lib/FastInfoset-1.2.7.jar:molgenis/lib/freemarker.jar:molgenis/lib/ganymed-ssh2-build250.jar:\
molgenis/lib/gson-2.2.1.jar:molgenis/lib/hsqldb.jar:molgenis/lib/icu4j_3_4.jar:molgenis/lib/iri.jar:molgenis/lib/jakarta-oro-2.0.8.jar:\
molgenis/lib/javassist-3.12.0.GA.jar:molgenis/lib/javax.mail.jar:molgenis/lib/javax.servlet.jar:molgenis/lib/jaxb-impl-2.2.1.1.jar:\
molgenis/lib/jaxb-xjc-2.2.1.1.jar:molgenis/lib/jaxen-1.1.jar:molgenis/lib/jdom-1.0.jar:molgenis/lib/jena.jar:molgenis/lib/jersey-json-1.1.5.jar:\
molgenis/lib/jettison-1.2.jar:molgenis/lib/jetty-6.1.21.jar:molgenis/lib/jetty-html-6.1.21.jar:molgenis/lib/jetty-plus-6.1.21.jar:molgenis/lib/jetty-util-6.1.21.jar:\
molgenis/lib/jopenid-1.07.jar:molgenis/lib/joseki.jar:molgenis/lib/jra-1.0-alpha-4.jar:molgenis/lib/js-1.7R1.jar:molgenis/lib/json.jar:molgenis/lib/jsr311-api-1.1.1.jar:\
molgenis/lib/jta-1.1.jar:molgenis/lib/junit-4.8.2.jar:molgenis/lib/jxl.jar:molgenis/lib/log4j-1.2.15.jar:molgenis/lib/lucene-core-3.0.2.jar:molgenis/lib/mail.jar:\
molgenis/lib/mysql-connector-java-5.1.2-beta-bin.jar:molgenis/lib/neethi-2.0.4.jar:molgenis/lib/oro-2.0.8.jar:molgenis/lib/postgresql-8.3-603.jdbc4.jar:\
molgenis/lib/quartz-1.6.0.jar:molgenis/lib/selenium-server-standalone-2.19.0.jar:molgenis/lib/serializer-2.7.1.jar:molgenis/lib/slf4j-api-1.6.1.jar:\
molgenis/lib/slf4j-log4j12-1.6.1.jar:molgenis/lib/smtp.jar:molgenis/lib/stax-utils-20060502.jar:molgenis/lib/tar.jar:molgenis/lib/testng-5.14.10.jar:\
molgenis/lib/tjws-1.98.jar:molgenis/lib/validation-api-1.0.0.GA.jar:molgenis/lib/velocity-1.6.4.jar:molgenis/lib/wsdl4j-1.6.2.jar:molgenis/lib/wss4j-1.5.8.jar:\
molgenis/lib/wstx-asl-3.2.8.jar:molgenis/lib/xalan-2.7.1.jar:molgenis/lib/xercesImpl.jar:molgenis/lib/xmlbeans-2.4.0.jar:molgenis/lib/xml-resolver-1.2.jar:\
molgenis/lib/xmlrpc-client-3.1.3.jar:molgenis/lib/xmlrpc-common-3.1.3.jar:molgenis/lib/XmlSchema-1.4.7.jar:molgenis/lib/xmlsec-1.4.3.jar:molgenis/lib/xmltask.jar:\
molgenis/lib/hibernate-validator-4.1.0.Final/hibernate-jpa-2.0-api-1.0.0.Final.jar:molgenis/lib/hibernate-validator-4.1.0.Final/hibernate-validator-4.1.0.Final.jar:\
molgenis/lib/hibernate-validator-4.1.0.Final/log4j-1.2.14.jar:molgenis/lib/hibernate/antlr-2.7.6.jar:\
molgenis/lib/hibernate-validator-4.1.0.Final/validation-api-1.0.0.GA.jar:\
molgenis/lib/hibernate/commons-collections-3.1.jar:molgenis/lib/hibernate/dom4j-1.6.1.jar:molgenis/lib/hibernate/hibernate3.jar:\
molgenis/lib/hibernate/hibernate-jpa-2.0-api-1.0.0.Final.jar:molgenis/lib/hibernate/hibernate-search-3.4.1.Final.jar:\
molgenis/lib/hibernate/javassist-3.12.0.GA.jar:molgenis/lib/hibernate/jta-1.1.jar:slf4j-api-1.6.1.jar \
org.molgenis.compute.test.util.WorkflowImporterJPA %s %s %s """
	command = command % (os.path.join(molgenis_apps_dir, '..'), parameters_fn, workflow_fn, protocols_dir)
	print "Running: " + command
	os.system(command)

def import_worksheet(run_name = 'test_001'):
	command = """ cd %s; java -cp molgenis_apps/build/classes:molgenis/bin:\
molgenis/lib/ant-1.8.1.jar:molgenis/lib/ant-apache-log4j.jar:molgenis/lib/aopalliance-1.0.jar:molgenis/lib/apache-poi-3.8.2:\
molgenis/lib/arq.jar:molgenis/lib/asm-3.3.jar:molgenis/lib/axiom-api-1.2.7.jar:molgenis/lib/axiom-impl-1.2.7.jar:\
molgenis/lib/bcprov-jdk15-1.43.jar:molgenis/lib/commons-codec-1.3.jar:molgenis/lib/commons-collections-3.2.1.jar:\
molgenis/lib/commons-dbcp-1.2.1.jar:molgenis/lib/commons-fileupload-1.1.jar:molgenis/lib/commons-io-2.4.jar:\
molgenis/lib/commons-lang-2.5.jar:molgenis/lib/commons-lang3-3.1.jar:molgenis/lib/commons-logging-1.1.1.jar:molgenis/lib/commons-pool-1.5.2.jar:\
molgenis/lib/concurrent.jar:molgenis/lib/cxf-bundle-minimal-2.5.2.jar:molgenis/lib/d2rq-0.7.jar:molgenis/lib/d2r-server-0.7.jar:\
molgenis/lib/dom4j-1.6.1.jar:molgenis/lib/FastInfoset-1.2.7.jar:molgenis/lib/freemarker.jar:molgenis/lib/ganymed-ssh2-build250.jar:\
molgenis/lib/gson-2.2.1.jar:molgenis/lib/hsqldb.jar:molgenis/lib/icu4j_3_4.jar:molgenis/lib/iri.jar:molgenis/lib/jakarta-oro-2.0.8.jar:\
molgenis/lib/javassist-3.12.0.GA.jar:molgenis/lib/javax.mail.jar:molgenis/lib/javax.servlet.jar:molgenis/lib/jaxb-impl-2.2.1.1.jar:\
molgenis/lib/jaxb-xjc-2.2.1.1.jar:molgenis/lib/jaxen-1.1.jar:molgenis/lib/jdom-1.0.jar:molgenis/lib/jena.jar:molgenis/lib/jersey-json-1.1.5.jar:\
molgenis/lib/jettison-1.2.jar:molgenis/lib/jetty-6.1.21.jar:molgenis/lib/jetty-html-6.1.21.jar:molgenis/lib/jetty-plus-6.1.21.jar:molgenis/lib/jetty-util-6.1.21.jar:\
molgenis/lib/jopenid-1.07.jar:molgenis/lib/joseki.jar:molgenis/lib/jra-1.0-alpha-4.jar:molgenis/lib/js-1.7R1.jar:molgenis/lib/json.jar:molgenis/lib/jsr311-api-1.1.1.jar:\
molgenis/lib/jta-1.1.jar:molgenis/lib/junit-4.8.2.jar:molgenis/lib/jxl.jar:molgenis/lib/log4j-1.2.15.jar:molgenis/lib/lucene-core-3.0.2.jar:molgenis/lib/mail.jar:\
molgenis/lib/mysql-connector-java-5.1.2-beta-bin.jar:molgenis/lib/neethi-2.0.4.jar:molgenis/lib/oro-2.0.8.jar:molgenis/lib/postgresql-8.3-603.jdbc4.jar:\
molgenis/lib/quartz-1.6.0.jar:molgenis/lib/selenium-server-standalone-2.19.0.jar:molgenis/lib/serializer-2.7.1.jar:molgenis/lib/slf4j-api-1.6.1.jar:\
molgenis/lib/slf4j-log4j12-1.6.1.jar:molgenis/lib/smtp.jar:molgenis/lib/stax-utils-20060502.jar:molgenis/lib/tar.jar:molgenis/lib/testng-5.14.10.jar:\
molgenis/lib/tjws-1.98.jar:molgenis/lib/validation-api-1.0.0.GA.jar:molgenis/lib/velocity-1.6.4.jar:molgenis/lib/wsdl4j-1.6.2.jar:molgenis/lib/wss4j-1.5.8.jar:\
molgenis/lib/wstx-asl-3.2.8.jar:molgenis/lib/xalan-2.7.1.jar:molgenis/lib/xercesImpl.jar:molgenis/lib/xmlbeans-2.4.0.jar:molgenis/lib/xml-resolver-1.2.jar:\
molgenis/lib/xmlrpc-client-3.1.3.jar:molgenis/lib/xmlrpc-common-3.1.3.jar:molgenis/lib/XmlSchema-1.4.7.jar:molgenis/lib/xmlsec-1.4.3.jar:molgenis/lib/xmltask.jar:\
molgenis/lib/hibernate-validator-4.1.0.Final/hibernate-jpa-2.0-api-1.0.0.Final.jar:molgenis/lib/hibernate-validator-4.1.0.Final/hibernate-validator-4.1.0.Final.jar:\
molgenis/lib/hibernate-validator-4.1.0.Final/log4j-1.2.14.jar:molgenis/lib/hibernate/antlr-2.7.6.jar:\
molgenis/lib/hibernate-validator-4.1.0.Final/validation-api-1.0.0.GA.jar:\
molgenis/lib/hibernate/commons-collections-3.1.jar:molgenis/lib/hibernate/dom4j-1.6.1.jar:molgenis/lib/hibernate/hibernate3.jar:\
molgenis/lib/hibernate/hibernate-jpa-2.0-api-1.0.0.Final.jar:molgenis/lib/hibernate/hibernate-search-3.4.1.Final.jar:\
molgenis/lib/hibernate/javassist-3.12.0.GA.jar:molgenis/lib/hibernate/jta-1.1.jar:slf4j-api-1.6.1.jar \
org.molgenis.compute.test.util.WorksheetImporter -workflow_name %s -worksheet_file %s -McId %s """
	command = command % (os.path.join(molgenis_apps_dir, '..'), os.path.split(workflow_fn)[1], worksheet_fn, run_name)
	print "Running: " + command
	os.system(command)

def import_workflow_to_molgenis(compile_molg = False):
	clean_compute()

	if compile_molg:
		compile_molgenis()

	start_molgenis()
	import_workflow()
	import_worksheet()


def run_command(to_exec = True):
	if molgenis_dir:
		command = ['sh', os.path.join(molgenis_dir, molgenis_script)]
		command += ['-worksheet=' + worksheet_fn]
		command += ['-parameters=' + parameters_fn]
		command += ['-workflow=' + workflow_fn]
		command += ['-protocols=' + protocols_dir]
		command += ['-templates=' + scripts_dir]
		command += ['-scripts=' + os.path.join(scripts_dir, 'molgenis_output')]
		command += ['-id=' + run_id]

		command_line = str.join(' ', command)
		print "---COMMAND LINE:---"
		print command_line
		print "-------------------"
		if to_exec:
			os.system(command_line)
	else:
		print "molgenis_dir is None. Skipping script standalone generation."

	if import_to_molgenis:
		import_workflow_to_molgenis()



if __name__ == '__main__':
	make_scripts()

	if len(sys.argv) > 1 and sys.argv[1] == '0':
		run_command(to_exec=False)
	else:
		run_command()

