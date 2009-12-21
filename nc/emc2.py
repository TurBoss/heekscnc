import nc
import iso
import iso_codes

class CodesEMC2(iso_codes.Codes):
	def SPACE(self): return(' ')

	# This version of COMMENT removes comments from the resultant GCode
	# def COMMENT(self,comment): return('')

iso_codes.codes = CodesEMC2()


class CreatorEMC2(iso.CreatorIso):
	def init(self): 
		iso.CreatorIso.init(self) 

	def program_begin(self, id, comment):
		self.write( ('(' + comment + ')' + '\n') )

 ############################################################################
    ##  Settings
    
	def imperial(self):
		self.write_blocknum()
		self.write( iso_codes.codes.IMPERIAL() + '\t (Imperial Values)\n')
		self.fmt = iso_codes.codes.FORMAT_IN()

	def metric(self):
		self.write_blocknum()
		self.write( iso_codes.codes.METRIC() + '\t (Metric Values)\n' )
		self.fmt = iso_codes.codes.FORMAT_MM()

	def absolute(self):
		self.write_blocknum()
		self.write( iso_codes.codes.ABSOLUTE() + '\t (Absolute Coordinates)\n')

	def incremental(self):
		self.write_blocknum()
		self.write( iso_codes.codes.INCREMENTAL() + '\t (Incremental Coordinates)\n' )

	def polar(self, on=True):
		if (on) :
			self.write_blocknum()
			self.write(iso_codes.codes.POLAR_ON() + '\t (Polar ON)\n' )
		else : 
			self.write_blocknum()
			self.write(iso_codes.codes.POLAR_OFF() + '\t (Polar OFF)\n' )

	def set_plane(self, plane):
		if (plane == 0) : 
			self.write_blocknum()
			self.write(iso_codes.codes.PLANE_XY() + '\t (Select XY Plane)\n')
		elif (plane == 1) :
			self.write_blocknum()
			self.write(iso_codes.codes.PLANE_XZ() + '\t (Select XZ Plane)\n')
		elif (plane == 2) : 
			self.write_blocknum()
			self.write(iso_codes.codes.PLANE_YZ() + '\t (Select YZ Plane)\n')

	def comment(self, text):
		self.write_blocknum()
		self.write((iso_codes.codes.COMMENT(text) + '\n'))

	# This is the coordinate system we're using.  G54->G59, G59.1, G59.2, G59.3
	# These are selected by values from 1 to 9 inclusive.
	def workplane(self, id):
		if ((id >= 1) and (id <= 6)):
			self.write_blocknum()
			self.write( (iso_codes.codes.WORKPLANE() % (id + iso_codes.codes.WORKPLANE_BASE())) + '\t (Select Relative Coordinate System)\n')
		if ((id >= 7) and (id <= 9)):
			self.write_blocknum()
			self.write( ((iso_codes.codes.WORKPLANE() % (6 + iso_codes.codes.WORKPLANE_BASE())) + ('.%i' % (id - 6))) + '\t (Select Relative Coordinate System)\n')

	def report_probe_results(self, x1=None, y1=None, z1=None, x2=None, y2=None, z2=None, x3=None, y3=None, z3=None, x4=None, y4=None, z4=None, x5=None, y5=None, z5=None, x6=None, y6=None, z6=None, xml_file_name=None ):
		self.comment('Generate an XML document describing the probed coordinates found');
		self.write_blocknum()
		self.write('(LOGOPEN,')
		self.write(xml_file_name)
		self.write(')\n')

		self.write_blocknum()
		self.write('(LOG,<POINTS>)\n')

		if ((x1 != None) or (y1 != None) or (z1 != None)):
			self.write_blocknum()
			self.write('(LOG,<POINT>)\n')

		if (x1 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + x1 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<X>#<_value></X>)\n')

		if (y1 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + y1 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<Y>#<_value></Y>)\n')

		if (z1 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + z1 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<Z>#<_value></Z>)\n')

		if ((x1 != None) or (y1 != None) or (z1 != None)):
			self.write_blocknum()
			self.write('(LOG,</POINT>)\n')

		if ((x2 != None) or (y2 != None) or (z2 != None)):
			self.write_blocknum()
			self.write('(LOG,<POINT>)\n')

		if (x2 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + x2 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<X>#<_value></X>)\n')

		if (y2 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + y2 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<Y>#<_value></Y>)\n')

		if (z2 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + z2 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<Z>#<_value></Z>)\n')

		if ((x2 != None) or (y2 != None) or (z2 != None)):
			self.write_blocknum()
			self.write('(LOG,</POINT>)\n')

		if ((x3 != None) or (y3 != None) or (z3 != None)):
			self.write_blocknum()
			self.write('(LOG,<POINT>)\n')

		if (x3 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + x3 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<X>#<_value></X>)\n')

		if (y3 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + y3 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<Y>#<_value></Y>)\n')

		if (z3 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + z3 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<Z>#<_value></Z>)\n')

		if ((x3 != None) or (y3 != None) or (z3 != None)):
			self.write_blocknum()
			self.write('(LOG,</POINT>)\n')

		if ((x4 != None) or (y4 != None) or (z4 != None)):
			self.write_blocknum()
			self.write('(LOG,<POINT>)\n')

		if (x4 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + x4 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<X>#<_value></X>)\n')

		if (y4 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + y4 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<Y>#<_value></Y>)\n')

		if (z4 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + z4 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<Z>#<_value></Z>)\n')

		if ((x4 != None) or (y4 != None) or (z4 != None)):
			self.write_blocknum()
			self.write('(LOG,</POINT>)\n')

		if ((x5 != None) or (y5 != None) or (z5 != None)):
			self.write_blocknum()
			self.write('(LOG,<POINT>)\n')

		if (x5 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + x5 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<X>#<_value></X>)\n')

		if (y5 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + y5 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<Y>#<_value></Y>)\n')

		if (z5 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + z5 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<Z>#<_value></Z>)\n')

		if ((x5 != None) or (y5 != None) or (z5 != None)):
			self.write_blocknum()
			self.write('(LOG,</POINT>)\n')

		if ((x6 != None) or (y6 != None) or (z6 != None)):
			self.write_blocknum()
			self.write('(LOG,<POINT>)\n')

		if (x6 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + x6 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<X>#<_value></X>)\n')

		if (y6 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + y6 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<Y>#<_value></Y>)\n')

		if (z6 != None):
			self.write_blocknum()
			self.write('#<_value>=[' + z6 + ']\n')
			self.write_blocknum()
			self.write('(LOG,<Z>#<_value></Z>)\n')

		if ((x6 != None) or (y6 != None) or (z6 != None)):
			self.write_blocknum()
			self.write('(LOG,</POINT>)\n')

		self.write_blocknum()
		self.write('(LOG,</POINTS>)\n')
		self.write_blocknum()
		self.write('(LOGCLOSE)\n')
			


nc.creator = CreatorEMC2()

