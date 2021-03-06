#Get Minimach
#wget http://www.sph.umich.edu/csg/cfuchsb/minimac-beta-2012.8.15.tgz

#tar xvf minimac-beta-2012.8.15.tgz
#srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/byelas/tools/python_scripts/AssemblyImpute2GprobsBins.py
#srmcp -server_mode=passive file:///$HOME/kanterak/AssemblyImpute2GprobsBins.py srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/byelas/tools/python_scripts/AssemblyImpute2GprobsBins.py
#srmls srm://carme.htc.biggrid.nl/dpm/htc.biggrid.nl/home/bbmri.nl/generated/2012-02-24/file61914e6b-ad7d-402b-a4eb-87345b1a257b
#srmls srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/byelas/tools/python_scripts/AssemblyImpute2GprobsBins.py

#srmcp -server_mode=passive file:///$HOME/data/convertGProbs2PEDMAP.py srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/kanterak/tools/python_scripts/convertGProbs2PEDMAP.py
#srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/data_for_mathijs/chr1_0_499

#Root: srmls srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/byelas
#To submit manually a job:
# glite-wms-job-submit  -d $USER -o manual-submit3 $HOME/maverick/maverick.jdl
#To request the status of the submition:
#glite-wms-job-status -i manual-submit2
#To get the output:
#glite-wms-job-output https://wms2.grid.sara.nl:9000/4buFFOeboWEOhwRQ3Tjbrg
#cp -r /scratch/kanterak_p-njjccBwoW293YBtdVyxg .

#Check status:
#glite-wms-job-status -i pilot-one

# Check result: 
# srmls srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/kanterak/groups/ebiobank/projects/imputation/benchmark/results

#To check script output from the database:
#select * from ComputeTask;

#The all.txt file:
#srmls srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/kanterak/groups/ebiobank/projects/imputation/benchmark/all.txt
#Notes:
##        other.GlueCEInfoHostName == "gb-ce-ams.els.sara.nl" ||         # putFile and getFile do not work. Blacklisted in maverick.jdl .

"""
Examples of usage:
python molgenis_helper.py action=compile
python molgenis_helper.py action=restart_server
python molgenis_helper.py action=drop_database
python molgenis_helper.py action=drop_database_restart_server
python molgenis_helper.py action=import_workflow
python molgenis_helper.py action=stop_server

python molgenis_helper.py username=kanterak password=1d1iotmega w:aposterioriThreshold=0.7 action=submit_worksheet_grid run_id=compare_0.7 dummy=True

python molgenis_helper.py pipeline=custom_command action=import_workflow
python molgenis_helper.py pipeline=custom_command action=submit_worksheet_grid username=kanterak password=1d1iotmega run_id=custom_command_module_avail

python molgenis_helper.py pipeline=ConvertTPEDtoBED action=import_workflow p:plinkInput=OUTPUT_0.9 p:plinkOutput=OUTPUT_0.9 dummy=True
python molgenis_helper.py pipeline=ConvertTPEDtoBED action=submit_worksheet_grid username=kanterak password=1d1iotmega run_id=convertTPED_BED_09

python molgenis_helper.py pipeline=SelectRegionFromBED action=import_workflow
python molgenis_helper.py pipeline=SelectRegionFromBED action=submit_worksheet_grid username=kanterak password=1d1iotmega w:plinkInput=OUTPUT_0.9 w:plinkOutput=OUTPUT_0.9 w:fromKB=0 w:toKB=5000 w:chr=1 run_id=SelectRegionFromBED dummy=True

---------------------
minimacV2 Step 1
# python molgenis_helper.py pipeline=minimac_patrickS1 action=import_workflow p:McWorksheet=\$\{root\}/home/akanterakis/worksheets/myProject.csv
# python molgenis_helper.py pipeline=minimac_patrickS1 action=submit_worksheet username=kanterak password=1d1iotmega w:studyInputDir=\$\{root\}/groups/gonl/projects/imputationBenchmarking/goldStandard/celiacNlSelectedSnps/pedmap/ w:prePhasingResultDir=\$\{root\}/groups/gonl/projects/imputationBenchmarking/imputationResult/celiacGoldStandardNl_MinimacV2_refGoNL3.1 run_id=celiacGoldStandardNl_MinimacV2_refGoNL3.1
python molgenis_helper.py pipeline=minimac_patrickS1 action=import_workflow p:remoteWorksheet=\$\{root\}/home/akanterakis/worksheets/myProject.csv 
python molgenis_helper.py pipeline=minimac_patrickS1 action=submit_worksheet_grid username=kanterak password=1d1iotmega w:studyInputDir=\$\{root\}/groups/gonl/projects/imputationBenchmarking/goldStandard/celiacNlSelectedSnps/pedmap/ w:prePhasingResultDir=\$\{root\}/groups/gonl/projects/imputationBenchmarking/imputationResult/celiacGoldStandardNl_MinimacV2_refGoNL3.1 run_id=celiacGoldStandardNl_MinimacV2_refGoNL3.1_S1
# Fetch worksheet (CHANGE TMP VALUE!):
python molgenis_helper.py action=fetch_from_grid username=kanterak password=1d1iotmega grid_path=groups/gonl/projects/imputationBenchmarking/imputationResult/celiacGoldStandardNl_MinimacV2_refGoNL3.1/tmp/ChunkChr20Worksheet.csv ui_path=/home/kanterak/worksheets/ChunkChr20Worksheet.csv local_path=/srv/molgenis/alex/scripts/worksheets/ChunkChr20Worksheet.csv

minimacV2 Step 2
python molgenis_helper.py pipeline=minimac_patrickS2 action=import_workflow
python molgenis_helper.py pipeline=minimac_patrickS2 action=submit_worksheet_grid username=kanterak password=1d1iotmega run_id=celiacGoldStandardNl_MinimacV2_refGoNL3.1_S2

minimacV2 Step 3
# sh /srv/molgenis/compute/molgenis_apps/modules/compute/protocols/imputation/minimacV2/add_variable.sh -w /srv/molgenis/alex/scripts/worksheets/ChunkChr20Worksheet.csv -v imputationResultDir -p \$\{root\}/groups/gonl/projects/imputationBenchmarking/imputationResult/celiacGoldStandardNl_MinimacV2_refGoNL3.1 -o /srv/molgenis/alex/scripts/worksheets/tmp_imputationWorksheet.csv
# sh /srv/molgenis/compute/molgenis_apps/modules/compute/protocols/imputation/minimacV2/add_variable.sh -w /srv/molgenis/alex/scripts/worksheets/tmp_imputationWorksheet.csv -v referencePanel -p gonl_release3.1 -o /srv/molgenis/alex/scripts/worksheets/imputationWorksheet.csv
python molgenis_helper.py pipeline=minimac_patrickS3 action=import_workflow
python molgenis_helper.py pipeline=minimac_patrickS3 action=submit_worksheet_grid username=kanterak password=1d1iotmega run_id=celiacGoldStandardNl_MinimacV2_refGoNL3.1_S3
---------------------
NGS pipeline
python molgenis_helper.py pipeline=ngs action=import_workflow
python molgenis_helper.py pipeline=ngs action=import_worksheet run_id=test1
---------------------
"""

