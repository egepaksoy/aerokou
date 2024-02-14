# TODO: Drone yonu de bilinmesi lazım simdilik drone ekvator cizgisinden kuzeye dogru gidiyor olarak yaptim


def atesin_konumu(dronenin_konumu, ekran_orani, pixel_pos, yukseklik, kamera_gps_uzakligi):
	# 640 - 16mt
	ekran_x = ekran_orani[0]
	# 480 - 12mt
	ekran_y = ekran_orani[1]

	drone_x = dronenin_konumu[0]
	drone_y = dronenin_konumu[1]

	pos_x = pixel_pos[0]
	pos_y = pixel_pos[1]

	oran = yukseklik / ekran_y

	sonuc = {"x": 0, "y": 0}

	# ates solundaysa
	if ekran_x // 2 >= pos_x:
		yatay_uzaklik = (ekran_x // 2 - pos_x) * oran
		sonuc["x"] = drone_x - yatay_uzaklik
	# ates sagindaysa
	else:
		yatay_uzaklik = (pos_x - ekran_x // 2) * oran
		sonuc["x"] = drone_x + yatay_uzaklik

	# ates kameranin arkasindaysa
	if ekran_y // 2 >= pos_y:
		dikey_uzaklik = (ekran_y // 2 - pos_y) * oran
		if dikey_uzaklik >= kamera_gps_uzakligi:
			dikey_uzaklik -= kamera_gps_uzakligi
		else:
			dikey_uzaklik = kamera_gps_uzakligi - dikey_uzaklik
		sonuc["y"] = drone_y - dikey_uzaklik
	# ates kameranin onundeyse
	else:
		dikey_uzaklik = (pos_y - ekran_y // 2) * oran + kamera_gps_uzakligi
		sonuc["y"] = drone_y + dikey_uzaklik
	
	return sonuc
