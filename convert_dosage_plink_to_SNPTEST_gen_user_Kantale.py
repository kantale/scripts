
"""
Copyright (c) 2012, 2013 The PyPedia Project 
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

http://www.opensource.org/licenses/BSD-2-Clause
"""

import sys
import gzip
from time import gmtime, strftime

def current_time():
	return strftime("%Y-%m-%d %H:%M:%S", gmtime())

def sample_plink_dosage_data():
	data = """SNP A1 A2 1 LL_WGA000079 1 LL_WGA000093 1 LL_WGA000122  1 LL_WGA000141
1:10583 G A 0.733 0.246 0.733 0.246 0.733 0.246 0.733 0.246
1:10611 C G 0.963 0.037 0.963 0.037 0.963 0.037 0.963 0.037
1:13302 C T 0.785 0.202 0.785 0.202 0.785 0.202 0.785 0.202
1:54421 A G 0.809 0.181 0.809 0.181 0.809 0.181 0.809 0.181
1:66507 T A 0.850 0.144 0.850 0.144 0.850 0.144 0.850 0.144
	"""

	return data

def open_file2(file_param, opener, mode):
	if type(file_param).__name__ == 'str':
		return opener(file_param, mode)
	elif mode == 'w':
		return file_param
	else:
		return opener(fileobj=file_param, mode=mode)

def convert_dosage_plink_to_SNPTEST_gen(input_plink_dosage_file, output_snptest_gen_file, output_snptest_sample_file):

	"""
	>>> import sys
	>>> from StringIO import StringIO
	>>> plink_dosage = sample_plink_dosage_data()
	>>> input_plink_dosage_write_file = StringIO()
	>>> output_snptest_gen_file = StringIO()
	>>> output_snptest_sample_file = StringIO()
	>>> f = gzip.GzipFile(fileobj = input_plink_dosage_write_file, mode='w')
	>>> sys.stdout.write('X'); f.write(plink_dosage) # doctest: +ELLIPSIS
	X...
	>>> f.close()
	>>> input_plink_dosage_file = StringIO(input_plink_dosage_write_file.getvalue())
	>>> sys.stdout.write('X'); convert_dosage_plink_to_SNPTEST_gen(input_plink_dosage_file, output_snptest_gen_file, output_snptest_sample_file) # doctest: +ELLIPSIS
	X...
	>>> print output_snptest_gen_file.getvalue()
	SNP_1:10583 1:10583 10583 G A 0.733 0.246 0.021 0.733 0.246 0.021 0.733 0.246 0.021 0.733 0.246 0.021
	SNP_1:10611 1:10611 10611 C G 0.963 0.037 3.46944695195e-17 0.963 0.037 3.46944695195e-17 0.963 0.037 3.46944695195e-17 0.963 0.037 3.46944695195e-17
	SNP_1:13302 1:13302 13302 C T 0.785 0.202 0.013 0.785 0.202 0.013 0.785 0.202 0.013 0.785 0.202 0.013
	SNP_1:54421 1:54421 54421 A G 0.809 0.181 0.01 0.809 0.181 0.01 0.809 0.181 0.01 0.809 0.181 0.01
	SNP_1:66507 1:66507 66507 T A 0.850 0.144 0.006 0.850 0.144 0.006 0.850 0.144 0.006 0.850 0.144 0.006
	<BLANKLINE>
	>>> print output_snptest_sample_file.getvalue()
	ID_1 ID_2 missing
	0 0 0
	1 LL_WGA000079 0
	1 LL_WGA000093 0
	1 LL_WGA000122 0
	1 LL_WGA000141 0
	<BLANKLINE>
	"""

	open_file = lambda file_param, opener, mode : opener(file_param, mode) if type(file_param).__name__ == 'str' else opener(fileobj=file_param, mode=mode)
	close_file = lambda file_param : file_param.close() if type(file_param).__name__ == 'str' else None

	input_plink_dosage = open_file2(input_plink_dosage_file, gzip.GzipFile, 'rb')
	output_snptest_gen = open_file2(output_snptest_gen_file, open, 'w')
	output_snptest_sample = open_file2(output_snptest_sample_file, open, 'w')

	lc = 0
	for line in input_plink_dosage:

		if lc % 1000 == 0:
			print 'Lines:', lc, current_time()

		ls = line.replace('\n', '').split()
		if not len(ls):
			continue

		if lc == 0:
			output_snptest_sample.write(' '.join(['ID_1', 'ID_2', 'missing']) + '\n')
			output_snptest_sample.write(' '.join(['0', '0', '0']) + '\n')
			sample_fid_iid = ls[3:]
			output_snptest_sample.write('\n'. join([' '.join([sample_fid_iid[index], sample_fid_iid[index+1], '0']) for index, x in enumerate(sample_fid_iid) if index % 2 == 0]) + '\n')

		else:
			to_print = ['SNP_' + ls[0], ls[0], ls[0].split(':')[1], ls[1], ls[2]]
			probs = ls[3:]
			output_snptest_gen.write(' '.join(to_print + [' '.join([probs[index], probs[index+1], str(1.0-float(probs[index])-float(probs[index+1]))]) for index, x in enumerate(probs) if index % 2 == 0]) + '\n')

		lc += 1

	close_file(output_snptest_gen)
	close_file(output_snptest_sample)

	print "Total lines:", lc


if __name__ == '__main__':
	if len(sys.argv) != 4:
		print """
Converts from plink's dosage file to SNPTEST gen format. Plink supports many different types of dosage files. This method supports only one type of dosage files:
The first line should be a header like this:

SNP A1 A2 FID1 IID1 FID2 IID2 FID3 IID3 

All the next lines should be like this:

<CHR>:<POS> ALLELE_1 ALLELE_2 prob_AA prob_AB prob_AA prob_AB prob_AA prob_AB ...

The included function sample_plink_dosage_data returns a sample of plink dosage data. This specific version is generated from 
this tool: http://github.com/fadern/dose_to_plink . This tool converts the dosage and prob files generated from minimac into 
a plink's dosage file. The function in this article can be the subsequent step to generate a SNPTEST gen file.
For more: http://www.pypedia.com/index.php/convert_dosage_plink_to_SNPTEST_gen_user_Kantale

		Usage:
		python convert_dosage_plink_to_SNPTEST_gen.py <input plink dosage file> <output SNPTEST gen file> <output snotest sample file>
"""
	else:
		input_plink_dosage_file = sys.argv[1]
		output_snptest_gen_file = sys.argv[2]
		output_snptest_sample_file = sys.argv[3]

		convert_dosage_plink_to_SNPTEST_gen_user_Kantale(input_plink_dosage_file, output_snptest_gen_file, output_snptest_sample_file)

