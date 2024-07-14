# from core.generator import Generator
# from utils import convert_image, plot_image
#
# model = Generator()
#
# z = model.get_z(123)
# w = model.get_w(z, truncation_psi=0.5)
# img = model.get_img(w)
# img = convert_image(img, (500, 500))
# plot_image(img)


# from core.generator import Generator
# from core.shifter import Shifter
# from utils import plot_image, convert_image
#
# model = Generator()
# shifter = Shifter()
#
# z = model.get_z(123)
#
# w = model.get_w(z, truncation_psi=0.5)
#
# w = shifter(w, 'age', 5)
# img = model.get_img(w)
# img = convert_image(img, (500, 500))
# plot_image(img)

from core.generator import Generator
from core.shifter import Shifter
from utils import convert_image, plot_image

model = Generator()
shifter = Shifter()

z = model.get_z(123)
w = model.get_w(z, truncation_psi=0.5)
w = shifter(w, 'age', 5)
img = model.get_img(w)
img = convert_image(img, (500, 500))
plot_image(img)
