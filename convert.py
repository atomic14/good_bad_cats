import coremltools

coreml_model = coremltools.converters.caffe.convert(('Epoch11/snapshot_iter_176.caffemodel', 'Epoch11/deploy.prototxt'), image_input_names='data', class_labels='Epoch11/labels.txt')

coreml_model.save('good_bad_cats.mlmodel')
