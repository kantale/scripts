import os
import time
import argparse
import itertools

def print_now_2():
	return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

def genotypes_to_tped(a1, a2, genotype):
	if genotype == 'AA':
		return [a1, a1]
	if genotype == 'AB':
		return [a1, a2]
	if genotype == 'BA':
		return [a2, a1]
	if genotype == 'BB':
		return [a2, a2]
	if genotype == 'NoCall':
		return ['0', '0']

	raise Exception('Unknown call', genotype)

def parse_file(input_filename, output_filename, keep_phenotypes=None):

	data = {}

	doubles = []
	doubles_exists = False

	#Load double
	if os.path.exists('doubles.txt'):
		with open('doubles.txt') as f:
			doubles = [x.replace('\n', '') for x in f.readlines()]
		doubles_exists = True

	if keep_phenotypes:
		keep_name = '_'.join(keep_phenotypes)
		keep_filename = keep_name + '.txt'
		keep_file = open(keep_filename, 'w')

	print input_filename
	removed = 0
	same_genotype = 0
	different_genotype = 0
	removed_snp_a = 0
	keep_affx_snp = 0
	ok = 0
	with open(input_filename) as input_file, open(output_filename + '.tped', 'w') as tped_file , open(output_filename + '.tfam', 'w') as tfam_file:

		line = input_file.readline()
		samples = line.replace('\n', '').split()[1:]

		line = input_file.readline()
		sex = line.replace('\n', '').split()[1:]

		line = input_file.readline()
		diagnosis = line.replace('\n', '').split()[1:]

		line = input_file.readline()
		response = line.replace('\n', '').split()[1:]

		#Save tfam file
		for sample_c, sex_c, d_c, r_c in zip(samples, sex, diagnosis, response):

			#Are we keeping this sample?
			if d_c in keep_phenotypes:
				keep_file.write(' '.join(['1', sample_c]) + '\n')

			if sex_c not in ['male', 'female']:
				raise Exception('Unknonn value:', sex_c)

			if d_c not in ['BPII', 'SAM', 'BPI']:
				raise Exception('Unknown value:', d_c)

			if r_c not in ['0', '1']:
				raise Exception('Unknown value:', r_c)

			if r_c == '0':
				phenotype = '1'
			elif r_c == '1':
				phenotype = '2'

			to_print = ['1', sample_c, '0', '0', '1' if sex_c == 'male' else '2', phenotype]
			tfam_file.write(' '.join(to_print) + '\n')

		line_counter = 0
		for line in input_file:
			line_counter += 1

			if line_counter % 10000 == 0:
				print print_now_2(), line_counter 

			line_s = line.replace('\n', '').split()

			snp_code = line_s[0]
			rs_code = line_s[1]
			chromosome = line_s[2]
			pos = line_s[3]
			strand = line_s[4]
			allele_1 = line_s[6]
			allele_2 = line_s[7]
			genotypes = line_s[8:]
			if rs_code == '---':
				if chromosome == '---':
					removed += 1
					continue
				else:
					rs_code = chromosome + '_' + pos

			if doubles_exists:
				if rs_code in doubles:
					if 'SNP_A' in snp_code:
						removed_snp_a += 1
						continue
					elif 'AFFX-SNP' in snp_code:
						keep_affx_snp += 1
					else:
						raise Exception('Unknown snp code:', snp_code)


			if rs_code in data:
				if ''.join(genotypes) != data[rs_code]:
					print rs_code, chromosome, pos
					print '   ', ''.join(genotypes)
					print '   ', data[rs_code]
					#raise Exception('AAA')
					different_genotype += 1
					doubles += [rs_code]
					continue
				else:
					same_genotype += 1
					continue
			else:
				data[rs_code] = ''.join(genotypes)

			#Save tped file
			to_print = [chromosome, rs_code, '0', pos] 
			to_print += [y for x in genotypes for y in genotypes_to_tped(allele_1, allele_2, x)]
			tped_file.write(' '.join(to_print) + '\n')
			ok += 1

	if keep_phenotypes:
		keep_file.close()

	print 'Removed:', removed
	print 'Same genotypes:', same_genotype
	print 'Different genotypes:', different_genotype
	print 'removed_snp_a:', removed_snp_a
	print 'keep_affx_snp:', keep_affx_snp
	print 'OK markers:', ok
	if not os.path.exists('doubles.txt'):
		with open('doubles.txt', 'w') as f:
			f.write('\n'.join(doubles) + '\n')

	plink_command = [
		'/Users/alexandroskanterakis/Tools/plink-1.07-mac-intel/plink',
		'--tfile', output_filename,
		'--noweb',
		'--assoc',
		'--pfilter', '1e-4',
		'--keep', keep_filename,
		'--out', output_filename + '_' + keep_name
	]

	plink_command = ' '.join(plink_command)
	print plink_command
	os.system(plink_command)

def all_combinations_TPED(input_DATA_filename, input_TPED_filename, phenotypes):

	read_file = lambda afile : afile.readline().replace('\n', '').split()[1:]

	with open(input_DATA_filename) as input_DATA_file:
		sample_names = read_file(input_DATA_file)
		sex = read_file(input_DATA_file) 
		diagnosis = read_file(input_DATA_file) 

	#Make appropriate keep file
	keep_name = '_'.join(phenotypes)
	keep_filename = keep_name + '.txt'
	keep_data = ['1' + ' ' + sample_names[index] for index, d in enumerate(diagnosis) if d in phenotypes]
	with open(keep_filename, 'w') as f:
		f.write('\n'.join(keep_data) + '\n')

	plink_command = [
		'/Users/alexandroskanterakis/Tools/plink-1.07-mac-intel/plink',
		'--tfile', input_TPED_filename.replace('.tped', ''),
		'--noweb',
		'--assoc',
		'--pfilter', '1e-4',
		'--keep', keep_filename,
		'--out', input_TPED_filename.replace('.tped', '') + '_' + keep_name
	]

	plink_command = ' '.join(plink_command)
	print plink_command
	os.system(plink_command)	

def all_combinations(input_filename, output_filename, input_DATA_filename=None, input_TPED_filename = None, phenotypes = None):

	phenotypes = phenotypes.split(',')
	for i in range(len(phenotypes)):
		for c in itertools.combinations(phenotypes, i+1):
			if not input_TPED_filename:
				parse_file(input_filename, output_filename, c)
			else:
				all_combinations_TPED(input_TPED_filename=input_TPED_filename, input_DATA_filename=input_DATA_filename, phenotypes=c)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument('--action', type=str, help='parse_file')
	parser.add_argument('--input_filename', type=str, help='input filename')
	parser.add_argument('--output_filename', type=str, help='output filename')
	parser.add_argument('--phenotypes', type=str, help='phenotypes')
	parser.add_argument('--input_DATA_filename', type=str, help='input DATA filename')
	parser.add_argument('--input_TPED_filename', type=str, help='input TPED filename')

	args = parser.parse_args()

	if args.action == 'parse_file':
		parse_file(input_filename=args.input_filename, output_filename=args.output_filename)
	elif args.action == 'all_combinations':
		all_combinations(
			input_filename=args.input_filename, 
			output_filename=args.output_filename,
			input_DATA_filename=args.input_DATA_filename,
			input_TPED_filename=args.input_TPED_filename, 
			phenotypes=args.phenotypes)


