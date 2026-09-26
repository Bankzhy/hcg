def report(self, output_file=sys.stdout):
        if self.verbose > 1:
            print('{}'.format(pprint.pformat(self.results['verbose infos'])), file=output_file)
        for level, cycles in self.results['cycles']:
            print('{} = {}'.format(
                level, self.conv_cy(cycles)[self._args.unit]), file=output_file)
        if self.verbose > 1:
            if 'memory bandwidth kernel' in self.results:
                print('memory cycles based on {} kernel with {}'.format(
                          self.results['memory bandwidth kernel'],
                          self.results['memory bandwidth']),
                      file=output_file)
        if self.verbose > 1:
            print(file=output_file)
            print(self.report_data_transfers(), file=output_file)