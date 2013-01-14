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
