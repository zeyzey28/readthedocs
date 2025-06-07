.. ShortestPath2220674052 documentation master file, created by
   sphinx-quickstart on Fri Jun  6 01:33:16 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ShortestPath2220674052 Dokümantasyonu
================================

ShortestPath2220674052, kampüs içi ve Türkiye'deki ilçeler arası en kısa yol hesaplama işlemleri için geliştirilmiş bir Python paketidir.

.. toctree::
   :maxdepth: 2
   :caption: İçindekiler:

   modules/installation
   modules/usage
   modules/api
   modules/examples

Özellikler
----------

* Dijkstra algoritması ile en kısa yol hesaplama
* Networkx ve Matplotlib ile görselleştirme
* CSV dosyalarından veri okuma
* Kampüs ve ilçe verileri desteği
* Detaylı loglama sistemi

Hızlı Başlangıç
--------------

Kurulum
~~~~~~~

.. code-block:: bash

   pip install -i https://test.pypi.org/simple/ ShortestPath2220674052

Basit Kullanım
~~~~~~~~~~~~~

.. code-block:: python

   from shortestpath2220674052 import ShortestPath
   
   # Graf oluşturma
   sp = ShortestPath()
   
   # CSV dosyalarından veri yükleme
   sp.load_from_csv("nodes.csv", "edges.csv")
   
   # En kısa yol hesaplama
   path, cost = sp.find_shortest_path("A", "G")
   
   # Sonuçları görselleştirme
   sp.visualize_path(path)

İndeksler ve Tablolar
-------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
