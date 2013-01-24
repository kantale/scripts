http://www.molgenis.org/ticket/1252

### Resources:
*  Documentation for molgenis compute imputation:
    * https://github.com/kantale/molgenis_apps/blob/master/doc/compute/02_compute_imputation.md
* Scripts already used: /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/prevend_MinimacV2_refGiant1000gv3.20101123
* Results: /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/

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
    
* The complete Step 2 Has to be done. ONLY ONCE. For both reference sets

### Waiting for chromosome 1. PrePhasing (regardless reference panel)

* I should have submitted to test scheduler. Not test-long queue
* Regenerate with default queue: Use default parameters.

.

    sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh -inputdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/ -outputdir=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_2/GoNLV4 -workflow=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/workflowMinimacStage2.csv -protocols=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/protocols/ -parameters=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/parametersMinimac.csv -worksheet=/target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/ImputationWorksheet_gonl_release4.csv -id=lifelines_gonlv4_2

* To login to test scheduler:
    * ssh scheduler02
    * cd /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_2/GoNLV4
    * sh submit_chr_1.sh

### Should I redo the first step? The reference set is not defined anywhere in the first step https://mail.google.com/mail/ca/?shva=1#sent/13c28fc5ea60dd5f
### New mail sent: https://mail.google.com/mail/ca/?shva=1#sent/13c2a1cb2296f3c3

* WC is done offline and is not described in the documentation. ImputationTool has to be called explicitly. Freerk made a script for QC with ImputationTool. 
    * This tool is located here: /target/gpfs2/gcc/groups/gcc/projects/prevend/prevend_b37/align_to_ref.sh
    * Current local dir: /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/
    * Copy the scipt to local directory: cp /target/gpfs2/gcc/groups/gcc/projects/prevend/prevend_b37/align_to_ref.sh ./
    * Copy ped and map files to local dir: cp /target/gpfs2/gcc/groups/gcc/projects/lifelines-imputation/liftover_to_b37/chr* ./
    * Edit align_to_ref.sh and edit second line to: INPUTDIR="/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/"
    * Edit align_to_ref.sh and edit line 40: --hap /target/gpfs2//gcc/resources/imputationReference/gonl_release4/TriTyper/Chr$CHR/
    * Execute align_to_ref.sh as a bash script: . align_to_ref.sh (not sh align_to_ref.sh)

* /target/gpfs2//gcc/resources/imputationReference/gonl_release4/ I don't have read permission. FIXED
* C-bash: /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252//result/chr2.ped: No such file or directory 
    * FIXED: mkdir result

### Waiting for initial QC (running on head node)

* Create PrePhasingWorksheet.csv with contents:

.

    project,studyInputDir,prePhasingResultDir,imputationPipeline,genomeBuild,chr,autostart
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr1/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr1,minimac,b37,1,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr2/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr2,minimac,b37,2,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr3/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr3,minimac,b37,3,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr4/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr4,minimac,b37,4,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr5/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr5,minimac,b37,5,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr6/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr6,minimac,b37,6,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr7/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr7,minimac,b37,7,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr8/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr8,minimac,b37,8,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr9/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr9,minimac,b37,9,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr10/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr10,minimac,b37,10,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr11/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr11,minimac,b37,11,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr12/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr12,minimac,b37,12,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr13/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr13,minimac,b37,13,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr14/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr14,minimac,b37,14,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr15/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr15,minimac,b37,15,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr16/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr16,minimac,b37,16,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr17/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr17,minimac,b37,17,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr18/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr18,minimac,b37,18,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr19/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr19,minimac,b37,19,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr20/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr20,minimac,b37,20,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr21/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr21,minimac,b37,21,FALSE
    lifelines_gonlV4,${root}/home/akanterakis/runs/ticket_1252/chr22/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/chr22,minimac,b37,22,FALSE

* Execute:

