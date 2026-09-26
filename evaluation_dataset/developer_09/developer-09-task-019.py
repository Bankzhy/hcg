def csv(self, filename=None, **format_params):
        if not self.pretty:
            return None
        if filename:
            outfile = open(filename, 'w')
        else:
            outfile = StringIO()
        writer = UnicodeWriter(outfile, **format_params)
        writer.writerow(self.field_names)
        for row in self:
            writer.writerow(row)
        if filename:
            outfile.close()
            return CsvResultDescriptor(filename)
        else:
            return outfile.getvalue()