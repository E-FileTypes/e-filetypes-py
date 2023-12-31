# Changelog

## [3.0.0](https://github.com/E-FileTypes/e-filetypes-py/compare/v2.0.1...v3.0.0) (2023-11-05)


### ⚠ BREAKING CHANGES

* changes file extension from e-* to e-# due to windows limitation

### Bug Fixes

* changes file extension from e-* to e-# due to windows limitation ([75c0b23](https://github.com/E-FileTypes/e-filetypes-py/commit/75c0b231297df70e461b8dc3f19ececf3b15db32))

## [2.0.1](https://github.com/E-FileTypes/e-filetypes-py/compare/v2.0.0...v2.0.1) (2023-11-05)


### Bug Fixes

* adds cryptography to dependencies ([7c3a95b](https://github.com/E-FileTypes/e-filetypes-py/commit/7c3a95b104f17d726e0341b4d783bc9760ca2b67))

## [2.0.0](https://github.com/E-FileTypes/e-filetypes-py/compare/v1.1.0...v2.0.0) (2023-11-05)


### ⚠ BREAKING CHANGES

* adds encrypting and decrypting folders. allows bypassing encrypted files. allows bypassing decrypting already decrypted files

### Features

* adds encrypting and decrypting folders. allows bypassing encrypted files. allows bypassing decrypting already decrypted files ([dfeb011](https://github.com/E-FileTypes/e-filetypes-py/commit/dfeb01114e5648b45aa4a5f9e779bf4c3d49af08))
* generates passphrases and passkeys ([ee2ccc6](https://github.com/E-FileTypes/e-filetypes-py/commit/ee2ccc65313cf233ac94542796f5ed3af812ddce))

## [1.1.0](https://github.com/E-FileTypes/e-filetypes-py/compare/v1.0.0...v1.1.0) (2023-11-05)


### Features

* better readme with more shields ([e10c43f](https://github.com/E-FileTypes/e-filetypes-py/commit/e10c43f5613439d6a9aa6cacc6c784f5f60b0860))


### Bug Fixes

* fixes links ([49d2d14](https://github.com/E-FileTypes/e-filetypes-py/commit/49d2d14aec8675abcf62e55f1088b8dbea5b855a))
* removes github-releases job as it is already handled by release-please ([ba22d91](https://github.com/E-FileTypes/e-filetypes-py/commit/ba22d91446fd83359d6366d424e4b8ff255f95e9))
* removes tag requirement for pushes to pypi as the file won't be updated for small releases anyways ([24c3eb4](https://github.com/E-FileTypes/e-filetypes-py/commit/24c3eb411e0d2f2aae4a60d8b5cddbe4b5e993f6))

## [1.0.0](https://github.com/E-FileTypes/e-filetypes-py/compare/v0.1.0...v1.0.0) (2023-11-05)


### ⚠ BREAKING CHANGES

* increased chunk size, moved chunk size to megabytes
* fixes overflows when encrypting large files (<2.14gb)
* benchmarks and changed main code to be relative as it was breaking the package

### Features

* adds pypi workflow ([0c53d39](https://github.com/E-FileTypes/e-filetypes-py/commit/0c53d3951edc325ff584c8c631a9025b6977566f))
* adds submodules pages ([ce6cd44](https://github.com/E-FileTypes/e-filetypes-py/commit/ce6cd44110ffc53f5c3e4fbe7ccd7b2172eaa55a))
* adds usages to helper functions ([9baa1e9](https://github.com/E-FileTypes/e-filetypes-py/commit/9baa1e9a344e49af0982792f40f75ebe12083bd0))
* autogen docs, proper description of package ([c49126a](https://github.com/E-FileTypes/e-filetypes-py/commit/c49126a85c99150e32e17952b2ca8022672da8a7))
* benchmarks and changed main code to be relative as it was breaking the package ([8a013cf](https://github.com/E-FileTypes/e-filetypes-py/commit/8a013cf65458ae6fc9554f5b072b018456ff7ce3))


### Bug Fixes

* changes order of workflow ([075c82a](https://github.com/E-FileTypes/e-filetypes-py/commit/075c82a477f58d8f73586e224eb1168b5f1052f1))
* fixes overflows when encrypting large files (&lt;2.14gb) ([34d9c8c](https://github.com/E-FileTypes/e-filetypes-py/commit/34d9c8cc0a00013b2c46776bb6f21775d6611f20))
* fixes release names ([6f7e7e2](https://github.com/E-FileTypes/e-filetypes-py/commit/6f7e7e26c70aa424ed4ff4a280d4fe58cb970c0d))
* fixes sphinx not seeing module folder ([b548baa](https://github.com/E-FileTypes/e-filetypes-py/commit/b548baa2491be18a34157d3dc633d36e08ddbb32))
* increased chunk size, moved chunk size to megabytes ([2ad5686](https://github.com/E-FileTypes/e-filetypes-py/commit/2ad568684622fbebdf4c2528f0f4763f3bf9c9b4))

## 0.1.0 (2023-11-05)


### ⚠ BREAKING CHANGES

* helper functions for encrypting files, and decrypting files, adds main functions for encrypt and decrypt
* encrypts data using aes-gcm, writes and reads file headers

### Features

* adds basic precommit hooks for safety ([a97efc7](https://github.com/E-FileTypes/e-filetypes-py/commit/a97efc721dd3c96fa2a7d82f2d80ef672c598fcf))
* adds py-pi ([066d77c](https://github.com/E-FileTypes/e-filetypes-py/commit/066d77c82fca1cc0831ac79617e0e824d0e6326a))
* adds readthedocs config ([4963857](https://github.com/E-FileTypes/e-filetypes-py/commit/496385750091ed28da6c77cb867b0556239ed2c2))
* adds release-please workflow ([5eebf10](https://github.com/E-FileTypes/e-filetypes-py/commit/5eebf10635bdd692dbfc93f561413fa3a6f165b9))
* adds ruff workflow ([cf36b7d](https://github.com/E-FileTypes/e-filetypes-py/commit/cf36b7db38dbb6bc0f1b648fef50c7eeb65400a0))
* adds title below image ([df43079](https://github.com/E-FileTypes/e-filetypes-py/commit/df4307938ad16cdab4a48b6e49b81bb7758ddff3))
* encrypts data using aes-gcm, writes and reads file headers ([152358d](https://github.com/E-FileTypes/e-filetypes-py/commit/152358d6c871d39989df1a707aa0858e82309d69))
* helper functions for encrypting files, and decrypting files, adds main functions for encrypt and decrypt ([c0f9d1b](https://github.com/E-FileTypes/e-filetypes-py/commit/c0f9d1bb178f79d9d1d67bb4ac8fd3dc0378ded2))
* readme upgrades and logos ([cbbd4b9](https://github.com/E-FileTypes/e-filetypes-py/commit/cbbd4b9cfc55f7c651fa431a6f18afaa4ab893c1))


### Bug Fixes

* fixes spacing and removes title ([5555046](https://github.com/E-FileTypes/e-filetypes-py/commit/55550461ea94271d4eb8bfd927560770a0892954))
* properly gives sphinx right conf location ([a8b16de](https://github.com/E-FileTypes/e-filetypes-py/commit/a8b16de643e159919bc6649c0aa69afe9ae4e075))
* removes redefinition of os. ([9c33cc6](https://github.com/E-FileTypes/e-filetypes-py/commit/9c33cc6999d5d106f31210327e81a4f6f8dfc9e0))
