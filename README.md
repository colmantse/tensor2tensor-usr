# Additional components for Tensor2Tensor

Extensions to the [Tensor2Tensor framework](https://github.com/tensorflow/tensor2tensor). 

* Exposes the [TensorFlow NMT tutorial](https://github.com/tensorflow/nmt) to tensor2tensor.
* Additional configurations (hparams and problems) for standard tensor2tensor models.

Installation
------------

* Follow the instructions on the [Tensor2Tensor page](https://github.com/tensorflow/tensor2tensor) to install tensor2tensor. The latest tested version is **T2T 1.2.4** with **TensorFlow 1.3**. Other versions might or might not work.
* Clone this repository to a separate directory (say `USR_DIR`).
* Add `USR_DIR` to your `$PYTHONPATH` environment variable.
* Use the `--t2t_usr_dir` flag to make T2T aware of the new problems and models. Validate your installation by checking if `tfnmt` shows up in the T2T registry:
```
t2t-trainer --t2t_usr_dir=USR_DIR --registry_help
```

Acknowledgements
----------------

The `usr/models/tfnmt/nmt` package is forked from the [TensorFlow NMT tutorial](https://github.com/tensorflow/nmt).