"""
#Login to molgenis18:
ssh akanterakis@proxy.gcc.rug.nl

ssh molgenis18

#Pull from blessed: molgenis_ass testing
git pull https://github.com/molgenis/molgenis_apps.git testing

To make standalone
ant -f build_compute.xml makedistro

# Drop database
echo 'DROP DATABASE IF EXISTS compute; CREATE DATABASE compute;' | mysql -u molgenis -pmolgenis

#Import workflow
sh molgenis_apps/modules/compute4/deployment/importWorkflow.sh molgenis_apps/modules/compute/protocols/imputation/minimacV2/parametersMinimac.csv molgenis_apps/modules/compute/protocols/imputation/minimacV2/workflowMinimacStage1.csv molgenis_apps/modules/compute/protocols/imputation/minimacV2/protocols/

#A samples worksheet:
project,studyInputDir,prePhasingResultDir,imputationPipeline,genomeBuild,chr,remoteWorksheet,autostart
hapmapCEUr22b37,${root}/groups/gonl/projects/imputationBenchmarking/goldStandard/celiacNlSelectedSnps/pedmap/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/celiacGoldStandardNl_MinimacV2_refGoNL3.1,minimac,b37,20,${root}/home/akanterakis/worksheets/worksheet_S1.csv,FALSE

#Copy to ui:
scp /srv/molgenis/compute/molgenis_apps/modules/compute/protocols/imputation/minimacV2/worksheet_S1.csv kanterak@ui.grid.sara.nl:/home/kanterak/tmptransfer/worksheet_S1.csv

#cp to srm:
srmcp -server_mode=passive file:////home/kanterak/tmptransfer/worksheet_S1.csv srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/RP2/home/akanterakis/worksheets/worksheet_S1.csv

#Import worksheet. Step 1
sh molgenis_apps/modules/compute4/deployment/importWorksheet.sh workflowMinimacStage1.csv ui.grid.sara.nl molgenis_apps/modules/compute/protocols/imputation/minimacV2/worksheet_S1.csv step01

#Submit to grid
sh molgenis_apps/modules/compute4/deployment/runPilots.sh ui.grid.sara.nl kanterak 1d1iotmega grid


am90-17.gina.sara.nl:
am91-17.gina.sara.nl
module load jdk/1.6.0_33
java -version

Error occurred during initialization of VM
Could not reserve enough space for object heap
Could not create the Java virtual machine.

State-> from Generated to Ready

#Fetch generated worksheet
srmcp -server_mode=passive srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/RP2/home/fvandijk/minimacV2fulltest5/prePhasingResult/generatedJobs/../concattedChunkWorksheet.csv file:////home/kanterak/worksheets/concattedChunkWorksheet.csv
scp kanterak@ui.grid.sara.nl:/home/kanterak/worksheets/concattedChunkWorksheet.csv molgenis_apps/modules/compute/protocols/imputation/minimacV2/concattedChunkWorksheet.csv

#Import forkflow step 2
sh molgenis_apps/modules/compute4/deployment/importWorkflow.sh molgenis_apps/modules/compute/protocols/imputation/minimacV2/parametersMinimac.csv molgenis_apps/modules/compute/protocols/imputation/minimacV2/workflowMinimacStage2.csv molgenis_apps/modules/compute/protocols/imputation/minimacV2/protocols/

#Import worksheet step 2
sh molgenis_apps/modules/compute4/deployment/importWorksheet.sh workflowMinimacStage2.csv ui.grid.sara.nl molgenis_apps/modules/compute/protocols/imputation/minimacV2/concattedChunkWorksheet.csv step02

#Submit to grid
sh molgenis_apps/modules/compute4/deployment/runPilots.sh ui.grid.sara.nl kanterak 1d1iotmega grid

#Import workflow step 3
sh molgenis_apps/modules/compute4/deployment/importWorkflow.sh molgenis_apps/modules/compute/protocols/imputation/minimacV2/parametersMinimac.csv molgenis_apps/modules/compute/protocols/imputation/minimacV2/workflowMinimacStage3.csv molgenis_apps/modules/compute/protocols/imputation/minimacV2/protocols/

#Fix step3 worksheet
sh /srv/molgenis/compute/molgenis_apps/modules/compute/protocols/imputation/minimacV2/add_variable.sh -w molgenis_apps/modules/compute/protocols/imputation/minimacV2/concattedChunkWorksheet.csv -v imputationResultDir -p \$\{root\}/groups/gonl/projects/imputationBenchmarking/imputationResult/celiacGoldStandardNl_MinimacV2_refGoNL3.1 -o molgenis_apps/modules/compute/protocols/imputation/minimacV2/tmp_imputationWorksheet.csv
sh /srv/molgenis/compute/molgenis_apps/modules/compute/protocols/imputation/minimacV2/add_variable.sh -w molgenis_apps/modules/compute/protocols/imputation/minimacV2/tmp_imputationWorksheet.csv -v referencePanel -p gonl_release3.1 -o molgenis_apps/modules/compute/protocols/imputation/minimacV2/imputationWorksheet_S3.csv

#Import worksheet step 3
sh molgenis_apps/modules/compute4/deployment/importWorksheet.sh workflowMinimacStage3.csv ui.grid.sara.nl molgenis_apps/modules/compute/protocols/imputation/minimacV2/imputationWorksheet_S3.csv step03

#Submit to grid
sh molgenis_apps/modules/compute4/deployment/runPilots.sh ui.grid.sara.nl kanterak 1d1iotmega grid
"""

