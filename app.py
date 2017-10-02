from flask import Flask, render_template
import mlab
from mongoengine import Document, StringField

mlab.connect()


class GirlType(Document): #collection
        name = StringField()
        image = StringField()
        description = StringField()


girl_type = GirlType(name="Gái tiểu thư",
                     image="https://via.placeholder.com/400x200",
                     description="Thường đến các nơi sang chảnh, uống trà sữa sang chảnh như Starbuck, Dingtea,... Thích chỗ sạch sẽ, thích con trai ăn mặc gọn gàng, biết chơi thể thao hoặc âm nhạc,...")
girl_type = GirlType(name="Gái tiểu thư",
                     image="https://via.placeholder.com/400x200",
                     description="Thường đến các nơi sang chảnh, uống trà sữa sang chảnh như Starbuck, Dingtea,... Thích chỗ sạch sẽ, thích con trai ăn mặc gọn gàng, biết chơi thể thao hoặc âm nhạc,...")

girl_type.save()

# 1. Connect to Mlab (x)
# 2. Add some data
# 3. Get data for render_template


app = Flask(__name__)

# g = [
#     {
#         "name": "Gái tiểu thư",
#         "image": "https://via.placeholder.com/640x420",
#         "description": "Thường đến các nơi sang chảnh, uống trà sữa sang chảnh như Starbuck, Dingtea,... Thích chỗ sạch sẽ, thích con trai ăn mặc gọn gàng, biết chơi thể thao hoặc âm nhạc,..."
#     },
#     {
#         "name": "Gái ngoan",
#         "image": "https://via.placeholder.com/640x420",
#         "description": "Tính khá bình dân, trẻ như học sinh, già như công sở. Cẩn thận, chăm học, thích đến thự viện. L'espace,... "
#     },
#     {
#         "name": "Gái hư",
#         "image": "https://via.placeholder.com/640x420",
#         "description": "Chỉ cần nhìn là biết"
#     }
# ]


@app.route('/')
def index():
    return render_template("index.html", girl_types=GirlType.objects())


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