.

    sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh -inputdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/ -outputdir=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/scripts_step1 -workflow=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/workflowMinimacStage1.csv -protocols=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/protocols/ -parameters=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/parametersMinimac.csv -worksheet=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/PrePhasingWorksheet.csv -id=lifelines_GoNLv4

## Waiting for Step 1 for all chromosomes in scheduler02

* Running Step 2:

.

    sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/add_variable.sh -w /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/concattedChunkWorksheet.csv -v imputationResultDir -p /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/ -o /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/tmpImputationWorksheet.csv
    sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/add_variable.sh -w /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/tmpImputationWorksheet.csv -v referencePanel -p gonl_release4 -o /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/ImputationWorksheet_gonl_release4.csv
    sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/add_variable.sh -w /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/tmpImputationWorksheet.csv -v referencePanel -p giant1000gv3.20101123 -o /target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/ImputationWorksheet_giant1000gv3.20101123.csv

* Generate jobs:

.

    sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh -inputdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/ -outputdir=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_2_GONLv4/ -workflow=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/workflowMinimacStage2.csv -protocols=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/protocols/ -parameters=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/parametersMinimac.csv -worksheet=/target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/ImputationWorksheet_gonl_release4.csv -id=lifelines_gonlv4_2
    
* Submitting:
    * cd /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_2_GONLv4

.

    head -n 3  submit.sh > header.txt
    grep s00_prePhasingMach_s00_lifelines_gonlV4_1_  submit.sh > submit_chr1_nh.sh
    cat header.txt submit_chr1_nh.sh > submit_chr1.sh 
    sh submit_chr1.sh
    
    To separate in chromosomes run the script:

    import os
    
    command = "head -n 3  submit.sh > header.txt"
    print command
    os.system(command)
    for x in range(1,23):
      command = "grep s00_prePhasingMach_s00_lifelines_gonlV4_%i_  submit.sh > submit_chr%i_nh.sh" % (x, x)
      print command
      os.system(command)
      command = "cat header.txt submit_chr%i_nh.sh > submit_chr%i.sh" % (x, x)
      print command
      os.system(command)

    
### Waiting for chromosome 1. GONL V4. 
* Scheduler crashed at Friday 18 January. Resubmitted Monday 21 January 2013. (We shouldn't. scheduler didn't crashed. Jobs finished normally)
* Chrosome 1,2,3 finished. Submitted: chromosome  **4, 5, 6, 7, 8, 9, 10**

* Generated scripts for step 3 (without step 2 having finished):

.

    sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh -inputdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/ -worksheet=/target/gpfs2/gcc/groups/gonl/projects/imputationBenchmarking/imputationResult/lifelines_MinimacV2_refGoNLv4/ImputationWorksheet_gonl_release4.csv -parameters=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/parametersMinimac.csv -workflow=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/workflowMinimacStage3.csv -protocols=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/protocols/ -outputdir=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_3_GoNL -id=lifelines_gonlv4_3

* scripts dir: /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/step_3_GoNL
* grep to create a subset that contains only chromosome 1

### Submitted chromosome 1, on main scheduler. Waiting

## Impute on Grid
* ssh grid
* startGridSession bbmri.nl
* cd copy_data_to_grid/
* curl  https://raw.github.com/kantale/scripts/master/gridShare.py > gridShare.py
* Finding copy directory in Grid:
    * srmmkdir srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/RP2/home/akanterakis/runs/ticket_1252/results/chr1 for 1..22
