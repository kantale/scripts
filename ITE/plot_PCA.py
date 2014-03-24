import argparse
import matplotlib.pyplot as plt


def plot_PCA(input_filenane, dimensions):
	f = open(input_filenane)
	d = [ map(float, x.replace('\n', '').split()) for x in f.readlines() if len(x) > 20]

	print 'Samples:', len(d)


	fig, ax = plt.subplots(dimensions-1, dimensions-1)

	for xplot in range(dimensions-1):
		for yplot in range(xplot + 1, dimensions):

			#print xplot, yplot

			xplot_index = xplot
			yplot_index = yplot-1

			ax[xplot_index, yplot_index].plot([x[xplot] for x in d], [x[yplot] for x in d], '.')
			[ax[xplot_index, yplot_index].annotate(str(x+1), xy=(d[x][xplot], d[x][yplot])) for x in range(len(d))]
			ax[xplot_index, yplot_index].set_title('PCA ' + str(xplot + 1) + '/' + str(yplot + 1))


			#plt.setp(ax[xplot_index, yplot_index].get_xticklabels(), visible=False)
			#plt.setp(ax[xplot_index, yplot_index].get_yticklabels(), visible=False)

	plt.show()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument('--input_filename', type=str, help='input_filenane')
	parser.add_argument('--dimensions', type=int, help='dimensions')

	args = parser.parse_args()

	plot_PCA(input_filenane=args.input_filename, dimensions=args.dimensions)