Örnekler
========

Kampüs İçi En Kısa Yol Bulma
--------------------------

.. code-block:: python

   from shortestpath2220674052 import ShortestPath

   # Graf oluştur
   sp = ShortestPath()

   # Kampüs verilerini yükle
   sp.load_from_csv('kampus_nodes.csv', 'kampus_edges.csv')