* Command to copy data: python gridShare.py GRIDROOT=srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/RP2/home/akanterakis/runs/ticket_1252/results CLUSTERDIR=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/result
* Copying the study data. Done.
* create dir in grid for redference: srmmkdir srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/RP2/groups/gonl/resources/imputationReference/gonl_release4/vcf
* Command to copy the data: `python gridShare.py GRIDROOT=srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/RP2/groups/gonl/resources/imputationReference/gonl_release4/vcf CLUSTERDIR=/target/gpfs2/gcc/groups/gonl/resources/imputationReference/gonl_release4/vcf`
* **WAITING FOR DATA TO BE COPIED**. DONE
* Create directory on grid: srmmkdir srm://srm.grid.sara.nl:8443/pnfs/grid.sara.nl/data/bbmri.nl/RP2/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4
* ssh akanterakis@molgenis18.target.rug.nl
* This sequence:
    * sudo kill `ps aux | grep apache-ant | grep -v grep | cut -d ' ' -f 2`
    * Create datbase: echo 'DROP DATABASE IF EXISTS compute; CREATE DATABASE compute;' | mysql -u molgenis -pmolgenis
    * sudo  mv /srv/molgenis/compute/molgenis_apps/nohup.out /srv/molgenis/compute/molgenis_apps/nohup.out.001
    * sudo su - molgenis
    * cd /srv/molgenis/compute/molgenis_apps/; nohup ant -f /srv/molgenis/compute/molgenis_apps/build_compute.xml runOn -Dport=8080 &
    * VISIT: http://molgenis18.target.rug.nl:8080/compute/molgenis.do (In order to generate tables)
* Impot workflow:
    * sudo sh importWorkflow_alex.sh /srv/molgenis/compute/molgenis_apps/modules/compute/protocols/imputation/minimacV2/parametersMinimac.csv /srv/molgenis/compute/molgenis_apps/modules/compute/protocols/imputation/minimacV2/workflowMinimacStage1.csv /srv/molgenis/compute/molgenis_apps/modules/compute/protocols/imputation/minimacV2/protocols/
* Create exactly the same worksheet as before. Location: /srv/molgenis/compute/PrePhasingWorksheet.csv
* Submit worksheet1:
    * cd /srv/molgenis/compute; sudo sh importWorkSheet_alex.sh workflowMinimacStage1.csv /srv/molgenis/compute/PrePhasingWorksheet.csv test1
* Run pilot:
    * sudo sh runPilot_alex.sh ui.grid.sara.nl kanterak GRID_PASSWORD grid

### Everything that was done in the grid was wrong!!
* The align_to_ref.sh script generates two sets of outputs:
    * the first is in /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/chrXX directories. These are TEMPORARY data
    * the second is in the /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/result/ directory this is the correct
    * In my PrePhasingWorksheet.csv I declared the first! The correct worksheet is:

.

    project,studyInputDir,prePhasingResultDir,imputationPipeline,genomeBuild,chr,autostart
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr1,minimac,b37,1,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr2,minimac,b37,2,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr3,minimac,b37,3,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr4,minimac,b37,4,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr5,minimac,b37,5,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr6,minimac,b37,6,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr7,minimac,b37,7,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr8,minimac,b37,8,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr9,minimac,b37,9,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr10,minimac,b37,10,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr11,minimac,b37,11,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr12,minimac,b37,12,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr13,minimac,b37,13,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr14,minimac,b37,14,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr15,minimac,b37,15,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr16,minimac,b37,16,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr17,minimac,b37,17,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr18,minimac,b37,18,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr19,minimac,b37,19,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr20,minimac,b37,20,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr21,minimac,b37,21,FALSE
    zz_gonlV4,${root}/home/akanterakis/runs/ticket_1252/result/,${root}/groups/gonl/projects/imputationBenchmarking/imputationResult/zz_MinimacV2_refGoNLv4/chr22,minimac,b37,22,FALSE

* Remove previous output directory for step 1
    * cd /target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/scripts_step1; rm -rf *
* Generate scripts for step 1: 
    * sh /target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/molgenis_compute.sh -inputdir=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/ -outputdir=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/scripts_step1 -workflow=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/workflowMinimacStage1.csv -protocols=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/protocols/ -parameters=/target/gpfs2/gcc/tools/MolgenisCompute4/molgenis_compute-0a00dd6/protocols/imputation/minimacV2/parametersMinimac.csv -worksheet=/target/gpfs2/gcc/home/akanterakis/runs/ticket_1252/PrePhasingWorksheet.csv -id=lifelines_GoNLv4
* Submit step 1:
