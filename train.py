from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pickle
from sklearn.svm import SVC
from facenet.facenet import *
from align.align_mtcnn import  *


from tkinter import messagebox


# ================== Function button =====================
def train(data_dir,
        model,
        classifier_filename,
        use_split_dataset=None,
        batch_size=1000,
        image_size=160,
        seed=123,
        min_nrof_images_per_class=20,
        nrof_train_images_per_class=10):

    with tf.Graph().as_default():
        with tf.Session() as sess:
            np.random.seed(seed=seed)
            if use_split_dataset:
                dataset_tmp = get_dataset(data_dir)
                train_set, test_set = split_dataset(dataset_tmp, min_nrof_images_per_class,
                                                    nrof_train_images_per_class)
                dataset = train_set
            else:
                dataset = get_dataset(data_dir)

            # Check that there are at least one training image per class
            for cls in dataset:
                assert (len(cls.image_paths) > 0)
                #messagebox.showerror('Error', 'There must be at least one image for each class in the dataset')

            paths, labels = get_image_paths_and_labels(dataset)


            messagebox.showinfo("Trainning Process",f'Number of people: %d'% len(dataset))
            messagebox.showinfo("Trainning Process", f'Number of images: %d' % len(paths))

            # Load the model
            load_model(model)

            # Get input and output tensors
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
            embedding_size = embeddings.get_shape()[1]

            # Run forward pass to calculate embeddings
            messagebox.showinfo('Training Process','Calculating features for images')
            nrof_images = len(paths)
            nrof_batches_per_epoch = int(math.ceil(1.0 * nrof_images / batch_size))
            emb_array = np.zeros((nrof_images, embedding_size))
            for i in range(nrof_batches_per_epoch):
                    start_index = i * batch_size
                    end_index = min((i + 1) * batch_size, nrof_images)
                    paths_batch = paths[start_index:end_index]
                    images = load_data(paths_batch, False, False, image_size)
                    feed_dict = {images_placeholder: images, phase_train_placeholder: False}
                    emb_array[start_index:end_index, :] = sess.run(embeddings, feed_dict=feed_dict)

            classifier_filename_exp = os.path.expanduser(classifier_filename)

            # =================== Train classifier =====================
            messagebox.showinfo('Trainning Conduct','Training classifier')
            model = SVC(kernel='linear', probability=True)
            model.fit(emb_array, labels)

            # Create a list of class names
            class_names = [cls.name.replace('_', ' ') for cls in dataset]

            # Saving classifier model
            with open(classifier_filename_exp, 'wb') as outfile:
                pickle.dump((model, class_names), outfile)
            messagebox.showinfo('Trainning Finish','Data has been trained successfully !!!')

def split_dataset(dataset, min_nrof_images_per_class, nrof_train_images_per_class):
    train_set = []
    test_set = []
    for cls in dataset:
        paths = cls.image_paths

        # Remove classes with less than min_nrof_images_per_class
        if len(paths) >= min_nrof_images_per_class:
            np.random.shuffle(paths)
            train_set.append(ImageClass(cls.name, paths[:nrof_train_images_per_class]))
            test_set.append(ImageClass(cls.name, paths[nrof_train_images_per_class:]))
    return train_set, test_set




if __name__ == '__main__':
    align_mtcnn('dataSet', 'face_align')
    train('face_align/', 'models/20180402-114759.pb', 'models/your_model.pkl')