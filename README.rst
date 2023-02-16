EO times series.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A brief demo of extracting time series for a point shapefile and writing as attributes. This is not exhaustive, simply what has been required of a recent project. These require CEDA credentials to access data.

**Met_data_tseries.ipynb**

Attribute a geometry file with met office climate modelling data from the CEDA archive. 

**Nextmapprocessing.ipynb**

Attribute a geometry file with Nextmap elevation data and derivatives from the CEDA archive. 

I have just provided cut down modules locally in the directory src. Provided you are using the notebook herein you can import the functions from the local files.

Installation and Use
~~~~~~~~~~~~~~~~~~~~

Installing the required libs (there are not many) uses the conda system so ensure you have this first. Clone this repo and cd into the directory then...

.. code-block:: bash

conda env create -f eot_demo.yml

conda activate eot

jupyter notebook


Then open the ipynb and cycle through the cells.

