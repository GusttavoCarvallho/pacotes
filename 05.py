import qrcode

# criar um Qrcode qr

qr = qrcode.QRCode(version=1, box_size=10, border=5)

# adicionar dados ao codgo

data = 'https://google.com'
qr.add_data(data)
qr.make(fit=True)

# criar a imagem doi codigo 

img = qr.make_image(fill_color='red',back_color='green')

# salvar imagem em um arquivo

img.save('qr_code1.png')