import os
import re
import sys
import random
import urllib2

def get_param(name, arguments, default):

	for argument in arguments:
		found = re.search(r'%s=(.*)' % (name), argument)
		if found:
			return found.group(1)

	return default

#pipeline = 'minimac'
#pipeline = 'beagle'
#pipeline = 'compare_grid'

pipeline = get_param('pipeline', sys.argv, None)

#environment = 'gpfs'
#environment = 'macbookair'
#environment = 'vm'

environment = get_param('environment', sys.argv, 'vm')

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

def fetch_file(path):
	print "Fetching: " + path
	fp = open(path)
	ret = fp.read()
	fp.close()
	return ret

def fetch_grid_file(path):
	print "Fetching from Grid:" + path


def fetch_page_l(url):
	return lambda : fetch_page(url)

def fetch_file_l(path):
	return lambda : fetch_file(path)

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
elif environment == 'hudson':
	molgenis_dir = None
	molgenis_apps_dir = '/data/hudson/jobs/molgenis_compute_imputation_pipeline/workspace/molgenis_apps'
	import_to_molgenies = True
else:
	raise Exception('Unknown value for environment variable: ' + str(environment))

molgenis_script = 'molgenis_compute.sh'

#Script specific parameters
run_id = 'run_01'

if environment == 'vm':
	scripts_dir_stem = '/srv/molgenis/alex/runs'
elif environment == 'gpfs':
	scripts_dir_stem = '/target/gpfs2/gcc/home/akanterakis/runs'
elif environment == 'macbookair':
	scripts_dir_stem = '/Users/alexandroskanterakis/runs'
elif environment == 'hudson':
	scripts_dir_stem = '/data/hudson/jobs/molgenis_compute_imputation_pipeline/workspace/runs'
else:
	raise Exception('Unknown value for environment variable: ' ,str(environment))

if pipeline:
	scripts_dir = os.path.join(scripts_dir_stem, pipeline)

if pipeline == 'minimac':
	scripts_dir = '/target/gpfs2/gcc/home/akanterakis/runs/Mach_5_Sep_2012/mach_minimach'
	workflow_name = 'workflowMachMinimac'
	worksheet = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/mach_minimach/worksheet_example.csv')
	workflow = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/mach_minimach/workflowMachMinimac.csv')
	parameters = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/mach_minimach/parameters.csv')
elif pipeline == 'minimac_patrickS1':
	workflow_name = 'workflow_minimac_PatrickS1'
#	worksheet = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/minimacV2/worksheet.csv')
	worksheet = fetch_file_l('/srv/molgenis/alex/scripts/worksheets/worksheet_minimacV2_S1.csv')
	workflow = fetch_page_l('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/imputation/minimacV2/workflowMinimacStage1.csv')
	parameters = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/minimacV2/parametersMinimac.csv')
