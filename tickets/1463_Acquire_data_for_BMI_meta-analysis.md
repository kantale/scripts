http://www.molgenis.org/ticket/1463

### Resources
* How to generate EFFECT, STDERR and P values for a GWAS: 
    * http://pngu.mgh.harvard.edu/~purcell/plink/anal.shtml#qt
    * Requires Quantitative trait association analysis
* Typical METAL input fields for a study:

.

    MARKER   SNP
    WEIGHT   N
    ALLELE   EFFECT_ALLELE NON_EFFECT_ALLELE
    FREQ     EFFECT_ALLELE_FREQ
    EFFECT   BETA
    STDERR   SE
    PVAL     P_VAL

### Actions
* Get location of Celiac Disease data (including phenotype)

## MAIL SENT TO PATRICK https://mail.google.com/mail/ca/?shva=1#sent/13c1b48cd61f94b4 Cluster down for maintenance

* Get MEtal  
   * curl http://www.sph.umich.edu/csg/abecasis/METAL/download/generic-metal-2011-03-25.tar.gz > generic-metal-2011-03-25.tar.gz
   * tar zxvf generic-metal-2011-03-25.tar.gz
   * make all  
On mac OSX: ld: library not found for -lcrt0.o  
   * Solution
      * http://appliedprocrastination.blogspot.nl/2008/12/dread-lcrt0o-error-on-mac-os-x.html
      * Remove the static from the last compilation command. Diff:

.

    31d30
    < CFLAGS_no_static=-O2 -I./libsrc -I./pdf  -D_FILE_OFFSET_BITS=64
    97,98c96
    <   $(CXX) $(CFLAGS_no_static) -o $@ -include version/VersionInfo.h $(TOOL)/*.cpp $(PDFLIB) $(LIBFILE) -lm -lz
    < #  $(CXX) $(CFLAGS) -o $@ -include version/VersionInfo.h $(TOOL)/*.cpp $(PDFLIB) $(LIBFILE) -lm -lz
    ---
    > 	$(CXX) $(CFLAGS) -o $@ -include version/VersionInfo.h $(TOOL)/*.cpp $(PDFLIB) $(LIBFILE) -lm -lz

* Meeting with Jana at 10 January 2013. https://mail.google.com/mail/ca/?shva=1#sent/13c1f324ddccc98d Postponed.
* Agreed to not experiment wth Celiac Data. Javier can help with showing around
* Analysis plan sent to Jana. New datasets that she might include is TRAILS (and perhaps NESDA)
* Invited to apply the comments about (1) family realationships and (2) additional traits.
* Mail: https://mail.google.com/mail/ca/?shva=1#sent/13c1f324ddccc98d

### Submit analysis plan
### Meeting with Javier to discuss it https://mail.google.com/mail/ca/?shva=1#sent/13c3988431b1943a

### Meeting notes:
* BMI is a continuous trait so the association will be done with linear refression
    * If it was a discrete train it would be done with logistic regression
* We should ask the biobanks for:
    * Format of data. Ask from them the first 10 lines fo their data files.
    * Supply the command lines for data conversion and data analysis 
    * Graphs and plots that show population stratification after PCA or MDS
* The association analysis (linear refression, additive model) can be done in R
* The most important data that we require from the databanks is: N (Total number of samples analyzed)
* Phenotype data looks like this:
<table>
    <tr>
        <td>BMI</td>
        <td>SNP_1</td>
        <td>SNP_2</td>
        <td>SNP_N</td>
        <td>Age</td>
        <td>Gender</td>
        <td>PC_1</td>
        <td>PC_2</td>
        <td>PC_20</td>
    </tr>
</table>
* The popylation stratification (PCA) can be done with EIGENSTRAT: http://genepath.med.harvard.edu/~reich/EIGENSTRAT.htm
* For meta-analysis:
    * Fixed weight analysis (if you consider all GWASes equal) or variable weight anlaysis
    * BETA, SE and PVAL will be the input for every GWAS
* Results of association. If we have cases / controls studies:
    * Search for hidden family relationships with tools like plink and king (http://people.virginia.edu/~wc9c/KING/)
    * This tools extract a PHAT value. 
    * If PHAT ~= 1m then monozygotic twins
    * if PHAT > 0.5 then siblings
    * if PHAT > 0.25 the cousins or other form of relatedness
    * if PHAT < 0.25 unrelated
* Look for inverse BMI and inverse WHR. Inverse BMI is height^2 / mass. Check: http://www.ncbi.nlm.nih.gov/pubmed/21846303

### Analysis plan updated with Javier's notes, new version sent to Jana

* The analysis files requested per study are more:
    * (4 traits: BMI, BMI_inv, WHR, WHR_inv) X 3 (sample subsets: all, male, female) X (2 analysis: common, rare) = 24
    * Is this OK?
* Also added: Data should be reported on NCBI build 37 (hg19).
* Also added: Details about imputation
* Resolved comment from Jana: **do we have family members in other studies? in LL GWA2 we excluded the subjects based on family relatedness QC step**
* Comments about the analysis plan from Elisa: https://mail.google.com/mail/?shva=1#inbox/13c3e261b0de2834
    * who is ...? (right after the title). **Corrected**
    * the second row of the methods still contains release 3.1 of GoNL... **Corrected**
    * you never explain that BMI is body mass index, but you do explain WHR. **Corrected**
    * why do you want date of birth? you never use this. **Corrected** Although we had a discussion about this with Jana who insisted this is important
    * Carolina will be the person to contact for ERGO, Lennart and I for ERF. **Corrected**
    * why do you want people to use minimac? what if cohorts used impute to impute their cohorts with 1kG? Reply: It only mentions once that we explicitlu prefer MACH and this was removed.. **Corrected**
    * section 3, you first say "adjustment for age and gender", but lateron you also mention age^2. **Corrected**. Removed the part: "and adjustment for age and gender."
        * Jana's comment: age and ageˆ2 is THE adjustment for age, there are different ways to do that of course... don't understand the comments actually...
        * Elisa's comment: Maybe use: adjustment for age, age^2 and gender. It is just that you want to be consistent in the whole plan, to make sure that people do the right analysis. **Finally changed to:** and adjustment for age, age^2 and gender. 
        * Jana's comment: (gender) should be removed as we will not have the analysis in a combined sample

* Comments about analysis plan from Setten, J. van:
    * J.vanSetten: Restructured the 'traits' paragraph in order to look more like a to-do list. 
    * "It is preferable a smaller sample size but measured under objective condition rather a larger sample size with a careless phenotype reporting". **Deleted**
    * So what is the optimal tradeoff between asking too much from cohorts and satisfying reviewers?

* TC 17 January 2013.
    * BMI and Height is (additionaly) for comparing GoNL and 1000G. Lipds differs because it seeks novel biology meaning in data imputed with Dutch reference. This is why Lipids ask fewer files (do not include imputation with 1000G).
    * Analysis deadline for data submission from the biobanks is 15 March (1 March too soo, 1 April too late and too relaxing!)
    * Cohorts have already done the submitted analysis many times and they know what to do. They shouldn't expect from us to provide any anaysis scripts
