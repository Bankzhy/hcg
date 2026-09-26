def burn(self):
		if not self.data:
			raise ValueError("No data available")
		if hasattr(self, 'calculations'):
			self.calculations()
		self.start_svg()
		self.calculate_graph_dimensions()
		self.foreground = etree.Element("g")
		self.draw_graph()
		self.draw_titles()
		self.draw_legend()
		self.draw_data()
		self.graph.append(self.foreground)
		self.render_inline_styles()
		return self.render(self.root)