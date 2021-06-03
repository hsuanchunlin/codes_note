# Some solutions for errors in TensorFlow and Keras

## Construct a model with None in shape
Use

```python
dim = tf.shape(Input)
dim = dim[0]
```
instead of 

```python
dim = Input.shape[0]
```

## Replace keras.backend.repeat_elements
Replace keras.backend.repeat_elements by tf.repeat

```python
keras.backend.repeat_elements(y, nb_dim, axis = 1)
equals to
tf.repeat(y, nb_dim, axis = 1)

```
## ```keras.backend.image_dim_ordering()``` in Keras 2.3
Replace it by 

```python
K.image_data_format()
# to set the image order
K.set_image_data_format()
```
and the function will return

```python
'channels_first'
'channels_last'
```
instead of 
```python
'th'
'tf'
```