elif pipeline == 'minimac_patrickS2':
	workflow_name = 'workflow_minimac_patrickS2'
	worksheet = fetch_file_l('/srv/molgenis/alex/scripts/worksheets/ChunkChr20Worksheet.csv')
	workflow = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/minimacV2/workflowMinimacStage2.csv')
	parameters = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/minimacV2/parametersMinimac.csv')
elif pipeline == 'minimac_patrickS3':
	workflow_name = 'workflow_minimac_patrickS3'
#	worksheet = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/minimacV2/imputationWorksheet.csv')
	worksheet = fetch_file_l('/srv/molgenis/alex/scripts/worksheets/imputationWorksheet.csv')
	workflow = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/minimacV2/workflowMinimacStage3.csv')
	parameters = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/minimacV2/parametersMinimac.csv')
elif pipeline == 'ngs':
	workflow_name = 'ngs'
	worksheet = fetch_page_l('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/ngsWorkflowRealignmentAndSnpCalling/demoWorksheet.csv')
	workflow = fetch_page_l('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/ngsWorkflowRealignmentAndSnpCalling/workflow.csv')
	parameters = fetch_page_l('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/ngsWorkflowRealignmentAndSnpCalling/parameters.csv')
	protocols_dir_git = 'https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/ngsWorkflowRealignmentAndSnpCalling/protocols'
elif pipeline == 'beagle':
	scripts_dir = '/target/gpfs2/gcc/home/akanterakis/runs/Beagle_19_Sep_2012/beagle/'
	workflow_name = 'workflowBeagle'
	worksheet = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/beagle/worksheet_example.csv')
	workflow = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/beagle/workflowBeagle.csv')
	parameters = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/mach_minimach/parameters.csv')
elif pipeline == 'compare_grid':

	#workflow_name = 'workflowComparison' # Step 1
	workflow_name = 'workflowComparison_step2' # Step 2

	worksheet = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/worksheet_example.csv')

	#workflow = fetch_page('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/workflowComparison.csv') # Step 1
	workflow = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/workflowComparison_step2.csv') # Step 2

	parameters = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/parameters.csv')
elif pipeline == 'custom_command':
	workflow_name = 'customCommand'
	worksheet = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/worksheet_example.csv')
	workflow = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/workflows/Runcommand.csv')
	parameters = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/parameters.csv')
elif pipeline == 'ConvertTPEDtoBED':
	workflow_name = 'ConvertTPEDtoBED'
	worksheet = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/workflows/ConvertTPEDtoBED_worksheet.csv')
	workflow = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/workflows/ConvertTPEDtoBED.csv')
	parameters = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/parameters.csv')
elif pipeline == 'SelectRegionFromBED':
	workflow_name = 'SelectRegionFromBED'
	worksheet = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/workflows/SelectRegionFromBED_worksheet.csv')
	workflow = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/workflows/SelectRegionFromBED.csv')
	parameters = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/parameters.csv')
elif pipeline == 'PlinkBEDConcordance':
	workflow_name = 'PlinkBEDConcordance'
	worksheet = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/workflows/PlinkBEDConcordance_worksheet.csv')
	workflow = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/workflows/PlinkBEDConcordance.csv')
	parameters = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/parameters.csv')
elif pipeline == 'RecodeAllelesACGT':
	workflow_name = 'RecodeAllelesACGT'
	worksheet = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/workflows/RecodeAllelesACGT_worksheet.csv')
	workflow = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/workflows/RecodeAllelesACGT.csv')
	parameters = fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/parameters.csv')

if pipeline:
	protocols_dir = os.path.join(scripts_dir, 'protocols')

def substitute_parameter(parameter_name, new_value, parameters_content):
	return re.sub(r'%s,[\w\-\/\.]*,' % (parameter_name), r'%s,%s,' % (parameter_name, new_value), parameters_content)

def substitute_parameters(parameters_content):
	#Substitue clusterQueue, scheduler
	new_parameters = str(parameters_content)
	new_parameters = substitute_parameter('clusterQueue', queue, new_parameters)
	new_parameters = substitute_parameter('scheduler', scheduler, new_parameters)

	if scheduler == 'GRID':
		new_parameters = substitute_parameter('root', '$WORKDIR', new_parameters)

	return new_parameters


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

#Compare imputation bins created by impute2
protocol_concatImputationResults = {
	"name" : 'concatImputationResults',
	"content" : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/concatImputationResults.ftl')
}

protocol_convertGProbs2PEDMAP = {
	"name" : 'convertGProbs2PEDMAP',
	"content" : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/comparison/convertGProbs2PEDMAP.ftl')
}

#Custom command
protocol_Runcommand = {
	'name' : 'Runcommand',
	'content' : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/Runcommand.ftl')
}

#Convert TPED to BED
protocol_ConvertTPEDtoBED = {
	'name' : 'ConvertTPEDtoBED',
	'content' : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/ConvertTPEDtoBED.ftl')
}

#Select region from BED
protocol_SelectRegionFromBED = {
	'name' : 'SelectRegionFromBED',
	'content' : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/SelectRegionFromBED.ftl')
}

#Get the concordance between two BED file-sets with plink
protocol_PlinkBEDConcordance = {
	'name' : 'PlinkBEDConcordance',
	'content' : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/PlinkBEDConcordance.ftl')
}

