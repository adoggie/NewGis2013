#--coding:utf-8--

from base import *

import os,os.path,sys,struct,time,traceback,signal,threading
import tcelib as tce
from sns_service import *

# y ( 0-15 ) ,x (16 - 31)
def CELL_INDEX(x,y):
	return ((x & 0xffff)<<16)| (y&0xffff)

def distance(a,b):
	import math
	return math.sqrt( math.pow(b[0]-a[0],2) + math.pow( b[1]-a[1],2) )

class MapCell:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.locs = {}      # LocationCachedObjectInfo_t
		self.mtxlocs = tce.utils.ReadWriteLock()


	def index(self):
		return CELL_INDEX(self.x,self.y)

	def update(self,d):
		self.mtxlocs.acquire_write()
#		cachedobj = self.locs.get(d.user_id)
#		if cachedobj:
#			cachedobj.loc = d
#		else:
		self.locs[d.user_id] = d
		self.mtxlocs.release_write()



	def isPtInRect(self,rc,pt):
		if pt[0]>rc[0] and pt[0] < rc[0]+rc[2] and \
			pt[1]>rc[1] and pt[1] < rc[1]+rc[3]:
			return True
		return False

	def spatialQuery(self,querycase,result):
		qc = querycase
		if qc.type == SpatialQueryGeomType.ByCircle: # cricle
			self.mtxlocs.acquire_read()
			for k,v in self.locs.items():
				x,y = v.loc.gps.loc.lon,v.loc.gps.loc.lat
				if distance((x,y),
				                      (qc.circle.center.lon,qc.circle.center.lat)
								) <= qc.circle.radius:
					result.append(v)
			self.mtxlocs.release_read()

		if qc.type == SpatialQueryGeomType.ByRect:
			c = querycase
			rc = (c.rect.x,c.rect.y,c.rect.width,c.rect.height)
			self.mtxlocs.acquire_read()
			for k,v in self.locs.items():
				x,y = v.loc.gps.loc.lon,v.loc.gps.loc.lat
				if self.isPtInRect((x,y),rc):
					result.append(v)
			self.mtxlocs.release_read()


class GlobalMap:
	def __init__(self,cellsize=(0.1,0.1),region=(70,10,30,30)):
		self.cellsize = cellsize
		self.region = region
		self.cells={}
		self.initdata()
		self.mtxcells = threading.Lock()




	def origin(self):
		return self.region[:2]

	def width(self):
		return self.region[2]


	def height(self):
		return self.region[3]

	def getCellIndex(self,x,y):
		distx = x - self.origin()[0]
		disty = y - self.origin()[1]
		idx_x = distx // self.cellsize[0]
		idx_y = disty // self.cellsize[1]
		return ( int(idx_x), int(idx_y) )

	def getCell(self,x,y):
		x,y = self.getCellIndex(x,y)
		cellid = CELL_INDEX(x,y)
		self.mtxcells.acquire()
		cell = self.cells.get(cellid)
		self.mtxcells.release()
		return cell

	def getCells(self,rc):
		x1,y1 = self.getCellIndex(rc[0],rc[1])
		x2,y2 = self.getCellIndex(rc[0]+rc[2],rc[1]+rc[3])
		cells =[]
		while y1<=y2:
			while x1<=x2:
				self.mtxcells.acquire()
				cellid = CELL_INDEX(x,y)
				cell = self.cells.get(cellid)
				self.mtxcells.release()
				cells.append(cell)
				x1+=1
			y1+=1
		#
		return cells

	#		struct StrangerSearchCase_t{
	#		                           // 1 - rect; 2 - circle
	#		int type;
	#		GeoRect_t rect;
	#		GeoCircle_t circle;
	#		int limit;
	#		// 1 - distance ,2 - time
	#		int order;
	#		int target_type;
	#		int target_subtype;
	#		};
	def spatialQuery(self,case):
		c = case
		rc = (c.rect.x,c.rect.y,c.rect.width,c.rect.height)
		if c.type == SpatialQueryGeomType.ByCircle:
			rc = (  c.circle.center.lon - c.radius,
					c.circle.center.lat - c.radius,
					c.circle.radius*2,
					c.circle.radius*2)
		locs = []
		cells = self.getCells(rc)
		for cell in cells:
			cell.spatialQuery(case,locs)
		# sort ,or limit
		#距离排序
		cxy = ()
		if c.type == SpatialQueryGeomType.ByCircle:
			cxy = (c.circle.center.lon,c.circle.center.lat)
		else:
			cxy = ( c.rect.x+c.rect.width/2.0, c.rect.y+c.rect.height/2.0 )

		sort(locs,cmp=lambda a,b:
			distance( (a.loc.gps.loc.lon,a.loc.gps.loc.lon),cxy) > distance( (b.loc.gps.loc.lon,b.loc.gps.loc.lon),cxy)
			)
		#limit限制
		locs = locs[:case.limit]
		return locs


	def update(self,d):
		x,y = d.loc.gps.loc.lon,d.loc.gps.loc.lat
		cell = self.getCell(x,y)
		if cell:
			cell.update(d)
		else:
			print 'location is out of bound of map!'



	def initdata(self):
		r = self.region
		x1,y1 = self.getCellIndex(r[0],r[1])
		x2,y2 = self.getCellIndex(r[0]+r[2],r[1]+r[3])
		while y1<=y2:
			while x1<=x2:
				cellid = CELL_INDEX(x1,y1)
				cell = MapCell(x1,y1)
				self.cells[cellid] = cell
				x1+=1
			y1+=1

if __name__ == '__main__':
	pass
#	sys.exit( MainApp().run())
