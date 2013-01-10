http://www.molgenis.org/ticket/1252

### Resources:
*  Documentation for molgenis compute imputation:
    * https://github.com/kantale/molgenis_apps/blob/master/doc/compute/02_compute_imputation.md
* Scripts already used: /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/prevend_MinimacV2_refGiant1000gv3.20101123

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
    a = 'sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/add_variable.sh -w /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr%iChunkWorksheet.csv -v imputationResultDir -p /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/ -o /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr%iImputationWorksheet.csv'
    b = 'sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/add_variable.sh -w /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr%iImputationWorksheet.csv -v referencePanel -p gonl_release4 -o /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr%iImputationWorksheet_usethis.csv'
    c = 'sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/add_variable.sh -w /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr%iImputationWorksheet.csv -v referencePanel -p giant1000gv3.20101123 -o /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr%iImputationWorksheet_usethis_giant1000.csv'
    for x in range(1,23):
        command_1 = a % (x, x)
        command_2 = b % (x, x)
        command_3 = c % (x, x)
        print command_1
        os.system(command_1)
        print command_2
        os.system(command_2)
        print command_3
        os.system(command_3)
        print '-' * 20
        

* Generating scripts for step 2  
Copying parameters file to: cp /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/parametersMinimac.csv /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/  
Change value: clusterQueue from defaultValue to test-long  
Create scripts by running:

.

    import os
    a = 'sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh -inputdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/ -outputdir=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_2/GoNLV4_chr%i -workflow=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/workflowMinimacStage2.csv -protocols=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/protocols/ -parameters=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/parametersMinimac.csv -worksheet=/target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr%iImputationWorksheet_usethis.csv -id=lifelines_gonlv4_2_%i'
    b = 'sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh -inputdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/ -outputdir=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_2/giant1000_chr%i -workflow=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/workflowMinimacStage2.csv -protocols=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/protocols/ -parameters=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/parametersMinimac.csv -worksheet=/target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr%iImputationWorksheet_usethis_giant1000.csv -id=lifelines_giant1000_2_%i'
    for x in range(1,23):
        command = a % (x, x, x)
        print command
        os.system(command)
        command = b % (x, x, x)
        print command
        os.system(command)
        print '-' * 20


### We do not submit GoNL. Blocked by: https://mail.google.com/mail/ca/?shva=1#inbox/13c249982d273c41

* Submit 1000G
   * Problem: /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_2/giant1000_chr1/s00_prePhasingMach_s00__1_10_1.sh 
   * /target/gpfs2/gcc//tools/mach.1.0.18/executables/mach1 -d /tmp//studyMerlin//chr1//chunk10-chr1_sampleChunk1.dat 
   * Why /tmp//studyMerlin//chr1//chunk10-chr1_sampleChunk1.dat ???
   * variable in parameters studyMerlinChrDir --> prePhasingResultDir
   * Worksheet /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr1ImputationWorksheet_usethis_giant1000.csv correct..
   * Generation command: sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh -inputdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/ -outputdir=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_2/giant1000_chr1 -workflow=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/workflowMinimacStage2.csv -protocols=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/protocols/ -parameters=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/parametersMinimac.csv -worksheet=/target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr1ImputationWorksheet_usethis_giant1000.csv -id=lifelines_giant1000_2_1
   * Generation with original parameters: sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh -inputdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/ -outputdir=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_2/giant1000_chr1 -workflow=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/workflowMinimacStage2.csv -protocols=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/protocols/ -parameters=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/parametersMinimac.csv  -worksheet=/target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr1ImputationWorksheet_usethis_giant1000.csv -id=lifelines_giant1000_2_1
   * Solved Insted of using: /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_1/concattedChunkWorksheet.csv I used: /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/Chr1ImputationWorksheet_usethis_giant1000.csv

* Correcting..

* Step 2 of workflow. (Imputation step)  
Running:

.


    sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/add_variable.sh -w /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_1/concattedChunkWorksheet.csv -v imputationResultDir -p /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/ -o /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/tmpImputationWorksheet.csv
    sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/add_variable.sh -w /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/tmpImputationWorksheet.csv -v referencePanel -p gonl_release4 -o /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/ImputationWorksheet_gonl_release4.csv
    sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/add_variable.sh -w /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/tmpImputationWorksheet.csv -v referencePanel -p giant1000gv3.20101123 -o /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/ImputationWorksheet_giant1000gv3.20101123.csv
        

* Generating scripts for step 2  
Copying parameters file to: cp /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/parametersMinimac.csv /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/  
Change value: clusterQueue from defaultValue to test-long  
Create scripts by running:

.

    sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh -inputdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/ -outputdir=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_2/GoNLV4 -workflow=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/workflowMinimacStage2.csv -protocols=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/protocols/ -parameters=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/parametersMinimac.csv -worksheet=/target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/ImputationWorksheet_gonl_release4.csv -id=lifelines_gonlv4_2
    sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh -inputdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/ -outputdir=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_2/giant1000 -workflow=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/workflowMinimacStage2.csv -protocols=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/protocols/ -parameters=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/parametersMinimac.csv -worksheet=/target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/ImputationWorksheet_giant1000gv3.20101123.csv -id=lifelines_giant10000_2

* Submitting GoNL.
    * cd /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_2/giant1000
    * NO NEED TO DO THIS: sed  's/sleep 0/sleep 1/g' submit.sh > submit_sleep_1.sh 
    * sh submit.sh . THIS BLOATS THE SCHEDULER. DO NOT DO THIS
    * Instead (for chromosome 1):

.

    head -n 3  submit.sh > header.txt
    grep s00_prePhasingMach_s00_lifelines_gonl_1_  submit.sh > submit_chr1_nh.sh
    cat header.txt submit_chr1_nh.sh > submit_chr1.sh 
    sh submit_chr1.sh
    
    
### Waiting for chromosome 1. PrePhasing (regardless reference panel)
