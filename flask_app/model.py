import numpy as np
import tensorflow as tf
import keras
from tensorflow.keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from PIL import Image
import io

model = load_model('./t_model.h5')

Categories_Dictionary={'001': 'Danaus_plexippus','002': 'Heliconius_charitonius',
'003': 'Heliconius_erato','004': 'Junonia_coenia','005': 'Lycaena_phlaeas',
'006': 'Nymphalis_antiopa','007': 'Papilio_cresphontes','008': 'Pieris_rapae',
'009': 'Vanessa_atalanta','010': 'Vanessa_cardui'}

Categories=('Danaus_plexippus','Heliconius_charitonius','Heliconius_erato','Junonia_coenia',
            'Lycaena_phlaeas','Nymphalis_antiopa','Papilio_cresphontes','Pieris_rapae',
            'Vanessa_atalanta','Vanessa_cardui')

Label_Encoding=LabelEncoder().fit_transform(Categories).reshape(-1,1)
One_Hot_Encoding=OneHotEncoder().fit_transform(Label_Encoding).toarray()
Categories_Dictionary={tuple(One_Hot_Encoding[i]):Categories[i] for i in range(len(Categories))}

def predict_butterfly(file):
    img_pil = Image.open(io.BytesIO(file))
    img_pil = img_pil.resize((128,128),Image.ANTIALIAS)
    # img = image.load_img(io.BytesIO(file), target_size=(128,128))
    img_array = image.img_to_array(img_pil)
    datagen = ImageDataGenerator(rescale=1./255)
    img_batch = np.expand_dims(img_array, axis=0)
    testing_image = datagen.flow(img_batch)
    prediction = model.predict(testing_image)
    prediction = (prediction>=0.5)
    # print(Categories_Dictionary[tuple(prediction[0])])
    return Categories_Dictionary[tuple(prediction[0])]