import qrcode
img = qrcode.make("https://staging.ke.com.pk:24555/")
print(type(img))
img.save ("ayaz channel.png")
print("QR code has been generated sucessfully")
                  