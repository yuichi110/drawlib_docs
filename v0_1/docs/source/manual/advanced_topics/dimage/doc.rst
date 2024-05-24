=================
Dimage
=================

Dimage is a image data class of drawlib.
It provides 2 features.

- Effecting images
- Cache (load data one place, use it many places)

Cache
=========

Dimage posses class attribute ``cache``.
The cache posses instance of ``DimageCache`` and it provides these methods.

- ``has(name:str)``: Whether posses cache or not 
- ``set(name:str, image:str|Dimage|PIL.Image)``: Cache image data with specified name
- ``list()``: get all cache names
- ``get(name:str)``: get cache data from name
- ``delete(name:str)``: delete cache




