select oi.freight_value, gs.geolocation_lat, gs.geolocation_lng, gc.geolocation_lat, gc.geolocation_lng
from order_items oi, sellers s, geolocation gs, orders o, customers c, geolocation gc
where oi.seller_id = s.seller_id and
s.seller_zip_code_prefix = gs.geolocation_zip_code_prefix and
o.order_id = oi.order_id and
o.customer_id = c.customer_id and
c.customer_zip_code_prefix = gc.geolocation_zip_code_prefix