#Change allele codings from 1,2,3,4 to A,C,G,T with plink
protocol_RecodeAllelesACGT = {
	'name' : 'RecodeAllelesACGT',
	'content' : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/RecodeAllelesACGT.ftl')
}

#prepare Ped MAP for Imputation tool
protocol_preparePedMapForImputationTool = {
	'name' : 'preparePedMapForImputationTool',
	'content' : fetch_page_l('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/imputation/minimac/protocols/preparePedMapForImputationTool.ftl')
}

protocol_convertPedMapToTriTyper = {
	'name' : 'convertPedMapToTriTyper',
	'content' : fetch_page_l('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/imputation/minimac/protocols/convertPedMapToTriTyper.ftl')
}

# minimac_party. MinimacV2
protocol_prepareStudy = {
	'name' : 'prepareStudy',
	#Molgenis tesint repo
#	'content' : fetch_page_l('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/imputation/minimacV2/protocols/prepareStudy.ftl')

	#Kantale's repo
	'content' : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/minimacV2/protocols/prepareStudy.ftl')
}

protocol_convertPlinkPedMapToMerlin = {
	'name' : 'convertPlinkPedMapToMerlin',
	'content' : fetch_page_l('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/imputation/minimac/protocols/convertPlinkPedMapToMerlin.ftl')
}

protocol_chunkChromosome = {
	'name' : 'chunkChromosome',
	'content' : fetch_page_l('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/imputation/minimac/protocols/chunkChromosome.ftl')
}

# for pipeline: minimac_party. MinimacV2
protocol_startMinimacStage2 = {
	'name' : 'startMinimacStage2',
	'content' : fetch_page_l('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/imputation/minimacV2/protocols/startMinimacStage2.ftl')
}

protocol_phaseChunk = {
	'name' : 'phaseChunk',
	'content' : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/minimacV2/protocols/phaseChunk.ftl')
}

protocol_minimacImputation = {
	'name' : 'minimacImputation',
	'content' : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/minimacV2/protocols/minimacImputation.ftl'),
}

