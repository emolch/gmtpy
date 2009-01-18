from gmtpy import GMT

gmt = GMT( config={'BASEMAP_TYPE':'fancy'})

gmt.pscoast( R='5/15/52/58',       # region
             J='B10/55/55/60/10c', # projection
             B='4g4',              # grid
             D='f',                # resolution
             S=(114,159,207),      # wet fill color 
             G=(233,185,110),      # dry fill color
             W='thinnest' )        # shoreline pen
             
gmt.save('example1.pdf')
gmt.save('example1.eps')
