Installation
============

GmtPy is implemented in a single source file `gmtpy.py
<https://github.com/emolch/gmtpy/blob/master/gmtpy.py>`_, which you may just
place into the directory, where you want to use it.  However I recommend to
install it properly, as described below.


Prerequisites
-------------

* Python
* `GMT <http://gmt.soest.hawaii.edu/>`_ (e.g. gmt package on .deb based Linuxes)
* `NumPy <http://numpy.scipy.org>`_ (e.g. python-numpy package on .deb based Linuxes)
* optional: `pycdf <http://pysclint.sourceforge.net/pycdf/>`_ (if you want to use the :py:func:`savegrd` and :py:func:`loadgrd` functions of GmtPy)

Ensure that the ``$GMTHOME`` environment variable is set properly.

Download
--------

GmtPy is hosted at `GitHub <https://github.com/>`_, so the simplest way to download is to use Git::

    cd ~/src/   # or wherever you keep your source packages
    git clone git://github.com/emolch/gmtpy.git gmtpy

Alternatively, you may download GmtPy as a `tar archive <http://github.com/emolch/gmtpy/tarball/master>`_, but updating is easier
with the method described above.

Install
-------

To install GmtPy system wide (usually somewhere under ``/usr/local``), simply run (from within GmtPy's source directory)::

    sudo python setup.py install

It is also possible to install to a custom location. To do so, use the
``--prefix`` option of ``setup.py`` and adjust the environment variable
``$PYTHONPATH``.

Update
------

If you used Git to download GmtPy, and you would later want to update, use the
following commands (from within GmtPy's source directory)::
    
    git pull origin master 
    sudo python setup.py install  

