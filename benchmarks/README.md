# Benchmarks

This directory contains benchmarks for the library.

The benchmarks were run on a Ryzen 5 7600X 6 Core CPU @ 4.7GHz, and 32GB of DDR5 RAM @ 5200MHz, on an NVMe SSD on Ubuntu 20 LTS.
With different hardware, your results may vary, especially if you have a slower drive or cpu, as those are the main bottlenecks.

Each benchmark was run 10 times, and the average was taken.

## Analysis

#### v0.1.0

It seems like ciphers are are limited to a max of around 2.14GB of data. I will have to revise the code to chunk the encryption properly. This is why I overflowed when trying to encrypt 10GB of data. I also noticed how slow my chunking code is, and I will have to revise that as well.

#### v1.0.0

Wow, I am personally super surprised about the new performance. On average a file encrypts around 400% faster than before (v0.1.0). This combined with the fact that now the library can encrypt files of any size faster than before, makes this a huge improvement. I am very happy with the results. Ram usage is much smaller now as well thanks to getting accurate chunk sizes. I think that if you upped the chunk size to 100MB or even 1GB for larger files, you will see huge improvements. It's still not possible to encrypt 10GB of data in one go, but that is just a limitation of the cipher, and not the library.

## Results

| Version | Benchmark | Total Time (seconds) | Average Per (seconds) |
| ------- | --------- | -------------------- | ---------------------- |
| v0.1.0 | Encrypt10MBChunking | 1.7412 | 0.17412 |
| v0.1.0 | Encrypt10MBNoChunking | 0.5158 | 0.0516 |
| v0.1.0 | Encrypt100MBChunking | 15.1253 | 1.5125 |
| v0.1.0 | Encrypt100MBNoChunking | 3.2853 | 0.3285 |
| v0.1.0 | Encrypt1GBChunking | 154.8952 | 15.4895 |
| v0.1.0 | Encrypt1GBNoChunking | 25.9607 | 2.5961 |
| v0.1.0 | Encrypt10GBChunking |  1571.0669 |  157.1067 |
| v0.1.0 | Encrypt10GBNoChunking | Overflowed | Overflowed |
| | | | |
| v1.0.0 | Encrypt10MBChunking | 0.5375 | 0.0538 |
| v1.0.0 | Encrypt10MBNoChunking | 0.5170 | 0.0517 |
| v1.0.0 | Encrypt100MBChunking | 3.4143 | 0.3414 |
| v1.0.0 | Encrypt100MBNoChunking | 3.1039 | 0.3104 |
| v1.0.0 | Encrypt1GBChunking | 35.3457 | 3.5346 |
| v1.0.0 | Encrypt1GBNoChunking | 28.0540 | 2.8054 |
| v1.0.0 | Encrypt10GBChunking | 410.9257 | 41.0926 |
| v1.0.0 | Encrypt10GBNoChunking | Overflowed | Overflowed |
| | | | |