protocol_mergeMinimacImputationResults = {
	'name' : 'mergeMinimacImputationResults',
	'content' : fetch_page_l('https://raw.github.com/kantale/molgenis_apps/master/modules/compute/protocols/imputation/minimacV2/protocols/mergeMinimacImputationResults.ftl'),
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

elif pipeline == 'minimac_patrickS1':
	protocols = [
		protocol_prepareStudy,
		protocol_startMinimacStage2,
	]
elif pipeline == 'minimac_patrickS2':
	protocols = [
		protocol_phaseChunk,
	]
elif pipeline == 'minimac_patrickS3':
	protocols = [
		protocol_minimacImputation,
		protocol_mergeMinimacImputationResults,
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
#		protocol_concatImputationResults, # Step 1
		protocol_convertGProbs2PEDMAP, # Step 2
	]
elif pipeline == 'custom_command':
	protocols = [
		protocol_Runcommand,
	]

elif pipeline == 'ConvertTPEDtoBED':
	protocols = [
		protocol_ConvertTPEDtoBED,
	]

elif pipeline == 'SelectRegionFromBED':
	protocols = [
		protocol_SelectRegionFromBED,
	]

elif pipeline == 'PlinkBEDConcordance':
	protocols = [
		protocol_PlinkBEDConcordance,
	]

elif pipeline == 'RecodeAllelesACGT':
	protocols = [
		protocol_RecodeAllelesACGT,
	]
else:
	protocols = None


#####################################################################
########## NO NEED TO EDIT FROM THAT POINT ##########################
#####################################################################
if pipeline:
	worksheet_fn = os.path.join(scripts_dir, project_name + '.csv')
	parameters_fn = os.path.join(scripts_dir, parameters_name + '.csv')
	workflow_fn = os.path.join(scripts_dir, workflow_name + '.csv')

#TODO! Make ftl files in scripts_dir

def exec_command(command, dummy=False, exit_if_problem=True, verbose=True):
	if verbose:
		print 'Running:', command
	if not dummy:
		return_code = os.system(command)
		if return_code:
			if verbose:
				print "Received error code: ", return_code
			if exit_if_problem:
				if return_code > 255: #Check: http://stackoverflow.com/questions/179565/exitcodes-bigger-than-255-possible
					return_code = 1
				if verbose:
					print "Exiting.."
				sys.exit(return_code)

def remove_empty_lines(text):
	return str.join('\n', [x for x in text.split('\n') if len(x) > 0])

def make_scripts(custom_parameters, custom_worksheet_parameters, dummy=False):

	global protocols

	if not dummy:
		#Check scripts directory
		if not os.path.exists(scripts_dir):
			os.mkdir(scripts_dir)

		if not os.path.exists(protocols_dir):
			os.mkdir(protocols_dir)

	#Get worksheet
	worksheet_nl = remove_empty_lines(worksheet())

	#Set custom worksheet parameters
	for param in custom_worksheet_parameters:
		worksheet_nl_s =  worksheet_nl.split('\n')
		
		try:
			param_index = worksheet_nl_s[0].split(',').index(param)
		except ValueError:
			raise Exception('%s is not in the worksheet' % param)

		substituted_s = [y[0:param_index] + [custom_worksheet_parameters[param]] + y[param_index+1:] for y in [x.split(',') for x in worksheet_nl_s[1:]]]
		worksheet_nl = '\n'.join([worksheet_nl_s[0]] + [','.join(x) for x in  substituted_s])
		if dummy:
			print "worksheet:"
			print worksheet_nl

	#Save worksheet
	if not dummy:
		open(worksheet_fn, 'w').write(worksheet_nl + '\n')
	print "Save worksheet to:", worksheet_fn

	#Remove empty lines of parameters
	parameters_nl = remove_empty_lines(parameters())

	#Do essential standard substitutions
	parameters_nl = substitute_parameters(parameters_nl)

	#Place user parameters
	for param in custom_parameters:
		parameters_nl = substitute_parameter(param, custom_parameters[param], parameters_nl)

	#Save parameters
	if not dummy:
		open(parameters_fn, 'w').write(parameters_nl + '\n')
	print "Saved parameters to:", parameters_fn

	#Remove empty lines of workflow
	workflow_nl = remove_empty_lines(workflow())

	#Save workflow
	if not dummy:
		open(workflow_fn, 'w').write(workflow_nl + '\n')
	print "Saved workflow to:", workflow_fn

	#If protocols have not defined. Build from protocols_dir_git
	if not protocols:
		protocols = [{'name': y, 'content' : fetch_page_l(os.path.join(protocols_dir_git, y+'.ftl'))} for y in [x.split(',')[1] for x in workflow_nl.split('\n')[1:]]]

	#Save protocols
	for protocol in protocols:
		protocol_fn = os.path.join(protocols_dir, protocol['name'] + '.ftl')
		if not dummy:
			open(protocol_fn, 'w').write(protocol['content']() + '\n')
		print "Saved protocol: %s to %s" % (protocol['name'], protocol_fn)

	#Necessary files
	if not dummy:
		open(os.path.join(protocols_dir, 'Header.ftl'), 'w').write(fetch_page('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/imputation/impute2/protocols/Header.ftl'))
		open(os.path.join(protocols_dir, 'Footer.ftl'), 'w').write(fetch_page('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/imputation/impute2/protocols/Footer.ftl'))
		open(os.path.join(protocols_dir, 'CustomSubmit.sh.ftl'), 'w')
		open(os.path.join(protocols_dir, 'Macros.ftl'), 'w').write(fetch_page('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/imputation/impute2/protocols/Macros.ftl'))
		open(os.path.join(protocols_dir, 'Helpers.ftl'), 'w').write(fetch_page('https://raw.github.com/molgenis/molgenis_apps/testing/modules/compute/protocols/imputation/impute2/protocols/Helpers.ftl'))


def clean_compute(dummy=False):
	command = "echo 'DROP DATABASE IF EXISTS compute; CREATE DATABASE compute;' | mysql -u molgenis -pmolgenis"
	print "Running: " + command
	if not dummy:
		os.system(command)

def compile_molgenis(dummy=False):
	exec_command("cd %s; ant -f build_compute.xml clean-generate-compile" % (molgenis_apps_dir), dummy)

	#After compile. Change persistence.xml.
	#build/classes/META-INF/persistence.xml
	exec_command("cd %s; sed -i 's/validate/update/g' build/classes/META-INF/persistence.xml" % (molgenis_apps_dir), dummy)

#	exec_command("cd %s; sed -i 's/innodb_autoinc_lock_mode=2?//g' build/classes/META-INF/persistence.xml" % (molgenis_apps_dir), dummy)

def stop_molgenis(dummy = False):
	if environment == 'vm':
		exec_command("kill `ps aux | grep ant-launcher | grep -v grep | cut -d ' ' -f 2`", dummy, exit_if_problem = False) # This doesn't always work
		exec_command("kill `ps aux | grep ant-launcher | grep -v grep | cut -d ' ' -f 3`", dummy, exit_if_problem = False) # So we are running this as well
		exec_command("kill `ps aux | grep ant-launcher | grep -v grep | cut -d ' ' -f 4`", dummy, exit_if_problem = False) # So we are running this as well
	else:
		exec_command("kill -9 `lsof -i :%i -t`" % (port), dummy, exit_if_problem = False)

def start_molgenis(port = 8080, dummy=False):

	stop_molgenis(dummy)

	#Move nohup in a new file
	hash_string = "%032x" % random.getrandbits(128)
	command = 'mv %s/nohup.out %s/nohup.out.%s' % (molgenis_apps_dir, molgenis_apps_dir, hash_string)
	exec_command(command, dummy)

	exec_command("cd %s; nohup ant -f build_compute.xml runOn -Dport=%i & " % (molgenis_apps_dir, port), dummy)

	print "Waiting for molgenis to start up.."
	exec_command("sleep 4", dummy)
	print "ok"

def ssh_command(
	username = None,
	host = None,
	password = None,
	remote_commands = None,
	verbose = False,
	):

	actions = [
		('spawn', 'ssh %s@%s' % (username, host)),
		('expect', "%s@%s's password:" % (username, host)),
		('send_password', password),
		('expect', '%s> $' % (username)),
	]

	for remote_command in remote_commands:
		actions += [('send', remote_command)]
		actions += [('expect', r'> $')]
		actions += [('print_output', None)]

	actions += [('send', 'logout')]

	Execute_pexpect_list(actions, verbose=verbose)

def scp_files(
	username = None,
	host = None,
	password = None,
	remote_dir = None,
	local_filenames = None,
	verbose = False,
	):

	actions = [
		('spawn', 'sftp %s@%s' % (username, host)),
		('expect', "%s@%s's password:" % (username, host)),
		('send_password', password),
		('expect', 'ftp> '),
		('send', 'cd %s' % (remote_dir)),
		('expect', 'ftp> '),
		]

	for local_filename in local_filenames:
		actions += [('send', 'put %s' % (local_filename))]
		actions += [('expect', 'ftp> ')]

	actions += [('send', 'bye')]

	Execute_pexpect_list(actions, verbose=verbose)

def scp_file_to_local(
	username = None,
	host = None,
	password = None,
	remote_dirs = None,
	remote_filenames = None,
	local_paths = None,
	verbose = False,
	):

	actions = [
		('spawn', 'sftp %s@%s' % (username, host)),
		('expect', "%s@%s's password:" % (username, host)),
		('send_password', password),
		('expect', 'ftp> '),
	]

	for remote_dir, remote_filename, local_path in zip(remote_dirs, remote_filenames, local_paths):
		actions += [('send', 'cd %s' % (remote_dir))]
		actions += [('expect', 'ftp> ')]
		actions += [('send', 'get %s' % (remote_filename))]
		actions += [('expect', 'ftp> ')]
		actions += [('local_action', 'mv %s %s' % (remote_filename, local_path))]

	actions += [('send', 'bye')]

	Execute_pexpect_list(actions, verbose=verbose)

def Execute_pexpect_list(
	actions,
	method = 'pexpect',
	verbose = False,
):

	def this_print(msg):
		if verbose:
			print msg

	try:
		import pexpect
	except ImportError as inst:
		print "pexpect has not been installed. Refer to http://www.noah.org/wiki/Pexpect#Download_and_Installation to download and install"
		raise inst

	for action in actions:
		if action[0] == 'spawn':
			this_print('Spawning: ' + action[1])
			child = pexpect.spawn(action[1])
		elif action[0] == 'expect':
			this_print('Expecting: ' + action[1])
			child.expect(action[1])
		elif action[0] == 'send_password':
			this_print('Sending password')
			child.sendline(action[1])
		elif action[0] == 'send':
			this_print('Sending: ' + action[1])
			child.sendline(action[1])
		elif action[0] == 'print_output':
			this_print('Received:')
			print child.before
		elif action[0] == 'local_action':
			this_print('Running locally: ' + action[1])
			exec_command(action[1], verbose=verbose)
		else:
			raise Exception('Invalid action: ' + str(action[0]))


def import_workflow(dummy=False):
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
molgenis/lib/hibernate/javassist-3.12.0.GA.jar:molgenis/lib/hibernate/jta-1.1.jar:slf4j-api-1.6.1.jar:\
molgenis/lib/hibernate/c3p0-0.9.1.jar \
org.molgenis.compute.db.util.WorkflowImporterJPA %s %s %s """

	if environment == 'hudson':
		command = command.replace('molgenis/lib/hibernate/c3p0-0.9.1.jar', 'molgenis_apps/WebContent/WEB-INF/lib/c3p0.jar')

	command = command % (os.path.join(molgenis_apps_dir, '..'), parameters_fn, workflow_fn, protocols_dir)
	print "Importing workflow.."
	exec_command(command, dummy)

def import_worksheet(run_name = 'test_001', dummy = False):
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
molgenis/lib/hibernate/c3p0-0.9.1.jar:\
molgenis/lib/hibernate/javassist-3.12.0.GA.jar:molgenis/lib/hibernate/jta-1.1.jar:slf4j-api-1.6.1.jar \
org.molgenis.compute.db.util.WorksheetImporter -workflow_name %s -backend_name %s -worksheet_file %s -McId %s """
	#Change RUN_ID!
	command = command % (os.path.join(molgenis_apps_dir, '..'), os.path.split(workflow_fn)[1], 'ui.grid.sara.nl', worksheet_fn, run_name) 
	print "Import worksheet.."
	exec_command(command, dummy)

def submit_script_to_grid(username, password, dummy=False):

	print 'Copying worksheet to ui..'
	scp_files(username, 'ui.grid.sara.nl', password, '/home/kanterak/worksheets', [worksheet_fn], verbose = True)

	worksheet_fn_lastfile = os.path.split(worksheet_fn)[1]

	remote_commands = [
		'srmrm %s' % (os.path.join('srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/RP2/home/akanterakis/worksheets', worksheet_fn_lastfile)),
		'srmcp -server_mode=passive %s %s' % (os.path.join('file:////home/kanterak/worksheets', worksheet_fn_lastfile), os.path.join('srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/RP2/home/akanterakis/worksheets', worksheet_fn_lastfile)),
	]

	ssh_command(username, 'ui.grid.sara.nl', password, remote_commands, verbose = True)

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
molgenis/lib/hibernate/c3p0-0.9.1.jar:\
molgenis/lib/hibernate/javassist-3.12.0.GA.jar:molgenis/lib/hibernate/jta-1.1.jar:slf4j-api-1.6.1.jar \
org.molgenis.compute.db.RunPilotsOnBackEnd %s %s %s %s"""

	command = command % (os.path.join(molgenis_apps_dir, '..'), 'ui.grid.sara.nl', username, password, 'grid')
	print 'Submit script to grid..'
	exec_command(command, dummy)

def import_workflow_to_molgenis(compile_molg = False, username = None, password = None, run_name = None, dummy=False):
	clean_compute(dummy)

	if compile_molg:
		compile_molgenis(dummy)

	start_molgenis(dummy)
	import_workflow(dummy)
	import_worksheet(run_name, dummy=dummy)
	submit_script_to_grid(username, password, dummy=dummy)

def run_command(username=None, password=None, to_exec = True, compile_molg = False, run_name=None, dummy=False):
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
		import_workflow_to_molgenis(compile_molg = compile_molg, username=username, password=password, run_name = None, dummy=dummy)

def check_run_name(run_name):
	if not run_name:
		raise Exception('Could not find parameter: run_id')

def check_username_password(username, password):
	if not username or not password:
		raise Exception('Please define username and password in arguments')

if __name__ == '__main__':

	username, password, to_exec, compile_molg, action = None, None, True, False, 'default' 
	run_name = None
	dummy = False

	username = get_param('username', sys.argv, None)
	password = get_param('password', sys.argv, None)
	grid_host = get_param('grid_host', sys.argv, None)
	to_exec  = eval(get_param('to_exec' , sys.argv, 'True'))
	compile_molg = eval(get_param('compile_molg', sys.argv, 'False'))
	action = get_param('action', sys.argv, None)
	run_name = get_param('run_id', sys.argv, None)
	dummy = eval(get_param('dummy', sys.argv, 'False'))

	#Get custom parameters:
	custom_parameters = {}
	custom_worksheet_parameters = {}
	for argument in sys.argv:
		found_p = re.search(r'p:([\w]*)=([\/\$\{\}\w\.\-]*)', argument)
		found_w = re.search(r'w:([\w]*)=([\/\$\{\}\w\.\-]*)', argument)
		if found_p:
			print 'Found custom parameter: %s = %s' % (found_p.group(1), found_p.group(2))
			custom_parameters[found_p.group(1)] = found_p.group(2)
		if found_w:
			print 'Found worksheet custom parameter: %s = %s' % (found_w.group(1), found_w.group(2))
			custom_worksheet_parameters[found_w.group(1)] = found_w.group(2)

 
	if action == 'default':
		check_username_password(username, password)
		check_run_name(run_name)

		#Generate workflow's script
		make_scripts(custom_parameters, custom_worksheet_parameters, dummy=dummy)

		run_command(username=username, password=password, to_exec=to_exec, compile_molg = compile_molg, run_name = run_name, dummy = dummy)

	elif action == 'drop_database':
		clean_compute(dummy)

	elif action == 'import_workflow':
		make_scripts(custom_parameters, custom_worksheet_parameters, dummy=dummy)
		import_workflow(dummy)

	elif action == 'stop_server':
		stop_molgenis(dummy = dummy)

	elif action == 'restart_server' or action == 'start_molgenis':
		start_molgenis(dummy = dummy)

	elif action == 'drop_database_restart_server':
		clean_compute(dummy)
		start_molgenis(dummy = dummy)

	elif action == 'submit_worksheet' or action=='import_worksheet':
		check_run_name(run_name)
		make_scripts(custom_parameters, custom_worksheet_parameters, dummy=dummy)
		import_worksheet(run_name, dummy = dummy)

	elif action == 'compile':
		compile_molgenis(dummy)

	elif action == 'submit_grid':
		check_username_password(username, password)
		check_run_name(run_name)
		make_scripts(custom_parameters, custom_worksheet_parameters, dummy=dummy)

		submit_script_to_grid(username, password, dummy = dummy)

	elif action == 'submit_worksheet_grid':
		check_username_password(username, password)
		check_run_name(run_name)
		make_scripts(custom_parameters, custom_worksheet_parameters, dummy=dummy)

		import_worksheet(run_name, dummy = dummy)
		submit_script_to_grid(username, password, dummy = dummy)

	elif action == 'fetch_from_grid':
		check_username_password(username, password)
		grid_path = get_param('grid_path', sys.argv, None)
		ui_path = get_param('ui_path', sys.argv, None)
		local_path = get_param('local_path', sys.argv, None)
		ui_path_1, ui_path_2 = os.path.split(ui_path)
		remote_commands = [
			'cd /home/kanterak/worksheets',
			'srmcp -server_mode=passive %s %s' % (os.path.join('srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/RP2', grid_path), os.path.join('file:///%s' % (ui_path)))
		]
		ssh_command(username, 'ui.grid.sara.nl', password, remote_commands, verbose = True)

		scp_file_to_local(username, 'ui.grid.sara.nl', password, [ui_path_1], [ui_path_2], [local_path], verbose=True)

	else:
		raise Exception('Unknown action:', action)


