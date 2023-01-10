# PICLas-Singularity

This repo provides the Singularity source code used for containerizing the Open Source Particle-in-Cell (PIC) code
[PICLas](https://piclas.readthedocs.io/en/latest/). Please visit the website of the developers [https://boltzplatz.eu/](https://boltzplatz.eu/).

## 1. Prerequisites

You need to have Singularity installed on your machine.

1. System dependencies

   ```sh
   # Ensure repositories are up-to-date
   sudo apt-get update && sudo apt-get install -y build-essential libseccomp-dev libglib2.0-dev \
   pkg-config squashfs-tools cryptsetup crun uidmap
   ```

2. Go language

   ```sh
   export VERSION=1.19.3 OS=linux ARCH=amd64  # change this as you need
   wget -O /tmp/go${VERSION}.${OS}-${ARCH}.tar.gz \
   https://dl.google.com/go/go${VERSION}.${OS}-${ARCH}.tar.gz
   sudo tar -C /usr/local -xzf /tmp/go${VERSION}.${OS}-${ARCH}.tar.gz
   export PATH=$PATH:/usr/local/go/bin
   ```

3. Install Singularity

   ```sh
   git clone --recurse-submodules https://github.com/sylabs/singularity.git
   cd singularity
   ./mconfig
   make -C builddir
   sudo make -C builddir install
   ```

## 2. Install the PICLas Image

You can directly pull it from the official [Singularity library](https://cloud.sylabs.io/library/inflowencer/openfoam/hystrath):

```sh
mkdir -p ~/containers/singularity && cd ~/images/singularity
singularity pull library://inflowencer/piclas/piclas
```

## 3. Benchmarks *native* vs. *image*

<!-- ### 1.2 From GitHub Repo

Alternatively, you can build it yourself from this GitHub repo. Clone the repo and build using:

```sh
cd ~/ && git clone https://github.com/inflowencer/hyStrath-Docker.git && cd hyStrath-Docker
docker build -t hystrath .
``` -->