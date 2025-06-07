Örnekler
========

Bu bölümde paketin kullanımına dair detaylı örnekler bulabilirsiniz.

Kampüs İçi En Kısa Yol Bulma
--------------------------

.. code-block:: python

   from shortestpath2220674052 import ShortestPath

   # Graf oluştur
   sp = ShortestPath()

   # Kampüs verilerini yükle
   sp.load_from_csv("kampus_nodes.csv", "kampus_edges.csv")

   # Kütüphane ile yemekhane arası en kısa yolu bul
   path, cost = sp.find_shortest_path("KUTUPHANE", "YEMEKHANE")
   print(f"En kısa yol: {path}")
   print(f"Toplam mesafe: {cost} metre")

   # Yolu görselleştir
   sp.visualize_path(path)

İlçeler Arası En Kısa Yol Bulma
-----------------------------

.. code-block:: python

   from shortestpath2220674052 import ShortestPath

   # Graf oluştur
   sp = ShortestPath()

   # İlçe verilerini yükle
   sp.load_from_csv("ilceler_nodes.csv", "ilceler_edges.csv")

   # Kadıköy ile Beşiktaş arası en kısa yolu bul
   path, cost = sp.find_shortest_path("KADIKOY", "BESIKTAS")
   print(f"En kısa yol: {path}")
   print(f"Toplam mesafe: {cost} km")

   # Yolu görselleştir
   sp.visualize_path(path)

Özel Graf Oluşturma
-----------------

.. code-block:: python

   from shortestpath2220674052 import ShortestPath

   # Graf oluştur
   sp = ShortestPath()

   # Düğümleri ve kenarları CSV dosyalarından yükle
   nodes_data = """id,name
   A,Başlangıç
   B,Orta Nokta
   C,Bitiş"""

   edges_data = """poi1,poi2,cost
   A,B,5
   B,C,3
   A,C,10"""

   with open("nodes.csv", "w") as f:
       f.write(nodes_data)
   
   with open("edges.csv", "w") as f:
       f.write(edges_data)

   sp.load_from_csv("nodes.csv", "edges.csv")

   # En kısa yolu bul ve görselleştir
   path, cost = sp.find_shortest_path("A", "C")
   sp.visualize_path(path)

Loglama Örneği
------------

Bu örnekte, detaylı loglama özelliğinin nasıl kullanılacağını göreceğiz.

.. code-block:: python

   import logging
   from shortestpath2220674052.shortestpath import main

   # Loglama seviyesini ayarla
   logging.basicConfig(
       level=logging.DEBUG,  # Tüm log seviyelerini göster
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
       handlers=[
           logging.FileHandler('shortestpath_detailed.log'),
           logging.StreamHandler()
       ]
   )

   # Test için örnek kullanım
   edges_file = "data/test/edges.csv"
   nodes_file = "data/test/nodes.csv"
   start_node = "A"
   end_node = "G"

   try:
       path, distance = main(edges_file, nodes_file, start_node, end_node)
       
       if path and distance:
           print(f"\nEn kısa yol bulundu:")
           print(f"Rota: {' -> '.join(path)}")
           print(f"Toplam mesafe: {distance} metre")
       else:
           print("Yol bulunamadı!")
           
   except Exception as e:
       logging.error(f"Program çalışırken hata oluştu: {str(e)}")
       print(f"Hata: {str(e)}")

Bu örnekte oluşturulan log dosyası (`shortestpath_detailed.log`) şu tür bilgileri içerecektir:

.. code-block:: text

   2024-03-14 10:30:15,123 - shortestpath2220674052 - INFO - Program başlatıldı: A -> G
   2024-03-14 10:30:15,124 - shortestpath2220674052 - INFO - Kenar bilgileri okunuyor: edges.csv
   2024-03-14 10:30:15,125 - shortestpath2220674052 - DEBUG - Yeni düğüm eklendi: A
   2024-03-14 10:30:15,126 - shortestpath2220674052 - DEBUG - Kenar eklendi: A -> B (Ağırlık: 9)
   2024-03-14 10:30:15,127 - shortestpath2220674052 - INFO - En kısa yol bulundu: A -> B -> C -> G 