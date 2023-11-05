Usage
=====

.. _installation:

Installation
------------

To use E-FileTypes-Py, first install it using pip:

.. code-block:: console

   (.venv) $ pip install e-filetypes-py



Encrypting a file
----------------

To encrypt a file use the ``efiletypes.encrypt()`` function:

.. autofunction:: efiletypes.encrypt

For example:

>>> from e_filetypes_py import efiletypes
>>> efiletypes.encrypt("test.txt", "password")



Decrypting a file
----------------

To decrypt a file use the ``efiletypes.decrypt()`` function:

.. autofunction:: efiletypes.decrypt

For example:

>>> from e_filetypes_py import efiletypes
>>> efiletypes.decrypt("test.e-#", "password") # decrypts with the extension e-# (required)
