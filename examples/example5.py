import gmtpy
import numpy as num

def to_flat_xyz(x,y,z):
    ny, nx = z.shape
    xx = x.repeat(ny,axis=0).flatten().copy()
    yy = y.repeat(nx,axis=1).flatten().copy()
    zz = z.flatten().copy()
    return xx,yy,zz
    
def finite_outline(x,y,z):
    left = []
    right = []
    for irow, row in enumerate(z):
        ii = num.nonzero(num.isfinite(row))
        if ii and len(ii[0]):
            ifirst = ii[0][0]
            ilast = ii[0][-1]
            
            left.append((irow,ifirst))
            right.append((irow,ilast))
            
    if not left or not right:
        return []
    ibottomleft = left[0][1]
    ibottomright = right[0][1]
    itopleft = left[-1][1]
    itopright = right[-1][1]
    top = []
    bottom = []
    for icol, col in enumerate(num.transpose(z)):
        ii = num.nonzero(num.isfinite(col))
        if ii and len(ii[0]):
            ifirst = ii[0][0]
            ilast = ii[0][-1]
            if ibottomleft < icol < ibottomright:
                bottom.append((ifirst,icol))
            if itopleft < icol < itopright:
                top.append((ilast,icol))
    
    left.reverse()
    top.reverse()
    iy, ix = num.array(bottom+right+top+left).transpose()
    return x[0,ix], y[iy,0]
    
    
nx,ny = 101,51
x = num.linspace(0,20,nx)[num.newaxis,:]
y = num.linspace(0,10,ny)[:,num.newaxis]
z = num.where(x>=y, num.sin(x)*num.sin(y), num.nan)
dx = x[0,1]-x[0,0]
dy = y[1,0]-y[0,0]
outline = finite_outline(x,y,z)

gmt = gmtpy.GMT( config={'PAGE_COLOR':'247/247/240'} )

layout = gmt.default_layout()
palette_layout = gmtpy.GridLayout(3,1)
layout.set_widget('center', palette_layout)


widget = palette_layout.get_widget(0,0)
spacer = palette_layout.get_widget(1,0)
palette_widget = palette_layout.get_widget(2,0)
spacer.set_horizontal(0.5*gmtpy.cm)
palette_widget.set_horizontal(0.5*gmtpy.cm)
w,h = gmt.page_size_points()
palette_layout.set_policy((w/gmtpy.golden_ratio, 0.), (0.,0.), aspect=1./gmtpy.golden_ratio )

xx,yy,zz = to_flat_xyz(x,y,z)

xax = gmtpy.Ax(label='Distance from Yoda')
yax = gmtpy.Ax(label='Height over Yoda')
zax = gmtpy.Ax(snap=True, label='The Force')

guru = gmtpy.ScaleGuru( [ (xx,yy,zz) ], axes=(xax,yax,zax) )

grdfile = gmt.tempfilename()
cptfile = gmt.tempfilename()

par = guru.get_params()
inc_interpol = ((par['xmax']-par['xmin'])/(widget.width()/gmtpy.inch*50.),
                (par['ymax']-par['ymin'])/(widget.height()/gmtpy.inch*50.))
                
rxyj = guru.R() + widget.XYJ()

gmt.surface( T=0.3, G=grdfile,  I=inc_interpol, in_columns=(xx,yy,zz), out_discard=True, *guru.R())
gmt.makecpt( I=True, C="hot", Z=True, out_filename=cptfile, *guru.T())
gmt.psclip( in_columns=outline, *rxyj )          
gmt.grdimage( grdfile, C=cptfile, *rxyj)
gmt.grdcontour( grdfile, C=cptfile, *rxyj )
gmt.psclip( C=True, *widget.XY() )
gmt.psbasemap( *(widget.JXY() + guru.RB(ax_projection=True)) )

gmtpy.nice_palette( gmt, palette_widget, guru, cptfile )

gmt.save('example5.pdf', bbox=layout.bbox())

