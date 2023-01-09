# PICLas-Singularity

This repo provides the Singularity source code used for containerizing the Open Source Particle-in-Cell (PIC) code
[PICLas](https://piclas.readthedocs.io/en/latest/). Please visit the website of the developers [https://boltzplatz.eu/](https://boltzplatz.eu/).

## 1. Installation

You need to have Singularity installed. Follow [this guide](install_Singularity.md) for instructions on how to install
Singularity on Ubuntu.

### 1.1 Singularity Image (recommended)

You can directly pull it from the official [Singularity library](https://cloud.sylabs.io/library/inflowencer/openfoam/hystrath):

```sh
mkdir -p ~/images/singularity && cd ~/images/singularity
singularity pull library://inflowencer/piclas/piclas
```

### 1.2 From GitHub Repo

Alternatively, you can build it yourself from this GitHub repo. Clone the repo and build using:

```sh
cd ~/ && git clone https://github.com/inflowencer/hyStrath-Docker.git && cd hyStrath-Docker
docker build -t hystrath .
```