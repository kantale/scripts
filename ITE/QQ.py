
import argparse
import numpy as np

import matplotlib.pyplot as plt

def ppoints(n):
	'''
	Save as R's ppoints
	'''
	if n <= 10:
		a = 3.0/8.0
	else:
		a = 0.5

 	return (np.array(range(1,n+1)) - a) / (n + 1 - 2.0*a)


def qq(input_assoc_filename, input_frq_filename, frq_filter):

	if not frq_filter:
		frq_filter = 0.001

	#Load frequencies
	print 'Loading freqs'
	with open(input_frq_filename) as f:
		f.readline()

		freqs = [l.replace('\n', '').split()[4] for l in f]
	print 'Done loading freqs'

	#Load p-values
	print 'Loading p-values'
	with open(input_assoc_filename) as f:
		f.readline()

		pvalues = [l.replace('\n', '').split()[8] for l in f]
	print 'Done loading p-values'

	observed = [float(p) for f, p in zip(freqs, pvalues) if f != 'NA' and f>=frq_filter and p != 'NA']

	print 'Total:', len(pvalues)
	print 'Plotted:', len(observed)

	observed = np.sort(observed)
	observed = -np.log10(observed)
	expected = -np.log10(ppoints(len(observed)))
	x_label = 'expected -log(10)'
	y_label = 'observed -log(10)'

	l = np.median(observed)/-np.log10(0.5)

	xmax = max(expected[np.invert(np.isinf(expected))]) + 1
	ymax = max(observed[np.invert(np.isinf(observed))]) + 1
	xymax = max(xmax, ymax)

	fig, ax = plt.subplots()

	#Set labels
	ax.set_xlabel(x_label)
	ax.set_ylabel(y_label)

	#plot ab line
	ax.plot([-0.2, xymax], [-0.2, xymax], color='red', linewidth=2.0)

	#Plot qq plot
	ax.plot(expected, observed, '.')

	plt.show()	

if __name__ == '__main__':

	parser = argparse.ArgumentParser()

	parser.add_argument('--input_frq_filename', type=str, help='input_frq_filenane')
	parser.add_argument('--input_assoc_filename', type=str, help='input_assoc_filename')
	parser.add_argument('--frq_filter', type=float, help='frequency filter')

	args = parser.parse_args()

	qq(
		input_assoc_filename=args.input_assoc_filename,
		input_frq_filename=args.input_frq_filename,
		frq_filter=args.frq_filter,
		)