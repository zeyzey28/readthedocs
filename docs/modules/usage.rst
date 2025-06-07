Kullanım
=======

Temel Kullanım
------------

ShortestPath sınıfını import edin:

.. code-block:: python

   from shortestpath2220674052 import ShortestPath

Graf oluşturun:

.. code-block:: python

   sp = ShortestPath()

CSV Dosyalarından Veri Yükleme
----------------------------

Düğüm ve kenar verilerini CSV dosyalarından yükleyebilirsiniz:

.. code-block:: python

   sp.load_from_csv("nodes.csv", "edges.csv")

CSV dosya formatları şu şekilde olmalıdır:

nodes.csv:
::

   id,name
   A,Nokta A
   B,Nokta B
   ...

edges.csv:
::

   poi1,poi2,cost
   A,B,9
   B,C,8
   ...

En Kısa Yol Hesaplama
-------------------

İki nokta arasındaki en kısa yolu hesaplamak için:

.. code-block:: python

   path, cost = sp.find_shortest_path("A", "G")
   print(f"En kısa yol: {path}")
   print(f"Toplam maliyet: {cost}")

Görselleştirme
------------

Grafı görselleştirmek için:

.. code-block:: python

   sp.visualize_graph()

En kısa yolu görselleştirmek için:

.. code-block:: python

   sp.visualize_path(path)

Loglama
-------

Paket otomatik olarak işlemleri loglar. Loglar varsayılan olarak "shortestpath.log" dosyasına kaydedilir. 