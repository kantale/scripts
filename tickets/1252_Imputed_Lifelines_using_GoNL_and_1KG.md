http://www.molgenis.org/ticket/1252

### Resources:
*  Documentation for molgenis compute imputation:
    * https://github.com/kantale/molgenis_apps/blob/master/doc/compute/02_compute_imputation.md

### Actions:
* Locate GoNL version 4 data  
/target/gpfs2/gcc/groups/gonl/resources/imputationReference/gonl_release4/vcf/

* Locate Lifelines Data  
/target/gpfs2/gcc/groups/gcc/projects/lifelines-imputation/liftover_to_b37

* Locate command line molgenis  
/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6
The symlink in the tools/molgenis_compute4 directory is outdated
We are using the "0a00dd6" version because Freerk has used this to do the Prevend imputation
Check: /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/prevend_MinimacV2_refGiant1000gv3.20101123/createPhasingScripts.sh

* Locate protools  
/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2

* Locate / Create results directory:
/target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4

* Create worksheet  
Example from examplePrePhasingWorksheet.csv:

.

    project,studyInputDir,prePhasingResultDir,imputationPipeline,genomeBuild,chr,autostart
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,1,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,2,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,3,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,4,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,5,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,6,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,7,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,8,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,9,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,10,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,11,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,12,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,13,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,14,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,15,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,16,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,17,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,18,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,19,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,20,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,21,FALSE
    lifelines_gonl,${root}/groups/gcc/projects/lifelines-imputation/liftover_to_b37,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4,minimac,b37,22,FALSE

Saved at:
/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/worksheet.csv

* Make command line  
sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh \
   -inputdir=input
   -outputdir=input/output
   -mcdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6
   -workflow=input/workflow.csv
   -protocols=input/protocols
   -parameters=input/parameters.csv
   -worksheet=input/worksheet.csv
   -id=output  

    What are the inputdir and outputdir parameters?
email sent: https://mail.google.com/mail/ca/?shva=1#sent/13c1b09610d553c9

Command line:

    sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh -inputdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/ -outputdir=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/scripts -workflow=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/workflowMinimacStage1.csv -protocols=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/protocols/ -parameters=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/parametersMinimac.csv -worksheet=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/worksheet.csv -id=lifelines

* Generate scripts.  
Locations: /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/scripts  
Submit: sh submit.sh

WAITING FOR END OF STEP 1 in CLUSTER. Cluster down for maintenance. Job finished.

* Step 2 of workflow. (Imputation step)  
Running:

.

    import os
    a = 'sh protocols/imputation/minimacV2/add_variable.sh -w /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr%iChunkWorksheet.csv -v imputationResultDir -p /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/ -o /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr%iImputationWorksheet.csv'
    b = 'sh protocols/imputation/minimacV2/add_variable.sh -w /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr%iImputationWorksheet.csv -v referencePanel -p gonl_release4 -o /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr%iImputationWorksheet_usethis.csv'
    for x in range(1,23):
        command_1 = a % (x, x)
        command_2 = b % (x, x)
        print command_1
        os.system(command_1)
        print command_2
        os.system(command_2)
        print '-' * 20
        

* Generating scripts for step 2  
Copying parameters file to: cp /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/parametersMinimac.csv /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/  
Change value: clusterQueue from defaultValue to test  
Create scripts by running:

.

    import os
    a = 'sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh -inputdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/ -outputdir=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_2/chr%i -workflow=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/workflowMinimacStage2.csv -protocols=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/protocols/ -parameters=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/parametersMinimac.csv -worksheet=/target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr%iImputationWorksheet_usethis.csv -id=lifelines_2_%i'
    for x in range(1,23):
        command = a % (x, x, x)
        print command
        os.system(command)


### We do not submit. Blocked by: https://mail.google.com/mail/ca/?shva=1#inbox/13c249982d273c41
